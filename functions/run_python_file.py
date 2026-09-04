import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
            
        path_workingdir = os.path.abspath(working_directory)
        path_target_file = os.path.normpath(os.path.join(path_workingdir, file_path))
        valid_target_file :bool = os.path.commonpath([path_workingdir,path_target_file]) == path_workingdir
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(path_target_file):
                return f'Error: "{file_path}" does not exists or is not a regular file'
        if not path_target_file[-3:] == ".py":
             return f'Error: "{file_path}" is not a Python file'
        command = ["python", path_target_file]
        if args is not None:
            command.extend(args)
        completed_process = subprocess.run(command,text=True, timeout=30, capture_output=True,cwd = path_workingdir)
        output_list = []
        if completed_process.returncode !=0:
             output_list.append(f"Process exited with code {completed_process.returncode}")
        if completed_process.stdout == "" and completed_process.stderr == "":
             output_list.append("No output produced")
        if completed_process.stdout != "":
             output_list.append(f"STDOUT: {completed_process.stdout}")
        if completed_process.stderr != "":
                     output_list.append(f"STDERR: {completed_process.stderr}")
        return "\n".join(output_list)


        
    except Exception as e:
        return f"Error: Error when executing the file '{file_path}': {e}" 




schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": f"Runs a python file from the working directory specified by name and given in with potential arguments given as a array of strings.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the python file to run, relative to the working directory (default is the working directory itself)",
                },
                "args" :{
                     "type": "array[str] | None",
                     "description": "Arguments for the python file to run (default is None)"
                },
                
            },
            "required": ["file_path"]
        },
    },
}