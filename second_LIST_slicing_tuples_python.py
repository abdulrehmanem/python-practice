# color= ['red','blue','green','yellow','brown']
#print(color)
"""
print(color[0])
print(color[1])
print(color[2])
print(color[3])
print(color[4])
"""

#print(color[-2])
#print(len(color))


'''color.sort(reverse=true) 
print(color)'''

'''color.append('pink')  #['red', 'blue', 'green', 'yellow', 'brown', 'pink'] add pink in last
print(color)'''

'''color[0] = 'REDiSH'   #['REDiSH', 'blue', 'green', 'yellow', 'brown']
print(color)'''



"""color.insert(3,'black') #['red', 'blue', 'green', 'black', 'yellow', 'brown']
print(color)

color.insert(5,'mehroon') #['red', 'blue', 'green', 'yellow', 'brown', 'mehroon']  
print(color)

---------------------------------------------------------
#del color[3]  #['red', 'blue', 'green', 'yellow', 'mehroon', 'brown']
#print(color)

#del color[3:5]  #['red', 'blue', 'green', 'mehroon', 'brown']
#print(color)

del color [3:] #['red', 'blue', 'green']
print(color)"""

#------------------------------------------

"""color.append(["pink","organ","white","gold"])  #['red', 'blue', 'green', 'yellow', 'brown', ['pink', 'organ', 'white', 'gold']]
print(color)

print(color)


#color.remove('pink')
#print(color)

popped_color = color.pop(5)
print(popped_color) #pink
print(color)        #['red', 'blue', 'green', 'yellow', 'brown', 'organ', 'white', 'gold']

popped_color = color.pop() # last item form list
print(popped_color)        # gold
print(color)               #['red', 'blue', 'green', 'yellow', 'brown', 'pink', 'organ', 'white']olor.extend(["pink","organ","white","gold"]) #['red', 'blue', 'green', 'yellow', 'brown', 'pink', 'organ', 'white', 'gold']
print(color)


#color.remove('pink')
#print(color)

popped_color = color.pop(5)
print(popped_color) #pink
print(color)        #['red', 'blue', 'green', 'yellow', 'brown', 'organ', 'white', 'gold']

popped_color = color.pop() # last item form list
print(popped_color)        # gold
print(color)               #['red', 'blue', 'green', 'yellow', 'brown', 'pink', 'organ', 'white']

"""

# print(color)

# #color.sort()
# #print(color)

# #color.reverse()
# #print(color)

# color.sort(reverse=True)
# print(color)

#--------------SLICING-----------------

# floors = ['Gnd','1st','2nd','3rd','4th','5th','6th','7th']
# print(floors[:2])     #['Gnd', '1st']
# #([start:stop:step])
# print(floors[0:8:2])  #['Gnd', '2nd', '4th', '6th']
# print(floors[1:8:3])  #['1st', '4th', '7th']
# print(floors[::2])    #['Gnd', '2nd', '4th', '6th']
# #--REvERSE--
# print(floors[::-1])   #['7th', '6th', '5th', '4th', '3rd', '2nd', '1st', 'Gnd']
# print(floors[::-2])    #['7th', '5th', '3rd', '1st']

#---------------TUPLES-----------------

# carc = ('BMW','Audi','Mercedes','Lamborghini','Ferrari')
# print(carc)
# print(carc[0])
# print(carc[1])

# not_a_tuple = ("Gnd")   # This is just a standard string (str)
# is_a_tuple  = ("Gnd",)  # This is a tuple with 1 item
# print(type(not_a_tuple))  # <class 'str'>
# print(type(is_a_tuple))   # <class 'tuple'>

# floors_tuple = ('Gnd', '1st', '2nd', '3rd', '4th')

# # Advanced slice: reverse the tuple
# print(floors_tuple[0:5])  
# # Output: ('4th', '3rd', '2nd', '1st', 'Gnd')

# room_no = (101, 102, 103, 104, 105)

# ROOM1st, ROOM2nd, ROOM3rd, ROOM4th, ROOM5th = room_no

# print(ROOM1st)  # 101
# print(ROOM2nd)  # 102
# print(ROOM3rd)  # 103

#room_no[0] = 201  # This will raise a TypeError since tuples are immutable
#room_no.append(201)  # This will also raise an AttributeError since tuples do not have an append method

room_no = (201, 202, 203, 204, 205)  # To change the values, we need to create a new tuple
print(room_no)  # Output: (201, 202, 203, 204, 205)