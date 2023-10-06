# llm-together

[![PyPI](https://img.shields.io/pypi/v/llm-together.svg)](https://pypi.org/project/llm-together/)
[![Changelog](https://img.shields.io/github/v/release/accudio/llm-together?include_prereleases&label=changelog)](https://github.com/wearedevx/llm-together/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/wearedevx/llm-together/blob/main/LICENSE)

Plugin for [LLM](https://llm.datasette.io/) adding support for [Together](https://together.ai/)

## Installation

Install this plugin in the same environment as LLM.
```bash
llm install llm-together
```
## Configuration

You will need an API key from Together. You can obtain one by creating an account and going to 'API Keys'.

You can set that as an environment variable called `TOGETHER_API_KEY`, or add it to the `llm` set of saved keys using:

```bash
llm keys set together
```
```bash
Enter key: <paste key here>
```

## Usage

This plugin adds together models that support inference without VM start to increase speed.

```bash
llm models list
```

```bash
llm -m <one-together-model> "Three names for my new ai project"
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-together
python3 -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

## Test

Execute unit test with:

```bash
pytest
```
