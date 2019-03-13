# coding:utf-8
from celery import Celery

celery_app = Celery('input_score')
celery_app.config_from_object('input_score_config')


if __name__ == '__main__':
    celery_app.send_task("input_score.add", queue='add', args=[2, 3])
    # celery_app.send_task("input_score.subtraction", queue='subtraction', args=[2, 3])
    # celery_app.send_task("input_score.multiplication", queue='multiplication', args=[2, 3])
