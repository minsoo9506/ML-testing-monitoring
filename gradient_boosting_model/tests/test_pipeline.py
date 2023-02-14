from gradient_boosting_model import pipeline
from gradient_boosting_model.config.core import config
from gradient_boosting_model.processing.validation import validate_inputs


def test_pipeline_drops_unnecessary_features(pipeline_inputs):
    X_train, _, y_train, _ = pipeline_inputs
    assert config.model_config.drop_features in X_train.columns
    pipeline.price_pipe.fit(X_train, y_train)

    transformed_inputs = pipeline.price_pipe[:-1].transform(X_train)

    assert config.model_config.drop_features in X_train.columns
    assert config.model_config.drop_features not in transformed_inputs.columns


def test_pipeline_transforms_temporal_features(pipeline_inputs):
    X_train, _, _, _ = pipeline_inputs

    transformed_inputs = pipeline.price_pipe[:-1].transform(X_train)

    assert (
        transformed_inputs.iloc[0]["YearRemodAdd"]
        == X_train.iloc[0]["YrSold"] - X_train.iloc[0]["YearRemodAdd"]
    )


def test_pipeline_predict_takes_validated_input(pipeline_inputs, sample_input_data):
    X_train, _, y_train, _ = pipeline_inputs
    pipeline.price_pipe.fit(X_train, y_train)

    validated_inputs, errors = validate_inputs(input_data=sample_input_data)
    predictions = pipeline.price_pipe.predict(
        validated_inputs[config.model_config.features]
    )

    assert predictions is not None
    assert errors is None