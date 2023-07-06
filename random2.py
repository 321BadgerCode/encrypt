#badger
import time
import hashlib

def get_seed()->int:
	seed:int=time.time()
	seed=int(hashlib.sha256(str(seed).encode("utf-8")).hexdigest(),16)
	return seed

def get_linear_feedback_shift_register(seed:int=1)->int:
	bit:int=(seed^(seed>>1))&1
	b1:int=(seed>>1)|(bit<<3)

	return b1

def get_random_int(min:int,max:int,seed:int=get_seed())->int:
	seed2=((1103515245*12345)%2**31)

	b1:int=seed+seed2
	b2:int=((max-min)+1)+min

	return b1%b2