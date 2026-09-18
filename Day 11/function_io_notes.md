# Function Inputs & Outputs — Quick Reference

## Reading a function: the checklist

**Find the inputs (parameters)**
Look at the `def` line — everything inside the parentheses. For each one, check: does the function actually *use* it, or is it sitting there unused?

**Find the outputs (`return`)**
Search the function body for `return`. Ask:
- How many values come after it, comma-separated?
- Is there only one `return`, or several in different `if`/`elif`/`else` branches? Do they all return the same things?
- Is there any path through the function that *doesn't* hit a `return` at all? (If so, it silently gives back `None` on that path.)

## Should something be a parameter?

Ask: does this function need info from *outside itself*, and could that info be different each time it's called? If yes → parameter.

If the function always works with the exact same thing no matter who calls it (like a fixed deck of cards), it usually doesn't need to be a parameter — it can just be referenced directly from the outer scope.

**Test**: could this function reasonably be called twice in the same program, wanting *different* values each time? If yes, that value should be a parameter, not assumed.

## Should it return what it took in?

Not necessarily. The real question: after this function finishes, what does the rest of the program need that it didn't have before? That's what gets returned — not a mechanical mirror of the parameter list.

- Modifies something the caller needs afterward → return it
- Calculates something new that didn't exist before → return that, even if it wasn't a parameter
- Uses a parameter internally but nothing about it needs to survive outside → no need to return it

## The scope rule (why `UnboundLocalError` happens)

Functions can automatically **read** variables from the outer/enclosing scope without needing them as parameters:

```python
cards = [11, 2, 3, 4]# Function Inputs & Outputs — Quick Reference

## Reading a function: the checklist

**Find the inputs (parameters)**
Look at the `def` line — everything inside the parentheses. For each one, check: does the function actually *use* it, or is it sitting there unused?

**Find the outputs (`return`)**
Search the function body for `return`. Ask:
- How many values come after it, comma-separated?
- Is there only one `return`, or several in different `if`/`elif`/`else` branches? Do they all return the same things?
- Is there any path through the function that *doesn't* hit a `return` at all? (If so, it silently gives back `None` on that path.)

## Should something be a parameter?

Ask: does this function need info from *outside itself*, and could that info be different each time it's called? If yes → parameter.

If the function always works with the exact same thing no matter who calls it (like a fixed deck of cards), it usually doesn't need to be a parameter — it can just be referenced directly from the outer scope.

**Test**: could this function reasonably be called twice in the same program, wanting *different* values each time? If yes, that value should be a parameter, not assumed.

## Should it return what it took in?

Not necessarily. The real question: after this function finishes, what does the rest of the program need that it didn't have before? That's what gets returned — not a mechanical mirror of the parameter list.

- Modifies something the caller needs afterward → return it
- Calculates something new that didn't exist before → return that, even if it wasn't a parameter
- Uses a parameter internally but nothing about it needs to survive outside → no need to return it

## The scope rule (why `UnboundLocalError` happens)

Functions can automatically **read** variables from the outer/enclosing scope without needing them as parameters:

```python
cards = [11, 2, 3, 4]

def draw_one_card():
    return random.choice(cards)   # reading `cards` - works fine, no parameter needed
```

But the moment you **assign/reassign** a variable with that name *anywhere* inside the function, Python treats it as local to the *entire* function, from the very first line - even lines before the assignment. It stops looking outward for that name entirely.

```python
def broken():
    print(player_score)     # crashes: player_score is about to become local...
    player_score = 5         # ...because of this line further down
```

**The real question per variable**: is the function only *reading* it, or does it *reassign* it?
- Only reading → fine to reference directly, no parameter/return needed
- Reassigning → needs to be a parameter (passed in, worked on, returned back out), or explicitly marked `global` inside the function

## `break` and `return` interaction (the bug that keeps showing up)

`break` immediately exits the nearest loop - every line below it in that loop, including a `return` statement, gets skipped entirely on that pass. If a function's only `return` sits after a `break` that fires unconditionally, the function silently gives back `None` instead of crashing loudly - worth checking for this specifically when a function returns `None` unexpectedly.

def draw_one_card():
    return random.choice(cards)   # reading `cards` - works fine, no parameter needed
```

But the moment you **assign/reassign** a variable with that name *anywhere* inside the function, Python treats it as local to the *entire* function, from the very first line - even lines before the assignment. It stops looking outward for that name entirely.

```python
def broken():
    print(player_score)     # crashes: player_score is about to become local...
    player_score = 5         # ...because of this line further down
```

**The real question per variable**: is the function only *reading* it, or does it *reassign* it?
- Only reading → fine to reference directly, no parameter/return needed
- Reassigning → needs to be a parameter (passed in, worked on, returned back out), or explicitly marked `global` inside the function

## `break` and `return` interaction (the bug that keeps showing up)

`break` immediately exits the nearest loop - every line below it in that loop, including a `return` statement, gets skipped entirely on that pass. If a function's only `return` sits after a `break` that fires unconditionally, the function silently gives back `None` instead of crashing loudly - worth checking for this specifically when a function returns `None` unexpectedly.