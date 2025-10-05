from functions.run_python_file import run_python_file

def print_result(title, result):
    print(title)
    if result.startswith("Error:"):
        print("    " + result)
    else:
        print(result)

test1 = run_python_file("calculator", "main.py") 
#test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet") 
#test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#test3 = get_file_content("calculator", "/bin/cat")
#test4 = get_file_content("calculator", "pkg/does_not_exist.py")
#
print(test1)
#print(test2)
#print(test3)
#print(test4)
#
#print_result("Result for current directory:", test1)
#print_result("Result for 'pkg' directory:", test2)
#print_result("Result for '/bin' directory:", test3)
#print_result("Result for '../' directory:", test4)