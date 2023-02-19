import redis

REDIS_SERVER = 'localhost'
REDIS_PORT = 6379
r = redis.Redis(host=REDIS_SERVER, port=REDIS_PORT, db=0)



