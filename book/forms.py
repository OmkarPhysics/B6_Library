from django import forms
from book.models import Employee, Book



## Django forms---->       This will create only html format.

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())


# print(StudentForm())                 # here we can get html format in console.
###############

## Django model-forms----->

from book.models import Book

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Book                  # here we are using book model.
#         fields = "__all__"            # here we are use all fields for creating html format.


class StudentForm(forms.ModelForm):
    class Meta:
        model = Book                 
        fields = "__all__"
        exclude = ("qty",)            # here exclude gives in tuple and comma..


# class StudentForm(forms.ModelForm):
#     is_published = forms.BooleanField()
#     image_field  = forms.FileField()
#     class Meta:
#         model = Book                  # here we are using book model.
#         fields = "__all__"

################

## Django crispy forms--->



STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)



class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)



class BookForm(forms.ModelForm):            # this is generate html format.
    class Meta:
        model = Book
        fields = "__all__"



class EmployeeForm(forms.ModelForm):  
  
    class Meta:
        model = Employee
        fields = '__all__'  





