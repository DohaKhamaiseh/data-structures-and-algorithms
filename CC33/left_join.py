from hash import hashtable

def left_join(hash1, hash2):
   """
   A function that will return the left join between two hashmaps
   """
   if hash1.count== 0 or hash2.count==0:
      return "No join"
   
   join_list = []
   for key in hash1.keys():
      if key in hash2.keys():
         row = [key,hash1.get(key),hash2.get(key)]
        
      else:
         row = [key,hash1.get(key),None]
      
      join_list.append(row)
    
   return join_list


# h1 = hashtable(5)
# h2 = hashtable(5)

# h1.set("diligent","employed")
# h1.set("fond","enamored") 
# h1.set("guide","usher") 
# h1.set("outfit","garb")  
# h1.set("wrath","anger") 

# h2.set("diligent","idle")
# h2.set("fond","averse") 
# h2.set("guide","follow") 
# h2.set("flow","jam")  
# h2.set("wrath","delight") 


h1 , h2 = hashtable(5), hashtable(5)

print(left_join(h1,h2))

