import numpy as np
import scipy.io.wavfile
from scipy.io.wavfile import write

def main():
    inputname = input("Input file: ")
    
    contents = scipy.io.wavfile.read(inputname)
    samplerate = contents[0]
    data = contents[1].tolist() # Now it's a Python list
    
    outputdata = process(data)
    outputname = inputname.replace(".wav", "-reverseValue.wav")
    scipy.io.wavfile.write(outputname, samplerate, 
    np.asarray(outputdata, dtype="int16"))
    
def process(data):
    result = []
    walker = len(data) - 1      
    for i in range(len(data)) :
        result.append(data[walker])
        walker -= 1
    return result

main()