# coding: utf-8

import time

from model.celery_app import celery


@celery.task
def add(x, y):
    time.sleep(5)
    return x + y


@celery.task
def multiply(x, y):
    time.sleep(5)
    return x * y
