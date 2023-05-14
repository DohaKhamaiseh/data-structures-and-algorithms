import re
from Stack import Stack
def validate_brackets(str):
    """
    this function will validate these kinds of brackets by taking a string that contain them in a certain way and returning a boolean value if brackets are written in the right way
    """

    stack = Stack()
    # Round Brackets : ()
    # Square Brackets : []
    # Curly Brackets : {}

    # Curly = None
    # Square = None
    # Round = None

    # Curly = re.search("\{[a-zA-Z]?\}",str)
    # Square = re.search("\[[a-zA-Z]?\]",str)
    # Round = re.search("\([a-zA-Z]?\)",str)

     

    # if (Curly or Square or Round ):
    #          if((str.count("{") + str.count("}"))%2==0) and((str.count("(") + str.count(")"))%2==0) and ((str.count("[") + str.count("]"))%2==0) :
    #            return True
    #          else :
    #           return False
    # else:
    #     return False
   
    for i in range(len(str)):
         if(str[i] == "(" ):
             stack.push(")")

         if(str[i]==")"):
                 if((stack.top.value=="}" or stack.top.value=="]")  and stack.get_size()!=0):
                      return False
                 stack.pop()

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
    
   