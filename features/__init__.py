import os
import glob
import importlib

# Automatically import modules from all Python files in this folder
module_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))

for module_file in module_files:
    module_name = os.path.basename(module_file)[:-3]  # Remove '.py' extension
    if module_name != "__init__":  # Avoid importing the __init__.py file itself
        importlib.import_module(f".{module_name}", package=__name__)
