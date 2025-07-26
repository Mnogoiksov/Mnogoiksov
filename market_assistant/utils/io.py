"""Utility functions for IO."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def get_data_path(*parts):
    return BASE_DIR / 'data' / Path(*parts)


def save_df(df, path):
    print(f"Saving dataframe to {path}")
    # TODO: implement real saving


def load_df(path):
    print(f"Loading dataframe from {path}")
    # TODO: implement real loading
    return {}
