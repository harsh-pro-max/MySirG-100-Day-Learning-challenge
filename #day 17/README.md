# Day 17 — Heap Theory + Min‑Heap in JavaScript

A heap is a specialized tree‑based data structure where every node obeys a simple order rule called the heap property. This project implements a Min‑Heap (smallest element at the root) in JavaScript and demonstrates inserts and extractions.

## What is a Heap?

- A heap is a complete binary tree:
  - “Complete” means all levels are filled left‑to‑right with no gaps except possibly the last level.
  - Heaps are typically stored in an array for efficiency.
- Two main variants:
  - Min‑Heap: parent ≤ children (root is the global minimum).
  - Max‑Heap: parent ≥ children (root is the global maximum).

## Array Representation (index math)

For a node at index \(i\):
- Parent index: \(\lfloor (i - 1) / 2 \rfloor\)
- Left child index: \(2i + 1\)
- Right child index: \(2i + 2\)

This mapping lets us navigate the tree without pointers, using only array indices.

## Heap Property (Min‑Heap)

- Every node’s value is ≤ the value of its children.
- The root (index 0) is always the smallest element present.
- The property is restored after mutations
