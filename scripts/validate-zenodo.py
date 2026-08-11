#!/usr/bin/env python3
"""Validate .zenodo.json against Zenodo's legacy schema and documented fields."""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

from jsonschema import Draft4Validator, FormatChecker

SCHEMA_URL = (
    "https://raw.githubusercontent.com/zenodo/zenodo/"
    "d8e8315c0bc4dd643b46a5e741c9f18bf51873ad/"
    "zenodo/modules/deposit/jsonschemas/deposits/records/legacyrecord.json"
)

with urllib.request.urlopen(SCHEMA_URL, timeout=30) as response:
    schema = json.load(response)

# Zenodo documents these fields for deposit metadata, but its linked legacy
# GitHub schema predates them. Keep the official schema strict while extending
# it only with the two documented properties used by this repository.
schema["properties"]["version"] = {"type": "string", "minLength": 1}
schema["properties"]["language"] = {
    "type": "string",
    "pattern": "^[a-z]{3}$",
}

metadata = json.loads(Path(".zenodo.json").read_text(encoding="utf-8"))
validator = Draft4Validator(schema, format_checker=FormatChecker())
errors = sorted(validator.iter_errors(metadata), key=lambda error: list(error.path))

if errors:
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        print(f".zenodo.json:{location}: {error.message}", file=sys.stderr)
    raise SystemExit(1)

print("ok -- .zenodo.json matches the Zenodo metadata schema")
