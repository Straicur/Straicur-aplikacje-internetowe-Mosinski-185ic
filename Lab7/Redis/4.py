from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)

redis_connection.sadd("key", "val1")
redis_connection.sadd("key", "val2")
redis_connection.sadd("key", "val3")
redis_connection.sadd("key", "val4")

print(redis_connection.smembers("key"))