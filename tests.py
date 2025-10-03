from functions.get_files_info import get_files_info

def print_result(title, result):
    print(title)
    if result.startswith("Error:"):
        print("    " + result)
    else:
        print(result)

test1 = get_files_info("calculator", ".")
test2 = get_files_info("calculator", "pkg")
test3 = get_files_info("calculator", "/bin")
test4 = get_files_info("calculator", "../")

print_result("Result for current directory:", test1)
print_result("Result for 'pkg' directory:", test2)
print_result("Result for '/bin' directory:", test3)
print_result("Result for '../' directory:", test4)