from redis import Redis
redis_connection = Redis(db=1,decode_responses=True)
hash_key ='test_hash'
redis_connection.hset(hash_key,'key','value')
redis_connection.hset(hash_key,'key2','value2')