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
def test_together_response(together):
    mock_response = Mock()
    mock_response.last = "hello"

    together.Complete.create.return_value = {
        "output": {
            "choices": [
                {
                    "text": "hello"
                }
            ]
        }
    }

    prompt = Prompt("hello", "")

    model = Together( {"name": "models/text-bison-001", "config": {}})
    items = list(model.response(prompt))
    
    assert items == ["hello"]


# @patch.dict(os.environ, {"TOGETHER_API_KEY": "X"})
# @patch("llm_together.together")
# def test_together_models(mock_together):
#     fake_models = [
#         {"name": "'models/chat-bison-001"},
#         {"name": "models/text-bison-001"},
#     ]
#     # Mock together.list_models()
#     mock_together.list_models.return_value = fake_models
#     runner = CliRunner()
#     result = runner.invoke(cli, ["together", "models"])
#     assert result.exit_code == 0, result.output
#     assert ast.literal_eval(result.output) == fake_models


# @patch.dict(os.environ, {"TOGETHER_API_KEY": "X"})
# @patch("llm_together.together")
# def test_together_prompt(mock_together):
#     mock_response = Mock()
#     mock_response.last = "🐶🐶"
#     mock_together.chat.return_value = mock_response
#     runner = CliRunner()
#     result = runner.invoke(cli, ["two dog emoji", "-m", "together"])
#     assert result.exit_code == 0, result.output
#     assert result.output == "🐶🐶\n"


# @pytest.mark.parametrize(
#     "prompt,conversation_messages,expected",
#     (
#         ("hello", [], "hello"),
#         ("hello 2", [("user 1", "response 1")], ["user 1", "response 1", "hello 2"]),
#         (
#             "hello 3",
#             [("user 1", "response 1"), ("user 2", "response 2")],
#             ["user 1", "response 1", "user 2", "response 2", "hello 3"],
#         ),
#     ),
# )
# def test_build_prompt_messages(
#     prompt: str, conversation_messages: List[Tuple[str, str]], expected: List[str]
# ):
#     model = get_model("together2")
#     conversation = None
#     if conversation_messages:
#         conversation = model.conversation()
#         for prev_prompt, prev_response in conversation_messages:
#             conversation.responses.append(
#                 Response.fake(
#                     prompt=prev_prompt,
#                     model=model,
#                     system=None,
#                     response=prev_response,
#                 )
#             )

#     messages = model.build_prompt_messages(prompt, conversation)
#     assert messages == expected
