from PIL.TiffTags import ASCII

print("Задание 1 и 2 ")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        print(self.table)
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[index].append([key, value])
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    def delete(self,key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return True
        return False
    def resize(self):
        f = []
        f.extend(self.table)
        self.table.clear()
        resize = [None] * self.size
        self.table.extend(resize)
        self.table.append(f)
        print(f)
table = HashTable(5)
table.insert("apple", 10)
table.insert("banana", 20)
print(table.search("apple"))
print(table.search("apple"))
table.insert("kiwi", 11)
table.insert("avocado", 13)
table.resize()
print(table.search("apple"))
table.insert("grape", 12)
table.insert("g", 14)
table.insert("gr", 15)
table.resize()
table.insert("grae", 16)
table.insert("grap", 17)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self, key):
        print(self.table)
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        print(self.table)
        return "not elements"
    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if self.table[index][i][0] == key:
                self.table[index].pop(i)
                return True
        return False
table = ChainedHashTable(1)
table.insert("apple", 10)
table.insert("banana", 20)
table.insert("gar", 8)
print(table.search("apple"))
print(table.search("gar"))
print(table.search("banana"))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("Задание 3 ")
def task3(value):
    x=[]
    for i in value:
        x.append(ord(i))
    y=sum(x)
    return y
print(task3("Hello, world!"))
print("Задание 4 ")
class Dict:
    def __init__(self, size):
        self.table = {}
    def insert(self, key):
        x = []
        for i in key:
            x.append(ord(i))
        y = sum(x)
        for pair in self.table:
            if pair is table:
                return
        self.table[key] = y
    def search(self, key):
        print(self.table)
        return self.table.get(key)
    def delete(self, key):
        del self.table[key]
table = Dict(1)
table.insert("apple")
table.insert("banana")
table.insert("banana")
table.insert("gar")
print(table.search("gar"))
table.delete("apple")
print(table.search("apple"))
print(table.search("banana"))