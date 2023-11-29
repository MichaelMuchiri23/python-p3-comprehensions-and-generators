#!/usr/bin/env python3

def return_evens(num_list):
    even_num_list = [n for n in num_list if n % 2 == 0]
    return even_num_list

def make_exclamation(sentence_list):
    sentence_list = [n + "!" for n in sentence_list]
    return sentence_list

#Case examples
print(make_exclamation(["Yo", "Hello", "I'm a software developer"]))
print(make_exclamation([]))
print(return_evens([1,2,3,4,5,6]))
print(return_evens([]))
