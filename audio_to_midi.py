import librosa
import pretty_midi
import numpy as np

# Load the mp3 file
def load_audio_file(mp3_file):
    y, sr = librosa.load(mp3_file)
    return y, sr

# Convert audio to MIDI
def audio_to_midi(mp3_file, midi_file):
    # Load audio
    y, sr = load_audio_file(mp3_file)
    
    # Detect pitches in the audio file
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    
    # Create a PrettyMIDI object
    midi = pretty_midi.PrettyMIDI()
    
    # Create an instrument (e.g., Piano)
    instrument = pretty_midi.Instrument(program=0)  # 0 is the program number for Acoustic Grand Piano
    
    # Loop through the pitches and add them to the MIDI file
    for t, pitch in enumerate(pitches):
        # Take the strongest pitch at each time step
        idx = magnitudes[:, t].argmax()
        pitch_hz = pitches[idx, t]
        
        if pitch_hz > 0:  # Filter out non-pitched time steps
            # Convert pitch to MIDI note number
            note_number = librosa.hz_to_midi(pitch_hz)
            note = pretty_midi.Note(
                velocity=100,  # Volume of the note
                pitch=int(note_number),  # MIDI note number
                start=t / sr,  # Note start time in seconds
                end=(t + 1) / sr  # Note end time in seconds
            )
            instrument.notes.append(note)
    
    # Add the instrument to the PrettyMIDI object
    midi.instruments.append(instrument)
    
    # Write out the MIDI data
    midi.write(midi_file)

# Example usage
mp3_file = 'input_audio.mp3'
midi_file = 'output_file.mid'
audio_to_midi(mp3_file, midi_file)
