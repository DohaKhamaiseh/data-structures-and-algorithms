### Pseudocode


```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

  ```

### Trace
#### Sample Arrays
  input array = [8,4,23,42,16,15]


####  Pass 1:
![pass1](./pass1.jpg)

In the first pass-through of the insert sorted, the value to be inserted (4) was smaller than the first value(8) on the sorted list so we swapped between them to have a sorted list = [4,8]

####  Pass 2:
![pass2](./pass2.jpg)

In the second pass-through of the insert sorted, the value to be inserted (23) was bigger than the first value(4) on the sorted list so we incresed the counter(i) until counter become equal the length of the sotred(2) so then we insertd (23)

####  Pass 3:
![pass3](./pass3.jpg)

In the third pass-through of the insert sorted, the value to be inserted (42) was bigger than the first value(4) on the sorted list so we incresed the counter(i) until counter become equal the length of the sotred(3) so then we insertd (42)

####  Pass 4:
![pass4](./pass4.jpg)

In the fourth pass-through of the insert sorted, the value to be inserted (16) was bigger than the first value(4) on the sorted list so we incresed the counter(i) until the value become smaller than element on the sorted(23) so then we swapped between (23) and (16) then between (23) and (42)

####  Pass 5:
![pass5](./pass5.jpg)

In the second pass-through of the insert sorted, the value to be inserted (15) was bigger than the first value(4) on the sorted list so we incresed the counter(i) until the value become smaller than element on the sorted(16) so then we swapped between (15) and (16) then between (16) and (23) then between (23) and (42)


### Big O : 
#### Time Complexity: O(n^2)
#### Space Complexity: O(n)

[PR link](https://github.com/DohaKhamaiseh/data-structures-and-algorithms/pull/39)