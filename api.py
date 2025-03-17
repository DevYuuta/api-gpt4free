from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para a raiz da API
@app.route('/')
def index():
    return "API GPT-4 Free está funcionando! Use o endpoint /generate para gerar respostas."

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Retorna uma resposta vazia com status 204 (No Content)

# Rota para gerar respostas
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Simulação de uma resposta
        response_text = f"Você perguntou: {prompt}. Esta é uma resposta simulada."
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)