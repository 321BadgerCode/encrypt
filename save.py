#badger
import json

def set_save(file_name:str,msg:str,key:int)->None:
	with open(file_name+".json",'w') as f:
		json.dump({"msg":msg,"key":str(bin(key))},f)

def set_load(file_name:str)->object:
	with open(file_name+".json",'r') as f:
		data=json.load(f)
		return data