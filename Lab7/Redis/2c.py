from redis import Redis

redis_connection = Redis(db=1, decode_responses=True)

key = "Kluczyk4"
value = 200

key2 = "Kluczyk5"
value2 = 1000

redis_connection.set(key, value)
redis_connection.set(key2, value2)

print(redis_connection.get(key))

print(redis_connection.incr(key, 50))

print(redis_connection.decr(key, 10))

print(redis_connection.get(key2))

print(redis_connection.incr(key2, 50))

print(redis_connection.decr(key2, 10))