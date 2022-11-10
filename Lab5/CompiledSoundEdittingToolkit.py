import numpy as np
import scipy.io.wavfile
from scipy.io.wavfile import write


def ReverseAudio():
    inputname = input("Input file: ")
    
    contents = scipy.io.wavfile.read(inputname)
    samplerate = contents[0]
    data = contents[1].tolist() # Now it's a Python list
    
    outputdata = Reverseprocess(data)
    outputname = inputname.replace(".wav", "-reverseValue.wav")
    scipy.io.wavfile.write(outputname, samplerate, 
    np.asarray(outputdata, dtype="int16"))
    return True
    
def Reverseprocess(data):
    result = []
    walker = len(data) - 1      
    for i in range(len(data)) :
        result.append(data[walker])
        walker -= 1
    return result

def MixingAudio():
    inputname = input("Input the first file: ")
    inputname2 = input("Input the second file: ")
    
    contents1 = scipy.io.wavfile.read(inputname)
    contents2 = scipy.io.wavfile.read(inputname2)
    samplerate1 = contents1[0]
    data1 = contents1[1].tolist() # Now it's a Python list
    data2 = contents2[1].tolist()
    
    outputdata = Mixingprocess(data1,data2)
    outputname = inputname.replace(".wav", "Mixed.wav") #Assumes first input as holder
    scipy.io.wavfile.write(outputname, samplerate1, np.asarray(outputdata, dtype="int16"))
    return True
    
def Mixingprocess(data1,data2):
    result = []
    pos1,pos2 = 0,0
    while(pos1 < len(data1) and pos2 < len(data2)):
        result.append((data1[pos1] + data2[pos2])/2)
        pos1 += 1
        pos2 += 1
        
    if (pos1 < len(data1)):
        while(pos1 < len(data1)):
            result.append(data1[pos1])
            pos1 += 1
    elif (pos2 < len(data2)):
        while(pos2 < len(data2)):
            result.append(data2[pos2])
            pos2 += 1
            
    return result

def FadeAudio():
    inputname = input("Input file: ")
    
    contents = scipy.io.wavfile.read(inputname)
    samplerate = contents[0]
    data = contents[1].tolist() # Now it's a Python list
    
    outputdata = Fadeprocess(data)
    outputname = inputname.replace(".wav", ".out.wav")
    scipy.io.wavfile.write(outputname, samplerate, 
    np.asarray(outputdata, dtype="int16"))
    return True

def Fadeprocess(data):
    result = []      
    for i in range(len(data)) :
        result.append(data[i] * (i/len(data)) )
    return result