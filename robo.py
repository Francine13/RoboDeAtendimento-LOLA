from chatterbot import ChatBot
from difflib import SequenceMatcher

ACEITACAO = 0.70

def comparar_mensagens(mensagem, mensagem_canditada):
    confianca = 0.0
    
    if mensagem.text and mensagem_canditada.text:
        texto_mensagem = mensagem.text
        texto_mensagem_candiata = mensagem_canditada.text
        
        confianca = SequenceMatcher(
            None, texto_mensagem,
            texto_mensagem_candiata
        )
        confianca = round(confianca.ratio(), 2)
        if confianca < ACEITACAO:
            confianca = 0.0
    
    return confianca

# def selecionar_resposta(mensagem, lista_respostas,storage=None):
#     resposta = lista_respostas[0]
    
#     print("resposta:", resposta)
    
#     return resposta

def executar_robo():
    robo = ChatBot("robô de atendimento para auxiliar as cacheadas",
                   read_only=True,
                   statement_comparison_function = comparar_mensagens,
                #    response_selection_method = selecionar_resposta,
                   
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch",
                       }
                   ])
    
    while True:
        entrada = input("Digite alguma coisa...\n")
        resposta = robo.get_response(entrada)
        if resposta.confidence > 0.0:
            print(resposta.text)
        else:
            print("Ainda não sei como responder essa pergunta")
            print("Pergunte outra coisa...")

if __name__ == "__main__":
    executar_robo()