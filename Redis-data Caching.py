import redis
import psycopg2

# Redis 연결
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# PostgreSQL 연결
db_conn = psycopg2.connect("dbname=test user=postgres password=secret")

def get_user(user_id):
    # 먼저 Redis에서 데이터 확인
    cached_user = redis_client.get(f"user:{user_id}")
    if cached_user:
        print("Cache hit!")
        return cached_user

    # Redis에 데이터가 없으면 DB에서 조회
    print("Cache miss!")
    with db_conn.cursor() as cur:
        cur.execute("SELECT name FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()

        if user:
            # Redis에 저장하여 캐싱
            redis_client.set(f"user:{user_id}", user[0], ex=3600)  # 1시간 TTL
            return user[0]

    return None

# 사용자 데이터 가져오기
print(get_user(1))
