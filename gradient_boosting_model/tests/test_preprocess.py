from gradient_boosting_model.config.core import config
from gradient_boosting_model.processing import preprocessors as pp

def test_drop_unecessary_feature_transformer(pipeline_inputs):
    X_train, _, _, _ = pipeline_inputs
    assert config.model_config.drop_features in X_train.columns

    transformer = pp.DropUnecessaryFeatures(
        variables_to_drop=config.model_config.drop_features
    )

    X_transformed = transformer.transform(X_train)

    assert config.model_config.drop_features not in X_transformed.columns

def test_temporal_variable_estimator(pipeline_inputs):
    X_train, _, _, _ = pipeline_inputs

    transformer = pp.TemporalVariableEstimator(
        variables=config.model_config.temporal_vars,
        reference_variable=config.model_config.drop_features
    )

    X_transformed = transformer.transform(X_train)

    assert (
        X_transformed.iloc[0]['YearRemodAdd']
        == X_train.iloc[0]['YrSold'] - X_train.iloc[0]['YearRemodAdd']
    )