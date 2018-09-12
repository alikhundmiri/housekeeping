'''
W H A T     D O E S     T H I S     F I L E     D O E S ?

This file will create a new form for you

RUN ONLY WITH PYTHON 3
_________________________________________________________________

H O W     T O     U S E     T H I S     F I L E

run this script to generate a new form file.
_________________________________________________________________

'''
import os

def main():
	# Ask user to enter NAME

	print("\n\n\tI M P O R T A N T: Run only in python3\n\n\t")

	file_name = input("Please enter the file name: ")
	print("Please hold on a moment...")
	os.chdir('/Users/alikhundmiri/Desktop/pythons/housekeeping/code/new_form')
	f= open("new_form_matter.txt","r")
	if f.mode == 'r':
		contents =f.read()
		f.close() 

	g = open("../"+ str(file_name)+".py","w+")
	g.write(contents)
	g.close()
	print("DONE! created a file called " + str(file_name) +".py")

	# open new_form_matter.txt
	# read the text
	# make a new file
	# name it as NAME.py
	# exit
if __name__ == '__main__':
	main()