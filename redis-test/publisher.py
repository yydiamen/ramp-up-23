import redis
import fastapi 
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True 
)
app = fastapi.FastAPI()

@app.post("/publish")
def post_message(message: str):
    "Post a message to the oylum"
    num = r.publish("message", message=message)
    return num