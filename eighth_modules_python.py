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

from seventh_functions_python import  fun1 as f1

print(f1('black',x=24 ,y=46))