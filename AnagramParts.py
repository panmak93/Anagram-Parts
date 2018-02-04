"""
Name: Cheuk Pan, Mak
Compsci 220
Assignment 2
"""

import sys
class Assignment2:
	def anagram(words):
		list_dict = dict()
		for word in words:
			word1 = "".join(sorted(word))
			if word1 not in list_dict:
				list_dict[word1] = [word]
			else:
				list_dict[word1] += [word]
		output_list = list()
		for key in list_dict:
			output_list.append(list_dict[key])
		output_list.sort()
		return output_list
		
	for line in sys.stdin:
		if not line or line == "\n":
			break
		if(line.index("\n")) > 0:
			line = line[0:len(line)-1]
		words = line.split(" ")
		words.sort()
		output_list = anagram(words)
		for list in output_list:
			words = ""
			for word in list:
				words += " " + word
			print(words.strip())
		print()