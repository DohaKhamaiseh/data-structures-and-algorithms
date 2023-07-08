
def left_join(hash1, hash2):
   """
   A function that will return the left join between two hashmaps
   """
   if len(hash1)== 0 or len(hash2)==0:
      return "No join"
   
   join_list = []
   for key in hash1:
      if key in hash2:
         row = [key,hash1[key],hash2[key]]
        
      else:
         row = [key,hash1[key],None]
      
      join_list.append(row)
    
   return join_list


h1 = {"diligent":"employed", "fond":"enamored", "guide":"usher", "outfit":"garb", "wrath":"anger"}

h2 = {"diligent":"idle", "fond":"averse", "guide":"follow", "flow":"jam", "wrath":"delight"}

# # h1 , h2 = {}, {}

print(left_join(h1,h2))

