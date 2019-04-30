import json
#import os

#os.chdir("../../../Desktop")

note_name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
note_ratio_harmonic = [
    1.0000,
    1.0666,
    1.1250,
    1.2000,
    1.2500,
    1.3333,
    1.4142,
    1.5000,
    1.6000,
    1.6667,
    1.7500,
    1.8333,
]
note_ratio_temperament = [
    1.0000,
    1.0595,
    1.1225,
    1.1892,
    1.2599,
    1.3348,
    1.4142,
    1.4983,
    1.5874,
    1.6818,
    1.7818,
    1.8897
]

A4 = 440.0
A3 = 220.0
A2 = 110.0
A1 = 55
A0 = 27.5
#C0 to C9
#starts at A4
def main():
    notes = {}
    for i in range(88):
        if i in [0,1,2]:
            new_note_name = "{name}{octave}".format(name=note_name[(i+9)%12], octave=0)
        else:
            new_note_name = "{name}{octave}".format(name=note_name[(i-3)%12], octave=((i-3)//12)+1)            
        notes[new_note_name] = find_eq_temp_freq(i+1)

    with open('equal_temperament_notes.json', 'w+') as f:
        f.write(json.dumps(notes))

def main2():
    notes = {}
    for i in range(88):
        if i in [0,1,2]:
            new_note_name = "{name}{octave}".format(name=note_name[(i+9)%12], octave=0)
        else:
            new_note_name = "{name}{octave}".format(name=note_name[(i-3)%12], octave=((i-3)//12)+1)            
        notes[new_note_name] = find_harm_ser_freq(i)


    with open('harmonic_series_notes.json', 'w+') as f:
        f.write(json.dumps(notes))

def find_eq_temp_freq(n):
    return float("{:.4f}".format(440 * 2 ** ((n-49)/12)))


def find_harm_ser_freq(n, starting_hz=A0):
    return float("{:.4f}".format(starting_hz*note_ratio_temperament[n%12]*(2**(n//12)) ) )

if __name__ == "__main__":
    main2()
    main()