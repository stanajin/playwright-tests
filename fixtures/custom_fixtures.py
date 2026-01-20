import pytest
import json
import os

@pytest.fixture(scope="session")
def load_test_data():
    """
    Example fixture that reads data from the data/ directory.
    """
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_data.json')
    with open(data_path, 'r') as f:
        data = json.load(f)
    return data

@pytest.fixture
def sample_user(load_test_data):
    """
    Returns a sample user from the loaded test data.
    """
    return load_test_data['users']['valid_user']
