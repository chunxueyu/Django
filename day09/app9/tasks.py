import time
from celery import task


@task
def test(n):
    print("睡前工资10000")
    time.sleep(n)
    print("睡后1000")
