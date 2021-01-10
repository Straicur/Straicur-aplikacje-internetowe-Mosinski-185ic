from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)  

key ="Kluczyk3"
value = 43

redis_connection.set(key, value)

print(redis_connection.get(key))

print(redis_connection.incr(key,5))

print(redis_connection.decr(key,20))