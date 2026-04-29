import os
import shutil

# Cookiecutter will inject the user's answer into this string before running the script
include_tools = '{{ cookiecutter.include_tools }}'

# If the user chose 'n', delete the src directory and everything inside it
if include_tools != 'y':
    if os.path.exists('src'):
        shutil.rmtree('src')
        print("🗑️  Removed 'src' directory because include_tools was set to 'n'.")

