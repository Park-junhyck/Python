from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus 메트릭 정의
player_connections = Counter('player_connections_total', 'Total number of player connections')

@app.route('/connect')
def connect_player():
    player_connections.inc()  # 플레이어 접속 수 증가
    return "Player connected!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
