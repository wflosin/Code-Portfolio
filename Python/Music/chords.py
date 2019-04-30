import pygame, pygame.sndarray
import numpy
import scipy.signal
import json

with open('harmonic_series_notes.json', 'r') as f:
    HS_hz = json.load(f)
with open('equal_temperament_notes.json', 'r') as f:
    ET_hz = json.load(f)


duration = 1.0          # in seconds
sample_rate = 44100
bits = 16
peak = 4096

# chord_ratio = {
#     'M': (4,5,6),
#     'm': (10,12,15),
#     'dim': (160,192,231),
#     'aug': (40,50,63),
#     '7': (20,25,30,36),
#     'm7': (10,12,15,18),
#     'M7': (8,10,12,15),
#     'sus2': (1975600,2217611,2637200),
#     'sus4': (25841200,34492129,34492129)
# }
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

note = {
    'P1':1.0000,
    'm2':1.0909,
    'M2':1.1250,
    'm3':1.2000,
    'M3':1.2500,
    'P4':1.3333,
    '-5':1.4000,
    'P5':1.5000,
    'm6':1.6000,
    'M6':1.6667,
    'm7':1.7500,
    'M7':1.8333,
    'P8':2.0000,
}

chord_ratio = {
    'M': [note['P1'],note['M3'],note['P5']],
    'm': [note['P1'],note['m3'],note['P5']],
    'dim': [note['P1'],note['m3'],note['-5']],
    'aug': [note['P1'],note['M3'],note['m6']],
    '7': [note['P1'],note['M3'],note['P5'],note['m7']],
    'm7': [note['P1'],note['m3'],note['P5'],note['m7']],
    'M7': [note['P1'],note['M3'],note['P5'],note['M7']],
    'sus2': [note['P1'],note['M2'],note['P5']],
    'sus4': [note['P1'],note['P4'],note['P5']]
}

major_key_chords = ['M','m','m','M','M','m','dim','M']
minor_key_chords = ['m','dim','M','m','m','M','M','m']

major_scale = {
    1:note['P1'],
    2:note['M2'],
    3:note['M3'],
    4:note['P4'],
    5:note['P5'],
    6:note['M6'],
    7:note['M7'],
    8:note['P8']
}
natural_minor_scale = {
    1:note['P1'],
    2:note['M2'],
    3:note['m3'],
    4:note['P4'],
    5:note['P5'],
    6:note['m6'],
    7:note['m7'],
    8:note['P8']
}
harmonic_minor_scale = {
    1:note['P1'],
    2:note['M2'],
    3:note['m3'],
    4:note['P4'],
    5:note['P5'],
    6:note['m6'],
    7:note['M7'],
    8:note['P8']    
}
melodic_minor_scale = {
    '1':note['P1'],
    '2':note['M2'],
    '3':note['m3'],
    '4':note['P4'],
    '5':note['P5'],
    '6d':note['m6'],
    '6u':note['M6'],
    '7d':note['m7'],
    '7u':note['M7'],
    '8':note['P8']    
}

def play_for(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

def sine_wave(hz, peak=peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16) 
    if hz == 0:
        return buf

    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    wave = numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)
    
    for i in range(n_samples):
        buf[i][0] =  wave[i]      # left
        buf[i][1] =  wave[i]*0.5  # right

    # with open('test.txt', 'w+') as f:
    #     numpy.savetxt(f,buf)

    return buf

def piano_wave(hz, peak=peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
    if hz == 0:
        return buf
    
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    onecycle = peak  * ( -1/4*numpy.sin(3*numpy.pi*xvalues) + 3/4*numpy.sin(numpy.pi*xvalues) + numpy.sqrt(3)/2*numpy.cos(numpy.pi*xvalues) )
    wave = numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)
    
    for i in range(n_samples):
        buf[i][0] =  wave[i]      # left
        buf[i][1] =  wave[i]*0.5  # right

    return buf

def test_wave(hz, peak=peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
    if hz == 0:
        return buf

    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    a1 = 1
    b1 = 3
    a2 = 0.1
    b2 = 0.4
    a3 = 2.15
    b3 = 1.5
    onecycle = peak  * ( a1*numpy.sin(b1*numpy.pi*xvalues) + a2*numpy.sin(b2*numpy.pi*xvalues) + a3*numpy.cos(b3*numpy.pi*xvalues) )
    wave = numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)
     
    for i in range(n_samples):
        buf[i][0] =  wave[i]      # left
        buf[i][1] =  wave[i]*0.5  # right

    return buf

def square_wave(hz, peak=peak, n_samples=sample_rate, duty_cycle=.5):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
    if hz == 0:
        return buf

    t = numpy.linspace(0, 1, 500 * 440/hz, endpoint=False)
    wave = scipy.signal.square(2 * numpy.pi * 5 * t, duty=duty_cycle)
    wave = numpy.resize(wave, (n_samples,))
    wave2 = (peak / 2 * wave.astype(numpy.int16))
 
    for i in range(n_samples):
        buf[i][0] =  wave2[i]      # left
        buf[i][1] =  wave2[i]*0.5  # right

    return buf

