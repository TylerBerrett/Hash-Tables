# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """

        index = self._hash_mod(key)
        # if index is already exists add to the list in it
        pointer = self.storage[index]

        if pointer is None:
            self.storage[index] = LinkedPair(key, value)

        elif self.retrieve(key):
            while pointer:
                if pointer.key == key:
                    pointer.value = value
                pointer = pointer.next

        else:
            if pointer.next is None:
                pointer.next = LinkedPair(key, value)
            else:
                # check to see if next is empty or not
                while pointer:
                    if pointer.next is None:
                        pointer.next = LinkedPair(key, value)
                        break
                    pointer = pointer.next



    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        pointer = self.storage[self._hash_mod(key)]
        if self.retrieve(key):
            while pointer:
                if pointer.key == key:
                    pointer.value = None
                pointer = pointer.next

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        index = self.storage[self._hash_mod(key)]
        if index:
            while index:
                if index.key == key:
                    return index.value
                if not index:
                    return None
                index = index.next


    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        self.capacity *= 2

        new_storage = []

        for item in self.storage:
            while item:
                key = item.key
                value = item.value
                new_storage.append([key, value])
                item = item.next

        self.storage = [None] * self.capacity
        for item in new_storage:
            self.insert(item[0], item[1])




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
