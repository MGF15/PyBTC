#PyBTC
#Coded by MGF15
#PyBTC it's Simple (script & library) 
#Bitcoin Address's Generator (offline) , Base58Check (WIF) Encode/Decode , WIF to Bitcoin Address
from hashlib import sha256,new
from base58 import b58encode as enb58, b58decode as deb58
from ecdsa import SigningKey , curves
import sys,random

help = '''
-a               Generator Bitcoin Address
-e  [wif]        Encode Base58
-d  [wif]        Decode Base58
-wa [wif]        WIF to Bitcoin Address
'''

def rankey():
	rand = random.randint(0x00000,0xfffff)
	key = sha256(str(rand).encode('hex')).hexdigest()
	return key
	
def EncodeB58(text):
	e = (text).decode('hex')
	encode = enb58(e)
	return encode
	
def DecodeB58(text):
	d = deb58(text)
	decode = (d).encode('hex')
	return decode
	
def WIFB(wif):
	w = DecodeB58(wif)
	b8 = w[2:-8]
	addr = Addr(b8)
	return addr

def WIF(key):
	privkey = '80' + key
	dbhsha = sha256((sha256((privkey).decode('hex')).hexdigest()).decode('hex')).hexdigest()
	checksum = dbhsha[:8]
	r =  privkey + checksum
	WIF = EncodeB58(r)
	return WIF
	
def Addr(key):
	if key == 0:
		key = rankey()
		print WIF(key)
	private_key = SigningKey.from_secret_exponent(int(key,16),curves.SECP256k1)
	public_key = sha256(('04'+(private_key.get_verifying_key().to_string()).encode('hex')).decode('hex')).hexdigest()
	RIPEMD = new('ripemd160',(public_key).decode('hex')).hexdigest()
	dbhash = sha256((sha256(('00'+RIPEMD).decode('hex')).hexdigest()).decode('hex')).hexdigest()
	o = '00'+RIPEMD+dbhash[:8]
	address = EncodeB58(o)
	return address

try:
	opt = sys.argv[1]
	if opt == '-h':
		print help
	if opt == '-a':
		try:
			key = sys.argv[2]
		except:
			key = rankey()
		address  = Addr(key)
		WIF = WIF(key)
		print 'Address : ', address ,'\nPrivkey : ', key ,'\nWIF\t: ', WIF
	if opt == '-e':
		argv = sys.argv[2]
		try:
			print EncodeB58(argv)
		except:
			print 'Invalid Base58 Character(s)!!'
	if opt == '-d':
		argv = sys.argv[2]
		try:
			print DecodeB58(argv)
		except:
			print 'Invalid Hex Character(s)!!'
	if opt == '-wa': #done
		argv = sys.argv[2]
		try:
			print 'Address : ', WIFB(argv)
		except:
			print 'Invalid Base58 Character(s)!!'
except:
	pass
