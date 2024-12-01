#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 ==0]

print(return_evens(range(1,10,2)))
print(return_evens([0,1,3,5,7,8,9]))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

print(make_exclamation([
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]))
