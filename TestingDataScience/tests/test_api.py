def test_metrics(client):  # client is fixtures from conftest.py
    rows = client.metrics()
    assert len(rows) > 0
