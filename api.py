from flask import Flask, request, jsonify

app = Flask(__name__)

# Função simulada para gerar respostas
def generate_response(prompt):
    """
    Simula a geração de uma resposta com base no prompt.
    Substitua esta função por uma lógica real, se necessário.
    """
    # Exemplo de respostas pré-definidas
    responses = {
        "Qual é a capital da França?": "A capital da França é Paris.",
        "Quem descobriu o Brasil?": "O Brasil foi descoberto por Pedro Álvares Cabral.",
        "Como está o tempo hoje?": "Hoje o tempo está ensolarado e agradável.",
    }

    # Retorna a resposta correspondente ao prompt ou uma resposta padrão
    return responses.get(prompt, "Desculpe, não sei responder a essa pergunta.")

@app.route('/generate', methods=['POST'])
def generate():
    # Obtém o prompt da requisição
    data = request.json
    prompt = data.get('prompt')

    # Verifica se o prompt foi fornecido
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Gera a resposta
        response_text = generate_response(prompt)
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)