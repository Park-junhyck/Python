import logging
from elasticsearch import Elasticsearch
from logging.handlers import TimedRotatingFileHandler

# Elasticsearch 클라이언트 설정
es = Elasticsearch("http://localhost:9200")

# 로그 설정
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# 파일 핸들러 (로컬 파일에 로그 저장)
file_handler = TimedRotatingFileHandler("app.log", when="midnight", interval=1)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def log_to_elasticsearch(record):
    # 로그를 Elasticsearch에 저장
    es.index(index="app-logs", body={
        "timestamp": record.asctime,
        "level": record.levelname,
        "message": record.message,
    })

# Elasticsearch 핸들러 추가
class ElasticsearchHandler(logging.Handler):
    def emit(self, record):
        log_to_elasticsearch(record)

logger.addHandler(ElasticsearchHandler())

# 로그 메시지 생성
logger.info("Application started successfully!")
logger.error("An error occurred in the application.")
