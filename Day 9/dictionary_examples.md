### create a dictionary

```programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
```

`print(programming_dictionary["Bug"])
`

### adding an item to a dictionary
```
programming_dictionary["Loop"] = "The action of doing something over and over again."
```

### create an empty dictionary
`empty_dictionary = {}
`


### wipe an existing dictionary
`programming_dictionary = {}
`

### edit an item in a dictionary
`programming_dictionary["Bug"] = "A month in your computer."
`

### loop through a dictionary
```for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
```

### nesting lists and dictionaries
```capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
```

### nested list in dictionary
```travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
    "Germany":["Stutgart", "Berlin",]
}
```

### print Lille
```
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany":["Stutgart", "Berlin"],
}

print(travel_log["France"][1])

OR

for x in travel_log.values():
    if "Lille" in x:
        print(x[1])
```