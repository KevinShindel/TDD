from Ch04.metrics import load_metrics, get_file_path
from pandera import DataFrameSchema, Column, Float64, Check, String, check_output
from pandas import DatetimeTZDtype

metric_schema = DataFrameSchema({
    'time': Column(DatetimeTZDtype('ns', 'UTC')),
    'metric': Column(String, checks=Check.isin({'cpu', 'mem'})),
    'value': Column(Float64, checks=Check.greater_than(0))
})


@check_output(metric_schema)
def test_metric_output():
    metric = load_metrics(get_file_path())
    return metric


def test_valid_df():
    metric = load_metrics(get_file_path())
    metric_schema.validate(metric)

