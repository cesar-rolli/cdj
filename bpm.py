import librosa

audio_data, sampling_rate = librosa.load('BPM/infinity.mp3', sr=22050)

tempo, _ = librosa.beat.beat_track(y=audio_data, sr=sampling_rate)

print(tempo)