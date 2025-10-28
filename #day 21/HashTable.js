class HashTable {
  constructor(size = 50) {
    this.table = new Array(size);
    this.count = 0;
  }

  _hashFunction(key) {
    let hash = 0;
    const k = String(key);
    for (let i = 0; i < k.length; i++) {
      hash += k.charCodeAt(i);
    }
    return hash % this.table.length;
  }

  set(key, value) {
    const index = this._hashFunction(key);
    if (this.table[index] === undefined) {
      this.table[index] = [];
    }
    const chain = this.table[index];

    for (let i = 0; i < chain.length; i++) {
      if (chain[i][0] === key) {
        chain[i][1] = value;
        return;
      }
    }
    chain.push([key, value]); // fix: push key-value pair
    this.count++;
  }

  get(key) {
    const index = this._hashFunction(key);
    const chain = this.table[index];

    if (chain) {
      for (let i = 0; i < chain.length; i++) {
        if (chain[i][0] === key) { // fix: no stray semicolon
          return chain[i][1];
        }
      }
    }
    return undefined;
  }

  remove(key) {
    const index = this._hashFunction(key);
    const chain = this.table[index];

    if (chain) {
      for (let i = 0; i < chain.length; i++) {
        if (chain[i][0] === key) {
          chain.splice(i, 1);
          this.count--;
          return true;
        }
      }
    }
    return false;
  }

  size() {
    return this.count;
  }
}

// Test
const ht = new HashTable(10);
ht.set("Arjun", 49);
ht.set("Harsh", 40);
ht.set("Dipak", 73);
ht.set("priya", 78);
ht.set("manoj", 90);

console.log(ht.get("Dipak")); // 73
