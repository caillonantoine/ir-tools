#coding:utf-8
import numpy as np
import wave
from scipy.io import wavfile as wf
from scipy.signal import chirp

def read(file):
	return wf.read(file)[1]/32767.
	
def write(file,array):
	output = wave.open(file,'w')
	array = ''.join([wave.struct.pack('h',elm) for elm in ((array*32767).astype('int'))])
	output.setparams((1,2,96000,0,'NONE','not compressed'))
	output.writeframes(array)
	output.close()
		
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
	Y = np.zeros(2**radix)
	Y[0:N] = array
	return array
	
def cvn(r,i):
	r_ = np.fft.rfft(radix2(r))
	i_ = np.fft.rfft(radix2(i))
	y_ = np.zeros_like(r_)
	for k in range(len(r_)):
		y_[k] = r_[k] * i_[k%len(i_)]
	y = np.fft.irfft(y_)
	return y/float(np.max(y))
	
def dcvn(r,i):
	return cvn(r,i[::-1])
	
def get_ir(r,i):
	y = dcvn(r,i)
	start = np.argmax(y)
	return y[start:]
		