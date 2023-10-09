from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="llm-together",
    description="Plugin for LLM adding support for Together",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Kévin Quesada",
    url="https://github.com/wearedevx/llm-together",
    project_urls={
        "Issues": "https://github.com/wearedevx/llm-together/issues",
        "CI": "https://github.com/wearedevx/llm-together/actions",
        "Changelog": "https://github.com/wearedevx/llm-together/releases",
    },
    license="MIT",
    classifiers=["Apache-2.0"],
    version=VERSION,
    entry_points={"llm": ["together = llm_together"]},
    install_requires=["llm>=0.5", "together"],
    extras_require={"test": ["pytest"]}
)
