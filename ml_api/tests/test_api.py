import json

import numpy as np
import pytest
from gradient_boosting_model.processing.data_management import load_dataset

@pytest.mark.integration
def test_health_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "ok"}

@pytest.mark.intgration
def test_prediction_endpoint(client):
    test_inputs_df = load_dataset(file_name="test.csv")
    input_length = len(test_inputs_df)  # test csv contains 1459 rows
    expected_output_length = input_length - 2  # we expect 2 rows to be filtered

    # When
    response = client.post(
        "/v1/predictions", json=test_inputs_df.to_dict(orient="records")
    )

    # Then
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["errors"] is None
    assert len(data["predictions"]) == expected_output_length

@pytest.mark.parametrize(
    "field, field_value, index, expected_error",
    (
        (
            "BldgType",
            1,  # expected str
            33,
            {"33": {"BldgType": ["Not a valid string."]}},
        ),
        (
            "GarageArea",  # model feature
            "abc",  # expected float
            45,
            {"45": {"GarageArea": ["Not a valid number."]}},
        ),
        (
            "CentralAir",
            np.nan,  # nan not allowed
            34,
            {"34": {"CentralAir": ["Field may not be null."]}},
        ),
        ("LotArea", "", 2, {"2": {"LotArea": ["Not a valid integer."]}},),
    ),
)

@pytest.mark.integration
def test_prediction_validation(field, field_value, index, expected_error, client):
    test_inputs_df = load_dataset(file_name="test.csv")  # dataframe

    # input에 일부러 틀린 값을 주고 예상되는 error가 맞는지 테스트 해본다
    test_inputs_df.loc[index, field] = field_value

    response = client.post(
        "/v1/predictions", json=test_inputs_df.to_dict(orient="records")
    )
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data == expected_error