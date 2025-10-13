# Day 6 — Python Monkey Patching

Replace or extend behavior at runtime by rebinding an object’s attribute/method without modifying the original library. Used here to bypass a slow 5‑second network call with a fast mock.

## Why it matters
- Speed up demos/tests by avoiding real I/O
- Keep the same API; swap implementation on the fly
- Great for isolated unit tests and prototyping

## Use with care
- Patch only in test/dev; restore originals after tests
- Avoid global side‑effects in long‑running apps
- Prefer test doubles frameworks (e.g., unittest.mock) for larger projects

Streak: 6/100 🔥 — Part of MySirG’s 100 Days Learning Challenge
