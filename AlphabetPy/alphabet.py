import argparse
import sys
from .planar import charactersPlanar
from .stereo import charactersStereo
from .calen import charactersCalen
def Alphabet(str, mode="planar"):
	if mode == "planar":
		height = 7
		characters = charactersPlanar
	elif mode == "stereo":
		height = 7
		characters = charactersStereo
	elif mode == "calen":
		height = 3
		characters = charactersCalen
	else:
		print("wrong parameter, please input \"--planar\" or \"--stereo\"!")
	result = []
	for i in range(0, height):
		tmp = ""
		for k in range(0, len(str)):
			tmp += characters[str[k].upper()][i]
		print(tmp)
		
def start():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--string", help="-s/--string <the string you want to change(a~z,A~Z,0~9)>", type=str)
	parser.add_argument("-m", "--mode", help="-m/--mode <the mode you want to choose(planar or stereo), if didn't choose, it'll be planar>")
	args = parser.parse_args()
	if args.string:
		if args.mode:
			Alphabet(args.string, args.mode)
			sys.exit()
		else:
			Alphabet(args.string, "planar")
			sys.exit()
	string = input("input the string you want to change:")
	mode = input("input the mode you want to use:(\"planar\" or \"stereo\")")
	Alphabet(string, mode)

def getAlphabet(str, mode="planar"):
	if mode == "planar":
		height = 7
		characters = charactersPlanar
	elif mode == "stereo":
		height = 7
		characters = charactersStereo
	elif mode == "calen":
		height = 3
		characters = charactersCalen
	else:
		print("wrong parameter, please input \"--planar\" or \"--stereo\"!")
	result = []
	for i in range(0, height):
		tmp = ""
		for k in range(0, len(str)):
			tmp += characters[str[k].upper()][i]
		result.append(tmp)
	return result


			