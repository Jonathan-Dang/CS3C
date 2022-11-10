from CompiledSoundEdittingToolkit import *

def main():
    while True:
        print("Please choose an option to run!:")
        print("(1) Reverse a WAV file")
        print("(2) Fade in a WAV file")
        print("(3) Mix Two WAV files")
        print("(4) Exit")
        option = int(input(":> "))
        if (option == 1):
            ReverseAudio()
        elif (option == 2):
            FadeAudio()
        elif (option == 3):
            MixingAudio()
        elif (option == 4):
            break;
        
main()