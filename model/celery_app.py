# coding: utf-8

import logging

from celery import Celery


celery = Celery('model')

# Optional configuration, see the application user guide.
celery.conf.update(
    BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    CELERY_IMPORTS=('model.worker',),
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER = 'json'
    # CELERY_REDIRECT_STDOUTS_LEVEL='DEBUG'
)


if __name__ == '__main__':
    celery.worker_main()
