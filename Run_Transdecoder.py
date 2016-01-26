import sys
import subprocess

"""
Step 1) TransDecoder.LongOrfs -t Tinca_tinca_gill_SOAPTrans1.03.scaffold.fasta 
Step 2) TransDecoder.Predict -t Tinca_tinca_gill_SOAPTrans1.03.scaffold.fasta
			This one takes ages :p 
"""
# purpose: run two bash commands on each file
class Run_Transdecoder():

	transdecoder_dir_addition = ".transdecoder_dir"

	def __init__(self, file_name):
		self.__find_long_ORFs(file_name)
		self.__predict_stats(file_name)
		self.__cleanup_dirs(file_name)

	# bash command for Transdecoder step 1
	def __find_long_ORFs(self, file_name):
		subprocess.call(['/home/amhayes/TransDecoder-2.0.1/TransDecoder.LongOrfs', '-t', file_name])

	# bash command for step 2
	def __predict_stats(self, file_name):
		subprocess.call(['/home/amhayes/TransDecoder-2.0.1/TransDecoder.Predict', '-t', file_name])

	def __cleanup_dirs(self, file_name):
		toks = file_name.split("/")
		subprocess.call(['mv', toks[1]+self.transdecoder_dir_addition, toks[0]+"/"])