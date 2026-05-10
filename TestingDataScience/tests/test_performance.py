import json
from timeit import timeit

from psutil import Process


def test_memory(forest_model, regression_data):
    proc = Process()
    mem_before = proc.memory_info().rss
    forest_model.clf.predict(regression_data.X)
    mem_after = proc.memory_info().rss
    report = {
        'model_version': forest_model.version,
        'data_version': regression_data.version,
        'mem_usage': mem_after - mem_before
    }
    print(f'memory: {json.dumps(report)}')
    # TODO: Report to regression database (Prometheus, InfluxDB ...)


def test_performance(forest_model, regression_data):
    n_times = 100
    duration = timeit(
        'forest_model.clf.predict(regression_data.X)',
        number=n_times,
        globals=locals(),
    )
    report = {
        'model_version': forest_model.version,
        'data_version': regression_data.version,
        'avg_time': duration / n_times,
        'n_times': n_times,
    }
    print(f'performance: {json.dumps(report)}')
    # TODO: Report to regression database (Prometheus, InfluxDB ...)