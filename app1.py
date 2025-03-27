from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

items = []  # Список товаров

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    items.append(data)
    return jsonify({"message": "Item added!"}), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if 0 <= index < len(items):
        items[index] = request.json
        return jsonify({"message": "Item updated!"})
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(items):
        items.pop(index)
        return jsonify({"message": "Item deleted!"})
    return jsonify({"error": "Item not found"}), 404

@app.route('/send-data', methods=['POST'])
def send_data():
    data = {"message": "Hello from Service 1"}
    response = requests.post("http://service2:5001/receive-data", json=data)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
