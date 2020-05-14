import pytest
import config
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--baseurl",
        action="store",
        default="baseurl",
        help="base URL for the AUT"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="the name of the browser you want to test with"
    )


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()

    if config.browser == "chrome":
        binary = "D:/Automation Projects/Python/bain-preprod/vendors/chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument("--incognito")
        driver_ = webdriver.Chrome(binary, options=chrome_options)
        driver_.maximize_window()

    # elif config.browser == "internet_explorer":
    #     binary = "D:/Automation Projects/Python/bain-preprod/vendors/IEDriverServer.exe"
    #     cap = DesiredCapabilities().INTERNETEXPLORER
    #     cap['ignoreProtectedModeSettings'] = True
    #     cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
    #     cap['nativeEvents'] = True
    #     cap['ignoreZoomSetting'] = True
    #     cap['requireWindowFocus'] = True
    #     cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    #     cap['ensureCleanSession'] = True
    #     cap['enableElementCacheCleanup'] = True
    #     driver_ = webdriver.Ie(capabilities=cap, executable_path=binary)
    #     driver_.maximize_window()
    #     driver_.delete_all_cookies()
    #
    # elif config.browser == "firefox":
    #     _geckodriver = "D:/Automation Projects/Python/bain-preprod/vendors/geckodriver.exe"
    #     driver_ = webdriver.Firefox(executable_path=_geckodriver)
    #     firefox_profile = webdriver.FirefoxProfile()
    #     firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    #     driver_.maximize_window()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_
