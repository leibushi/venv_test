# -*- coding: utf-8 -*-
# author: xu3352<xu3352@gmail.com>
"""
Python 日志工具包
@see https://blog.csdn.net/chosen0ne/article/details/7319306
"""
import logging
import logging.config
import logging.handlers
import os

import yaml


def setup_logging(log_path='log_config.yml', default_level=logging.INFO):
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_config.yml')
    path = log_path if os.path.exists(log_path) else default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()
logger = logging.getLogger('main')

if __name__ == '__main__':
    logger.debug('223 debug message')
    logger.info('1123 info message')
    logger.warning('112 warn message')
    logger.error('00 error message')
    logger.critical('12 critical message')
    try:
        print(3 / 0)
    except Exception as e:
        logger.error(e)
        logger.error('Error', exc_info=True)
