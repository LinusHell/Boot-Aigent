from functions.get_file_content import get_file_content

print("Result for 'lorem.txt' in 'calculator' directory:")
result = get_file_content("calculator","lorem.txt")
print(f"lorem.txt length:{len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

for file in ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
    print(f"Results for file: {file}:")
    print(get_file_content("calculator", file))

