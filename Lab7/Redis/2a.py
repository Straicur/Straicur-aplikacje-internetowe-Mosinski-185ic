from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)  

key ="Kluczyk2"
value ="Mosiński"

redis_connection.set(key, value)
print(redis_connection.get(key))
redis_connection.append(key," Damian")
print(redis_connection.get(key))
redis_connection.delete(key)
print(redis_connection.get(key))