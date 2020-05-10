# ArWave Converter 🔊

Convert MIDI files into [ArWave](https://bitbucket.org/torunar/arwave) melody files.

# Requirements

1. Python3 with the `mido` module installed.

# Installation

1. `pip -r requirements.txt`

# How to convert a melody

1. Put your melody in the `input.mid` file inside the project folder.
2. Run the program: `python3 __main__.py`.
3. Save the program output into the `src/melody.h` melody file of your [ArWave](https://bitbucket.org/torunar/arwave) project.

# Tips on creating a good melody

1. Use single track MIDI files only.
2. Make your tune as simple as possible: don't use chords, legato or any polyphony at all.
3. Don't use _kewl_ effects: forget about vibrato, palm mutes, slides and all that jibber-jabber.
4. Don't use too low-pitched notes: anything lower than A3 is almost indistinguishable on a PC speaker.

You can use examples from the `examples` directory to test a program.