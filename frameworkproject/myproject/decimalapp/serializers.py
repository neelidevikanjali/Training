from rest_framework import serializers
from .models import Decimalvalue
def fun(n,d):
    result = (f'%.{d}f' % n)
    print(result)
    return result
class decimalvalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decimalvalue
        fields = 'numbers','decimal_field'

    def create(self, validated_data):
        number = validated_data['numbers']
        digits = validated_data['decimal_field']
        decimal_value = fun(n=number, d=digits)
        print(decimal_value)
        user = Decimalvalue.objects.create(numbers=validated_data['numbers'], decimal_field=validated_data['decimal_field'],
                                           converted_value=decimal_value)
        user.save()
        return user


# user = request.POST.get('username')
# user = "madhu"
# userdata = table.objects.get(name =user)
#
#
# password = request.POST.get('password')
# password = "kishdch"
# passcode = userdata.Password
# passcode = '1212121'
# if password==passcode:
#     print('kjzbdckjsckjsdb')
# else:
#     print('wrong  password')

