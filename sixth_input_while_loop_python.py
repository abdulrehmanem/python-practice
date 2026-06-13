# message = input("Enter a message (type 'exit' to quit): ")
# print("You entered:", message)

#-----------------------------------

# no = int(input("Enter a number : "))

# while no != 0:
#     print("You entered:", no)
#     no = int(input("\nEnter a number : "))

#-----------------------------------

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#-----------------------------------

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = []
# user_input = ""
# while user_input != 'quit':
#     user_input = input(prompt)
#     message.append(user_input)

# print("\nYou entered the following messages:")
# if message != ['']:
#         message.remove('quit')  
#         print(" ".join(message))

#-----------------------------------

prompt = "\nPlease enter the name of a student: "

students = []
 
# active = True
# while active :
#     std = input(prompt)
#     students.append(str(std))
#     if std == 'exit':
#         active = False
#         students.remove('exit')

# total_student = f'the total students are {len(students)} in which {", ".join(students)} are the students'     

# print(total_student)
 
#or

# while True:
#     std = input(prompt)
#     if std.lower() == 'exit':
#         break
#     students.append(std)

# print(students) 

#-----------------------------------

# number = []
# current_no =0
# while current_no <=11 :
#     current_no += 1
#     if current_no % 2 ==0:
#         continue
#     number.append(current_no)

# print(number)

#-----------------------------------

# usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

# registered_usernames = []

# while usernames :
#     currentuser = usernames.pop() 
#     if currentuser == 'admin':
#         print("Hello admin, would you like to see a status report?")
#     else:
#         registered_usernames.append(currentuser)

# print(f"\nRegistered usernames: {', '.join(reversed(registered_usernames))}")      

#-----------------------------------

# pet = ['cat', 'dog','cat', 'rabbit', 'cat','hamster','cat', 'parrot']

# #print(set(pet))
# print(pet)

# while 'cat' in pet:
#     pet.remove('cat')
# print(pet)

#------------------advance------------------

# The user types: John 25 Engineer
# name, age, job = input("Enter name, age, and job (separated by spaces): ").split()

# print(f"{name} is a {age}-year-old {job}.")

#----------X----------------

# attempts = 0

# while attempts < 3:
#     password = input("Enter password: ")
#     if password == "secret":
#         print("Access Granted!")
#         break
#     attempts += 1
# else:
#     # This only runs if the loop finished all 3 rounds without a 'break'
#     print("Too many wrong attempts. Account locked.")

#-------------------X------------------

# This assigns the input to 'command' AND checks if it's != 'quit' at the same time
# while (command := input("Enter command: ")) != "quit":
#     print(f"Executing: {command}")b  