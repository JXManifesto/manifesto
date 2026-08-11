#!/usr/bin/env bash
set -euo pipefail

CFF_SCHEMA_URL="https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json"
ZENODO_SCHEMA_URL="https://raw.githubusercontent.com/zenodo/zenodo/d8e8315c0bc4dd643b46a5e741c9f18bf51873ad/zenodo/modules/deposit/jsonschemas/deposits/records/legacyrecord.json"

check-jsonschema --schemafile "$CFF_SCHEMA_URL" CITATION.cff
check-jsonschema --schemafile "$ZENODO_SCHEMA_URL" .zenodo.json
