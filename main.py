import time
from create_csv_files import create_csv_files
from redis_client import RedisClient
from utils import create_files_metadata
from constants import NUMBER_OF_INITIAL_FILES, NUMBER_OF_NEW_FILES


def save_files_into_redis():
    redis = RedisClient()
    files_metadata = create_files_metadata()
    if len(files_metadata) > 0:
        redis.set_hash_data('files', files_metadata)


def update_files_metadata():
    redis = RedisClient()
    files_metadata = create_files_metadata()
    if len(files_metadata) > 0:
        redis.update_hash_value('files', files_metadata)


def start():
    create_csv_files(NUMBER_OF_INITIAL_FILES)  # create initial csv files
    save_files_into_redis()

    time.sleep(10)

    create_csv_files(NUMBER_OF_NEW_FILES)  # create new csv files
    save_files_into_redis()

    time.sleep(60)
    update_files_metadata()


if __name__ == '__main__':
    start()
