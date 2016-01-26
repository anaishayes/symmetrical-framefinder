import sys
import os
import subprocess

class Directory_Setup():

	file_name = ""
	out_dir = ""
	new_path = ""

	common_substring = "_SOAPTrans1.03.scaffold.fasta"

	def __init__(self, file_name):
		# don't need path for file because we'll be running it from the directory
		self.file_name = file_name
		self.__make_directory()
		self.__move_file()

	# make directory based on the file's name
	# argument file_name = string, name of fasta file working with
	def __make_directory(self):
	# before making directory, create directory name
		self.out_dir = self.file_name.replace(self.common_substring, "")
		if not os.path.exists(self.out_dir):
			os.makedirs(self.out_dir)
		else:
			print "Directory exists"
			sys.exit()
		self.new_path = self.out_dir+"/"+self.file_name

	# moves fasta file from parent directory into out_dir,
	# by renaming the file and adding the new directory before it
	def __move_file(self):
		subprocess.call(['mv', self.file_name, self.new_path])

	# returns the new path for the working fasta file
	# to access new_path variable outside of make_directory function
	# and within the Transdecoder class
	def get_new_path(self):
		return self.new_path