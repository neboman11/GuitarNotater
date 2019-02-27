from sys import argv
import numpy as np
import pyaudio
import time

eString = ""
BString = ""
GString = ""
DString = ""
AString = ""
EString = ""

# Takes a string - note, and checks if it is one of the possible notes listed. If it is, it adds the tab version to the corresponding line for
# each string.
# Parameters: string - note
# Returns: Nothing
def noteToTab(note):
    global eString
    global BString
    global GString
    global DString
    global AString
    global EString
    if(note == "E2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "0-"
    if(note == "F2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "1-"
    if(note == "F#2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "2-"
    if(note == "G2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "3-"
    if(note == "G#2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "4-"
    if(note == "A2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "0-"
        EString += "--"
    if(note == "A#2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "1-"
        EString += "--"
    if(note == "B2"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "2-"
        EString += "--"
    if(note == "C3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "3-"
        EString += "--"
    if(note == "C#3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "4-"
        EString += "--"
    if(note == "D3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "0-"
        AString += "--"
        EString += "--"
    if(note == "D#3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "1-"
        AString += "--"
        EString += "--"
    if(note == "E3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "2-"
        AString += "--"
        EString += "--"
    if(note == "F3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "3-"
        AString += "--"
        EString += "--"
    if(note == "F#3"):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "4-"
        AString += "--"
        EString += "--"
    if(note == "G3"):
        eString += "--"
        BString += "--"
        GString += "0-"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "G#3"):
        eString += "--"
        BString += "--"
        GString += "1-"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "A3"):
        eString += "--"
        BString += "--"
        GString += "2-"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "A#3"):
        eString += "--"
        BString += "--"
        GString += "3-"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "B3"):
        eString += "--"
        BString += "0-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "C4"):
        eString += "--"
        BString += "1-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "C#4"):
        eString += "--"
        BString += "2-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "D4"):
        eString += "--"
        BString += "3-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "D#4"):
        eString += "--"
        BString += "4-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "E4"):
        eString += "0-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "F4"):
        eString += "1-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "F#4"):
        eString += "2-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "G4"):
        eString += "3-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "G#4"):
        eString += "4-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "A4"):
        eString += "5-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "A#4"):
        eString += "6-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "B4"):
        eString += "7-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "C5"):
        eString += "8-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "C#5"):
        eString += "9-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note == "D5"):
        eString += "10-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "D#5"):
        eString += "11-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "E5"):
        eString += "12-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "F5"):
        eString += "13-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "F#5"):
        eString += "14-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "G5"):
        eString += "15-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "G#5"):
        eString += "16-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "A5"):
        eString += "17-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "A#5"):
        eString += "18-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "B6"):
        eString += "19-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "C6"):
        eString += "20-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "C#6"):
        eString += "21-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "D6"):
        eString += "22-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "D#6"):
        eString += "23-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "E6"):
        eString += "24-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == "F6"):
        eString += "24b25-"
        BString += "------"
        GString += "------"
        DString += "------"
        AString += "------"
        EString += "------"
    if(note == "F#6"):
        eString += "24b26-"
        BString += "------"
        GString += "------"
        DString += "------"
        AString += "------"
        EString += "------"
    if(note == "G6"):
        eString += "24b27-"
        BString += "------"
        GString += "------"
        DString += "------"
        AString += "------"
        EString += "------"
#    if(note == "custom"):
#        ceString = input("Tab for e:")
#        cBString = input("Tab for B:")
#        cGString = input("Tab for G:")
#        cDString = input("Tab for D:")
#        cAString = input("Tab for A:")
#        cEString = input("Tab for E:")
#        eString += ceString
#        BString += cBString
#        GString += cGString
#        DString += cDString
#        AString += cAString
#        EString += cEString

# Outputs the tab to the console and writes it to a file named "tab.txt"
# Parameters: none
# Returns: nothing
def outputTab():
        print("e|" + eString + "\n" + "B|" + BString + "\n" + "G|" + GString + "\n" + "D|" + DString + "\n" + "A|" + AString + "\n" + "E|" + EString)
        fn = "tab.txt"
        target = open(fn, "w")
        target.write("e|" + eString + "\n" + "B|" + BString + "\n" + "G|" + GString + "\n" + "D|" + DString + "\n" + "A|" + AString + "\n" + "E|" + EString)


## Forty lines of code I used from an already existing program and edited it to fit my project
## https://github.com/mzucker/python-tuner (technically copyright infringement since there's no license)
## Has been modified to fit this application

NOTE_MIN = 40                       # E2 (lowest note in E standard)
NOTE_MAX = 91                       # G6 (highest note with a bend in E standard)
FSAMP = 44100                       # Sampling frequency in Hz
FRAME_SIZE = 4096                   # samples per frame
FRAMES_PER_FFT = 16                 # FFT takes average across how many frames?
loopTimer = 30                      # set the time to loop for in seconds

SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT

NOTE_NAMES = "C C# D D# E F F# G G# A A# B".split()

######################################################################
# functions based upon this webpage:
# https://newt.phys.unsw.edu.au/jw/notes.html

def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
def number_to_freq(n): return 440 * 2.0**((n-100)/12.0)
def note_name(n): return NOTE_NAMES[n % 12] + str(int(n/12) - 1)

def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))

buf = np.zeros(SAMPLES_PER_FFT, np.dtype(np.float32))
num_frames = 0

stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=FSAMP, input=True, frames_per_buffer=FRAME_SIZE)

stream.start_stream()

window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))

print("sampling at", FSAMP, "Hz with max resolution of", FREQ_STEP, "Hz")
print("\n")

# Read audio input, calculate note letter and octave, and add it to the tab
while time.time() < time.time() + loopTimer:
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)

    fft = np.fft.rfft(buf * window)

    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    noteNum = freq_to_number(freq)
    noteNumWhole = int(round(noteNum))

    num_frames += 1

    if num_frames >= FRAMES_PER_FFT:
        print("freq: {:7.2f} Hz     note: {:>3s} {:+.2f}".format(freq, note_name(noteNumWhole), noteNum-noteNumWhole))
        noteToTab(note_name(noteNumWhole))

outputTab()