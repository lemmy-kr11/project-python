from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta raíz para verificar si la API funciona
@app.route('/', methods=['GET'])
def home():
    return "Bienvenido a la API RESTful de Kr-11"

# Ruta para obtener un mensaje de saludo
@app.route('/api/hola', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "Hello"})

# Ruta para enviar datos a la API
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"recibido": data})

if __name__ == '__main__':
    app.run(debug=True)
