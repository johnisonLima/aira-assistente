import unittest
from transcritor import *
from assistente import *

CAMINHO_AUDIO = "audios/"

AMELIA = f"{CAMINHO_AUDIO}amelia.wav"
ACIONAR_TORRE = f"{CAMINHO_AUDIO}acionar torre de controle.wav"
ACIONAR_TRANSPONDER = f"{CAMINHO_AUDIO}acionar transponder.wav"
ATIVAR_LUZES_EMERGENCIA = f"{CAMINHO_AUDIO}ativar luzes de emergencia.wav"
ATIVAR_LUZES_POUSO = f"{CAMINHO_AUDIO}ativar luzes de pouso.wav"
ATIVAR_PILOTO_AUTOMATICO = f"{CAMINHO_AUDIO}ativar piloto automatico.wav"
ATIVAR_TRANSPONDER = f"{CAMINHO_AUDIO}ativar transponder.wav"
CHECAR_NIVEL_COMBUSTIVEL = f"{CAMINHO_AUDIO}checar nivel de combustivel.wav"
DESATIVAR_ASSISTENTE = f"{CAMINHO_AUDIO}desativar assistente.wav"
DESATIVAR_LUZES_EMERGENCIA = f"{CAMINHO_AUDIO}desativar luzes de emergencia.wav"
DESATIVAR_LUZES_POUSO = f"{CAMINHO_AUDIO}desativar luzes de pouso.wav"
DESATIVAR_PILOTO_AUTOMATICO = f"{CAMINHO_AUDIO}desativar piloto automatico.wav"
DESLIGAR_ASSISTENTE = f"{CAMINHO_AUDIO}desligar assistente.wav"
DESLIGAR_LUZES_POUSO = f"{CAMINHO_AUDIO}desligar luzes de pouso.wav"
DESLIGAR_LUZES_EMERGENCIA = f"{CAMINHO_AUDIO}desligar luzes de emergencia.wav"
DESLIGAR_PILOTO_AUTOMATICO = f"{CAMINHO_AUDIO}desligar piloto automatico.wav"
LIGAR_LUZES_EMERGENCIA = f"{CAMINHO_AUDIO}ligar luzes de emergencia.wav"
LIGAR_LUZES_POUSO = f"{CAMINHO_AUDIO}ligar luzes de pouso.wav"
LIGAR_PILOTO_AUTOMATICO = f"{CAMINHO_AUDIO}ligar piloto automatico.wav"
MODO_EMERGENCIA = f"{CAMINHO_AUDIO}modo emergencia.wav"
MODO_SEGURANCA = f"{CAMINHO_AUDIO}modo seguranca.wav"
VERIFICAR_COMBUSTIVEL = f"{CAMINHO_AUDIO}verificar nivel de combustivel.wav"
TESTE_ERRO = f"{CAMINHO_AUDIO}teste erro.wav"

def setup_ambiente_teste(): 
    global contexto
    contexto = iniciar()

setup_ambiente_teste()

class BaseTeste(unittest.TestCase):
    def setUp(self):
        self.iniciado, self.processador, self.modelo, self.gravador, self.palavras_de_parada, self.configuracao = contexto

class TesteModeloInicializado(BaseTeste):
    
    def testar_modelo_carregado(self):
        self.assertTrue(self.iniciado)

class TesteTranscricao(BaseTeste):

    def validar_transcricao(self, caminho_audio, texto_esperado):
        fala = carregar_fala(caminho_audio)
        self.assertIsNotNone(fala)

        transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(transcricao)
        self.assertEqual(texto_esperado, transcricao)
    
    def testar_transcricao_acionar_torre(self):
        self.validar_transcricao(AMELIA, "amélia")

    def testar_transcricao_acionar_torre(self):
        self.validar_transcricao(ACIONAR_TORRE, "acionar torre de controle")

    def testar_transcricao_acionar_transbonder(self):
        self.validar_transcricao(ACIONAR_TRANSPONDER, "acionar transponder")

    def testar_transcricao_ativar_luzes_emergencia(self):
        self.validar_transcricao(ATIVAR_LUZES_EMERGENCIA, "ativar luzes de emergência")

    def testar_transcricao_ativar_luzes_pouso(self):
        self.validar_transcricao(ATIVAR_LUZES_POUSO, "ativar luzes de pouso")

    def testar_transcricao_ativar_piloto_automatico(self):
        self.validar_transcricao(ATIVAR_PILOTO_AUTOMATICO, "ativar piloto automático")

    def testar_transcricao_ativar_transponder(self):
        self.validar_transcricao(ATIVAR_TRANSPONDER, "ativar transponder")

    def testar_transcricao_checar_nivel_combustivel(self):
        self.validar_transcricao(CHECAR_NIVEL_COMBUSTIVEL, "checar nível de combustível")

    def testar_transcricao_desativar_assistente(self):
        self.validar_transcricao(DESATIVAR_ASSISTENTE, "desativar assistente")

    def testar_transcricao_desativar_luzes_emergencia(self):
        self.validar_transcricao(DESATIVAR_LUZES_EMERGENCIA, "desativar luzes de emergência")

    def testar_transcricao_desativar_luzes_pouso(self):
        self.validar_transcricao(DESATIVAR_LUZES_POUSO, "desativar luzes de pouso")

    def testar_transcricao_desativar_piloto_automatico(self):
        self.validar_transcricao(DESATIVAR_PILOTO_AUTOMATICO, "desativar piloto automático")

    def testar_transcricao_desligar_assistente(self):
        self.validar_transcricao(DESLIGAR_ASSISTENTE, "desligar assistente")

    def testar_transcricao_desligar_luzes_pouso(self):
        self.validar_transcricao(DESLIGAR_LUZES_POUSO, "desligar luzes de pouso")

    def testar_transcricao_desligar_luzes_emergencia(self):
        self.validar_transcricao(DESLIGAR_LUZES_EMERGENCIA, "desligar luzes de emergência")

    def testar_transcricao_desligar_piloto_automatico(self):
        self.validar_transcricao(DESLIGAR_PILOTO_AUTOMATICO, "desligar piloto automático")

    def testar_transcricao_ligar_luzes_emergencia(self):
        self.validar_transcricao(LIGAR_LUZES_EMERGENCIA, "ligar luzes de emergência")

    def testar_transcricao_ligar_luzes_pouso(self):
        self.validar_transcricao(LIGAR_LUZES_POUSO, "ligar luzes de pouso")

    def testar_transcricao_ligar_piloto_automatico(self):
        self.validar_transcricao(LIGAR_PILOTO_AUTOMATICO, "ligar piloto automático")

    def testar_transcricao_modo_emergencia(self):
        self.validar_transcricao(MODO_EMERGENCIA, "modo emergência")

    def testar_transcricao_modo_seguranca(self):
        self.validar_transcricao(MODO_SEGURANCA, "modo segurança")

    def testar_transcricao_verificar_combustivel(self):
        self.validar_transcricao(VERIFICAR_COMBUSTIVEL, "verificar nível de combustível")

