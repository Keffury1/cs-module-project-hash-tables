class HashTableEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


MIN_CAPACITY = 8


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0 

        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        
        self.storage = [None] * capacity

    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        return self.size / self.capacity

    def djb2(self, key):
        hash = 5381
        for item in key:
            hash = (hash * 33) + ord(item)
        return hash

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        item = self.storage[index]
        entry = HashTableEntry(key, value)
        self.size += 1

        if item:
            self.storage[index] = entry
            self.storage[index].next = item
        else:
            self.storage[index] = entry

    def delete(self, key):
        if self.get(key):
            self.put(key, None)
            self.count -= 1
        else:
            print("No Key Found")

    def get(self, key):
        index = self.hash_index(key)
        item = self.storage[index]

        while item:
            if item.key == key:
                return item.value
            item = item.next
        return None
    

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
