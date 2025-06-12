from django import forms
from .models import DemandePerso,Reservation


class DemandePersoForm(forms.ModelForm):
     class Meta:
         model=DemandePerso
         fields=['first_name', 'last_name', 'email', 'phone', 'picture']


class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=['nom_client', 'nom_famille','num_phone', 'email', 'service_choice']