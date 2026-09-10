
import random
from collections import Counter

def main():

	         #'helloifyouarereadingthisyouhave'
	message = 'DKFFQHXAQBUTKTKUGHJNMDHPAQBDUCKO' + \
	'TUOEKGMDKOQGKVHMDAQBTPBSKTHQTUJU' + \
	'FAMHOPPEHFFPHVUJMKGMQMDUJEAQBXQTT' + \
	'KUGHJNMDKSBYYFQTXQTMDKPKSUPMMKJA' + \
	'KUTPUJGFKMAQBEJQVMDUMMDHPVHFFRKM'  + \
	'DKFUPMSBYYFKMDHPDUPRKKJUVQJGKTXBF'  + \
	'QSSQTMBJHMAXQTIKMQOQJMTHRBMKMQMD'  + \
	'KHJXQTIPOQIIBJHMAUJGIKKMIUJAJKVSKQS'  + \
	'FKRBMHMPMHIKMQOFQPKMDHPODUSMKTUJ'  + \
	'GIQCKQJMQJKVQSSQTMBJHMHKPMDUJEAQB'
	
	#frequency analysis
	#print(Counter(message))
	collection_info = {"A":"y",
	"B":"u",
	"C":"v",
	"D":"h",
	"E":"k",
	"F":"l",
	"G":"d",
	"H":"i",
	"I":"m",
	"J":"n",
	"K":"e",
	"L":" ",
	"M":"t",
	"N":"g",
	"O":"c",
	"P":"s",
	"Q":"o",
	"R":"b",
	"S":"p",
	"T":"r",
	"U":"a",
	"V":"w",
	"W":" ",
	"X":"f",
	"Y":"z",
	"Z":" "

	}

	newmessage = ""
	info = ""
	for i in range(0, len(message)):
		info = message[i]
		if info == " ":
			newmessage+=info
		else:
			newmessage += collection_info[info]
	print(newmessage)

if __name__ == "__main__":
	main()