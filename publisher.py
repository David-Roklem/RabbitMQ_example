import sys
from loguru import logger
from config import get_connection


def main():
    logger.remove()
    logger.add(sys.stderr, format='{time} {level} {message}', level='INFO')
    with get_connection() as connection:
        logger.info(f"Created connection: {connection}")
        with connection.channel() as channel:
            logger.info(f"Created channel: {channel}")

            while True:
                pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Bye!")
