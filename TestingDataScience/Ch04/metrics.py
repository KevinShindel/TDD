import pandas as pd


def load_metrics(jsonl_file):
    return pd.read_json(
        jsonl_file,
        orient='records',
        lines=True,
        convert_dates=['time'],
    )


def get_file_path():
    from pathlib import Path
    here = Path(__file__).absolute().parent.parent / 'data'
    jsonl_file = here / 'metrics.jsonl'
    return jsonl_file
