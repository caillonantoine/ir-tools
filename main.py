#coding:utf-8
import numpy as np
import wave as wa
from scipy.io import wavfile as wf
import scipy.signal.chirp as chirp

def read(file):
	return wf.read(file)[1]
	
def write(file,array):
	with wa.open(file,'w') as output:
		array = ''.join(wa.struct.pack('h',elm) for elm in ((array*32767).astype('int'))
		output.setparams((1,2,44100,0,'NONE','not compressed'))
		output.writeframes(array)
		
def generate_chirp(f0,f1,T,fe):
	space = np.linspace(0,T,fe*T)
	return chirp(space,f0,T,f1)
	
def radix2(array):
	N = len(array)
	radix = 0
	while 1:
		if 2**radix < N:
			radix += 1
		else:
			break
	Y = np.zeros(radix)
	Y[0:N] = array
	return array