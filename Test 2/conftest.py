# -*- coding: utf-8 -*-
import os
import allure
import pytest
import sys
from appium import webdriver as appium_webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

from Web.application import Application as web_app


def search_folder(end_folder):
    path = os.path.abspath(os.curdir)
    while path:
        for root, dirs, files in os.walk(path, topdown=True):
            if end_folder in root:
                return root
        path = os.path.dirname(path)
#
# if os.name != 'nt':
#     path = search_folder('Latista.iOS.UItests')
#     print(path)
#     os.path.join(path)
#     sys.path.insert(0, path)
if os.name !='nt':
    path = ''
    end_folder = 'Latista.iOS.UItests'
    stop_finding = False
    current_path = os.getcwd()
    if end_folder in current_path:
        path = os.path.join(os.getcwd()[0:os.getcwd().find(end_folder)], end_folder)
    else:
        path_list = current_path.split('/')
        num_folders = len(path_list)
        stop_finding_folder = False
        for folder in reversed(path_list):
            current_path = current_path[0:current_path.find(folder)]
            for dirs in os.walk(current_path):
                for int_dir in dirs:
                    if end_folder in int_dir:
                        path = os.path.join(dirs[0], end_folder)
                        print(path)
                        stop_finding = True
                        stop_finding_folder = True
                        break
                if stop_finding:
                    break
            if stop_finding_folder:
                break
    import sys
    sys.path.insert(0, path)#'/Users/ekravchenko/Documents/mobile.ios/Latista.iOS.UItests')


from Droid.application import Application as droid_app
from API.application import Application as api_app
import work_dir.environment_testing
import work_dir.environment_staging
import work_dir.environment_cross
import work_dir.environment



__author__ = 'EKravchenko'


class CurrentObject:
    def __init__(self):
        pass


class Storage(object):
    pass



current_object = CurrentObject()


def pytest_addoption(parser):
    # -----------API part---------#
    parser.addoption("--api", action="store_true", default=False, help="Run API part of frau")
    # parser.addoption("--api", action="store", default="False", help="Run API part of frau")
    parser.addoption("--service", action="store", default="VS", help="Set up application on project")
    parser.addoption("--server_url", action="store", default="http://den02mqu.us.oracle.com:7001",
                     help="base url")

    # -----------Web part---------#
    # browsers = {'firefox': 'firefox',
    #             'ie': 'ie',
    #             'chrome': 'chrome',
    #             'edge': 'edge'}
    parser.addoption("--browser", action="store", default="chrome",
                     type='choice', choices=['chrome',
                                             'ie',
                                             'edge',
                                             'firefox',
                                             'phantomjs'],
                     help='Runs tests only for given browser')
    if os.name != 'nt':
        parser.addoption("--base_url", action="store",
                         default="https://app-staging.latista.com",
                         choices=["https://testing-obn.latista.com",
                                  "https://app-staging.latista.com",
                                  "https://app-staging-beta.latista.com"],
                         help="base server https://URL")
        parser.addoption("--ipa", action="store",
                         default=sys.path[0] + "/iOS/Latista.app",
                         # os.path.abspath(os.path.join(os.path.dirname(__file__), "iOS/Latista.app")),
                         help="ipa")
    else:
        parser.addoption("--base_url", action="store",
                         default="https://app-staging.latista.com",
                         choices=["https://testing-obn.latista.com",
                                  "https://app-staging.latista.com",
                                  "https://app-staging-beta.latista.com"],
                         help="base server https://URL")
    parser.addoption("--work_dir", action="store",
                     default=os.path.abspath(os.path.join(os.path.dirname(__file__), 'work_dir')),
                     help="path to dir with input data")
    parser.addoption("--temp_res", action="store",
                     default=os.path.join(os.path.dirname(__file__), 'temp_res'),
                     help="path to dir with TEMP OUTPUT")
    parser.addoption("--latista_version", action="store_true", dest="verbose",
                     help="Get about latista version for Allure report")
    parser.addoption("--runslow", action="store_true",
                     help="need --runslow option to run")

    # -----------Droid part---------#
    parser.addoption("--apk", action="store",
                     default=os.path.abspath(os.path.join(os.path.dirname(__file__), "Droid\Latista.apk")),
                     help="app")
    parser.addoption("--package", action="store",
                     default="com.latista.android",
                     help="package")
    parser.addoption("--activity", action="store",
                     default="md56044dd347302a594c9d34e97177693d2.MainActivity",
                     help="package")

    # -----------iOS part---------#

    parser.addoption("--simulate", action="store", default="iPad Air 2",
                     help="type of simulator")
    parser.addoption("--version_ios", action="store", default="10.2",
                     help="ios version")
    parser.addoption("--version_app", action="store", default="16.1.2",
                     help="ios version")
    parser.addoption("--fullReset", action="store", default="False",
                     help="full reset appium server")
    parser.addoption("--noReset", action="store", default="True",
                     help="reset appium server")

    from sys import platform as _platform

    if _platform == "win32":  # Windows
        parser.addoption("--web", action="store_true", default=True, help="platform")
    else:
        parser.addoption("--web", action="store_true", default=False, help="platform")

    if _platform == "darwin":  # MAC OS X
        parser.addoption("--ios", action="store_true", default=True, help="platform")
    else:
        parser.addoption("--ios", action="store_true", default=False, help="platform")

    parser.addoption("--droid", action="store_true", default=False, help="platform")

    parser.addoption("--cross", action="store_true", default=False, help="run cross tests")


