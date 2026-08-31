import os
import re
import shutil
import sys

PROJECT_SLUG = "{{ cookiecutter.project_slug }}"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
TOOL_NAME = "{{ cookiecutter.tool_name }}"
INCLUDE_MAKEFILE = "{{ cookiecutter.include_makefile }}"
INCLUDE_TOOLS = "{{ cookiecutter.include_tools }}"

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")
PYTHON_NAME_RE = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")


def fail(message: str) -> None:
    print(f"[cookiecutter] {message}", file=sys.stderr)
    raise SystemExit(1)


if not SLUG_RE.fullmatch(PROJECT_SLUG):
    fail("project_slug must start with a lowercase letter and contain only lowercase letters, numbers and hyphens")

for label, value in {"package_name": PACKAGE_NAME, "tool_name": TOOL_NAME}.items():
    if not PYTHON_NAME_RE.fullmatch(value):
        fail(f"{label} must be a valid Python package name (letters, numbers and underscores)")

if INCLUDE_MAKEFILE != "y" and os.path.exists("Makefile"):
    os.remove("Makefile")
    print("Removed Makefile because include_makefile was set to 'n'.")

if INCLUDE_TOOLS != "y" and os.path.exists("src"):
    shutil.rmtree("src")
    print("Removed src/ because include_tools was set to 'n'.")
