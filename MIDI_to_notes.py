# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:04:22 2020

@author: abhij
"""

from pandas import DataFrame
import py_midicsv

# make a csv file from the midi file.
track_csv = py_midicsv.midi_to_csv(r"C:\Users\abhij\Desktop\Projects\Automation and Robotics club\Automatic Flute\Midi Files\test-1.mid")
#put your filepath of the midi there.


#find the start and end of notes of the first track. Currently, the program can only scrape from the first track.

start_note_pos = 0
while(not('Note_on_c' in track_csv[start_note_pos])):
    start_note_pos += 1

end_note_pos = start_note_pos
while(not('End_track' in track_csv[end_note_pos])):
    end_note_pos += 1

end_note_pos -= 1

print("notes start at position", start_note_pos)
print("notes end at position", end_note_pos)


#the following array stores notes as int and 
num_notes = []

#process track_csv, convert note and sound values to int, and put in a two dimensional array.
i = 0 
for i in range(start_note_pos, end_note_pos):
    track_csv[i] = track_csv[i].rstrip("\r\n")
    a =(track_csv[i].split(","))
    a = a[-2:]
    a[0] = int(a[0])
    a[1] = int(a[1])
    
    num_notes.append(a)
   
notes = []

#dictionary to convert note numbers to letters
notes_conversion = {1 : 'C', 2: 'C#',
                    3 : 'D', 4: 'D#',
                    5 : 'E', 0:  'B',
                    6 : 'F', 7: 'F#',
                    8 : 'G', 9: 'G#',
                    10: 'A',11: 'A#',}


for i in range(0, len(num_notes)):
    note_data = ['',0]
    note = num_notes[i][0]
    amplitude = num_notes[i][1]
    note += 1
    #increase note by one for easy human readability
    octave = 0
    if (note <= 12):
        octave = -1
    elif (note <= 24 and note > 12):
        octave = 0
    elif (note <= 36 and note > 24):
        octave = 1
    elif (note <= 48 and note > 36):
        octave = 2
    elif (note <= 60 and note > 48):
        octave = 3
    elif (note <= 72 and note > 60):
        octave = 4
    elif (note <= 84 and note > 72):
        octave = 5
    elif (note <= 96 and note > 84):
        octave = 6
    elif (note <= 108 and note > 96):
        octave = 7
    elif (note <= 120 and note > 108):
        octave = 8
    elif (note <= 132 and note > 120):
        octave = 9
    #set the octave
    
    
    note = note%12
    #find the note in the octave
    
    note_data[0] = notes_conversion.get(note)
    #get note letter from dictionary
    
    note_data[1] = int(amplitude/2 + (amplitude*(octave/9))/2)
    #amplitude is proportional to actual amplitude as well as amplitude multiplied
    
    notes.append(note_data)

#find max amplitude and scale each amplitude to that factor.
max_amp = max(volume[1] for volume in notes)
for note in notes:
    note[1] /= max_amp


#put notes and volumes in excel
key = []
for note in notes:
    key.append(note[0])

volume = []
for note in notes:
    volume.append(note[1])
    
notes_list = {'Note':   key,
              'Volume': volume}

df = DataFrame(notes_list, columns = ['Note','Volume'])
export_excel = df.to_excel(r'C:\Users\abhij\Desktop\Projects\Automation and Robotics club\Automatic Flute\Excel files\Notes.xlsx', index = None, header = True)


