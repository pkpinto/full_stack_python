# Full Stack Python

Python project providing a skeleton for a full stack project. This project is powered by a
presentation layer based on Flask, backend workers provided by Celery, Redis is used to broker
messages to the workers and caching, and Postgres is the database where data is stored.

## Redis and Celery

http://download.redis.io/releases/redis-3.2.4.tar.gz

```
redis-server
```

```
celery -A model worker -l info
```
