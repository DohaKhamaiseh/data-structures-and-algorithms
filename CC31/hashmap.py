

def repeated_word(str):
    """"
    A function to return the first repeated word
    """
    dic = {}
    repeated_words = []

    if len(str) == 0 or str == " ":
        return None

    else:
        words_list = str.lower().replace(","," ").split()
    
        for word in words_list:
            if word in dic:
                dic[word] +=1
                repeated_words.append(word)
            else:
                dic[word] =1
        
        return repeated_words[0]



if __name__ == "__main__":

    s1 = "Once upon a time, there was a brave princess who..."
    s2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    s3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    

    # s1 = s1.lower().replace(","," ").split()
    # s2 = s2.lower().replace(","," ").split()
    # s3 = s3.lower().replace(","," ").split()
    
    # print(s1)
    print(repeated_word(s1))

    # print(s2)
    print(repeated_word(s2))

    # print(s3)
    print(repeated_word(s3))
