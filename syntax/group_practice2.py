# Aucoeur, Liya, Sandy -  SPD 1.41 Breakout Group
# Technical Interview Practice
# https://docs.google.com/document/d/1mfJEclhDUPnLn7EkPs-zr2Figs7pKZecCOYPUced4Ao/edit?usp=sharing

'''
Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.


‘one fish two fish blue fish red fish’
2
''' 

#histogram first of all the words
#sort a dict by the value

#tuple
#sort the tuple
#the last k elts

def hist_text(text, k):
 text_hist = {}
 text_arr = text.split(' ')
 for i in text_arr:
   # if i is in the hist
   # increment by 1
   if i in text_hist:
     text_hist[i] += 1
   # if not make a key and assign it to 1
   else:
     text_hist[i] = 1
 
 text_hist = sorted(text_hist.items(), key= lambda x: x[1], reverse=True)
 
 sub_text = text_hist[:k]
 return sub_text
 
print(hist_text('one fish two fish red fish blue fish',3))