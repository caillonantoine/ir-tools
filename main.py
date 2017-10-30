#coding:utf-8
import numpy as np
import wave
from scipy.io import wavfile as wf
from scipy.signal import chirp

fe = 44100

def read(file):
	return wf.read(file)[1]/32767.
	
def write(file,array):
	output = wave.open(file,'w')
	array = ''.join([wave.struct.pack('h',elm) for elm in ((array*32767).astype('int'))])
	output.setparams((1,2,fe,0,'NONE','not compressed'))
	output.writeframes(array)
	output.close()
		
def generate_chirp(f0,f1,T,fe):
	space = np.linspace(0,T,fe*T)
	return chirp(space,f0,T,f1,method='linear')
	
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
	return Y
	
def cvn(r,i):
	i2 = np.zeros_like(r)
	i2[0:len(i)] = i
	r_ = np.fft.rfft(radix2(r))
	i_ = np.fft.rfft(radix2(i2))
	y_ = r_ * i_
	y = np.fft.irfft(y_)
	return y/float(np.max(abs(y)))
	
def dcvn(r,i):
	return cvn(r,i[::-1])
	
def get_ir(r,i):
	y = dcvn(r,i)
	start = np.argmax(y)
	return y[start:]
		
def main():
	print "Import de l'impulse"
	i = read('impulse.wav')
	print "Import de la réponse"
	r = read('response.wav')
	print "Calcul de la réponse impulsionnelle"
	ri = get_ir(r,i)
	return ri