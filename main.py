import os
import shutil
import argparse
def create(depth=0,dir=""):
	if(depth<5):
		for i in range(5):
			name=dir+str(i+1)
			print(" "*depth,"Creating directory",name)
			os.mkdir(name)
			os.chdir(name)
			create(depth+1,name+".")
		os.chdir("..")
	else:
		os.chdir("..")
def cleanup():
	for i in range(5):
		print("Removing",i+1,"and its subdirectories")
		shutil.rmtree(str(i+1))
parser = argparse.ArgumentParser(description='Program creates a folder tree with depth of 5 and folder count 5.')
parser.add_argument("--cleanup", "-c", help="Deletes all created folders", action='store_true')
args = parser.parse_args()
if(args.cleanup):
	cleanup()
else:
	create()
