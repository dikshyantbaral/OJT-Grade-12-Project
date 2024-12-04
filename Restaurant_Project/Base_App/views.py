from django.shortcuts import render
from django.http import HttpResponse


from Base_App.models import BookTable, AboutUS, Feedback, ItemList, Items

def Homeview(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list, 'review': review})

def Aboutview(request):
    data = AboutUS.objects.all()
    return render(request, 'about.html', {'data': data})

def Menuview(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def BookTableview(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')
        print('---->', name, email, booking_data)
        

        if name != '' and email != '' and total_person != 0 and booking_data != '':
            data = BookTable( Name = name,
                             Phone_number =  phone_number, 
                             Email = email,  
                             Total_Person = total_person, 
                              Booking_date = booking_data )
            data.save()
            print(data)


    return render(request, 'book_table.html')

def Feedbackview(request):
    return render(request, 'feedback.html')
