from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']

    def clean_latitude(self):
        lat = self.cleaned_data['latitude']
        if lat < -90 or lat > 90:
            raise forms.ValidationError("Invalid latitude.")
        return lat

    def clean_longitude(self):
        lon = self.cleaned_data['longitude']
        if lon < -180 or lon > 180:
            raise forms.ValidationError("Invalid longitude.")
        return lon
