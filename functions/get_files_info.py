import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
    try:
        path_workingdir = os.path.abspath(working_directory)
        path_target_dir = os.path.normpath(os.path.join(path_workingdir, directory))
        valid_target_dir :bool = os.path.commonpath([path_workingdir,path_target_dir]) == path_workingdir
    except Exception as e:
         return "Error: When trying to determine the paths raised '{type(e).__name__}' with message '{e.args[0]}'"
    except:
         return "Error: When trying to determine the paths raised unknown Exception" 
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path_target_dir):
            return f'Error: "{directory}" is not a directory'
    try:
        files_in_target = os.listdir(path_target_dir)
    except Exception as e:
         return f'Error: {e.args} Could not list files in directory "{path_target_dir}"'
    files_information = []
    try:
        for file in files_in_target:
            files_information.append({"name" : file, "file_size" : os.path.getsize('/'.join([path_target_dir,file])), "is_dir" : os.path.isdir('/'.join([path_target_dir,file])) })
    except Exception as e:
         return f'Error: {e.args} Could not collect information about files in "{path_target_dir}"'
    info_string = ""
    for file_info in files_information:
         info_string += f'- {file_info["name"]}: file_size={file_info["file_size"]} bytes, is_dir={file_info["is_dir"]}\n'
    info_string = info_string.rstrip()
    return info_string 