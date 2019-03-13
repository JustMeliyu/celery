# coding:utf-8
from celery import Celery
# from celery.utils.log import logger
import logging
import logging.config

celery_app = Celery('input_score')
celery_app.config_from_object("input_score_config")
logging.config.fileConfig('logger.conf', disable_existing_loggers=False)


@celery_app.task
def add(x, y):
    logging.info("add")
    return x + y


@celery_app.task
def subtraction(x, y):
    logging.info("subtraction")
    return x - y


@celery_app.task
def multiplication(x, y):
    logging.info("multiplication")
    return x * y
