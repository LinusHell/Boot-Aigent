import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        
        path_workingdir = os.path.abspath(working_directory)
        path_target_file = os.path.normpath(os.path.join(path_workingdir, file_path))
        valid_target_file :bool = os.path.commonpath([path_workingdir,path_target_file]) == path_workingdir
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(path_target_file):
             return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(path_target_file),exist_ok=True)
        with open(path_target_file, "w") as f:
             f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
           return f"Error: Error when writing to file '{file_path}': {e}" 



schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": f"Overwrites a file with content given in as an input of the function. If the file does not yet first creates the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to overwrite and possibly create, relative to the working directory (default is the working directory itself)",
                },
                "content" :{
                     "type": "string",
                     "description": "Content to write into the file"
                }, 
            },
            "required": ["file_path","content"]
        },
    },
}