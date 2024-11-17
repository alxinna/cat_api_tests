import json
import os
from typing import Union, List, Dict

from _pytest.fixtures import fixture

from modules.dataclass_collection import TestArgsApi
from setup.cat_api import CatAPISuite


@fixture(scope='session')
def test_args() -> TestArgsApi:
    return TestArgsApi()


@fixture(scope='module')
def cat_api(test_args: TestArgsApi):
    return CatAPISuite(args=test_args)


@fixture(scope='function')
def test_parameter(request):
    return request.param[0] if len(request.param) == 1 else request.param


def pytest_generate_tests(metafunc):
    """
    predefined pytest function to be able to parametrize tests of fixtures
    :param metafunc: pytest object
    """
    # Get path to json files
    paths_to_files = get_path_to_test_data_param_file(metafunc)
    # Read json file
    for path in paths_to_files:
        data: Union[List, Dict] = read_json_file(path)
        # Check if file is iterable
        if not isinstance(data, list):
            raise Exception(f'The file cannot be used for parametrization {paths_to_files} as is it not iterable')
        # Parametrize the test from the file data
        params = list()
        ids = list()
        for item in data:
            params.append((item['param'],))
            ids.append(item.get('id'))
        metafunc.parametrize("test_parameter", params, ids=ids, indirect=True)


def get_path_to_test_data_param_file(metafunc):
    # Get path to test data root folder
    path_to_test_data = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "../", "test_data"
    )
    paths = list()
    # Check if "params_to_file" marker exists
    for marker in metafunc.definition.own_markers:
        if marker.name == "params_from_file":
            # append path to file for parametrization
            paths.append(
                os.path.join(path_to_test_data, marker.kwargs['filename'])
            )
    return paths


def read_json_file(path_to_file):
    if not os.path.exists(path_to_file):
        raise Exception(f'The json file is not found {path_to_file}')
    with open(path_to_file, 'r+') as f:
        data: Union[Dict, List] = json.load(f)
    return data
