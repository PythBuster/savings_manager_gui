import tomllib
from pathlib import Path
from typing import Any


def get_app_data() -> dict[str, Any]:
    """Extract app information from pyproject.toml.

    :return: The app data section from pyproject.toml as dict
    :rtype: :class:`dict[str, Any]`
    """

    pyproject_file_path = Path(__file__).resolve().parent.parent / "pyproject.toml"

    with pyproject_file_path.open(mode="rb") as pyproject_file:
        pyproject_data = tomllib.load(pyproject_file)

    return pyproject_data["tool"]["poetry"]