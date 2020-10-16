"""
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

>>> stringMatching(["mass","as","hero","superhero"])
["as","hero"]

>>> stringMatching(["leetcode","et","code"])
["et","code"]

>>> stringMatching["blue","green","bu"]
[]

"""