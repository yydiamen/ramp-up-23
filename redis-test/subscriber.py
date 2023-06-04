import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

mobile = r.pubsub()


mobile.subscribe("Message: ")

for message in mobile.listen():
    print(message)