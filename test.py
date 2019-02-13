from sys import argv
import numpy as np
import pyaudio
import time

def firstnote(note):
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    #note = raw_input("Enter note: ")
    if(note == "E2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|0-"
    if(note == "F2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|1-"
    if(note == "F#2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|2-"
    if(note == "G2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|3-"
    if(note == "G#2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|4-"
    if(note == "A2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|0-"
        line6 += "E|--"
    if(note == "A#2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|1-"
        line6 += "E|--"
    if(note == "B2"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|2-"
        line6 += "E|--"
    if(note == "C3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|3-"
        line6 += "E|--"
    if(note == "C#3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|4-"
        line6 += "E|--"
    if(note == "D3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|0-"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "D#3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|1-"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "E3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|2-"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "F3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|3-"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "F#3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|4-"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "G3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|0-"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "G#3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|1-"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "A3"):
        line1 = line1 + "e|--"
        line2 += "B|--"
        line3 += "G|2-"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "A#3"):
        line1 += "e|--"
        line2 += "B|--"
        line3 += "G|3-"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "B3"):
        line1 += "e|--"
        line2 += "B|0-"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "C4"):
        line1 += "e|--"
        line2 += "B|1-"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "C#4"):
        line1 += "e|--"
        line2 += "B|2-"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "D4"):
        line1 += "e|--"
        line2 += "B|3-"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "D#4"):
        line1 += "e|--"
        line2 += "B|4-"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "E4"):
        line1 += "e|0-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "F4"):
        line1 += "e|1-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "F#4"):
        line1 += "e|2-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "G4"):
        line1 += "e|3-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "G#4"):
        line1 += "e|4-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "A4"):
        line1 += "e|5-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "A#4"):
        line1 += "e|6-"
        line2 += "B|--"
        line3 += "G|--"
        line4 += "D|--"
        line5 += "A|--"
        line6 += "E|--"
    if(note == "custom"):
        cline1 = input("Tab for e:")
        cline2 = input("Tab for B:")
        cline3 = input("Tab for G:")
        cline4 = input("Tab for D:")
        cline5 = input("Tab for A:")
        cline6 = input("Tab for E:")
        line1 += cline1
        line2 += cline2
        line3 += cline3
        line4 += cline4
        line5 += cline5
        line6 += cline6
    if(note == "exit"):
        print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6)
        fn = "tab.txt"
        target = open(fn, "w")
        target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6)
        return
    #notes()

def notes(note):
    global line1
    global line2
    global line3
    global line4
    global line5
    global line6
    #note = raw_input("Enter note: ")
    if(note == "E2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "0-"
    if(note == "F2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "1-"
    if(note == "F#2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "2-"
    if(note == "G2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "3-"
    if(note == "G#2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "4-"
    if(note == "A2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "0-"
        line6 += "--"
    if(note == "A#2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "1-"
        line6 += "--"
    if(note == "B2"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "2-"
        line6 += "--"
    if(note == "C3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "3-"
        line6 += "--"
    if(note == "C#3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "4-"
        line6 += "--"
    if(note == "D3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "0-"
        line5 += "--"
        line6 += "--"
    if(note == "D#3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "1-"
        line5 += "--"
        line6 += "--"
    if(note == "E3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "2-"
        line5 += "--"
        line6 += "--"
    if(note == "F3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "3-"
        line5 += "--"
        line6 += "--"
    if(note == "F#3"):
        line1 += "--"
        line2 += "--"
        line3 += "--"
        line4 += "4-"
        line5 += "--"
        line6 += "--"
    if(note == "G3"):
        line1 += "--"
        line2 += "--"
        line3 += "0-"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "G#3"):
        line1 += "--"
        line2 += "--"
        line3 += "1-"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "A3"):
        line1 += "--"
        line2 += "--"
        line3 += "2-"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "A#3"):
        line1 += "--"
        line2 += "--"
        line3 += "3-"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "B3"):
        line1 += "--"
        line2 += "0-"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "C4"):
        line1 += "--"
        line2 += "1-"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "C#4"):
        line1 += "--"
        line2 += "2-"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "D4"):
        line1 += "--"
        line2 += "3-"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "D#4"):
        line1 += "--"
        line2 += "4-"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "E4"):
        line1 += "0-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "F4"):
        line1 += "1-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "F#4"):
        line1 += "2-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "G4"):
        line1 += "3-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "G#4"):
        line1 += "4-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "A4"):
        line1 += "5-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "A#4"):
        line1 += "6-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "B4"):
        line1 += "7-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "C5"):
        line1 += "8-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "C#5"):
        line1 += "9-"
        line2 += "--"
        line3 += "--"
        line4 += "--"
        line5 += "--"
        line6 += "--"
    if(note == "D5"):
        line1 += "10-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "D#5"):
        line1 += "11-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "E5"):
        line1 += "12-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "F5"):
        line1 += "13-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "F#5"):
        line1 += "14-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "G5"):
        line1 += "15-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "G#5"):
        line1 += "16-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "A5"):
        line1 += "17-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "A#5"):
        line1 += "18-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "B6"):
        line1 += "19-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "C6"):
        line1 += "20-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "C#6"):
        line1 += "21-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "D6"):
        line1 += "22-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "D#6"):
        line1 += "23-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "E6"):
        line1 += "24-"
        line2 += "---"
        line3 += "---"
        line4 += "---"
        line5 += "---"
        line6 += "---"
    if(note == "custom"):
        cline1 = input("Tab for e:")
        cline2 = input("Tab for B:")
        cline3 = input("Tab for G:")
        cline4 = input("Tab for D:")
        cline5 = input("Tab for A:")
        cline6 = input("Tab for E:")
        line1 += cline1
        line2 += cline2
        line3 += cline3
        line4 += cline4
        line5 += cline5
        line6 += cline6
    if(note == "exit"):
        print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6)
        fn = "tab.txt"
        target = open(fn, "w")
        target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6)
        return
    #notes()

#firstnote()




firstnote("A3")

letter = ""

#########Forty lines of code I used from an already existing program and edited it to fit my project
 ## https://mzucker.github.io/2016/08/07/ukulele-tuner.html  

NOTE_MIN = 40       ## not C4  anymore ###########Try to fix
NOTE_MAX = 120      # nope A4    #####################try to fix
FSAMP = 44100       # Sampling frequency in Hz
FRAME_SIZE = 4096   # samples per frame
FRAMES_PER_FFT = 16 # FFT takes average across how many frames?



SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT


NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

######################################################################
# functions based upon this webpage:
# https://newt.phys.unsw.edu.au/jw/notes.html

def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
def number_to_freq(n): return 440 * 2.0**((n-100)/12.0)
def note_name(n): return NOTE_NAMES[n % 12] + str(n/12 - 1)


def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))

buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
num_frames = 0

stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

stream.start_stream()

window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))

print("sampling at", FSAMP, "Hz with max resolution of", FREQ_STEP, "Hz")
print("\n")

t_end = time.time() + 30        # set the time in seconds

while time.time() < t_end:     ##make program end


    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)

    fft = np.fft.rfft(buf * window)

    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

    n = freq_to_number(freq)
    n0 = int(round(n))

    num_frames += 1

    if num_frames >= FRAMES_PER_FFT:
        print("freq: {:7.2f} Hz     note: {:>3s} {:+.2f}".format(freq, note_name(n0), n-n0))
        notes(note_name(n0))
        letter += note_name(n0)
        letter += " "
notes("exit")