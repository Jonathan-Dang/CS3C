import numpy as np
import scipy.io.wavfile
from scipy.io.wavfile import write

def main():
    inputname = input("Input file: ")
    
    contents = scipy.io.wavfile.read(inputname)
    samplerate = contents[0]
    data = contents[1].tolist() # Now it's a Python list
    
    outputdata = process(data)
    outputname = inputname.replace(".wav", ".out.wav")
    scipy.io.wavfile.write(outputname, samplerate, 
    np.asarray(outputdata, dtype="int16"))
   
#THIS IS GIVEN FROM THE OFFICIAL DOCUMENTATION OF scipy.io.wavefile
#url = https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html
#We use the WAV file from this function to allow the audibility of the modification.
#The WAV files provided did not provide noticible results.
def create100hzFile():
    samplerate = 44100; fs = 100
    t = np.linspace(0., 10., samplerate)
    amplitude = np.iinfo(np.int16).max
    data = amplitude * np.sin(2. * np.pi * fs * t)
    write("example.wav", samplerate, data.astype(np.int16))
   
def process(data):
    result = []      
    for i in range(len(data)) :
        result.append(data[i] * (i/len(data)) )
    return result
#create100hzFile()
main()