# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:31:18 2019

@author: ashar
"""

#Create a peice of code that will searh for the biggest combination of letters in two string
import sys
a = "michaelfrancis" 
b = "francis"

def matcher(a1, b1):
    a_list = []
    b_list = []
    for i in range(len(a1)):
        a_list.append(a1[i])
    for j in range(len(b1)):
        b_list.append(b1[j])

    

    
    def matchsearch(a_list,b_list):
        og = ""
        ahead = ""
        trailing = ""
        big_combo = trailing + og + ahead
        
        list_of_word = []
        
        for k in range(len(a_list)):
            for l in range(len(b_list)):
                if (a_list[k] == b_list[l]):
                    og = a_list[k]
                    
                    for n in range(len(a_list)):
                        try:
                            if (a_list[k+(n+1)] == b_list[l+(n+1)]):
                                ahead += a_list[k+(n+1)]
                               
                            if (a_list[k-(n+1)] == b_list[l-(n+1)]):
                                trailing += a_list[k-(n+1)]
                                
                        except:
                            big_combo = trailing[::-1] + og + ahead
                            if (big_combo > ""):
                                list_of_word.append(big_combo)
                            og = ""
                            ahead = ""
                            trailing = ""
        return(list_of_word)
                    
    the_word = (matchsearch(a_list,b_list))
    
    maxi = max(the_word , key = len)

    return maxi       
        
        
        
print(matcher(a,b)
    
matcher(a,b)
