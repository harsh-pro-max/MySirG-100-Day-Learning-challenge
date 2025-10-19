# Day 12 — JavaScript Queue (FIFO)

A simple, readable Queue built in JavaScript with a clear API: `enqueue`, `dequeue`, `getFront`, `getRear`, `isEmpty`, and `getSize`. Includes a small console demo to verify FIFO behavior.

## Why this matters
Queues model real‑world waiting lines and power scheduling, request pipelines, and graph algorithms like BFS. Writing one from scratch clarifies time complexity trade‑offs in JavaScript arrays.

## Features
- FIFO semantics with `enqueue` (add) and `dequeue` (remove)
- O(1) access helpers: `getFront`, `getRear`, `getSize`, `isEmpty`
- Safe guards: returns `null` on empty `dequeue/getFront/getRear`
- Tiny test to show state before/after a removal


## Complexity  (current array + shift)
- enqueue: O(1) amortized (push)
- dequeue: O(n) due to `shift()` reindexing
- getFront / getRear / isEmpty / getSize: O(1)

## Recommended improvement (O(1) dequeue)
For long‑running or heavy workloads, prefer a head/tail index queue to keep `dequeue` at O(1):

