# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:20:48 2022

@author: Kpatel
"""
main_list = ['BITCOIN','MICROSOFT','SAMSUNG','APPLE','GOOGLE']
random_list = ['ELAPP','LOOGEG','GUMSNAS','CROSFITOM','COTINBI']
count=0
it_main = iter(main_list)
it_random = iter(random_list)
i=0
while i<len(main_list):
    i+=1
    # element_main=next(it_main)
    element_random=next(it_random)
    print("Arrange the word :- ",element_random)
    # print(element_random)
    
    a = input()
    
    for e in main_list:
        
        
        if a == e:
            count+=1
            break
    else:
        count-=1

print("YOUR SCORE IS: ")

print(count)




# main_list = ['APPLE','SAMSUNG','MICROSOFT','BITCOIN','GOOGLE']
# random_list = ['ELAPP','LOOGEG','GUMSNAS','CROSFITOM','COTINBI']
# count=0
# it_main = iter(main_list)
# it_random = iter(random_list)
# i=0
# while i<len(main_list):
#     i+=1
#     element_main=next(it_main)
#     element_random=next(it_random)
#     print("Arrange the word :- ",element_random)
#     # print(element_random)
    
#     a = input()
#     if a == element_main:
#         count+=1
#     else:
#         count-=1

# print("YOUR SCORE IS: ")

# print(count)
