
## Title Case Example
f_name = str(input("What is your first name?\n"))
l_name = str(input("What is your first last?\n"))

def format_name(f_name, l_name):
    print(f"Hello, {f_name.title()} {l_name.title()}! How do you do?")

format_name(f_name, l_name)

## Another title case example
def format_name(f_name, l_name):
   formatted_f_name = f_name.title()
   formatted_l_name = l_name.title()

   return f"{formatted_f_name} {formatted_l_name}"

# calling the function directly
# format_name("ALKSDNOiyyoiydosa", "ASYUIOYSApkah")

# assigning the function to a variable
formatted_string = format_name("ALKSDNOiyyoiydosa", "ASYUIOYSApkah")
print(formatted_string)

# function in a function example
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)