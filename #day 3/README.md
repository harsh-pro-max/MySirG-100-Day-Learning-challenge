from pathlib import Path

# Define README content
readme_content = """# Day 3: Python Soft Keywords & Type Hints

🎯 **Today's Focus**
Explored Python's soft keywords and modern type hinting system introduced in Python 3.10+.  
Understanding context-dependent keywords and advanced type annotations.

---

📚 **Topics Covered**

### 🧩 Soft Keywords in Python
**Definition:** Keywords that behave as keywords only in specific contexts.

**Examples:** `match`, `case`, `type` (introduced in Python 3.10+)

**Flexibility:** Can be used as variable names outside their keyword context.

**Difference from Hard Keywords:** Unlike `if`, `for`, `while` which are always reserved.

---

### ⚙️ Example: Pattern Matching with match-case

```python
# Example of using soft keywords

# 'match' used as a soft keyword in pattern matching
value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# The same word 'match' can still be used as a normal variable
match = "Hello Soft Keyword!"
print(match)
