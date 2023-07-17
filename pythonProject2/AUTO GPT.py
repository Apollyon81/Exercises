"""Utilities for the json_fixes package."""
import json
import os
import re

from jsonschema import Draft7Validator
@@ -9,6 +10,7 @@

CFG = Config()
LLM_DEFAULT_RESPONSE_FORMAT = "llm_response_format_1"
LLM_RESPONSE_DIRECTORY = os.path.dirname(__file__)


def extract_char_position(error_message: str) -> int:
@@ -35,7 +37,8 @@ def validate_json(json_object: object, schema_name: str) -> dict | None:
    :param schema_name: str
    :type json_object: object
    """
    with open(f"autogpt/json_utils/{schema_name}.json", "r") as f:
    scheme_file = os.path.join(LLM_RESPONSE_DIRECTORY, f"{schema_name}.json")
    with open(scheme_file, "r") as f:
        schema = json.load(f)
    validator = Draft7Validator(schema)
