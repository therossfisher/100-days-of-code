## Title Case Example

```
f_name = str(input("What is your first name?\n"))
l_name = str(input("What is your first last?\n"))

def format_name(f_name, l_name):
    print(f"Hello, {f_name.title()} {l_name.title()}! How do you do?")



format_name(f_name, l_name)
```