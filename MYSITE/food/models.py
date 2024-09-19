from django.db import models

class Item(models.Model):
    item_name=models.CharField(max_length=100, null=True)
    item_detail=models.CharField(max_length=200, null=True)
    item_price=models.IntegerField(null=True)
    item_image=models.CharField(max_length=500, default="https://media.istockphoto.com/id/1324356458/vector/picture-icon-photo-frame-symbol-landscape-sign-photograph-gallery-logo-web-interface-and.jpg?s=612x612&w=0&k=20&c=ZmXO4mSgNDPzDRX-F8OKCfmMqqHpqMV6jiNi00Ye7rE=")


    def __str__(self):
        return self.item_name
    

