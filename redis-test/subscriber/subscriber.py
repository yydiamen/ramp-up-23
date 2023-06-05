import redis
from redis.client import PubSub
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

mobile = r.pubsub()


mobile.subscribe("message")

for message in mobile.listen():
    print(message)