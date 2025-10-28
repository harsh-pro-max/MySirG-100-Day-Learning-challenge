# 🧩 Day 21 - Hash Table Implementation (JavaScript)

This project demonstrates a simple **Hash Table** implementation in **JavaScript** using **separate chaining** to handle collisions.

---

## ⚙️ What is a Hash Table?
A **Hash Table** stores data in key-value pairs and allows **fast data access** using a **hash function**.

It works by converting a key into an index (using the hash function) and storing the value at that index.

> ✅ Average Time Complexity:  
> Insert → O(1) | Search → O(1) | Delete → O(1)

---

## 🏗️ How It Works

### 🔹 `_hashFunction(key)`
Converts a given key (string or number) into a valid array index.  
This ensures that each key is mapped consistently to the same position.

### 🔹 `set(key, value)`
- Calculates index using hash function  
- Stores the key-value pair at that index  
- Handles **collisions** using an array (separate chaining)

### 🔹 `get(key)`
- Finds the index of the key using the hash function  
- Returns the stored value if found  

### 🔹 `remove(key)`
- Locates the key and removes it from the chain  
- Returns `true` if key existed, otherwise `false`

### 🔹 `size()`
Returns the total number of key-value pairs stored.

---

## 💻 Example Code

```js
const ht = new HashTable(10);
ht.set("Arjun", 49);
ht.set("Harsh", 40);
ht.set("Dipak", 73);
ht.set("Priya", 78);
ht.set("Manoj", 90);

console.log(ht.get("Dipak")); // Output: 73
