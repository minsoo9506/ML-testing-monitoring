import pytest
from sklearn.model_selection import train_test_split

from gradient_boosting_model.config.core import config
from gradient_boosting_model.processing.data_management import load_dataset

@pytest.fixture(scope='session')
def pipiline_inputs():
    data = load_dataset(file_name=config.app_config.training_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state
    )

    return X_train, X_test, y_train, y_test

@pytest.fixture()
def raw_training_data():
    return load_dataset(file_name=config.app_config.training_data_file)

@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)