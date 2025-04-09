from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 백엔드 서비스 URL (예: 사용자 서비스와 주문 서비스)
USER_SERVICE_URL = "http://localhost:5001"
ORDER_SERVICE_URL = "http://localhost:5002"

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 사용자 서비스로 요청 전달
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    return jsonify(response.json()), response.status_code

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # 주문 서비스로 요청 전달
    response = requests.get(f"{ORDER_SERVICE_URL}/orders/{order_id}")
    return jsonify(response.json()), response.status_code

@app.route('/proxy', methods=['POST'])
def proxy_request():
    # 클라이언트의 요청 데이터를 가져와 처리
    data = request.json
    target_url = data.get("url")
    response = requests.post(target_url, json=data.get("payload"))
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000)
