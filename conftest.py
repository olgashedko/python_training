import importlib
import json
import os.path

import jsonpickle
import pytest
from fixture.db import DbFixture
from fixture.application import Application
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture()
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    db_fixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                           password=db_config['password'])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture1 in metafunc.fixturenames:
        if fixture1.startswith("data_"):
            testdata = load_from_module(fixture1[5:])
            metafunc.parametrize(fixture1, testdata, ids=[str(x) for x in testdata])
        elif fixture1.startswith("json_"):
            testdata = load_from_json(fixture1[5:])
            metafunc.parametrize(fixture1, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


@pytest.fixture(scope="session")
def ormdb(request):
    ormdb_config = load_config(request.config.getoption("--target"))['db']
    ormdb_fixture = ORMFixture(host=ormdb_config['host'], name=ormdb_config['name'], user=ormdb_config['user'],
                               password=ormdb_config['password'])
    return ormdb_fixture
