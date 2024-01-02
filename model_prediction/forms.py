from django import forms


class PredictionForm(forms.Form):
    class Meta:
        fields = ['age','gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active' ]



