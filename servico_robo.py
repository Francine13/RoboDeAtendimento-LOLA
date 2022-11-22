from robo import *
from flask import Flask

VERSAO = "1.0"
robo = ChatBot("robô de atendimento para auxiliar as cacheadas",
               read_only=True,
               statement_comparison_function=comparar_mensagens,
            #    response_selection_method=selecionar_resposta,

               logic_adapters=[
                   {
                       "import_path": "chatterbot.logic.BestMatch",
                   }
               ])

servico_robo = Flask(__name__)

@servico_robo.route("/versao", methods=["GET"])
def get_verso():
    return VERSAO

@servico_robo.route("/resposta/<mensagem>", methods=["GET"])
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)
    
    return resposta.text

if __name__ == "__main__":
    servico_robo.run()