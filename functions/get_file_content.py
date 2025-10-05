import os
from config import *
from google import genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets file content in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file we want read content, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_path_full_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    abs_work_with_sep = abs_path_working if abs_path_working.endswith(os.sep) else abs_path_working + os.sep
    
    if not (abs_path_full_path == abs_path_working or abs_path_full_path.startswith(abs_work_with_sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path_full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f"Error: {e}"
