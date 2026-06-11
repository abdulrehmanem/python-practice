# leds =['L1','L2','L3','L4','L5']
# for led in leds:
#     if led == 'L3':
#         print(f'{led} is the brightest')
#     else:
#         print(f'{led} is OFF') 
#----out come >>>
# L1 is OFF
# L2 is OFF
# L3 is the brightest
# L4 is OFF
# L5 is OFF

#-------------------------------------
# age = 17

# if age<18:
#     print('You are a minor')
# elif age>=18:
#     print('You are an adult')

# a = (age==17)
# print(a) #True

# a = (age==18)
# print(a) #False
#-------------------------------------

age = 17
# if age:
#  if age<=4:
#     print('free for under 5')
#  elif age>4 and age<=12:
#     print('child ticket') 
#  elif age>12 and age<=18:
#     print('teenager ticket')
#  elif age>18 and age<=60:
#     print('adult ticket')
# else:    print('Please enter your age')

# status = "adult" if age >= 18 else "minor" >>>>>------important-------
# print(status) 

items = []

# No need for: if len(items) == 0:
if not items:
    print("The list is empty!") 
