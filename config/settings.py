BASE_URL = "https://www.saucedemo.com" # No / at the end of the URL, because later we can easily construct URLs
BROWSER = "chromium"
HEADLESS = False
DEFAULT_TIMEOUT = 5000

ENVIRONMENTS = {

    "dev": {
        "base_url": "https://dev.example.com"
    },

    "qa": {
        "base_url": "https://qa.example.com"
    },

    "uat": {
        "base_url": "https://uat.example.com"
    },

    "prod": {
        "base_url": "https://www.saucedemo.com"
    }
}
 