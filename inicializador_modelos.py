import torch

from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

def iniciar_modelo(nome_modelo):
    iniciado, processador, modelo = False, None, None

    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"

    print(f"iniciando modelo: {nome_modelo}")

    try:
        processador = Wav2Vec2Processor.from_pretrained(nome_modelo)
        modelo = Wav2Vec2ForCTC.from_pretrained(nome_modelo).to(dispositivo)
   
        iniciado = True
    except Exception as e:
        print(f"erro iniciando modelo: {str(e)}")

    return iniciado, processador, modelo


if __name__ == "__main__":    
    MODELOS = ["lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"]

    for modelo in MODELOS:
        iniciado,_,__ = iniciar_modelo(modelo)
        if iniciado:
            print(f"Modelo {modelo} iniciado com sucesso")