import json

import pytest
from gradient_boosting_model.processing.data_management import load_dataset

from tests.test_api import SECONDARY_VARIABLES_TO_RENAME
from .compare import compare_differences


@pytest.mark.differential
def test_model_prediction_differentials(client):
    test_inputs_df = load_dataset(file_name="test.csv")
    old_model_inputs_df = test_inputs_df.rename(
        columns=SECONDARY_VARIABLES_TO_RENAME
    )

    # new model의 예측
    new_model_response = client.post(
        "v1/predictions/gradient", json=test_inputs_df.to_dict(orient="records")
    )
    new_model_predictions = json.loads(new_model_response.data)["predictions"]

    # old model의 예측
    old_model_response = client.post(
        "v1/predictions/regression",
        json=old_model_inputs_df.to_dict(orient="records"),
    )
    old_model_predictions = json.loads(old_model_response.data)["predictions"]

    # 각 model의 예측값 10개를 이용
    # 예측값의 차이가 많이 나면 test fail
    compare_differences(
        expected_predictions=new_model_predictions[:10],
        actual_predictions=old_model_predictions[:10],
        rel_tol=0.2,
    )
