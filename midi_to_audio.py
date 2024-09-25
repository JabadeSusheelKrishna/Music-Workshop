import mido
import fluidsynth
from pydub import AudioSegment
import os

# Path to your MIDI file and soundfont file
midi_file = "input.mid"  # Your MIDI file path
soundfont_file = "soundfont.sf2"  # Your soundfont file path

# Create a FluidSynth object with the sound font
fs = fluidsynth.Synth()
fs.start(driver="alsa")
sfid = fs.sfload(soundfont_file)
fs.program_select(0, sfid, 0, 0)

# Read the MIDI file
midi = mido.MidiFile(midi_file)

# Output wav file to save the rendered audio
output_wav = "output.wav"

# Open the output wav file to write the rendered audio
with open(output_wav, 'wb') as wav_file:
    for message in midi.play():
        if message.type == 'note_on' or message.type == 'note_off':
            fs.noteon(0, message.note, message.velocity) if message.type == 'note_on' else fs.noteoff(0, message.note)
        elif message.type == 'control_change':
            fs.cc(0, message.control, message.value)
        elif message.type == 'program_change':
            fs.program_change(0, message.program)
    fs.write(wav_file, fs.get_samples(44100))  # Write the generated samples to wav file

# Stop the synthesizer
fs.delete()

# Convert wav to mp3 using pydub
sound = AudioSegment.from_wav(output_wav)
output_mp3 = "output.mp3"
sound.export(output_mp3, format="mp3")

# Remove the wav file as it's no longer needed
os.remove(output_wav)

print(f"Generated {output_mp3} successfully.")
