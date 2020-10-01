# Given two strings str1 and str2, write a function to determine if str1 is an anagram of str2. The string will only contain lowercase english letters.

def anagrams(str1,str2):
    str1List = [ s for s in str1]
    str2List = [ s for s in str2]
    str1Set = set(str1List)
    str2Set = set(str2List)
    return str1Set == str2Set

str1 = 'bob'
str2 = 'bbo'
print(anagrams(str1,str2))

str1 = "bob"
str2 = "bod"
print (anagrams(str1, str2)) 

str1 = "race"
str2 = "acer"
print (anagrams(str1, str2))


#def anagram(str1, str2):
#  d1 = {}
#  d2 = {}
#  for s in str1:
#    d1[s] = d1.get(s,0) + 1
#  for s in str2:
#    d2[s] = d2.get(s,0) + 1
#  return d1 == d2 