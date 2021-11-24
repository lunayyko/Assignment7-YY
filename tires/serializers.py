from rest_framework import serializers

from .models        import Tire


class TireSerializers(serializers.ModelSerializer):
    section_width  = serializers.IntegerField()
    aspect_ratio   = serializers.IntegerField(source='aspect_ratio')
    rim_diameter   = serializers.IntegerField(source='rim_diameter')

    class Meta:
        model  = Tire
        fields = ('section_width', 'aspect_ratio', 'rim_diameter')