def make_chord(hz, ratios, waveform=sine_wave):
    """Make a chord based on a list of frequency ratios
       using a given waveform (defaults to a sine wave).
    """
    sampling = 4096
    chord = waveform(hz, sampling)
    for r in ratios[1:]:
        chord = sum([chord, waveform(hz * r / ratios[0], sampling)])
    return chord

def build_key(hz, scale, majMin, waveform=sine_wave):
    sampling = 4096

    notes = [hz*note for note in scale.values()]
    built_notes = [waveform(note_freq, sampling) for note_freq in notes]

    built_chords = []
    if majMin == "major":
        for note_freq in notes:
            for chord in major_key_chords:
                built_chords.append(make_chord(note_freq, chord_ratio[chord], waveform))
                break
    elif majMin == "minor":
        for note_freq in notes:
            for chord in minor_key_chords:
                built_chords.append(make_chord(note_freq, chord_ratio[chord], waveform))
                break

    return built_notes, built_chords

# # Play A (440Hz) for 1 second as a sine wave:
#play_for(sine_wave(hz["A4"], 4096), 1000)

# # Play A-440 for 1 second as a square wave:
# play_for(square_wave(440, 4096), 1000)

# play_for(sum([sine_wave(440, 4096), sine_wave(880, 4096)]), 1000)

time_signature = (4,4)
bbm = 160
speed = 60/bbm

w = int(1    * time_signature[1] * 1000)
h = int(1/2  * time_signature[1] * 1000)
q = int(1/4  * time_signature[1] * 1000)
e = int(1/8  * time_signature[1] * 1000)
s = int(1/16 * time_signature[1] * 1000)

raw_song = [
    [
        ("G4", e), ("G4", q), ("G4", q), ("D4", e), ("E4", q), ("C4", h), ("C5", q)
    ]#,
    # [
    #     ("C4", w*7/4)
    # ]
]

def build_song(raw_song, speed, waveform=square_wave, hz=ET_hz):
    #gets a dictionary of the longest of each note used in the song
    #{"G4":1000,"C3":250,...}
    num_channels = len(raw_song)

    note_data_used = {}
    for channel in raw_song:
        for note_data in channel:
            if note_data[0] in note_data_used.keys():
                if note_data[1] > note_data_used[note_data[0]]:
                    #replace a key value pair if a duration is longer
                    note_data_used[note_data[0]] = note_data[1]
            else:
                note_data_used[note_data[0]] = note_data[1]

    sounds_used = {key:waveform(hz[key], 
                   n_samples=int(sample_rate*value/1000*speed)) 
                        for key,value in note_data_used.items()}

    len_of_song = sum([note[1] for note in raw_song[0]])

    channel_waveforms = [[sounds_used[note[0]] for note in channel] for channel in raw_song]
    #[[channel 1 waves],[channel 2 waves]]

    built_channels = [channel_waveforms[0][0],channel_waveforms[1][0]]
    for i in range(num_channels):
        for j in range(len(channel_waveforms[i])-1):
            a = built_channels[i]
            b = channel_waveforms[i][j+1]
            built_channels[i] = numpy.append(a, b, axis=0)

    # for i in range(num_channels-1):
    #     if built_channels[i].shape()
    built_song = sum(built_channels)

    return built_song, len_of_song

def play_song(built_song, len_of_song):
    play_for(built_song, int(len_of_song))


try:
    pygame.mixer.init(frequency = sample_rate, size = -bits, channels = 2)
    
    #built_song, len_of_song = build_song(raw_song, speed)
    #play_song(built_song, len_of_song)

    #wave = sine_wave(440)
    #play_for(wave, 1000)
    #A_sus4 = make_chord(440, chord_ratio["sus4"], square_wave)
    # A_M = make_chord(440, chord_ratio["M"], square_wave)
    ##play_for(sine_wave(hz["A0"]), 5000)
    # play_for(A_M, 1000)
    play_for(sum([square_wave(HS_hz["C4"]), square_wave(HS_hz["E4"]), square_wave(HS_hz["G4"])]), 3000)
    #play_for(sum([square_wave(ET_hz["C4"]), square_wave(ET_hz["E4"]), square_wave(ET_hz["G4"])]), 3000)

    #notes, chords = build_key(261.6, major_scale, "major", piano_wave)
    #notes, chords = build_key(261.6, harmonic_minor_scale, "minor", square_wave)
    #play chords chromatically
    # for i in range(len(chords)):
    #     print(i+1)
    #     play_for(chords[i], 1000)
    # for item in notes:
    #     play_for(item, 1000)

    # #a melody
    # melody = [1,1,5,1,3,4,2,3,5,6,5,5,8,8,7,8]
    # for i in range(len(melody)):
    #     play_for(notes[melody[i]-1], 500)

    #a chord progression
    # prog = [1,4,5,1]
    # for i in range(len(prog)):
    #     play_for(chords[prog[i]-1], 1000)

    #play_for(make_chord(440, chord_ratio['sus4'], piano_wave), 1000)
    # play_for(make_chord(440*note['P4'], chord_ratio['M'], square_wave), 1000)
    # play_for(make_chord(440, chord_ratio['dim'], square_wave), 1000)
    # play_for(make_chord(440, chord_ratio['M'], square_wave), 1000)

finally:
    pygame.mixer.quit()
