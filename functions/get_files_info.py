import os

def get_files_info(working_directory, directory="."):
    if not os.path.isdir(directory):
        raise Exception(f'Error: "{directory}" is not a directory')

    abs_path = os.path.abspath(directory)
    full_path = os.path.join(working_directory, directory)

    if not abs_path.startswitch(working_directory):
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    dir_content = os.listdir(directory)
    response_list = []
    for item in dir_content:
        response_list.append(f"- {item}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}")
    return response_list.join("\n")
