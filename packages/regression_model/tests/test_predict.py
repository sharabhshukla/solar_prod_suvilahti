import math

from regression_model.predict import make_prediction
from regression_model.processing.data_management import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(filename='test.csv')
    single_test_json = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_json)

    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0], float)

def test_make_multiple_predictions():
    # Given
    test_data = load_dataset(filename='test.csv')
    original_data_length = len(test_data)
    multiple_test_json = test_data

    # When
    subject = make_prediction(input_data=multiple_test_json)

    # Then
    assert subject is not None

    # We expect some rows to be filtered out
    assert len(subject.get('predictions')) == original_data_length