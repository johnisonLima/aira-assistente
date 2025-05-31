from inicializador_modelos import *
import torchaudio
import torch

MODELO = "lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"
TAXA_AMOSTRAGEM = 16_000

CAMINHO_AUDIO = "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//"

AUDIOS = [ 
    {
        "comando": "acionar torre de controle",
        "wav": f"{CAMINHO_AUDIO}acionar torre de controle.wav" 
    },
    {
        "comando": "acionar transponder",
        "wav": f"{CAMINHO_AUDIO}acionar transponder.wav" 
    },
    {
        "comando": "ativar luzes de emergência",
        "wav": f"{CAMINHO_AUDIO}ativar luzes de emergencia.wav" 
    },
    {
        "comando": "ativar luzes de pouso", 
        "wav": f"{CAMINHO_AUDIO}ativar luzes de pouso.wav"
    },
    {
        "comando": "ativar piloto automático",
        "wav": f"{CAMINHO_AUDIO}ativar piloto automatico.wav" 
    },
    {
        "comando": "ativar transponder",
        "wav": f"{CAMINHO_AUDIO}ativar transponder.wav" 
    },    
    {
        "comando": "checar nível de combustível",
        "wav": f"{CAMINHO_AUDIO}checar nível de combustível.wav" 
    },
    {
        "comando": "desativar assistente",
        "wav": f"{CAMINHO_AUDIO}desativar assistente.wav" 
    },    
    {
        "comando": "desativar luzes de emergência",
        "wav": f"{CAMINHO_AUDIO}desativar luzes de emergencia.wav" 
    },   
    {
        "comando": "desativar luzes de pouso", 
        "wav": f"{CAMINHO_AUDIO}desativar luzes de pouso.wav"
    }, 
    {
        "comando": "desativar piloto automático",
        "wav": f"{CAMINHO_AUDIO}desativar piloto automatico.wav" 
    },
    {
        "comando": "desligar assistente",
        "wav": f"{CAMINHO_AUDIO}desligar assistente.wav" 
    },    
    {
        "comando": "desligar luzes de emergência",
        "wav": f"{CAMINHO_AUDIO}desligar luzes de emergencia.wav" 
    },    
    {
        "comando": "desligar luzes de pouso",
        "wav": f"{CAMINHO_AUDIO}desligar luzes de pouso.wav" 
    },    
    {
        "comando": "desligar piloto automático",
        "wav": f"{CAMINHO_AUDIO}desligar piloto automatico.wav" 
    },    
    {
        "comando": "ligar luzes de emergência",
        "wav": f"{CAMINHO_AUDIO}ligar luzes de emergencia.wav" 
    },    
    {
        "comando": "ligar luzes de pouso",
        "wav": f"{CAMINHO_AUDIO}ligar luzes de pouso.wav" 
    },    
    {
        "comando": "ligar piloto automático",
        "wav": f"{CAMINHO_AUDIO}ligar piloto automatico.wav" 
    },    
    {
        "comando": "modo emergência",
        "wav": f"{CAMINHO_AUDIO}modo emergencia.wav" 
    },
    {
        "comando": "modo segurança",
        "wav": f"{CAMINHO_AUDIO}modo seguranca.wav" 
    },
    {
        "comando": "verificar nível de combustível",
        "wav": f"{CAMINHO_AUDIO}verificar nivel de combustivel.wav" 
    }             
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