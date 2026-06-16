# import seventh_functions_python

# m = seventh_functions_python.fun('blue' ,23,'black','white')
# print(m)  #('blue', (23, 'black', 'white'))

#-----

# import seventh_functions_python as seven
# m = seven.fun2('black',x=24 ,y=46)
# print(m)  #{'x': 24, 'y': 46, 'paper': 'black'}

#---------------------------------------------------------------------

# from seventh_functions_python import fun1
# print(fun1('black',x=24 ,y=46))  #('black', {'x': 24, 'y': 46})

#---------------------------------------------------------------------

# from seventh_functions_python import fun,fun1,fun2
# print(fun('red' ,23,'black','white'))
# print(fun1('black',x=24 ,y=46))
# print(fun2('black',x=24 ,y=46)) 

#---------------------------------------------------------------------

# from seventh_functions_python import  fun1 as f1

# print(f1('black',x=24 ,y=46))

#---------------------------------------------------------------------

# import ninth_oop_python 

# Le_d = ninth_oop_python.led("RED",'4mm')
# Le_d.on()

# import ninth_oop_python as oop

# do_g = oop.dog('bond',4)
# do_g.sit()
# do_g.roll()

# from ninth_oop_python import restaurant as rest

# my_restaurant = rest("PC","french")

# my_restaurant.describe_restaurant()

from ninth_oop_python import students,led

le_d = led('BLUE','3mm')
le_d.off()

std = students('michael',"A11")
std.welcome()