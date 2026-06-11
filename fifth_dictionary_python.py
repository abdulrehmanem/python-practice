car = {
    "brand" : ["Ford", "BWM", "Volvo", "Audi", "Mercedes", "Lexus"],
    "year" : [2005, 2010, 2018],
    "color" : ["red","black","white"] 
    }

# print(car["year"])
# print(car["brand"])
# print(car["color"])

# print(car["year"][1])
# print(car["brand"][2:6])
# print(car["color"][2])

# for key in car.keys():
#     print(key)

# for value in car.values():
#     print(value)

#---------------------------------- 

# for k, v in car.items():
#     if k=="brand":
#         # print(f'we have {len(v)} {k} of cars in which:')
#         # for i in v:
#         #     print(i)
#         # print('included.') ----OR----
#         print(f'we have {len(v)} {k} of cars in which: {", ".join(v)} included.')  # we have 6 brand of cars in which: Ford, BWM, Volvo, Audi, Mercedes, Lexus included.
      
#     elif k=="year":
#         print(f'and if we talk about {k} of cars, they are : {", ".join(str(f"'{i}'") for i in v)}') # and if we talk about year of cars, they are :2005, 2010, 2018}

#     elif k=='color' :
#         print(f'and we happily say that we have {len(v)} {k} of cars like: {", ".join(str(i.upper()) for i in v)}') # and we happily say that we have 3 color of cars like: red, black, white
            
#---------------------------------- 

#new_car = car[:] # this will give error because we cannot copy a dictionary by slicing

#----------------------------------

# new_car = car.copy() # this is the correct way to copy a dictionary

# del new_car["color"] # this will delete the color key and its value from new_car dictionary

# #new_car.append("color": ["red","black","white"]) # this will give error because we cannot use append method to add a new key-value pair in a dictionary

# new_car["model"] = ["Mustang", "X5", "XC90", "Q7", "S-Class", "RX"] # this will add a new key model and its value to new_car dictionary

# new_car["color"] = ["red","blue","white"] # this will add color key and its value to new_car dictionary

# new_car["color"].append("black") # this will add black color in the color list of new_car dictionary

# print(new_car)

# new_car["color"].remove("black") # this will remove black color from the color list of new_car dictionary
# print(new_car)

# C_L_keys = list(new_car.keys())[0:2] # this will give us the first two keys of new_car dictionary
# print(C_L_keys) # ['brand', 'year']
# print(len(C_L_keys))

# C_L_keys = list(new_car.keys()) # this will give us all the keys of new_car dictionary in a list
# print(C_L_keys) # ['brand', 'year', 'model', 'color']
 
#-------------------------------

# new2_car = car.copy() 
# new2_car["location"] = {
#     "country" : ["USA", "Germany", "Sweden", "Italy", "Japan"],
#     "city" : ["Detroit", "Munich", "Gothenburg", "Ingolstadt", "Tokyo"]
#     }

# for k, v in new2_car.items():
#     if k=='brand':
#         print(f' {k} : {", ".join(v)}')
#     elif k=='year':    
#         print(f' {k} : {", ".join(str(x) for x in v)}')
#     elif k=='color':
#         print(f' {k} : {", ".join(v)}')
#     elif k=='location':
#         for k1, v1 in v.items():    
#             print(f' {k1} : {", ".join(v1)}')

# del new2_car["location"] # this will delete the location key and its value from new2_car dictionary

# print(new2_car)

# #print(new2_car["location"]) # this will give error because we have deleted the location key from new2_car dictionary

# print(new2_car.get("location", "Location information is not available")) # this will return the default value because we have deleted the location key from new2_car dictionary

# The original data
matrix = {
    "row_A": {"x": 1, "y": 2},
    "row_B": {"x": 3, "y": 4}
}

# 1. Create an empty container for the final result
doubled_matrix = {}

# 2. START OUTER LOOP: Grab the rows
for row, data in matrix.items():
    
    # 3. Create a temporary empty dictionary for the new inner values
    new_inner_dict = {}
    
    # 4. START INNER LOOP: Grab the coordinates and double the values
    for coord, val in data.items():
        new_inner_dict[coord] = val * 2
        
    # 5. Save the finished inner dictionary into our main container
    doubled_matrix[row] = new_inner_dict

print(doubled_matrix)


# matrix = {
#     "row_A": {"x": 1, "y": 2},
#     "row_B": {"x": 3, "y": 4}
# }

# doubled_matrix = {
    
#     row: {coord: val * 2 for coord, val in data.items()} for row, data in matrix.items()

# }

# print(doubled_matrix)