from functions.get_files_info import get_files_info

print(f'Result for current directory:')
print(get_files_info("calculator", "."))
for dir in [ "pkg", "/bin", "../"]:
    print(f"Result for '{dir}' directory:")
    print(get_files_info("calculator", dir))


