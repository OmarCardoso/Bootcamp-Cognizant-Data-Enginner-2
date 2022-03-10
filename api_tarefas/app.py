from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefasafazer = [
{
     'id':0,
     'responsavel':'Rafael',
     'tarefa':'Desenvolver método GET',
     'Status':'concluido'
},
{    'id':1,
    'responsavel':'Galeane',
     'tarefa':'Desenvolver método POST',
     'Status':'pendente'
    }
]

# consulta por id
#@app.route('/tarefas/<int:id>', methods=['GET', 'POST'])
#def tarefas(id):
#    if request.method == 'POST':
#        dados = json.loads(request.data)
#        tarefasafazer.append(dados)
#    elif request.method == 'GET':
#        tarefas = tarefasafazer[id]
#        return jsonify({tarefas})

# consulta geral e inclusão
@app.route('/tarefas/<int:id>', methods=['PUT', 'DELETE'])
def tarefas(id):
    if request.method == 'PUT':
        dados = json.loads(request.data)
        tarefasafazer[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        tarefas = tarefasafazer[id]
        print(tarefas)
        return jsonify({tarefas})



if __name__ == '__main__':
    app.run(debug=True)