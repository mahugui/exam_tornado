REDIS_CONFIG = {
    'default': {
        'host': 'redis.exam.info',
        'port': 6379,
        'password': '',
        'db': 0 if TEST else 4
    },
    'exam': {
        'host': 'redis.exam.info',
        'port': 6379,
        'password': '',
        'db': 5 if TEST else 4
    },
    'student': {
        'host': 'redis.exam.info',
        'port': 6379,
        'password': '',
        'db': 6 if TEST else 4
    }
}