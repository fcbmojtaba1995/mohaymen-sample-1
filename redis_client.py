import redis
import json
from local_config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD


class Singleton(type):
    """
    An metaclass for singleton purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisClient(metaclass=Singleton):
    def __init__(self):
        self.redis_connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

    def create_redis_pipeline(self, hash_name, files):
        """
        create redis pipeline and set data in redis hash type function.

        :param hash_name: hash name
        :param files: files(values)
        """

        with self.redis_connection.pipeline(files) as pipe:
            for file in files:
                for key, value in file.items():
                    pipe.hsetnx(str(hash_name), str(key), json.dumps(value))
            pipe.execute()
            pipe.bgsave()

    def get_all_values(self, hash_name):
        """
        get all values function.

        :param hash_name: hash name
        :return: hash values
        """

        return self.redis_connection.hvals(str(hash_name))

    def get_number_of_elements(self, hash_name):
        """
        get number of elements function.

        :param hash_name: hash name
        :return: hash length
        """

        return self.redis_connection.hlen(str(hash_name))
