from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .mysignal import mysignal


def pre_save_admin(sender,**kwargs):
    print(sender)
    print(kwargs)

pre_save.connect(pre_save_admin)

@receiver(post_save)
def hehe(sendr,**kwargs):
    print(sendr)
    print(kwargs)

@receiver(mysignal)
def callback(sender,**kwargs):
    print(sender)
    print(kwargs)