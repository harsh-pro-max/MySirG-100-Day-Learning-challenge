# 🧠 Day 19 - Priority Queue using Min Heap (JavaScript)

This project implements a **Priority Queue** using a **Min Heap** in JavaScript.  
It helps process tasks based on their priority instead of the normal FIFO order.

---

## ⚙️ What is a Priority Queue?
A **Priority Queue** stores elements with a priority value.  
- Lower priority number → Higher importance  
- The task with the smallest priority number is served first.

---

## 🏗️ How It Works
Two classes are used:

### 🔹 `MinHeap`
Handles heap operations like:
- `insert(value)` → Add new element  
- `extractMin()` → Remove smallest element  
- `bubbleUp()` and `sinkDown()` maintain heap order

### 🔹 `PriorityQueue`
Built on top of `MinHeap` for easy use:
- `enqueue(data, priority)` → Add a task  
- `dequeue()` → Remove the highest-priority task  
- `peek()` → See next task  
- `isEmpty()` → Check if queue is empty  

---

## 💻 Example
```js
const taskQueue = new PriorityQueue();
taskQueue.enqueue("fix shower",7);
taskQueue.enqueue("market",3);
taskQueue.enqueue("Vacation plan",1);

while(!taskQueue.isEmpty()){
    const nextTask = taskQueue.dequeue();
    console.log('Task:', nextTask.data, '| Priority:', nextTask.priority);
}
