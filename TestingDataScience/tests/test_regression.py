import json

from sklearn.metrics import accuracy_score


def test_regression(pipeline_model, regression_data):
    out = pipeline_model.clf.predict(regression_data.X)
    score = accuracy_score(regression_data.y, out)
    report = {
        'model_version': pipeline_model.version,
        'data_version': regression_data.version,
        'accuracy': score,
    }
    print(f'regression: {json.dumps(report)}')
    # TODO: Report to regression database (Prometheus, InfluxDB ...)