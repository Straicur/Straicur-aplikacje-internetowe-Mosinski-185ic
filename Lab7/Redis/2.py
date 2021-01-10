from redis import Redis

redis_connection = Redis(db=1)  

key ="Kluczyk"
value ="Mosiński"

redis_connection.set(key, value)
print(redis_connection.get(key))