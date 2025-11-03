# 🧠 Day 27 — Python Generators (Primes)

## 📘 What I Learned

- A **generator** is a special type of function that returns an **iterator** and produces values **lazily** using the `yield` keyword.  
- Each `yield` temporarily **pauses** the function, **preserves its internal state**, and **resumes** execution when the next value is requested.  
- When the generator runs out of values, it raises a `StopIteration` exception automatically to signal the end of the stream.  
- Generators are **memory-efficient**, as they produce items **on demand** rather than storing large sequences in memory — making them ideal for **large or infinite data streams**.

---

## 🧩 Today’s Exercise (Summary)

### Step 1 — Prime Helpers
- Implemented two helper functions:
  - `isPrime(n)`: Checks if a number `n` is prime.
  - `nextPrime(n)`: Finds the next prime number after `n`.

### Step 2 — Prime Generator
- Created a generator function `primeGenerator(k)` that:
  - Yields the first `k` prime numbers **one by one**.
  - Uses the `yield` keyword to return primes sequentially without building a full list in memory.

#### 🧪 Demo
```python
prime_list = [p for p in primeGenerator(10)]
print(prime_list)  
# Output → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
