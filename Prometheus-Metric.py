from flask import Flask, jsonify
from prometheus_client import start_http_server, Summary, Counter

app = Flask(__name__)

# Prometheus 메트릭 정의
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/health', methods=['GET'])
@REQUEST_TIME.time()  # 요청 처리 시간을 측정
def health_check():
    REQUEST_COUNT.inc()  # 요청 횟수 증가
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # Prometheus 메트릭 수집 엔드포인트 시작
    start_http_server(8000)  # 메트릭은 http://localhost:8000/metrics에서 제공
    app.run(port=5000)
