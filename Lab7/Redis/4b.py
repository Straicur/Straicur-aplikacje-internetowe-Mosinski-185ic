from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)

redis_connection.zadd("sorted_set_key", {"key1": 2})
redis_connection.zadd("sorted_set_key", {"key2": 2})
redis_connection.zadd("sorted_set_key", {"key3": 5})
redis_connection.zadd("sorted_set_key", {"key4": 4})

print(redis_connection.zrange("sorted_set_key", 0, -1))