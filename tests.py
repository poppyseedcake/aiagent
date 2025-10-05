from functions.run_python_file import run_python_file

def print_result(title, result):
    print(title)
    if result.startswith("Error:"):
        print("    " + result)
    else:
        print(result)

test1 = run_python_file("calculator", "main.py") 
test2 = run_python_file("calculator", "main.py", ["3 + 5"]) 
test3 = run_python_file("calculator", "tests.py")
test4 = run_python_file("calculator", "../main.py")
test5 = run_python_file("calculator", "nonexistent.py")
#
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
#
#print_result("Result for current directory:", test1)
#print_result("Result for 'pkg' directory:", test2)
#print_result("Result for '/bin' directory:", test3)
#print_result("Result for '../' directory:", test4)