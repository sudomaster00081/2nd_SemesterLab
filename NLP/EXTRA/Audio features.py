import librosa

import parselmouth

# pip install librosa
# pip install python_speech_features
# pip install matplotlib




def extract_voice_features(audio_path):
    # Load audio file
    audio, sr = librosa.load(audio_path)
    librosa.display.waveshow(audio)
    librosa.display.specshow(audio)
    # Pre-processing
    # ...

    # Feature extraction
    features = {}

    # Tone analysis
    sound = parselmouth.Sound(audio, sampling_frequency=sr)
    features["mean_intensity"] = sound.to_intensity().get_average()

    # Pitch analysis
    pitch = sound.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    features["mean_pitch"] = sum(pitch_values) / len(pitch_values)

    return features

# Example usage
audio_file = "test1.wav"
extracted_features = extract_voice_features(audio_file)
print("Mean Intensity:", extracted_features["mean_intensity"])
print("Mean Pitch:", extracted_features["mean_pitch"])

