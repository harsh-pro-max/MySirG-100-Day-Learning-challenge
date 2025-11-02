# 🧮 Day 26 – Custom Iterators in Python

In this session, we learned how to create **custom iterators** in Python.  
A `for` loop in Python works on any **iterable** object such as lists, strings, and tuples.  
But we can also make our own class iterable by implementing the **iterator protocol**,  
which means defining the `__iter__()` and `__next__()` methods.

---

## 🔹 Example 1: Counter Class

### 🔸 Code:
```python
class Counter:
  def __init__(self, start = 1, end = 10):
    self.start = start
    self.end = end

  def __iter__(self):
    return self.Counter_Iterator(self)

  class Counter_Iterator:
    def __init__(self, counter):
      self.counter = counter
      self.beg = counter.start

    def __next__(self):
      if self.counter.start > self.counter.end:
        self.counter.start = self.beg
        raise StopIteration
      current_value = self.counter.start
      self.counter.start += 1
      return current_value


# Object creation and iteration
my_counter = Counter(1,5)
for i in my_counter:
  print(i)
print('*****************')

my_counter = Counter(6,10)
for i in my_counter:
  print(i)
print('*****************')

my_counter = Counter(11,20)
for i in my_counter:
  print(i)
print('*****************')
