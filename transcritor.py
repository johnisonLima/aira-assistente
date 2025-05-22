from inicializador_modelos import *
import torchaudio
import torch

MODELO = "lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"
TAXA_AMOSTRAGEM = 16_000

AUDIOS = [ 
    {
        "comando": "ativar luzes de pouso", 
        "wav": "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//ativar luzes de pouso.wav"
    },
    {
        "comando": "desativar luzes de pouso", 
        "wav": "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//desativar luzes de pouso.wav"
    },{
        "comando": "ativar piloto automático",
        "wav": "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//ativar piloto automatico.wav" 
    },
    {
        "comando": "desativar piloto automático",
        "wav": "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//desativar piloto automatico.wav" 
    },
    {
        "comando": "checar nível de combustível",
        "wav": "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//checar nível de combustível.wav" 
    },
]

def carregar_fala(caminho_audio):
    audio, amostragem = torchaudio.load(caminho_audio)

    if audio.shape[0] > 0:
        audio = torch.mean(audio, dim=0, keepdim=True)

    adaptador_amostragem = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)

    audio = adaptador_amostragem(audio)

    return audio.squeeze()

def transcrever_fala(fala, modelo, processador):
    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"

    resultado = processador(fala, return_tensors="pt", sampling_rate=TAXA_AMOSTRAGEM).input_values.to(dispositivo)

    resultado = modelo(resultado).logits

    predicao = torch.argmax(resultado, dim=-1)
    transcricao = processador.batch_decode(predicao)[0]

    return transcricao.lower()

if __name__ == "__main__": 
    

    iniciado, processador, modelo =  iniciar_modelo(MODELO)

    if iniciado:
        for audio in AUDIOS:
            print(f"Testando transcrição do comando: { audio['comando'] }")

            try:
                fala = carregar_fala(audio['wav'])
            except Exception as e:
                print(f"Erro ao carregar áudio: {e}")

            transcricao = transcrever_fala(fala, modelo, processador)

            print(f"transcrição: {transcricao}")
            assert audio['comando'] == transcricao