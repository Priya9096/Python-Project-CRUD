from django.db import models

# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=122)
    item_desc=models.CharField(max_length=122)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=5000,default='https://t4.ftcdn.net/jpg/03/16/15/47/360_F_316154790_pnHGQkERUumMbzAjkgQuRvDgzjAHkFaQ.jpg')
