#coding:utf-8
import numpy as np
import wave as wa
from scipy.io import wavfile as wf

def read(file):
	return wf.read(file)[1]
	
def write(file,array):
	with wa.open(file,'w') as output:
		array = ''.join(wa.struct.pack('h',elm) for elm in ((array*32767).astype('int'))
		output.setparams((1,2,44100,0,'NONE','not compressed'))
		output.writeframes(array)