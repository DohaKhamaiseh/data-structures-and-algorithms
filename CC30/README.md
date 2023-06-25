# Hash Table



## Approach & Efficiency

*The **hashtable** class is used to create and manipulate a hashtable. It has multiple methods :*

**set(self,key,value):**  a method that will add a new pair to the table

**get(self,key):**   a method to get the pair of the given key

**has(self,key):**   a method to check if the pair is in the table by its key

**hash(self,key):**  a method that will calculate the index where the key should store in the table(array)

**keys(self):**   a method to get all keys



| Method | Time | Space |
|--------|------|-------|
| set    | O(1) | O(1)  |
| get    | O(1) | O(1)  |
| has    | O(1) | O(1)  |
| keys   | O(n) | O(n)  |
| hash   | O(1) | O(1)  |

## Code : [Hashtable](./hash.py)