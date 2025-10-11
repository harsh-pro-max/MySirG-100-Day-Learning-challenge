# Day 4 — Python Walrus Operator (:=)

Assignment expression that lets you assign and use a value in the same expression (Python 3.8+). Cleaner loops and conditionals, fewer repeated calls.

## Why use it
- Read/compute once, use immediately in condition.
- Reduces lines and avoids duplicate function calls.
- Keeps I/O loops and regex checks concise.

## Core examples
Input loop
while (data := input("Enter: ")) != "quit":
print("Entered:", data)

Regex match
if (m := re.search(r"\d+", s)):
print(m.group(0))

Length check
if (n := len(items)) > 0:
print(f"{n} items found")

Tips: Use for short, readable conditions; avoid over‑nesting.

Streak: 4/100 🔥 | Part of MySirG’s 100 Days Learning Challenge.