@pytest.fixture(scope="session")
def optns(request):
    ops = {'web': {}, 'ios': {}, 'droid': {}, 'api': {}}
    ops['api']['run'] = request.config.getoption("--api")
    ops['api']['url'] = request.config.getoption("--server_url")
    ops['api']['service'] = request.config.getoption("--service")
    ops['web']['run'] = request.config.getoption("--web")
    ops['web']['browser_type'] = request.config.getoption("--browser")
    ops['web']['base_url'] = request.config.getoption("--base_url")
    ops['web']['work_dir'] = request.config.getoption("--work_dir")
    ops['web']['temp_res_dir'] = request.config.getoption("--temp_res")
    ops['web']['version'] = request.config.getoption("--latista_version")
    ops['web']['runslow'] = request.config.getoption("--runslow")

    if os.name != 'nt':


        ops['ios']['ipa'] = request.config.getoption("--ipa")
        ops['ios']['simulator'] = request.config.getoption("--simulate")
        ops['ios']['version_ios'] = request.config.getoption("--version_ios")
        ops['ios']['version_app'] = request.config.getoption("--version_app")
        ops['ios']['fullReset'] = request.config.getoption("--fullReset")
        ops['ios']['noReset'] = request.config.getoption("--noReset")

    ops['ios']['run'] = request.config.getoption("--ios")
    ops['ios']['cross'] = request.config.getoption("--cross")

    ops['droid']['run'] = request.config.getoption("--droid")
    ops['droid']['apk'] = request.config.getoption("--apk")
    ops['droid']['package'] = request.config.getoption("--package")
    ops['droid']['activity'] = request.config.getoption("--activity")
    return ops


