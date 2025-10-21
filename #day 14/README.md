# Day 14 — JavaScript Deque (Double‑Ended Queue)

A lightweight, index‑based Deque that supports O(1) adds/removes from both ends using a sparse object with moving `head`/`tail` pointers. Includes a tiny demo and a `print()` helper to visualize state.

## What is a Deque?
A Deque (Double‑Ended Queue) is a generalized queue that allows insertion and removal at both the front and the rear. It’s useful for problems like sliding window, palindrome checks, BFS variants, and task schedulers.

## Features
- Add/remove at both ends: `addHead`, `addTail`, `removeHead`, `removeTail`
- Inspect ends without removing: `peekHead`, `peekTail`
- Constant‑time checks: `isEmpty`, `size`
- Human‑readable `print()` for quick debugging


## Complexity
- `addHead`, `addTail`: O(1)
- `removeHead`, `removeTail`: O(1)
- `peekHead`, `peekTail`, `isEmpty`, `size`: O(1)
- `print`: O(n)
