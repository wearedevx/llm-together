import ast
from click.testing import CliRunner
from unittest.mock import patch, Mock
from llm_together import Together
from llm.cli import cli

from llm import Prompt, get_model, Response
import os
import pytest
from typing import List, Tuple


@patch("llm_together.together")
def test_together_response(mock_together):
    mock_together.Complete.create.return_value = {
        "output": {
            "choices": [
                {
                    "text": "hello"
                }
            ]
        }
    }
    mock_together.Complete.create_streaming.return_value = ["hello"]

    prompt = Prompt("hello", "")

    model = Together( {"name": "models/text-bison-001", "config": {}})
    items = list(model.response(prompt))
    
    assert items == ["hello"]