# ------------Global App---------#
@pytest.fixture(scope="session")
def app(optns, request, storage):
    if optns['api']['run']:
        current_object.api = api_app(optns['api']['service'], optns['api']['url'])
    else:
        if optns['web']['run']:
            current_object.web = web_app(optns['web']['browser_type'],
                                         optns['web']['base_url'],
                                         optns['web']['work_dir'],
                                         optns['web']['temp_res_dir'],
                                         optns['web']['version'],
                                         storage,
                                         env)
            # allure.issue.tracker.pattern = 'https://jira.latista.com/browse/%s'
            allure.environment(browser=optns['web']['browser_type'], server=optns['web']['base_url'])
            # current_object.web.personal_browser_window_positional_size()

        if optns['ios']['run'] and os.name != 'nt':
            import iOS
            from iOS.application import Application as ios_app
            import iOS.global_driver as global_driver
            ios_driver = init_ios_driver(optns['ios']['ipa'],
                                                         optns['ios']['simulator'],
                                                         optns['ios']['version_ios'],
                                                         optns['ios']['fullReset'],
                                                         optns['ios']['noReset'])
            #current_object.ios = ios_app(ios_driver, storage, env, platform_flag(optns), version_app_flag(optns))
            global_driver.driver = ios_driver
            current_object.ios = ios_app(optns['web']['base_url'], storage)
            #global_driver.driver = ios_driver

        if optns['droid']['run']:
            current_object.droid = droid_app(init_droid_driver(optns['droid']['apk'],
                                                               optns['droid']['package'],
                                                               not optns['droid']['activity']),
                                             storage)
    return current_object


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if optns(request)['web']['run']:
            # current_object.web.attach_current_url()
            # current_object.web.attach_screenshot()
            # current_object.web.attach_console_log()
            try:
                current_object.web.terminate()
            except AttributeError:
                print('fin() EXCEPTION')
        if optns(request)['ios']['run'] and os.name != 'nt':
            print("resource_teardown")
            pass
        if optns(request)['droid']['run']:
            current_object.droid.terminate()

    request.addfinalizer(fin)
    return current_object


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

        if call.excinfo is not None:
            if call.excinfo.typename and call.excinfo.typename != 'XFailed':

                if "jenkins_ios_work_test" in item.keywords:
                    try:
                        current_object.ios.attach_screenshot()
                    except:
                        print('screenshot can not be attached')

                if "droid_jenkins" in item.keywords:
                    # TODO print normal assert
                    current_object.droid.attach_screenshot()
                    current_object.droid.hints_in_app.hp.ok_btn.click()

                if "web_jenkins" in item.keywords:
                    try:
                        current_object.web.attach_screenshot()
                        # current_object.web.attach_current_url()
                        current_object.web.attach_console_log()
                    except UnexpectedAlertPresentException:
                        print('UnexpectedAlertPresentException')
                        current_object.web.driver.switch_to_alert().accept()
                        print('pytest_runtest_makereport switch_to_alert().accept()')
                        current_object.web.attach_screenshot()
                        # current_object.web.attach_current_url()
                        current_object.web.attach_console_log()
                    except:
                        print('screenshot or console_log can not be attached')

            elif call.excinfo.typename != 'XFailed':
                print('excinfo: ', call.excinfo.typename)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            # @allure.severity('minor')
            severity = previousfailed.keywords._markers.get("allure_label.severity")
            if severity:
                if 'minor' in severity.args:
                    return
            pytest.xfail("previous test failed (%s)" % previousfailed.name)


def init_droid_driver(apk, package, activity):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '21'  # '22'#'23' #'19'
    desired_caps['deviceName'] = 'Android Emulator'  # 'Android' #'Android Emulator'
    desired_caps['app'] = apk
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    # return ad.Remote('http://ondemand.saucelabs.com:80', desired_caps)
    return appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # return ad.Remote('http://192.168.40.86:4444/wd/hub', desired_caps)


def init_ios_driver(ipa, simulator, version, f_reset, n_reset):
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = version
    desired_caps['deviceName'] = simulator
    desired_caps['app'] = ipa
    desired_caps['orientation'] = "LANDSCAPE"
    desired_caps['fullReset'] = f_reset
    desired_caps['noReset'] = n_reset

    return appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


@pytest.fixture(scope="session", autouse=True)
def storage(request):
    return Storage


@pytest.fixture(scope="session")
def env(request, optns):
    if optns['api']['run']:
        return work_dir.environment
    else:
        if 'testing' in optns['web']['base_url']:
            return work_dir.environment_testing
        elif 'staging' in optns['web']['base_url'] and not optns['ios']['cross']:
            return work_dir.environment_staging
        else:
            return work_dir.environment_cross


@pytest.fixture
def slow(request):
    return pytest.mark.skipif(
        not request.config.getoption("--runslow"),
        reason="need --runslow option to run"
    )


# @pytest.fixture(scope="session", autouse=True)
def platform_flag(optns):
    platform  = optns['ios']['version_ios']
    return platform

# @pytest.fixture(scope="session", autouse=True)
def version_app_flag(optns):
    return optns['ios']['version_app'] == '16.1.2'
