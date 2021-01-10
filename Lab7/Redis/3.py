from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)

list_key ="example-list"

redis_connection.rpush(list_key,1,2,3,4,5,6,7,8,9)

print(redis_connection.lrange(list_key,2,5))