from msilib.schema import MsiAssembly
import traceback
from django.shortcuts import redirect, render
from book.models import Book, Employee
from django.http import HttpResponse
import logging
# Create your custom logger:-->
logger = logging.getLogger("first")

## function bsaed view / class based view


#   http://127.0.0.1:8000/home/ -----> Base URL (uniform resource locator)


def hompage(request):                                     # request is HTTPRequest  (hypertext transfer protocol)
    logger.info("In homepage")
    books = Book.objects.all()
    logger.info(books)
    # print(request.method)                                 # to check what method is used.
    # print(request.POST)                                    # type of this is querydict.
    if request.method == "POST":
        logger.info(request.POST)
        if not request.POST.get("bid"):
            book_name = request.POST["bname"]
            book_price = request.POST["bprice"]
            book_qty = request.POST["bqty"]                 # In if condition, we r creating the data.
            # print(book_name, book_price, book_qty)             # fetching the data from frontend. class is a str.

            Book.objects.create(name=book_name, price=book_price, qty=book_qty)  # Data insert into mysql.

            return redirect("homepage")                        # redirect to homepage directly.
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)

            book_obj.name = request.POST["bname"]
            book_obj.price = request.POST["bprice"]
            book_obj.qty = request.POST["bqty"]            # In else, we r updating the data.
            book_obj.save()
            return redirect("show_all_books")               # redirect to show_all_books directly.

    # print(request.build_absolute_uri())                   # to check what url is used.
    # a = [1,2,3,4,5]
    # return HttpResponse("Hi...Hello..!")                  # this normal string of python, so we import from django.http import HttpResponse.
    # return HttpResponse("<h3>Hi..Hello</h3><h4>Good Morning</h4>")
    elif request.method == "GET":
        return render(request, template_name="home.html")     # here we are return file ka data.


def show_all_books(request):
    logger.info("In show all books")
    all_books = Book.objects.all()                          # fetching the data from backend(db).
    logger.info(all_books)
    data = {"books": all_books}                             # context=data--> if u want to show the data on page.
    logger.info(request.POST)
    return render(request, template_name="show_books.html", context=data)


def edit_data(request, id):
    logger.info("In edit page")
    book = Book.objects.get(id=id)
    logger.info(book)
    return render(request, template_name= "home.html", context={"single_book": book})


def Delete_data(request, id):
    # print(request.method)
    if request.method == "POST":
        try:
            logger.info("In delete data page")
            book = Book.objects.get(id=id)
            logger.debug(book)
        except Book.DoesNotExist as err_msg:
            # traceback.print_exc()                                    # detail error msg.
            print(err_msg)    
            # return HttpResponse(f"Book Does not exit for ID:- {id}")  
            logger.error(f"{err_msg}-- in exception")
        else:     
            book.delete()
            return redirect("show_all_books")
    else:
        # return HttpResponse("Error..!")
        logger.error((f"request method: {request.method} not allowed.. only post request is allowed"))


### Deleting all book records:----->

def Delete_all_books(request):
    logger.info("In delete-all-books")
    all_books = Book.objects.all()
    all_books.delete()
    logger.info(all_books)
    return render(request, template_name="show_books.html", context={"all_book": all_books})


def is_inactive(request):
    logger.info("In is_inactive page")
    all_inactive_books = Book.inactive_obj.all()
    logger.info(all_inactive_books)
    return render(request, template_name="show_books.html", context={"all_aval_books": all_inactive_books})



def update_deleted_books(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist as msg:
        # return HttpResponse(f"book does not exist for id:-- {id}")     
        logger.error(f"{msg}")
    else:
        book.is_active = "n"
        book.save()       
    return redirect("show_all_books")   

def restore_book(request, id):
    try:
        book = Book.objects.get(id=id) 
    except Book.DoesNotExist as msg:
        # return HttpResponse(f"book does not exist for id:-- {id}")
        logger.error(f"{msg}")
    else:
        book.is_active = "y"
        book.save()
    return redirect("soft_delete")    

#####################################################



from book.forms import StudentForm, BookForm

# def form_home(request):
#     if request.method == "POST":
#         print(request.POST)
#         form = BookForm(request.POST)           # when data comes from frontend, we r giving to bookform.
#         if form.is_valid():
#             print(form.cleaned_data["name"])      # fetching single data if u see the result in console.
#             # form.save()
#         return HttpResponse("Data Saved...!")  

#     elif request.method == "GET":
#         print("In get request")
#         context = {"form": BookForm()}                # this is the student object and render the html format.
#         return render(request, "form_home.html", context)

    # else:
    #     return HttpResponse("Invalid HTTP method") 


# from book.forms import AddressForm, BookForm

# def form_home(request):
#     if request == "POST":
#         pass
#     else:
#         print("In get request")
#         context ={"form": AddressForm()}                # this is the student object and render the html format.
#         return render(request, "form_home.html", context)




##### Data Save by using Form:--------->

from django.contrib import messages

def form_home(request):                       # Function based view
    if request.method == "POST":
        form = BookForm(request.POST)       # Data comes from frontend, so here we r giving to bookform.
        if form.is_valid():
            # print(form.cleaned_data["name"])     # here we r fetching the one by one data.
            form.save()
            messages.success(request, "your Data Saved Successfully..")   # masseges comes from html.
            messages.info(request, "Redirecting to home page")
        else:
            messages.error(request, "Invalid Data..!")    
        return redirect("form_home")
 
    elif request.method == "GET":
        print("In get request")
        context ={"form": BookForm()}                         
        return render(request, "form_home.html", context)

    else:
        return HttpResponse("Invalid HTTP method")

######################################################################################################


## Class Based View------>  It will handle post and get request autometically.
# 'django.middleware.csrf.CsrfViewMiddleware-->go to settings and commentthis before done below operations.

## idempotent method == GET,PUT, DELETE method
## Non-idempotent method == POST method



from django.views import View

class HomePage(View):
    def get(self, request):
        print("In get request")
        return HttpResponse("in GET")


    def post(self, request):
        # print(dir(request))
        print(request.POST)     # here we r fetching data.
        print("In post request")
        return HttpResponse("in POST")


    def delete(self, request):
        print("In delete request")
        return HttpResponse("in DELETE")

    def put(self, request):
        print("In put request")
        return HttpResponse("in PUT")

    def patch(self, request):
        print("In patch request")
        return HttpResponse("in PATCH")
###########################################################

from django.views.generic.base import TemplateView

class  CBVTemplateView(TemplateView):
    extra_context = {"form": BookForm()}   
    template_name = 'form_home.html'




from django.urls import reverse, reverse_lazy  
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView  
from django.views.generic.edit import UpdateView  
from django.views.generic.edit import DeleteView  



class EmployeeCreate(CreateView):  
    model = Employee  
    fields = '__all__'  
    success_url = reverse_lazy("EmployeeCreate")     #"http://127.0.0.1:8000/emp-gcreate/"     # here is redirecting the page.
    # return render(request, "employee_form.html", {"form": "EmployeeForm"})




class EmployeeRetrieve(ListView):  
    model = Employee  
    # return render(request, "employee_list.html", {"object_list": "data"})


class EmployeeDetail(DetailView):  
    model = Employee
    # return render(request, "employee_form.html", {"object": "data"})



class EmployeeUpdate(UpdateView):  
    model = Employee  
    fields = '__all__'  
    success_url = "http://127.0.0.1:8000/emp-gcreate/"  



  
class EmployeeDelete(DeleteView):  
    model = Employee  
    fields = '__all__'  
    success_url = "http://127.0.0.1:8000/emp-gcreate/"  






















