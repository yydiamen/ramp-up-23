import redis
from redis.client import PubSub

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    decode_responses=True
)

mobile = r.pubsub()


mobile.subscribe("Message: ")

for message in mobile.listen():
    print(message)