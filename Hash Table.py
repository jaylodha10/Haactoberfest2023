class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if the key already exists
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the value associated with the key
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]  # Remove the key-value pair

# Usage example
if __name__ == "__main__":
    hash_table = HashTable(10)
    hash_table.insert("apple", 5)
    hash_table.insert("banana", 7)
    hash_table.insert("cherry", 3)

    print("Value for 'apple':", hash_table.search("apple"))  # Output: 5
    print("Value for 'banana':", hash_table.search("banana"))  # Output: 7

    hash_table.delete("cherry")
    print("Value for 'cherry':", hash_table.search("cherry"))  # Output: None
