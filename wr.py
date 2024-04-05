from rq import Queue
from redis import Redis
import logging

import time

q = Queue(connection=Redis())
