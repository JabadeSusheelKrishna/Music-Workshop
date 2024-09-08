from midi2audio import FluidSynth

# Initialize the FluidSynth object with the path to the SoundFont file
fs = FluidSynth('b.sf2')

# Convert MIDI to WAV (output will be in the same directory as the script)
fs.midi_to_audio('greensleeves.mid', 'output2.wav')

from pydub import AudioSegment

# Convert WAV to MP3
audio = AudioSegment.from_wav("output2.wav")
audio.export("output2.mp3", format="mp3")
