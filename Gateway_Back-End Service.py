from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 간단한 사용자 데이터 반환
    return jsonify({"user_id": user_id, "name": "John Doe", "email": "john@example.com"})

if __name__ == "__main__":
    app.run(port=5001)
