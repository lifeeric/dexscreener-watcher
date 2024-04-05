from rq import Queue
from redis import Redis

q = Queue(connection=Redis())
