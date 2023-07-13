from linkedlist import LinkedList

class hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size

    def hash(self,key):
        """"
        a method that will calculate the index where the key should store in the table(array)
        """

        sum_hash = 0
        if isinstance(key, int):
          return 0
        
        for ch in key:
            ch_hash = ord(ch)
            sum_hash+=ch_hash
        
        idx = sum_hash*599
        idx = idx % self.size
     
        return idx
    
    def set(self,key,value):
        """
        a method that will add a new pair to the table
        """
        hashed = self.hash(key)
        # if the bucket is empty
        if self.table[hashed] is None:
            self.table[hashed] = [key , value]
        
        else:
            # if the bucket has one value
            if not isinstance(self.table[hashed],LinkedList):
                exist_pair = self.table[hashed]
                new_pair = [key , value]

                bucket = LinkedList()
                self.table[hashed] = bucket
                
                bucket.add(exist_pair)
                bucket.add(new_pair)

            # if the bucket is linked list
            else:
                self.table[hashed].add([key,value])
    
    def get(self,key):
        """
        a method to get the pair of the given key
        """
        idx = self.hash(key)
        if self.table[idx] is None:
          return "Empty bucket ^_^"
        
        if not isinstance(self.table[idx],LinkedList) and self.table[idx][0]!=key :
            return None
        
        if isinstance(self.table[idx],LinkedList):
            curr = self.table[idx].head
            while curr:
                if curr.data[0]==key:
                    return curr.data[1]
    
                curr = curr.next
        
        else:
            return self.table[idx][1]
    
    def has(self,key):
        """
        a method to check if the pair is in the table by its key
        """
        idx = self.hash(key)
        if self.table[idx] is None:
          return False
        
        elif self.table[idx][0]!=key:
            return False
        
        
        return True
    
    def keys(self):
        """
        a method to get all keys
        """
        keys = []

        if self.table is None:
          return []
        
        # key = None

        for bucket in self.table:
            if bucket is not None:
                if isinstance(bucket,LinkedList):
                    curr = bucket.head
                    while curr:
                        keys.append(curr.data[0])
                        curr = curr.next
             
                else:
                    key = bucket[0]
                    # print(key)
                    keys.append(key)

        return keys

    def values(self):
        """
        a method to get all keys
        """
        values = []

        if self.table is None:
          return []
        
        # key = None

        for bucket in self.table:
            if bucket is not None:
                if isinstance(bucket,LinkedList):
                    curr = bucket.head
                    while curr:
                        values.append(curr.data[1])
                        curr = curr.next
             
                else:
                    val = bucket[1]
                    # print(key)
                    values.append(val)

        return values

    




# h = hashtable(4)
# h.set("Doha","Sun")
# h.set("Saba","Wind")
# h.set("Saja","Calmness")
# h.set("Eman","Faith")

# # print(h.hash("Doha"))
# # print(h.hash("Saba"))
# # print(h.hash("Saja"))
# # print(h.hash("Eman"))

# # print(h.get("h"))
# # print(h.has("El"))
# print(h.keys())
