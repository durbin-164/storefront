from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print("sending 10k message...")
    print(message)
    sleep(10)
    print("Succesfully send mail")
