from django import forms
from .models import MyCollection



class MyCollectionForm(forms.ModelForm):
    class Meta:
        model = MyCollection
        fields = ['CriminalName','Age', 'Criminality', 'CriminalPic']



class DeleteRecordForm(forms.Form):
    record_id = forms.ModelChoiceField(queryset=MyCollection.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
