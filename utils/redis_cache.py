from threading import local
from redis import StrictRedis

import settings

DEFAULT_CACHE_ALIAS = 'default'
EXAM_CACHE_ALIAS = "exam"
STUDENT_CACHE_ALIAS = "student"


class RedisCache(object):
    def __init__(self):
        self._caches = local()

    def __getitem__(self, item):
        try:
            return self._caches.caches[item]
        except AttributeError:
            self._caches.caches = {}
        except KeyError:
            pass

        cache = StrictRedis(host=settings.REDIS_CONFIG[item]["host"],
                            port=settings.REDIS_CONFIG[item]["port"],
                            password=settings.REDIS_CONFIG[item]["password"],
                            db=settings.REDIS_CONFIG[item]["db"])

        self._caches.caches[item] = cache
        return cache

    def all(self):
        return getattr(self._caches, 'caches', {}).values()


caches = RedisCache()


class DefaultCache(object):

    def __getattr__(self, name):
        return getattr(caches[DEFAULT_CACHE_ALIAS], name)

    def __setattr__(self, name, value):
        return setattr(caches[DEFAULT_CACHE_ALIAS], name, value)

    def __delattr__(self, name):
        return delattr(caches[DEFAULT_CACHE_ALIAS], name)

    def __contains__(self, key):
        return key in caches[DEFAULT_CACHE_ALIAS]

    def __eq__(self, other):
        return caches[DEFAULT_CACHE_ALIAS] == other

    def __ne__(self, other):
        return caches[DEFAULT_CACHE_ALIAS] != other


class ExamCache(object):
    def __getattr__(self, name):
        return getattr(caches[EXAM_CACHE_ALIAS], name)

    def __setattr__(self, name, value):
        return setattr(caches[EXAM_CACHE_ALIAS], name, value)

    def __delattr__(self, name):
        return delattr(caches[EXAM_CACHE_ALIAS], name)

    def __contains__(self, key):
        return key in caches[EXAM_CACHE_ALIAS]

    def __eq__(self, other):
        return caches[EXAM_CACHE_ALIAS] == other

    def __ne__(self, other):
        return caches[EXAM_CACHE_ALIAS] != other


class StudentCache(object):
    def __getattr__(self, name):
        return getattr(caches[STUDENT_CACHE_ALIAS], name)

    def __setattr__(self, name, value):
        return setattr(caches[STUDENT_CACHE_ALIAS], name, value)

    def __delattr__(self, name):
        return delattr(caches[STUDENT_CACHE_ALIAS], name)

    def __contains__(self, key):
        return key in caches[STUDENT_CACHE_ALIAS]

    def __eq__(self, other):
        return caches[STUDENT_CACHE_ALIAS] == other

    def __ne__(self, other):
        return caches[STUDENT_CACHE_ALIAS] != other


redis_cache = DefaultCache()
exam_cache = ExamCache()
student_cache = StudentCache()