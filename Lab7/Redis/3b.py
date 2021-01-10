from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(db=1, decode_responses=True)

redis_connection.set("key", "value1")
redis_connection.expire("key", 30)


print(datetime.now().time(), redis_connection.get("key"))
sleep(15)
print(datetime.now().time(), redis_connection.get("key"))
sleep(5)
print(datetime.now().time(), redis_connection.get("key"))