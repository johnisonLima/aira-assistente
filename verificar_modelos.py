import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

MODELO = ["openai/whisper-large-v3-turbo"]

def iniciar_modelo(nome_modelo, dispositivo = "cpu"):
    iniciado, processador, modelo = False, None, None

    dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print(f"iniciando modelo: {nome_modelo}")

    try:
        processador = AutoProcessor.from_pretrained(nome_modelo)
        modelo = AutoModelForSpeechSeq2Seq.from_pretrained(
            nome_modelo, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        modelo.to(dispositivo)

        pipe = pipeline(
            "automatic-speech-recognition",
            model=modelo,
            tokenizer=processador.tokenizer,
            feature_extractor=processador.feature_extractor,
            torch_dtype=torch_dtype,
            device=dispositivo,
        )

        iniciado = True
    except Exception as e:
        print(f"erro iniciando modelo: {str(e)}")

    return iniciado, processador, modelo

if __name__ == "__main__":
    for modelo in MODELO:
        iniciado,_,__ = iniciar_modelo(modelo)
        if iniciado:
            print(f"Modelo {modelo} iniciado com sucesso")

