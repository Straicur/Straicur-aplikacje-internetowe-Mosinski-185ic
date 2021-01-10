from redis import Redis

redis_connection = Redis(db=1,decode_responses=True)

list_key ="example-list2"

whileTrue:print(redis_connection.brpop(list_key))