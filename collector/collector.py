import redis

r = redis.StrictRedis(host='192.168.255.100', port=6379, db=0)
p = r.pubsub()
p.subscribe('queue')
for i in range(1,10000):
    r.publish('queue','data:'+i.__str__())
    print i