class TesteValidacaoComandoAcoes(BaseTeste):

    def validar_comando_acoes_transcrito(self, caminho_audio):
        fala = carregar_fala(caminho_audio)
        transcricao = transcrever_fala(fala, self.modelo, self.processador)

        comando = remover_palavras_de_parada(transcricao, self.palavras_de_parada)
        valido, _, _ = validar_comando(comando, self.configuracao["acoes"])

        self.assertTrue(valido)

    def testar_validacao_acionar_torre(self):
        self.validar_comando_acoes_transcrito(ACIONAR_TORRE)

    def testar_transcricao_acionar_transbonder(self):
        self.validar_comando_acoes_transcrito(ACIONAR_TRANSPONDER)

    def testar_transcricao_ativar_luzes_emergencia(self):
        self.validar_comando_acoes_transcrito(ATIVAR_LUZES_EMERGENCIA)

    def testar_transcricao_ativar_luzes_pouso(self):
        self.validar_comando_acoes_transcrito(ATIVAR_LUZES_POUSO)

    def testar_transcricao_ativar_piloto_automatico(self):
        self.validar_comando_acoes_transcrito(ATIVAR_PILOTO_AUTOMATICO)
    
    def testar_transcricao_ativar_transponder(self):
        self.validar_comando_acoes_transcrito(ATIVAR_TRANSPONDER)

    def testar_transcricao_checar_nivel_combustivel(self):
        self.validar_comando_acoes_transcrito(CHECAR_NIVEL_COMBUSTIVEL)

    def testar_transcricao_desativar_assistente(self):
        self.validar_comando_acoes_transcrito(DESATIVAR_ASSISTENTE)

    def testar_transcricao_desativar_luzes_emergencia(self):
        self.validar_comando_acoes_transcrito(DESATIVAR_LUZES_EMERGENCIA)

    def testar_transcricao_desativar_luzes_pouso(self):
        self.validar_comando_acoes_transcrito(DESATIVAR_LUZES_POUSO)

    def testar_transcricao_desativar_piloto_automatico(self):
        self.validar_comando_acoes_transcrito(DESATIVAR_PILOTO_AUTOMATICO)

    def testar_transcricao_desligar_assistente(self):
        self.validar_comando_acoes_transcrito(DESLIGAR_ASSISTENTE)

    def testar_transcricao_desligar_luzes_pouso(self):
        self.validar_comando_acoes_transcrito(DESLIGAR_LUZES_POUSO)

    def testar_transcricao_desligar_luzes_emergencia(self):
        self.validar_comando_acoes_transcrito(DESLIGAR_LUZES_EMERGENCIA)

    def testar_transcricao_desligar_piloto_automatico(self):
        self.validar_comando_acoes_transcrito(DESLIGAR_PILOTO_AUTOMATICO)

    def testar_transcricao_ligar_luzes_emergencia(self):
        self.validar_comando_acoes_transcrito(LIGAR_LUZES_EMERGENCIA)

    def testar_transcricao_ligar_luzes_pouso(self):
        self.validar_comando_acoes_transcrito(LIGAR_LUZES_POUSO)

    def testar_transcricao_ligar_piloto_automatico(self):
        self.validar_comando_acoes_transcrito(LIGAR_PILOTO_AUTOMATICO)    

    def testar_transcricao_verificar_combustivel(self):
        self.validar_comando_acoes_transcrito(VERIFICAR_COMBUSTIVEL)

class TesteValidacaoComandoModos(BaseTeste):
    
    def validar_comando_modo_transcrito(self, caminho_audio):
        fala = carregar_fala(caminho_audio)
        transcricao = transcrever_fala(fala, self.modelo, self.processador)

        comando = remover_palavras_de_parada(transcricao, self.palavras_de_parada)
        valido, _, _ = validar_modo(comando, self.configuracao["modos"])

        self.assertTrue(valido)

    def testar_transcricao_modo_emergencia(self):
        self.validar_comando_modo_transcrito(MODO_EMERGENCIA)

    def testar_transcricao_modo_seguranca(self):
        self.validar_comando_modo_transcrito(MODO_SEGURANCA)

if __name__ == "__main__":
    unittest.main()