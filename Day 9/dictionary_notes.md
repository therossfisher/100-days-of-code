# Dictionary Methods — Notes

Quick reference for the three main ways to loop over or pull data from a Python dictionary.

## `.keys()`

Gives you just the keys, on their own.

```python
student_scores = {'Harry': 88, 'Ron': 78}
for name in student_scores.keys():
    print(name)
# prints: Harry, Ron
```

**Use case**: when you only care about *what exists* (names, categories, IDs) and don't need the values yet.

Note: `for name in student_scores:` (no `.keys()` at all) does the exact same thing — Python defaults to keys when you loop over a dictionary plainly. `.keys()` is mostly there for clarity, or when you need to explicitly convert it to a list: `list(student_scores.keys())`.

## `.values()`

Gives you just the values, on their own.

```python
for score in student_scores.values():
    print(score)
# prints: 88, 78
```

**Use case**: when you need to do math or comparisons across all the values but don't care whose value it is — like finding the highest score, or averaging them, without needing names at all.

```python
highest = max(student_scores.values())  # 88
```

## `.items()`

Gives you key and value **together**, paired, for each entry.

```python
for name, score in student_scores.items():
    print(name, "scored", score)
# prints: Harry scored 88 / Ron scored 78
```

**Use case**: any time you need both pieces of information at once to make a decision — e.g. building a new dictionary keyed by name, where you need to know *whose* value you're looking at (`student_grades[name] = grade`). Using `.values()` alone would give the score with no way to know which student it belonged to.

## Quick way to pick

Ask: do I need the key, the value, or both, to do what I'm trying to do? That answer tells you which method to reach for.

## Getting a value by position (e.g. "the third value")

Dictionaries preserve insertion order (Python 3.7+), but there's no built-in `dict[2]`-style index access like lists have. Convert to a list first:

```python
student_scores = {'Harry': 88, 'Ron': 78, 'Hermione': 95}

values_list = list(student_scores.values())
print(values_list[2])   # 95 - third item, indexing starts at 0
```

Same trick works for keys: `list(student_scores.keys())[2]` gets the third key.

Note: needing "the Nth item" a lot from a dictionary can be a sign a list (or list of tuples) might fit the data better - dictionaries are meant to be looked up by key, not position.

## Nested dictionaries/lists inside a dictionary

No separate method needed - just chain the access together, one layer at a time:

```python
students = {
    "Harry": {"score": 88, "subjects": ["Potions", "Herbology"]},
    "Ron": {"score": 78, "subjects": ["Charms"]}
}

print(students["Harry"]["score"])          # 88 - dict inside a dict
print(students["Harry"]["subjects"][0])    # "Potions" - list inside a dict inside a dict
```

Read left to right: `students["Harry"]` gets Harry's entire inner dictionary, `["score"]` then reaches into that inner dictionary for one value. Same idea for the list - `["subjects"]` gets the whole list, `[0]` grabs the first item by normal list indexing.

Looping through nested structures uses the same `.items()`/`.values()`, just applied at each level:

```python
for name, info in students.items():
    print(name, "scored", info["score"])
```