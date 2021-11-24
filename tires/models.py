from django.db import models


class Tire(models.Model):
    pk_id           = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    f_section_width = models.PositiveSmallIntegerField()
    f_aspect_ratio  = models.PositiveSmallIntegerField()
    f_rim_diameter  = models.PositiveSmallIntegerField()
    r_section_width = models.PositiveSmallIntegerField()
    r_aspect_ratio  = models.PositiveSmallIntegerField()
    r_rim_diameter  = models.PositiveSmallIntegerField()
    
    class Meta:
        db_table = 'tires'