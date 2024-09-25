from midi2audio import FluidSynth

# Initialize the FluidSynth object with the path to the SoundFont file
fs = FluidSynth('../others/neat.sf2')

# Convert MIDI to WAV (output will be in the same directory as the script)
fs.midi_to_audio('../others/basic_pitch.mid', '../audio/output.wav')

from pydub import AudioSegment

# Convert WAV to MP3
audio = AudioSegment.from_wav("../audio/output.wav")
audio.export("../audio/output.mp3", format="mp3")
