from rest_framework import serializers

from .models        import Tire

class TireSerializers(serializers.ModelSerializer):
    pk_id           = serializers.IntegerField(source='pk_id')
    trimid          = serializers.IntegerField(source='trimid')
    f_section_width = serializers.IntegerField(source='f_section_width')
    f_aspect_ratio  = serializers.IntegerField(source='f_aspect_ratio')
    f_rim_diameter  = serializers.IntegerField(source='f_rim_diameter')
    r_section_width = serializers.IntegerField(source='r_section_width')
    r_aspect_ratio  = serializers.IntegerField(source='r_aspect_ratio')
    r_rim_diameter  = serializers.IntegerField(source='r_rim_diameter')

    class Meta:
        model  = Tire
        fields = '__all__'