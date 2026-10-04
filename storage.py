"""Reads and writes the app's data file. Everything lives in one JSON file."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "studysprint.json"


def load_data(path=DATA_FILE):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data, path=DATA_FILE):
    with open(path, "r", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
