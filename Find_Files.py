import glob

from Directory_Setup import Directory_Setup
from Run_Transdecoder import Run_Transdecoder

class Find_Files():

	ext = ""

	def __init__(self, ext):
		self.ext = ext
		self.globbing()

	def globbing(self):
		for file in glob.glob(self.ext):
			#print(file)
			ds = Directory_Setup(file)
			rt = Run_Transdecoder(ds.get_new_path())