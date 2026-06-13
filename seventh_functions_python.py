# def user_name():
#     name = input("Please enter your name: ")
#     print(name)

# user_name()

#----------------------------------------------

# def user_name(firstname,lastname):
#     f_name = firstname
#     l_name = lastname
#     full_name = f'{f_name} {l_name}'
#     print(full_name.title()) 

# user_name('haris','ali')
# user_name(lastname='haris',firstname='ali')

#----------------------------------------------

# def user_name(firstname="petter",lastname): --------------X worng way to set default it give error
# def default_L_name(firstname,lastname="majid"):   
#     f_name = firstname
#     l_name = lastname
#     full_name = f'{f_name} {l_name}'
#     print(full_name.title()) 

# default_L_name('ali') #-----Ali Majid

# def default_name (firstname="jenny", lastname="michael"):
#     f_name = firstname
#     l_name = lastname
#     full_name = f'{f_name} {l_name}'
#     print(full_name.title()) 

# default_name(lastname='petter') #Jenny Petter
# default_name(firstname='mina')  #Mina Michael
# default_name('malik','hayat')   #Malik Hayat
# default_name('jasmeen')         #Jasmeen Michael

#----------------------------------------------

# def profile(first,last,age=None):
#     profile = { 'frist_name' : first , 'last_name' : last }
#     if age:
#         profile['age']=age

#     return profile

# profile_1 = profile("qasim","khalid")    #{'frist_name': 'qasim', 'last_name': 'khalid'}
# profile_1 = profile("qasim","khalid",22) #{'frist_name': 'qasim', 'last_name': 'khalid', 'age': 22}

# print(profile_1)

#----------------------------------------------

# def users ():
#     print("pls enter your details....")
#     all_users = []
#     while True :
#         name1 = str(input('your name : '))
#         if name1=='q':
#             break
#         age1 =  int(input('your age : '))
#         if age1=='q':
#             break
#         lang1 = str(input('your language : '))
#         if lang1=='q':
#             break
#         users ={
#             'Name' : name1,
#             'Age' : age1,
#             'Language' : lang1
#         }
#         print(f'your name is {users['Name']}and you are {users['Age']} old and  known {users['Language']} langauge .')
#         all_users.append(users)
#     return all_users

# data = users()

# print('\nfinal data is :')
# print(data)

#----------------------------------------------

# def names(list_of_name):
#     for list in list_of_name :
#         msg = f'\n {list} added in list' 
#         print(msg)

# list_of_names = ['clark', 'michael', 'petter']
# names(list_of_names)

# def names(listname):
#     while listname :
#         n = listname.pop(0)
#         print(n)

# list_of_names = ['clark', 'michael', 'petter']
# names(list_of_names[:])

# print(list_of_names)

#-----------------------------------------

# design = ['clark', 'michael', 'petter']
# models = []
# def un_print(unprint_design,complete_model):
   
#     while unprint_design:
#          temp = unprint_design.pop()
#          complete_model.append(temp)

# def print_m(models):
#      print('models we have : ')
#      for m in models:
#           print(m)


# un_print(design[:],models)
# print_m(models)

# print(f'list of designs : {design}')
# print(f'list of models : {models}')

#------------------------------------------

def fun(size,*colors):
   return size,colors

# print(fun('red' ,23,'black','white'))   #('red', (23, 'black', 'white'))  it always give tuples

def fun1(paper,**demision):
   return paper , demision

# print(fun1('black',x=24 ,y=46))        #('black', {'x': 24, 'y': 46})

def fun2(paper,**demision):
   demision['paper'] = paper
   return demision

# print(fun2('black',x=24 ,y=46))        #{'x': 24, 'y': 46, 'paper': 'black'}