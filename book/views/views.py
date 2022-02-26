# import traceback
# from django.shortcuts import redirect, render
# from book.models import Book
# from django.http import HttpResponse

# # Create your views here.

# ## function bsaed view / class based view


# #   http://127.0.0.1:8000/home/ -----> Base URL (uniform resource locator)


# def hompage(request):                                     # request is HTTPRequest  (hypertext transfer protocol)
    
#     # print(request.method)                                 # to check what method is used.
#     # print(request.POST)                                    # type of this is querydict.
#     if request.method == "POST":
#         if not request.POST.get("bid"):
#             book_name = request.POST["bname"]
#             book_price = request.POST["bprice"]
#             book_qty = request.POST["bqty"]                 # In if condition, we r creating the data.
#             # print(book_name, book_price, book_qty)             # fetching the data from frontend. class is a str.

#             Book.objects.create(name=book_name, price=book_price, qty=book_qty)  # Data insert into mysql.
            

#             return redirect("homepage")                        # redirect to homepage directly.
#         else:
#             bid = request.POST.get("bid")
#             try:
#                 book_obj = Book.objects.get(id=bid)
#             except Book.DoesNotExist as err_msg:
#                 print(err_msg)

#             book_obj.name = request.POST["bname"]
#             book_obj.price = request.POST["bprice"]
#             book_obj.qty = request.POST["bqty"]            # In else, we r updating the data.
#             book_obj.save()
#             return redirect("show_all_books")               # redirect to show_all_books directly.

#     # print(request.build_absolute_uri())                   # to check what url is used.
#     # a = [1,2,3,4,5]
#     # return HttpResponse("Hi...Hello..!")                  # this normal string of python, so we import from django.http import HttpResponse.
#     # return HttpResponse("<h3>Hi..Hello</h3><h4>Good Morning</h4>")
#     elif request.method == "GET":
#         return render(request, template_name="home.html")     # here we are return file ka data.


# def show_all_books(request):
#     all_books = Book.objects.all()                          # fetching the data from backend(db).
#     data = {"books": all_books}                             # context=data--> if u want to show the data on page.
#     return render(request, template_name="show_books.html", context=data)


# def edit_data(request, id):
#     book = Book.objects.get(id=id)
#     return render(request, template_name= "home.html", context={"single_book": book})


# def Delete_data(request, id):
#     # print(request.method)
#     if request.method == "GET":
#         try:
#             book = Book.objects.get(id=id)
#         except Book.DoesNotExist as err_msg:
#             traceback.print_exc()            # detail error msg.
#             print(err_msg)    
#             return HttpResponse(f"Book Does not exit for ID:- {id}")  
#         else:     
#             book.delete()
#             return redirect("show_all_books")
#     else:
#         return HttpResponse("Error..!")








































































