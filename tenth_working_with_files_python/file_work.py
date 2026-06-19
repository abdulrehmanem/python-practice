# with open ('tenth_working_with_files_python/text.txt') as file_object:
#     # content = file_object.read()
#     content1 = file_object.readlines()
# # print(content.split())
# # print(content.lstrip())
# clean_list=[items.strip()  for items in content1] 
# print(','.join(clean_list))         #3.672534764275348,6742657894359769,6347859436238346              
# print(content1)                     #['3.672534764275348\n', ' 6742657894359769\n', ' 6347859436238346']

#---------------------------------------------------

# with open ('tenth_working_with_files_python/text.txt') as file_object :
#         read = file_object.readlines()
#         for line in read :
#                 print(line.strip())

# 3.672534764275348
# 6742657894359769
# 6347859436238346

#---------------------------------------------------

# with open('tenth_working_with_files_python/text.txt') as file_object :
#     data = file_object.readlines()
# A_string = ''
# for line in data :
#     A_string += line.strip()
# print(data)  #['3.672534764275348\n', ' 6742657894359769\n', ' 6347859436238346']
# print(A_string) #3.67253476427534867426578943597696347859436238346

#---------------------------------------------------

# filename = 'tenth_working_with_files_python/text1.txt'

# # with open(filename,'w') as file_object :         # 'w' it over write  the file

# #     file_object.write("i love programming.")      # 'a' it add  the file
# # with open(filename,'a') as file_object :
# #     file_object.write('i love briyani.')
# #     file_object.write('i learn python.')

# #---------------------------------------------------

# def file_mode(mode,data=None):
#     try:
#         match mode:
#             case 'w' :
#              with open(filename,'w') as file_object:
#                 file_object.write(data)
            
#             case 'a' :
#              with open(filename,'a') as file_object:
#                 file_object.write(data)

#             case 'r' :
#              with open(filename,'r') as file_object:
#                 file_data = file_object.readlines()
#              return file_data
#     except Exception as e:
#         print(f'not work for now{e}')
        
    
   
        
        
          
             
# data = file_mode('r')

# print(type(data))  #<class 'list'>

# clean_data = [items.strip() for items in data]

# for i in range(len(clean_data)):
#    print(clean_data[i])

# join_form = ''.join(clean_data)
# print(join_form)


# data = "i love sleeping all day"
# file_mode('w',data)   # over write the whole file

# data = "i like read novels"
# file_mode('a',data)
         

# with open(filename, encoding='utf-8') as file_object:
#    data = file_object.readlines()
#    print(data)




# import json


# json_string = '''
# [
#     {
#         "name": "Alex Reed",
#         "age": 30,
#         "is_working": true
#     },
#     {
#         "name": "Sarah Chen",
#         "age": 25,
#         "is_working": true
#     },
#     {
#         "name": "Marcus Johnson",
#         "age": 42,
#         "is_working": false
#     },
#     {
#         "name": "Elena Rostova",
#         "age": 19,
#         "is_working": false
#     }
# ]

# '''

# data = json.loads(json_string)

# # print(type(data))

# # for no,item in  enumerate(data, start=1):
# #     print(f'{no} :-')
# #     for key , value in item.items():
# #         print(f"key : {key}  , value : {value}")    
# #     print('')
    

# input_data = []

# while True :
#     name = input('please ente your name: ')
    
#     if name == 'q':
#         break
    
#     age = int(input('please ente your age: '))
    
#     input_data.append({
#             'name': name,
#             'age' : age
#             })
        
# print(input_data)

# data += input_data[:]     
# updated_json_string = json.dumps(data,indent=1)
# print(updated_json_string)
            
        
             
import json
data_json = 'tenth_working_with_files_python/data.json'
 
with open(data_json,'r') as file_json:
# with open(data_json) as file_json:
    data = json.load(file_json)
    #data = json.loads(file_json.read())
print(f"BEFORE DATA : \n {data}")
data_dump =[{'name': 'herry','age': '12','is_working': 'False'},{'name': 'janyy','age': '20','is_working': 'False'}]

data += data_dump[:]

with open(data_json,'w') as file_json:
    json.dump(data,file_json,indent=1)
     

with open(data_json,'r') as file_json:
# with open(data_json) as file_json:
    data = json.load(file_json)
print('\n AFTER DATA :')
for no,item in enumerate(data,0):
    print(f'{no} :-')
    for k,v in item.items():
        print(f'{{"{k}": "{v}"}}')












