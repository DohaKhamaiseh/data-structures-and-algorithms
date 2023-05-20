import re
from Stack import Stack
def validate_brackets(str):
    """
    this function will validate these kinds of brackets by taking a string that contain them in a certain way and returning a boolean value if brackets are written in the right way
    """

    stack = Stack()
    for i in range(len(str)):     #(){}[]     ((){}[])

         if(str[i] == "(" ):
             stack.push(")")  #stack = )

         if(str[i]==")"):   # ({)} or ([)]
                 if((stack.top.value=="}" or stack.top.value=="]")  and stack.get_size()!=0):
                      return False
                 stack.pop() #stack = empty

         if(str[i] == "{" ):
            stack.push("}")

         if(str[i]=="}"):
                if((stack.top.value=="]" or stack.top.value==")")  and stack.get_size()!=0):
                      return False
                stack.pop()

         if(str[i] == "[" ):
            stack.push("]")

         if(str[i]=="]"):
                if((stack.top.value=="}" or stack.top.value==")")  and stack.get_size()!=0):
                      return False
                stack.pop()

    return stack.get_size()==0
            


if __name__ == "__main__":
    print(validate_brackets("[(])"))
    
   