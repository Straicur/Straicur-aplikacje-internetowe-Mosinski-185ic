
"""
from redis import Redis
redis_connection = Redis(decode_responses=True, db=1)
script ="""

"""
print(redis_connection.eval(script,0))
"""

"""
from redis import Redis
redis_connection = Redis(decode_responses=True, db=1)
script ="""

"""
print(redis_connection.eval(script,2,1,2,'first','second'))
"""
"""
from redis import Redis
redis_connection = Redis(decode_responses=True, db=1)
script ="""

"""
print(redis_connection.eval(script,0))# lista od 1 do 10
"""

"""
from redis import Redis
from json import dumps
redis_connection = Redis(decode_responses=True, db=1)
script ="""

"""
print(redis_connection.eval(
    script,1, dumps({'a': 1,'b': 6})))  # wynik to 7
"""
"""
from redis import Redis
redis_connection = Redis(decode_responses=True, db=1)
redis_connection.set("key1",10)
script ="""

"""
print(redis_connection.eval(script,1,5))# None, ze względu na "return nil"
print(redis_connection.get("key2"))  # 15, bo 10 + 5 = 15
"""



from redis import Redis
redis_connection = Redis(decode_responses=True, db=1)
permission ='ADD_BOOKING' 
redis_connection.sadd("users_group:2", *list(range(0,50))) 
redis_connection.sadd('permissions', permission)


add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""


from redis import Redis
redis_connection = Redis(decode_responses=True, db=0)
permission ='ADD_BOOKING'
redis_connection.sadd("users_group:2", *list(range(0,50))) 
redis_connection.sadd('permissions', permission) 


add_permission_script ="""
local is_valid_permission = redis.call('sismember', 'permissions', KEYS[2])
if is_valid_permission == 1 then
    local users = redis.call('smembers','users_group:'..KEYS[1])
    for _, user in ipairs(users) do
        redis.call('sadd', 'user_permissions:'..user, KEYS[2])
    end
    return true
else
    return false
end
"""

print(redis_connection.eval(add_permission_script,2,2, permission))

