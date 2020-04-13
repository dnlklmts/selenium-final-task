import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
            help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
            help='Specify language: e.g. --language=es')


@pytest.fixture(scope='function')
def browser(request):

    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    browser = None
    if user_language is not None:

        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs',
                    {'intl.accept_languages': user_language})

            print('\nstart chrome browser..')
            browser = webdriver.Chrome(options=options)

        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference('intl.accept_languages', user_language)

            print('\nstart firefox browser..')
            browser = webdriver.Firefox(firefox_profile=fp)

        else:
            raise pytest.UsageError('--browser_name should be chrome or firefox')

    else:
        raise pytest.UsageError('--language should be specified')

    yield browser
    print('\nquit browser..')
    browser.quit()
