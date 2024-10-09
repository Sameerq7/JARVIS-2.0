import os
import glob

# Automatically import all functions from all Python files in this folder
module_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))

for module_file in module_files:
    module_name = os.path.basename(module_file)[:-3]  # Remove '.py' extension
    if module_name != "__init__":  # Avoid importing the __init__.py file itself
        exec(f"from .{module_name} import *")  # Import all from the module
