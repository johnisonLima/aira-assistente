import unittest
from transcritor import *
from assistente import *

CAMINHO_AUDIO = "E://MEGAsync//projectServ//www//projetos//ia//dev//aira-assistente//audios//"

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

class TesteTranscricao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.processador, cls.modelo, cls.gravador, cls.palavras_de_parada, cls.configuracao = iniciar()

    def testar_modelo_carregado(self):
        self.assertTrue(self.iniciado)

    def testar_transcricao_acionar_torre(self):
        fala = carregar_fala(ACIONAR_TORRE)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("acionar torre de controle", self.transcricao)

    def testar_transcricao_acionar_transbonder(self):
        fala = carregar_fala(ACIONAR_TRANSPONDER)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("acionar transponder", self.transcricao)

    def testar_transcricao_ativar_luzes_emergencia(self):
        fala = carregar_fala(ATIVAR_LUZES_EMERGENCIA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ativar luzes de emergência", self.transcricao)

    def testar_transcricao_ativar_luzes_pouso(self):
        fala = carregar_fala(ATIVAR_LUZES_POUSO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ativar luzes de pouso", self.transcricao)

    def testar_transcricao_ativar_piloto_automatico(self):
        fala = carregar_fala(ATIVAR_PILOTO_AUTOMATICO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ativar piloto automático", self.transcricao)

    def testar_transcricao_ativar_transponder(self):
        fala = carregar_fala(ATIVAR_TRANSPONDER)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ativar transponder", self.transcricao)

    def testar_transcricao_checar_nivel_combustivel(self):
        fala = carregar_fala(CHECAR_NIVEL_COMBUSTIVEL)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("checar nível de combustível", self.transcricao)

    def testar_transcricao_desativar_assistente(self):
        fala = carregar_fala(DESATIVAR_ASSISTENTE)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desativar assistente", self.transcricao)

    def testar_transcricao_desativar_luzes_emergencia(self):
        fala = carregar_fala(DESATIVAR_LUZES_EMERGENCIA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desativar luzes de emergência", self.transcricao)

    def testar_transcricao_desativar_luzes_pouso(self):
        fala = carregar_fala(DESATIVAR_LUZES_POUSO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desativar luzes de pouso", self.transcricao)

    def testar_transcricao_desativar_piloto_automatico(self):
        fala = carregar_fala(DESATIVAR_PILOTO_AUTOMATICO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desativar piloto automático", self.transcricao)

    def testar_transcricao_desligar_assistente(self):
        fala = carregar_fala(DESLIGAR_ASSISTENTE)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desligar assistente", self.transcricao)

    def testar_transcricao_desligar_luzes_pouso(self):
        fala = carregar_fala(DESLIGAR_LUZES_POUSO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desligar luzes de pouso", self.transcricao)

    def testar_transcricao_desligar_luzes_emergencia(self):
        fala = carregar_fala(DESLIGAR_LUZES_EMERGENCIA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desligar luzes de emergência", self.transcricao)

    def testar_transcricao_desligar_piloto_automatico(self):
        fala = carregar_fala(DESLIGAR_PILOTO_AUTOMATICO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("desligar piloto automático", self.transcricao)
    
    def testar_transcricao_ligar_luzes_emergencia(self):
        fala = carregar_fala(LIGAR_LUZES_EMERGENCIA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ligar luzes de emergência", self.transcricao)

    def testar_transcricao_ligar_luzes_pouso(self):
        fala = carregar_fala(LIGAR_LUZES_POUSO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ligar luzes de pouso", self.transcricao)

    def testar_transcricao_ligar_piloto_automatico(self):
        fala = carregar_fala(LIGAR_PILOTO_AUTOMATICO)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("ligar piloto automático", self.transcricao)
    
    def testar_transcricao_modo_emergencia(self):
        fala = carregar_fala(MODO_EMERGENCIA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("modo emergência", self.transcricao)

    def testar_transcricao_modo_emergencia(self):
        fala = carregar_fala(MODO_SEGURANCA)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("modo segurança", self.transcricao)

    def testar_transcricao_verificar_combustivel(self):
        fala = carregar_fala(VERIFICAR_COMBUSTIVEL)
        self.assertIsNotNone(fala)

        self.transcricao = transcrever_fala(fala, self.modelo, self.processador)
        self.assertIsNotNone(self.transcricao)
        self.assertEqual("verificar nível de combustível", self.transcricao)

class TesteValidacaoComando(TesteTranscricao):

    def testar_validacao_acionar_torre(self):
        super().testar_transcricao_acionar_torre()
        
        comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
        valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
        self.assertTrue(valido)

#     def testar_validacao_acionar_transponder(self):
#         super().testar_transcricao_acionar_transponder()
#         comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
#         valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
#         self.assertTrue(valido)

#     def testar_validacao_ativar_luzes_emergencia(self):
#         super().testar_transcricao_ativar_luzes_emergencia()
#         comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
#         valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
#         self.assertTrue(valido)

#     def testar_validacao_desligar_luzes_pouso(self):
#         super().testar_transcricao_desligar_luzes_pouso()
#         comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
#         valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
#         self.assertTrue(valido)

#     def testar_validacao_modo_emergencia(self):
#         super().testar_transcricao_modo_emergencia()
#         comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
#         valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
#         self.assertTrue(valido)

#     def testar_validacao_verificar_combustivel(self):
#         super().testar_transcricao_verificar_combustivel()
#         comando = remover_palavras_de_parada(self.transcricao, self.palavras_de_parada)
#         valido, _, _ = validar_comando(comando, self.configuracao["acoes"])
        # self.assertTrue(valido)

if __name__ == "__main__":
    unittest.main()
