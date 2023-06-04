import redis
import fastapi 
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True 
)
app = FastAPI()

@app.post("/publish")
def post_message(message: str):
    "Post a message to the oylum"
    r.publish("message", message=message)