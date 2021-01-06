from django.db import models

class Inventory(models.Model):
    costumer = models.CharField(db_column='COSTUMER', primary_key=True, max_length=10)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ossenm = models.CharField(db_column='OSSENM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    site_name = models.CharField(db_column='SITE_NAME', max_length=50)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_number = models.CharField(db_column='PRODUCT_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_revision = models.CharField(db_column='PRODUCT_REVISION', max_length=5, blank=True, null=True)  # Field name made lowercase.
    production_date = models.DateField(db_column='PRODUCTION_DATE', blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='SERIAL_NUMBER', max_length=50)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='LAST_UPDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'
        unique_together = (('costumer', 'site_name', 'serial_number'),)