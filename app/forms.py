from django import forms
def validate_for_a(Sname):
    if Sname[0].lower()=='a':
        raise forms.ValidationError('first letter should not be a')


def validate_for_len(Sname):
    if len(Sname)<=5:
        raise forms.ValidationError('length should be less')





class StudentForms(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    Sage=forms.IntegerField()
    Email=forms.EmailField(validators=[validate_for_a])