#badger
def get_encrypt(message:str,key:int)->str:
	b1:str=''

	for a in range(len(message)):
		b1+=chr(ord(message[a%len(message)])^key)

	return b1

def get_salt_hash(a1:str,salt:int=1315423911)->int:
	hash:int=salt
	b1:int=0

	for a in range(len(a1)):
		b1=ord(a1[a])
		hash^=((hash<<5)+b1+(hash>>2))

	return (hash&0x7FFFFFFF)