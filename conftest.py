import os
import pytest
from playwright.sync_api import sync_playwright
from config.settings import BROWSER, HEADLESS, DEFAULT_TIMEOUT, ENVIRONMENTS
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="Environment to run tests against"
    )

    
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_name = BROWSER
    valid_browsers = ["chromium", "firefox", "webkit"]

    if browser_name not in valid_browsers:
        raise ValueError(f"Invalid browser: {browser_name}")

    browser_type = getattr(playwright_instance, browser_name)
    browser = browser_type.launch(headless=HEADLESS)

    yield browser

    browser.close()


# @pytest.fixture(scope="function")
# def context(browser):
#     context = browser.new_context()
#     yield context
#     context.close()

@pytest.fixture(scope="function")
def context(browser,request):
        
    os.makedirs("traces",exist_ok=True)
    
    os.makedirs("videos",exist_ok=True)
    
    test_name = request.node.name
    trace_path = (f"traces/{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip")
    
    video_enabled = request.config.getoption("--video")
    context_options ={}
    
    if video_enabled == "on":
            context_options= {"record_video_dir" : "videos/", "record_video_size" : {
            "width": 1280,
            "height": 720
        } }
            
    context = browser.new_context(**context_options)

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    context.tracing.stop(
        path=trace_path)       # "traces/trace.zip"

    context.close()


@pytest.fixture(scope="function")
def page(context,request):
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT)
    
    # Attach page to current test
    request.node.page = page

     
    yield page

    page.close()



@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def base_url(environment):
    return ENVIRONMENTS[environment]["base_url"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and report.failed
    ):

        page = getattr(
            item,
            "page",
            None
        )

        if page:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = (f"screenshots/"
                f"{item.name}_{timestamp}.png")

            page.screenshot(path=screenshot_path)