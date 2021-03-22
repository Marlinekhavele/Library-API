import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Customer

class Order(models.Model):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(_('Cost'), decimal_places=2, max_digits=15)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)
    
   

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

