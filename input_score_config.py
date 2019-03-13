# coding:utf-8
from kombu import Queue
from config import BACKEND_REDIS_URL, BROKER_REDIS_URL

BROKER_URL = BROKER_REDIS_URL
CELERY_RESULT_BACKEND = BACKEND_REDIS_URL
CELERY_QUEUES = (
    Queue('add', routing_key='input_score_add'),
    Queue('subtraction', routing_key='input_score_subtraction'),
    Queue('multiplication', routing_key='input_score_multiplication'),
)

CELERY_ROUTES = {  # routes
    'rules_srv.tasks.add': {
        # 'queue': 'add',
        # 'routing_key': 'input_score',
    },
    'rules_srv.tasks.subtraction': {
        'queue': 'subtraction',
        'routing_key': 'input_score_subtraction',
    },
    'rules_srv.tasks.multiplication': {
        'queue': 'multiplication',
        'routing_key': 'input_score_multiplication',
    }
}
# CELERY_HIJACK_ROOT_LOGGER=False
