# Tuples
genders = ("males", "females", "trans")
print(genders.count("males"))


# sets
s = {56, 76, 43}
print(s)

#set operation
s1 = {1,3,4,5}
s2 = {3, 5, 4, 0,9,}
print(s1|s2) # unio
print(s1&s2) # inntersection
print(s1-s2)

#set methods #(s.remove
#            s.add
#            s.discard to dont display a error if check it once
#           s.pop)
s= {3,4,5,66}  
s.add(4)
print(s)
#if in sets as only one word aafter we put(comma)