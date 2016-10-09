# coding: utf-8

from model.celery_app import celery
import model.worker

del model.model, celery_app
