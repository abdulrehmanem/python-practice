import json
# file_jsondata = 'data_handling/json_file_data.json'
# with open(file_jsondata,'r') as readjson:
#     loaded_data = json.load(readjson)
#     readable_file = 'data_handling/readablejson.json'

# with open(readable_file ,'w') as writejson:
#     json.dump(loaded_data,writejson,indent=2)


def json_handling(file,action,data=None):
    act  = action.lower()
    if act=='r':
       try:
           with open(file,action,encoding='utf-8') as data:
                   data = json.load(data)
                   return data
       except FileNotFoundError:
            print(f"❌ Error: The file '{file}' does not exist.")
            return None
       except json.JSONDecodeError:
            print(f"❌ Error: '{file}' contains invalid JSON or is completely empty.")
            return None   
    elif act=='w':
       try:
           with open(file,action,encoding='utf-8') as f:
               json.dump(data,f,indent=4)
               return f"data successfuly write in {file}"
       except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
       
data = json_handling('data_handling/json_file_data.json',"r")
print(data)

wirte = json_handling('data_handling/readablejson.json',"w",data)
print(wirte)