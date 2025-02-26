import sounddevice as sd
import soundfile as sf
import numpy as np
import keyboard

# Carrega os arquivos de áudio
data1, samplerate1 = sf.read("CDJ/titanium.wav")
data2, samplerate2 = sf.read("CDJ/infinity.wav")

# Garante que as taxas de amostragem sejam iguais
if samplerate1 != samplerate2:
  raise ValueError("As músicas precisam ter a mesma taxa de amostragem!")

# Converte áudio mono para estéreo
def garantir_estereo(data):
  if len(data.shape) == 1:  # Se for mono, duplica o canal
    return np.column_stack((data, data))
  return data

data1 = garantir_estereo(data1)
data2 = garantir_estereo(data2)

# Ajusta para o mesmo tamanho
min_len = min(len(data1), len(data2))
data1, data2 = data1[:min_len], data2[:min_len]

# Inicializa volumes
volume1 = 0.5
volume2 = 0.5

# Callback para mixar o áudio em tempo real
def audio_callback(outdata, frames, time, status):
  global volume1, volume2
  if status:
    print(status)

  # Aplica volume e mixa as duas músicas
  mixed_audio = (data1[:frames] * volume1 + data2[:frames] * volume2) / 2
  outdata[:] = mixed_audio

# Função para capturar teclas e alterar o volume
def controlar_volume():
  global volume1, volume2
  while True:
    if keyboard.is_pressed("a"):
      volume1 = min(1.0, volume1 + 0.05)
      print(f"🔊 Volume da música 1: {int(volume1 * 100)}%")
    
    if keyboard.is_pressed("q"):
      volume1 = max(0.0, volume1 - 0.05)
      print(f"🔉 Volume da música 1: {int(volume1 * 100)}%")

    if keyboard.is_pressed("s"):
      volume2 = min(1.0, volume2 + 0.05)
      print(f"🔊 Volume da música 2: {int(volume2 * 100)}%")
    
    if keyboard.is_pressed("w"):
      volume2 = max(0.0, volume2 - 0.05)
      print(f"🔉 Volume da música 2: {int(volume2 * 100)}%")

    if keyboard.is_pressed("esc"):
      print("⏹ Parando a reprodução...")
      break

# Criar stream de áudio garantindo número correto de canais
stream = sd.OutputStream(samplerate=samplerate1, channels=data1.shape[1], callback=audio_callback)

# Inicia o áudio e o controle de volume
stream.start()
controlar_volume()
stream.stop()
