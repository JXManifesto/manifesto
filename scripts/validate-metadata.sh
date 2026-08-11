#!/usr/bin/env bash
set -euo pipefail

CFF_SCHEMA_URL="https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json"

check-jsonschema --schemafile "$CFF_SCHEMA_URL" CITATION.cff
python scripts/validate-zenodo.py
