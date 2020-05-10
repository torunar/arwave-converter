from mido import MidiFile, tempo2bpm

def getNoteFromMidiKey(key):
    notes = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
    note = notes[key  % 12]
    octave = key // 12
    return '%s%d' % (note, octave)

def getDurationFromTicks(time):
    durationInBeats = message.time / source.ticks_per_beat
    return int(4 / durationInBeats)

if __name__ == '__main__':
    source = MidiFile('input.mid')
    bpm = None
    notes = []
    durations = []
    for message in source.tracks[0]:
        if message.type == 'set_tempo' and bpm is None:
            bpm = int(tempo2bpm(message.tempo))
            continue

        if message.type != 'note_off' and message.type != 'note_on':
            continue

        try:
            note = None
            if message.type == 'note_on' and message.time != 0:
                note = 'N_REST'
            elif message.type == 'note_off':
                note = 'N_' + getNoteFromMidiKey(message.note)
            
            if note is not None:
                notes.append(note)
                durations.append('%d' % getDurationFromTicks(message.time))
        except Exception as e:
            pass

    print('#define BPM %d' % bpm)
    print('#define LENGTH %d' % len(notes))
    print('#define NOTES {%s}' % ','.join(notes))
    print('#define DURATIONS {%s}' % ','.join(durations))
