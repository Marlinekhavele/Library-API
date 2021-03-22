from django.apps import AppConfig
from django.contrib.auth.models import User
from accounts.models import Customer
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from orders.signals import create_customer_order, save_customer_order




class OrdersConfig(AppConfig):
    name = 'orders'
    verbose_name = _('Order')
    def ready(self):
        post_save.connect(create_customer_order, sender=User)
        post_save.connect(save_customer_order, sender=User)