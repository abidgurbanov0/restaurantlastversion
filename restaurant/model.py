from django.db import models
from django.contrib.auth.models import User


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField( verbose_name='Name', max_length=255, blank=False)
    description = models.TextField(blank=False)
    url = models.URLField()
    rate_count = models.IntegerField(default=0, blank=False)
    avarage_rate = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    text = models.TextField(verbose_name = "Review's text", blank = False)
    rate = models.IntegerRangeField(blank = False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

    def __str__(self):
        return self.restaurant_id