import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        if not os.path.isdir(working_directory):
                return f'Error: "{working_directory}" is not a directory'
    
        path_workingdir = os.path.abspath(working_directory)
        path_target_file = os.path.normpath(os.path.join(path_workingdir, file_path))
        valid_target_file :bool = os.path.commonpath([path_workingdir,path_target_file]) == path_workingdir
        if not valid_target_file:
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path_target_file):
                return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(path_target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                    file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
          return f"Error: Error when reading file '{file_path}': {e}"             

    
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Reads the content of a file.",
        "parameters": {
                "type": "object",
                "properties": {
                        "file_path": {
                                "type": "string",
                                "description": "Path to the file whose contents to read out, relative to the working directory (default is the working directory itself)",
                        },
                "required": ["file_path"],

            },
        },
    },
}

        