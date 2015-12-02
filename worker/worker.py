import redis
import time

r = redis.StrictRedis(host='192.168.255.100', port=6379, db=0)
p = r.pubsub()

while True:
    message = p.get_message()
    print "Message: ", message
    time.sleep(5)
