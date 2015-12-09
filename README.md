PyBTC
------
Coded by MGF15

PyBTC it's Simple (script & library) 

Bitcoin Address's Generator (offline) , Base58Check (WIF) Encode/Decode , WIF to Bitcoin Address


Usage (library)
------

#Address 

	>>> from PyBTC import Addr
	>>> Addr('0000000000000000000000000000000000000000000000000000000000000002')
	'1LagHJk2FyCV2VzrNHVqg3gYG4TSYwDV4m'

#WIF 

	>>> from PyBTC import WIF
	>>> WIF('0000000000000000000000000000000000000000000000000000000000000002')
	'5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH'

#Base58 Encode/Decode

	>>> from PyBTC import EncodeB58
	>>> EncodeB58('800C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D507A5B8D')
	'5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ'
	
	>>> from PyBTC import DecodeB58
	>>> DecodeB58('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')
	'800c28fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d507a5b8d'
	
Usage (Script)
------
	
	PyBTC.py -h
		Help 
		-a               Generator Bitcoin Address
		-e  [wif]        Encode Base58
		-d  [wif]        Decode Base58
		-wa [wif]        WIF to Bitcoin Address


	PyBTC.py -a 
	Address :  1LagHJk2FyCV2VzrNHVqg3gYG4TSYwDV4m
	Privkey :  0000000000000000000000000000000000000000000000000000000000000002
	WIF     :  5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAvUcVfH
	
	PyBTC.py -e 00d6c8e828c1eca1bba065e1b83e1dc2a36e387a4274d4b4aa
	1LagHJk2FyCV2VzrNHVqg3gYG4TSYwDV4m
	
	PyBTC.py -d 1LagHJk2FyCV2VzrNHVqg3gYG4TSYwDV4m 00d6c8e828c1eca1bba065e1b83e1dc2a36e387a4274d4b4aa

	PyBTC.py -wa 5JN7pp4BX6rM8wBEmuisnveuZEUEZwXZXUBeqMGWQQEKwKE1ZNe 
	Address : 1bu4oRfE2cTM6cnWMp4cRg6rjAxu6mGnV
	
Installation
------
	Base58
	
	https://pypi.python.org/pypi/base58
	
	ECDSA
	
	https://pypi.python.org/pypi/ecdsa
	
License
------

This library is free and open-source software released under the MIT license
	
