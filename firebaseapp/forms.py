from django import forms
from firebaseapp.models import KmsModel, KmsDelete, KmsUpdate


class KmsForm(forms.ModelForm):
    class Meta:
        model = KmsModel
        fields = "__all__"


class KmsDeleteForm(forms.ModelForm):
    class Meta:
        model = KmsDelete
        fields = "__all__"


class KmsUpdateForm(forms.ModelForm):
    class Meta:
        model = KmsUpdate
        fields = "__all__"

