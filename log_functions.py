#!/usr/bin/env python
# encoding: utf-
"""
Logging...
"""
import logging

def init_logger(log_filename='mail_scripts.log'):
    """ Creating Logger for the scripts """
    logger = logging.getLogger(log_filename)
    handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter('%(asctime)s - %(filename)s - \
        %(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
