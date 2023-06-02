from redis import Redis
from redis.client import PubSub
r: Redis =  Redis("localhost", 5000, db=0)
pubsub: PubSub = r.pubsub()
pubsub.subscribe("messages")

for messages in pubsub.listen():
    data = messages['data']
    if isinstance(data, bytes):
        print(data.decode())
    else:
        print(data)
