from django.db import models
from variables.models import Variable
from places.models import Place

class Measurement(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)