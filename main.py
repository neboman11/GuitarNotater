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

# Takes a int - note, and adds the tab version to the corresponding line for each string.
# Parameters: int - note
# Returns: Nothing
def noteToTab(note):
    global eString
    global BString
    global GString
    global DString
    global AString
    global EString
    if(note < 45):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += str(note - 40) + "-"
    if(note > 44 and note < 50):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += str(note - 45) + "-"
        EString += "--"
    if(note > 49 and note < 55):
        eString += "--"
        BString += "--"
        GString += "--"
        DString += str(note - 50) + "-"
        AString += "--"
        EString += "--"
    if(note > 54 and note < 59):
        eString += "--"
        BString += "--"
        GString += str(note - 55) + "-"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note > 58 and note < 64):
        eString += "--"
        BString += str(note - 55) + "-"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note > 63 and note < 73):
        eString += str(note - 64) + "-"
        BString += "--"
        GString += "--"
        DString += "--"
        AString += "--"
        EString += "--"
    if(note > 72 and note < 88):
        eString += str(note - 73) + "-"
        BString += "---"
        GString += "---"
        DString += "---"
        AString += "---"
        EString += "---"
    if(note == 89):
        eString += "24b25-"
        BString += "------"
        GString += "------"
        DString += "------"
        AString += "------"
        EString += "------"
    if(note == 90):
        eString += "24b26-"
        BString += "------"
        GString += "------"
        DString += "------"
        AString += "------"
        EString += "------"
    if(note == 91):
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
loopTimer = time.time() + 3         # set the time to loop for in seconds

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
while time.time() < loopTimer:
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)

    fft = np.fft.rfft(buf * window)

    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    noteNum = freq_to_number(freq)
    noteNumWhole = int(round(noteNum))

    num_frames += 1

    if num_frames >= FRAMES_PER_FFT:
        print("freq: {:7.2f} Hz     note: {:>3s} {:+.2f} MIDI {:}".format(freq, note_name(noteNumWhole), noteNum-noteNumWhole, noteNumWhole))
        noteToTab(noteNumWhole)

outputTab()