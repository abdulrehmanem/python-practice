class dog : 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll(self):
        print(f'{self.name} rolled over.')

# my_dog = dog('bond',5)
# your_dog = dog('katti',4)


# print(f'my dog name is {my_dog.name}.')
# print(f'his age is {my_dog.age} years .')
# my_dog.sit()
# my_dog.roll()

# print(f'your dog name is {your_dog.name}.')
# print(f'his age is {your_dog.age} years .')
# your_dog.sit()
# your_dog.roll()

# my_dog.name = ["max","bond"]

# print(my_dog.name)

#-------------------------------------------------

class restaurant :
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'the restaurant is called {self.restaurant_name}.')
        print(f'the cusisne type is {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'the restaurant  {self.restaurant_name} is opend.')

# in_put = [input(f" enter your restaurant :"),input(f" enter your cuisine :")]

# if in_put != "":
#     my_restaurant = restaurant(in_put[0],in_put[1])

# print(f'your restaurant name is {my_restaurant.restaurant_name} and cuisne {my_restaurant.cuisine_type}')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# n_rest = {'name' : 'MovingPick' , 'cuisine' : 'french' }
# if my_restaurant.restaurant_name == "PC":
#     neigbhor_restaurant = restaurant(n_rest['name'] , n_rest['cuisine'])

#     print(f'\n {neigbhor_restaurant.restaurant_name}')
#     print(neigbhor_restaurant.cuisine_type)
#     neigbhor_restaurant.describe_restaurant()
#     neigbhor_restaurant.open_restaurant()

#-------------------------------------------------

class led :
    def __init__(self,color,size):
        self.color = color
        self.size = size
        self.model = 000

    def on(self):
        print(f'{self.color} is ON')

    def off(self):
        print(f'{self.color} is OFF')

    def descibe(self):
        print(f'the color is {self.color} and size is {self.size} and model is {self.model}')

# my_led = led("RED",'4mm')

# my_led.off()
# my_led.on()

# print(f' model no {my_led.model}')

# my_led.model = 111

# print(f' updated model {my_led.model}')

# print('\n')

# my_led.descibe()

#-------------------------------------------------

# class student:
#     def __init__(self,name,present,absent):
#         self.name = name
#         self.present = present
#         self.absent = absent

#     def thanks(self):
#         if self.present and self.absent != '':
#             print (f'hey {self.name}!, your attendence successfully registered')
    
# class details(student):
#     def __init__(self, name, present, absent, grades=None):
#         super().__init__(name, present, absent)
#         self.grades = grades
    
#     def atendence(self):
#         if self.absent > self.present :
#             print(f'😢 your attendence is not good for your career...')
#         else:
#             print(f'😊 you are going good...')

#         # if grades != None :
#         #    match grades :
#         #        case 'A' : print("")

# class_1 = student('mick',7,3)
# class_1.thanks()

# data = details('harry',4 ,6)
# data.thanks()
# data.atendence()

#---------------------------------------------------------


class students:
    def __init__(self,name,clas_s):
        self.name = name
        self.clas_s = clas_s

    def welcome(self):
        print(f' hey {self.name}, you are successfully register ... \n welcome as a {self.clas_s} student. ')

class details:
    # Instead of inheriting, we just accept a student object as an argument
    def __init__(self, student_object,present,absent, grades=None):
        self.student = student_object  # Storing the student data inside details
        self.grades = grades
        self.present = present
        self.absent = absent
    
    def atendence(self):
        # We access the parent data through the student object we passed in
        if self.absent > self.present:
            print(f'😢 {self.student.name}, your attendance is not good for your career...')
        else:
            print(f'😊 {self.student.name}, you are going good...')        
    

# std = students("petter","1A_Class")

# std.welcome()

# data = details(std,12 ,1 ,"A")

# data.atendence()

# std2 = students("janny","1C_Class")

# std2.welcome()

# data2 =details(std2,5,6)

# data2.atendence()