import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
        
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            [sys.executable, abs_file_path, *args],
            capture_output=True,
            text=True,
            timeout=30)

        if not result.stdout and result.stderr:
            return "No output produced."

        response = []

        if result.stdout:
            response.append(f"STDOUT: {result.stdout}")

        if result.stderr:
            response.append(f"STDERR: {result.stderr}")

        if result.returncode != 0:
            response.append(f"Process exited with code {result.returncode}")
    
        return "\n".join(response)

    except Exception as e:
        return f"Error: executing Python file: {e}"