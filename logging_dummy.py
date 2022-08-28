import logging
import time


def standard_logging():
    logging.debug('This is DEBUG log')
    logging.info('This is INFO log')
    logging.warning('This is WARNING log')
    logging.error('This is ERROR log')
    logging.critical('This is CRITICAL log')


def logging_print_all_level():
    logging.basicConfig(level=logging.DEBUG)

    logging.debug('This is DEBUG log')
    logging.info('This is INFO log')
    logging.warning('This is WARNING log')
    logging.error('This is ERROR log')
    logging.critical('This is CRITICAL log')


def logging_to_file():
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('파일에 저장될 DEBUG 수준 로깅')
    logging.info('파일에 저장될 INFO 수준 로깅')
    logging.warning('파일에 저장될 WARNING 수준 로깅')
    logging.error('파일에 저장될 ERROR 수준 로깅')
    logging.critical('파일에 저장될 CRITICAL 수준 로깅')


def logging_formatting():
    logging.basicConfig(format=f'[%(asctime)s] [%(levelname)s] %(filename)s - %(funcName)s : %(message)s', level=logging.DEBUG)
    logging.debug('test')
    time.sleep(1)
    logging.debug('test')


if __name__ == '__main__':
    pass
