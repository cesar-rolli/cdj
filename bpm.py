import librosa

arquivo = "infinity.wav"
audio_data, sampling_rate = librosa.load(arquivo, sr=22050)

tempo, _ = librosa.beat.beat_track(y=audio_data, sr=sampling_rate)

print(tempo)