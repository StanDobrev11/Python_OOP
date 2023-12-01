"""In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a
structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash
code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed
and the resulting hash indicates where the corresponding value is stored.
1. Overview
Create a HashTable class that should have the needed functionality for a hash table, such as:
• hash(key: str) - a function that should figure out where to store the key-value pair
• add(key: str, value: any) - adds a new key-value pair using the hash function
• get(key: str) - returns the value corresponding to the given key
• additional "magic" methods, that will make the code in the example work correctly
The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon
initialization, the default length of the array should be 4. After each addition of an element if the HashTable gets too
populated, double the length of the array and re-add the existing data.
You are not allowed to inherit any classes. Feel free to implement your own functionality (and unit tests) or to write
the methods by yourself"""


class HashTable:
    def __init__(self):
        self.__capacity = 4
        self.__key_array = [None] * self.__capacity
        self.__value_array = [None] * self.__capacity
        self.__length = 0

    def get(self, key: str, error_msg=None):
        """ returns the value corresponding to the given key """

        try:
            return self.__getitem__(key)
        except KeyError:
            return error_msg

    def add(self, key: str, value):
        """ adds key: value pair to the hash table """

        return self.__setitem__(key, value)

    def __delitem__(self, key):
        """ the method deletes item from the hash table using 'del' """

        # get key index of the key array
        try:
            idx = self.__key_array.index(key)
            self.__key_array[idx] = None
            self.__value_array[idx] = None
            self.__length -= 1
        except ValueError:
            raise KeyError(f"{key} is not a valid HashTable key")

    def __setitem__(self, key, value):
        """ the method is required to set the class to act as dict and to be able to call key-value pair
        we need hash algorith to store the index
        the problem to solve is if the index is already occupied [collision]
        we need to calculate if have sufficient space in the array """

        # check for sufficient space in the array and apply resize algorithm
        if len(self) == self.__capacity:
            self.__resize()

        # calculate index and validate it
        idx = self.__calc_index(key)

        # the key and value are placed in the respective arrays on the pre-calculated index
        self.__key_array[idx] = key
        self.__value_array[idx] = value
        self.__length += 1

    def __getitem__(self, item):
        """ sets the class to be subscriptable and to be able to use 'get' method """

        # get key index of the key array
        try:
            idx = self.__key_array.index(item)
        except ValueError:
            raise KeyError(f"{item} is not a valid HashTable key")

        # return the value on the corresponding index in the value array
        return self.__value_array[idx]

    def __resize(self):
        """ implement resize algorithm to increase size of the array
        if not on python -> create 2 additional arrays with the newly increased
        length and deep copy the values from the old arrays """

        self.__key_array = self.__key_array + [None] * self.__capacity
        self.__value_array = self.__value_array + [None] * self.__capacity
        self.__capacity *= 2

    def __calc_index(self, key):
        """ the hash function to return indexes
        in order to have valid index, we need to divide % to the length of the array, i.e. -> the capacity
        the result values will always be in range(0, capacity)
        we must check for valid index"""

        # get the initial index
        idx = sum(ord(sym) for sym in key) % self.__capacity

        # checks if new key exist on this index and overwrites it
        if key == self.__key_array[idx]:
            return idx

        # validate index
        idx = self.__get_valid_idx(idx)

        return idx

    def __get_valid_idx(self, idx):
        """ method returns bool value if the idx in both arrays is available
        in order to skip additional 'if' for checking index range due to IndexError,
        we divide by capacity to get ALWAYS valid index """

        for _ in range(self.__capacity):
            if self.__key_array[idx % self.__capacity] is None:
                return idx % self.__capacity
            else:
                idx += 1

    def __len__(self):
        return self.__length

    def __repr__(self):
        """ representation of the hash table """

        return "{" + ', '.join(f"{self.__key_array[i]}: {self.__value_array[i]}" for i in range(self.__capacity) if
                               self.__key_array[i]) + "}"


if __name__ == '__main__':
    table = HashTable()
    table["name"] = "Peter"
    table['name'] = "Ivan"
    table["age"] = 25
    table["is_pet_owner"] = True
    table["is_driver"] = False
    table["check len"] = 8
    table.add('Ivan', 55)
    print(table)
    print(table.get("name"))
    print(table["age"])
    # print(table['iv'])
    print(table.get('iv'))
    print(len(table))
