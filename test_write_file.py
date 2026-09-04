from functions.write_file import write_file

print(f'Results for writing to "lorem.txt":')
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(f'Results for writing to "pkg/morelorem.txt":')
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(f'Results for writing to "/tmp/temp.txt":')
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))