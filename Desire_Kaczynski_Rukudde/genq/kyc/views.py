from django.shortcuts import render
from .models import FormData
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def capture_message(request):
    _firstname = request.POST['firstname']
    _lastname = request.POST['lastname']
    _dob = request.POST['dob']
    _gender = request.POST['gender']
    _country = request.POST['country']
    _state_or_district = request.POST['state_or_district']
    _town = request.POST['town']
    _zip_code = request.POST['zip_code']
    _phone_number1 = request.POST['phone_number1']
    _phone_number2 = request.POST['phone_number2']
    _email = request.POST['email']

    captured_details = FormData(
        firstname = _firstname,
        lastname = _lastname,
        dob = _dob,
        gender = _gender,
        country = _country,
        state_or_district = _state_or_district,
        town = _town,
        zip_code = _zip_code,
        phone_number1 = _phone_number1,
        phone_number2 = _phone_number2,
        email = _email
    )
    captured_details.save()
    chats = FormData.objects.all()
    messages.success(request, ("Form has been submitted successfully!"))  
        

    return render(request, 'index.html')#{'messages':messages})