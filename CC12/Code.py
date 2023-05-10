from Queue import Queue


class Animal :
    def __init__(self,species,name):
       self.species = species
       self.name = name

class AnimalShelter:
    def __init__(self):
        self.queue = Queue()

    
    def enqueue(self,animal):
       """
       this method will add a cat or dog to the Animal Shelter in FIFO approach
       """
       if(animal.species=="dog" or animal.species=="cat"):
        self.queue.enqueue(animal.species)
       else:
          print("Not allowed to add this animal, just cat or dog")

    
    def dequeue(self,pref):
        """
        this method will delete the preference from the Animal Shelter
        """
        pr = ""
        temp = self.queue.front
        # print(temp.value)
        if(pref=="dog" or pref=="cat"):
         while(self.queue.front is not None):
          if(self.queue.front.value==pref):
            pr =  self.queue.dequeue()
            return pr
          temp = self.queue.front
          self.queue.front =  self.queue.front.next
          self.queue.enqueue(temp.value)

         return "Empty Shelter"
        else:
         return "null"
        
        
    





shelter = AnimalShelter()

animal1 = Animal("dog","lila")
animal2 = Animal("dog","sharlk")
animal3 = Animal("dog","sese")
animal4 = Animal("cat","dody")

# shelter.enqueue(animal1)
# shelter.enqueue(animal2)
# shelter.enqueue(animal3)
# shelter.enqueue(animal4)

# print(shelter.queue.show_nodes())
# print(shelter.queue.size)

print(shelter.dequeue("dog"))
print(shelter.queue.show_nodes())

# print(shelter.dequeue("cat"))
# print(shelter.queue.show_nodes())



