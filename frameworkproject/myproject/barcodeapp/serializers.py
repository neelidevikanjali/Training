import pyqrcode
from rest_framework import serializers

from .code import logic
from .models import folderapp, barimage
import base64


class folderappSerializer(serializers.ModelSerializer):
    class Meta:
        model = folderapp
        fields = ('book_name', 'book_address', 'book_field')

    def create(self, validated_data):
        book_name = validated_data['book_name']
        book_address = validated_data['book_address']
        book_field = validated_data['book_field']
        code_generator = book_address + " " + book_field
        #c = pyqrcode.create(b)
        data = logic(code_generator, book_name)
        with open(data, "rb") as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            page = folderapp.objects.create(book_name=book_name, book_address=book_address, book_field=book_field, book_code=encoded)
            page.save()
            return page
class barimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = barimage
        fields = '__all__'

