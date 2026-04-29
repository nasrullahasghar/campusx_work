import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True   # automatically returns strings
    )

try:
    if r.ping():
        print("Connected to Redis!")
except redis.ConnectionError:
    print("Redis Connection Failed!")

r.set("framework","FASTAPI")

value  = r.get("framework")
print(f"Stored value for framework: {value}")
