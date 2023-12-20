# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:06:37 2023

@author: Brendan
"""

with open('Day1AdvOfCode.txt', 'r') as file:
    coords = file.read().splitlines()

target_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

first_num = []
second_num = []

first_word = []
second_word = []

first_loc = []
second_loc = []

first_numLoc = []
second_numLoc = []

for each in coords:
    
    loc_list1=[]
    for word in target_words:
        loc_list1.append(each.find(word))
    if sum(loc_list1) != -9:
        noNones = [i for i in loc_list1 if i != -1]
        firstWord = min(noNones)
        first_loc.append(firstWord)
        first_word.append(loc_list1.index(firstWord)+1)
        
    loc_list2=[]
    for word in target_words:
        loc_list2.append(each.rfind(word))
    if sum(loc_list2) != -9:
        noNones = [i for i in loc_list2 if i != -1]
        lastWord = max(loc_list2)
        second_loc.append(lastWord)
        second_word.append(loc_list2.index(lastWord)+1)
   
    else:
        second_loc.append(-1)
        second_word.append("none")
        first_loc.append(-1)
        first_word.append("none")

    for letter in each:
        if letter.isdigit():
            first_num.append(letter)
            first_numLoc.append(each.index(letter))
            break
    
    for letter in reversed(each):
        if letter.isdigit():
            second_num.append(letter)
            second_numLoc.append(each.rindex(letter))
            break
        
first_coord = []
second_coord = []

for i in range(0, len(coords)):
    
    if first_loc[i] == -1:
        first_coord.append(int(first_num[i]))
        second_coord.append(int(second_num[i]))
        
    else:
        if first_loc[i] < first_numLoc[i]:
            first_coord.append(int(first_word[i]))
        if first_loc[i] > first_numLoc[i]:
            first_coord.append(int(first_num[i]))
        
        if second_loc[i] < second_numLoc[i]:
            second_coord.append(int(second_num[i]))
        if second_loc[i] > second_numLoc[i]:
            second_coord.append(int(second_word[i]))
        
        
    
combined_list = [int(str(x) + str(y)) for x, y in zip(first_coord, second_coord)]
answer = sum(combined_list)
print(answer)
