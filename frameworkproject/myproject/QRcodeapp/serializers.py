import pyqrcode
from rest_framework import serializers
from .models import folder
import base64

class folderSerializer(serializers.ModelSerializer):
    class Meta:
        model = folder
        fields = ('item_name', 'item_address', 'item_code')

    def create(self, validated_data):
        item_name = validated_data['item_name']
        item_address = validated_data['item_address']
        a = item_name+item_address
        b = pyqrcode.create(a)
        combined = b.png(f'{item_name}.png', scale=6)
        with open('qrcode.png', "rb") as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            page = folder.objects.create(item_name=item_name, item_address=item_address, item_code=encoded)
            page.save()
            return page


