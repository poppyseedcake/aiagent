import os
from google import genai
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path_full_path = os.path.abspath(full_path)
    abs_path_working = os.path.abspath(working_directory)
    abs_work_with_sep = abs_path_working if abs_path_working.endswith(os.sep) else abs_path_working + os.sep
    
    if not (abs_path_full_path == abs_path_working or abs_path_full_path.startswith(abs_work_with_sep)):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    try:
        if not os.path.isdir(abs_path_full_path):
            return(f'Error: "{directory}" is not a directory')
    except Exception as e:
        return (f"Error: {e}")

    try:
        dir_content = os.listdir(abs_path_full_path)
    except Exception as e:
        return (f"Error: {e}")

    response_list = []
    for item in dir_content:
        try:
            item_path = os.path.join(abs_path_full_path, item)
            response_list.append(f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")
        except Exception as e:
            return (f"Error: {e}")
    return "\n".join(response_list)
