import torchaudio
import torch

SAMPLE_WAV = "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//ligar lampada.wav"
TAXA_AMOSTRAGEM = 16_000

print(f"Versão do troch - {torch.__version__}")
print(f"Versão do torchaudio - {torchaudio.__version__}")

metadata = torchaudio.info(SAMPLE_WAV)
print(f"Metadado - {metadata}")

audio, amostragem = torchaudio.load(SAMPLE_WAV)

print(f"Audio - {audio}")

print(f"Audio shape - {audio.shape}")

print(f"Amostragem - {amostragem}")

print(f"Tamanho do Audio - {audio.size()}")

if audio.shape[0] > 0:
    audio = torch.mean(audio, dim=0, keepdim=True)

adaptador_amostragem = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)

audio = adaptador_amostragem(audio)

print(f"Audio Modificado - {audio}")

print(f"Audio shape Modificado - {audio.shape}")

print(f"Amostragem Modificado - {amostragem}")

print(f"Tamanho do Audio Modificado - {audio.size()}")

