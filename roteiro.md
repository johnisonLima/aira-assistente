<!-- Roteiro apresentação do projeto -->

<!-- Explicar tema e seu funcionamento -->
# O agente autonomo desenvolvida é especializada em executar algumas tarefas para auxiliar os pilotos na cabine do aviao durante o voo. Ela se apresenta na persona chamada Amélia uma homenagem a Amelia Mary Earhart, pioneira na aviação, conhecida por ter sido a primeira mulher a voar sozinha sobre o Oceano Atlântico em 1932. Ela desapareceu no Oceano Pacífico em 1937, enquanto tentava dar a volta ao mundo. 

# Para a assistente entrar em funcionamento deve-se executar o arquivo `assistente.py`.

1. O método `iniciar()` é chamado, inicializando o modelo e configurando as palavras de parada. Por exemplo, a palavra "de" é considerada válida, pois comandos como "ativar luzes de pouso" dependem dela.
2. Em seguida, o fluxo principal entra em um loop contínuo utilizando a função `capturar_fala_com_silencio`, que monitora o áudio ambiente em busca de comandos de voz. Essa função permanece em execução até detectar uma fala relevante, garantindo que a assistente esteja sempre pronta para receber comandos.
3. Quando um possível comando é identificado, a função `escutar_comando_ativacao` é chamada. Ela também opera em loop, ouvindo atentamente até que a frase de ativação correta seja pronunciada, filtrando ruídos e comandos irrelevantes.
4. Após a ativação, o comando é processado e executado pela assistente, que retorna a resposta apropriada ao piloto.

Esse fluxo garante que a assistente permaneça atenta e responsiva durante todo o voo, executando comandos apenas quando acionada corretamente.
<!-- Como executar o assistente -->

<!-- Explicar uso dos comandos e testes -->

# Exemplos de comandos e testes

A assistente Amélia foi projetada para compreender comandos naturais e específicos do contexto da aviação. Alguns exemplos de comandos que podem ser utilizados durante o voo:

- "Ativar luzes de pouso"
- "Desligar piloto automático"
- "Qual é a altitude atual?"
- "Reportar condições meteorológicas"
- "Iniciar checklist de pouso"

Para testar a assistente, siga os passos:

1. Execute o arquivo `assistente.py`.
2. Aguarde a confirmação de que a assistente está pronta.
3. Fale um dos comandos de exemplo ou outro comando relevante para o contexto da cabine.
4. Observe a resposta da assistente e verifique se a ação foi executada corretamente.

Caso a assistente não reconheça o comando, verifique a clareza da pronúncia e a ausência de ruídos no ambiente. O sistema foi treinado para filtrar comandos irrelevantes, mas pode ser ajustado conforme necessário para melhorar a precisão.

# Considerações finais

A assistente Amélia representa um avanço no auxílio à operação de aeronaves, proporcionando maior segurança e praticidade aos pilotos. O projeto pode ser expandido com novos comandos, integração com sistemas de bordo e melhorias no reconhecimento de fala, tornando-se cada vez mais eficiente e adaptável às necessidades da aviação moderna.