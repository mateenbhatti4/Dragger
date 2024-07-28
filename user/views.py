import json
import os

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from os.path import exists as file_exists
from django.contrib.auth import authenticate, login, logout
from file.models import File
from django.shortcuts import redirect
from user.models import Payments
from django.contrib.auth.models import User

# Create your views here.
from user.models import BootstrapClasses


def index(request):
    return render(request, "user/index.html")


def userdashboard(request):
    files = File.objects.filter(user_id=request.user.id).filter(isProfile=1)
    plan = Payments.objects.filter(user_id=request.user.id).first()
    name = request.user.first_name
    data = []
    for file in files:
        data.append(file.get_download_url)
    return render(request, "user/dashboard.html", context={'url': data, 'name': name.split()[0],'plan':plan})


# def get_data(request):
#     if request.method == 'POST':
#         id = request.POST.get('offId', 'default')
#         name = request.POST.get('empName', 'default')
#         cnic = request.POST.get('cnic', 'default')
#         address = request.POST.get('address', 'default')
#         if id != "" or name != "" or cnic != "" or address != "":
#             record = Employees.objects.create(officeId=id, name=name, cnic=cnic, address=address)
#             record.save()
#
#         record = Employees.objects.all()
#         # print(record.id)
#         return render(request, 'base.html',{'record':record})
#     else:
#         return HttpResponse("page not found")
# return HttpResponse("hello this is login")
# def edit(request):
#     id = request.GET.get('getID', 'default')
#     update = Employees.objects.filter(id = id)
#     parm = {'officeId':0,'name':0,'cnic':0,'address':0}
#     for i in update:
#         parm = {'officeId':i.officeId,'name':i.name,'cnic':i.cnic,'address':i.address}
#     return render(request,'display.html',parm)
#
# def saveUpdation(request):
#     if request.method == 'POST':
#         officeid = request.POST.get('offId', 'default')
#         name = request.POST.get('empName', 'default')
#         cnic = request.POST.get('cnic', 'default')
#         address = request.POST.get('address', 'default')
#
#         Employees.objects.filter(officeId=officeid).update(name=name, cnic=cnic, address=address)
#
#         record = Employees.objects.all()
#         return render(request, 'base.html',{'record':record})
#     else:
#         return HttpResponse("page not found")
#
# def delete(request):
#     id = request.GET.get('getID', 'default')
#     update = Employees.objects.filter(id=id)
#     update.delete()
#     record = Employees.objects.all()
#     return render(request, 'base.html', {'record': record})
#
# def show(request):
#     record = Employees.objects.all()
#     return render(request, 'base.html', {'record': record})

def editor(request):
    classes = BootstrapClasses.objects.filter(custom=False)

    return render(request, 'user/editor.html', context={'classes': classes})


def gallery(request):
    return render(request, 'user/gallery.html')


def profile(request):
    files = File.objects.filter(user_id=request.user.id).filter(isProfile=1)
    print(request.user.id)
    name = request.user.first_name
    data = []
    for file in files:
        data.append(file.get_download_url)
    return render(request, 'user/profile.html', context={'url': data, 'name': name.split()[0],
                                                         'idName': request.user.first_name,
                                                         'username': request.user.username,
                                                         'email': request.user.email})


def ChangePassword(request):
    if request.method=="POST":
        newpass = request.POST.get('newpass', 'default')
        cnewpass = request.POST.get('cnewpass', 'default')
        if not newpass == cnewpass:
            return render(request, 'user/profile.html', context={'message': "password does not match"})
        user=User.objects.filter(id=request.user.id).first()
        user.set_password(newpass)
        user.save()
        return render(request, 'user/index.html', context={'message': "Password change success"})
    return HttpResponse("method not allowed")


# def allsides(request):
#     return render(request, 'user/allsides.html')

# def uploadfile(request):
#     return render(request, 'user/uploadfile.html')


def insertClasses(request):
    Images = ["img-fluid", "img-thumbnail", "rounded", "float-left", "float-left" "figure-img", "mx-auto", "d-block",
              "rounded-circle", "float-start", "float-end"]

    if BootstrapClasses.objects.filter(category="image").count() <= 0:
        for x in Images:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="image")
            save_image_classes.save()

    table = ["table", "table-bordered", "table-hover", "table-responsive", "table-borderless", "table-striped",
             "table-sm", "table-dark", "table-active", "table-light", "table-info", "table-warning", "table-danger",
             "table-success", "table-secondary", "table-primary", "table-responsive-sm", "table-responsive-md",
             "table-responsive-lg", "table-responsive-xl"]

    if BootstrapClasses.objects.filter(category="table").count() <= 0:
        for x in table:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="table")
            save_image_classes.save()

    Buttons = ["btn", "btn-primary", "btn-secondary", "btn-success", "btn-danger", "btn-light", "btn-dark", "btn-info",
               "btn-link", "btn-warning", "btn-outline-primary", "btn-outline-secondary", "btn-outline-success",
               "btn-outline-danger", "btn-outline-warning", "btn-outline-info", "btn-outline-light", "btn-outline-dark",
               "btn-lg", "btn-sm", "active", "disabled", "text-toolbar", "text-primary", "text-secondary",
               "text-success", "text-danger", "text-light", "text-dark", "text-info", "text-warning", "btn-block"]

    if BootstrapClasses.objects.filter(category="buttons").count() <= 0:
        for x in Buttons:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="buttons")
            save_image_classes.save()

    Card = ["card", "card-body", "card-title", "card-text", "card-subtitle", "card-link", "card-image-top",
            "card-header", "card-header-tabs", "card-footer", "text-muted", "text-center", "text-right",
            "card-header-pills", "card-img-top", "card-img-bottom", "card-img-overlay", "bg-primary", "bg-secondary",
            "bg-success", "bg-danger", "bg-light", "bg-dark", "bg-info", "border-primary", "border-secondary",
            "border-success", "border-danger", "border-light", "border-dark", "border-info", "bg-transparent",
            "text-primary", "card-deck"]

    if BootstrapClasses.objects.filter(category="card").count() <= 0:
        for x in Card:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="card")
            save_image_classes.save()

    Modal = ["modal", "modal-dialog", "modal-content", "modal-header", "modal-title", "modal-body", "modal-footer",
             "modal-fade", "modal-dialog-scrollable", "modal-dialog-centered", "modal-xl", "modal-lg", "modal-sm"]

    if BootstrapClasses.objects.filter(category="modal").count() <= 0:
        for x in Modal:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="modal")
            save_image_classes.save()

    Form = ["form-control", "form-check", "form-check-label", "form-control-color", "form-check-input",
            "form-control-file", "form-control-lg", "form-control-sm", "form-control-plaintext", "form-inline",
            "form-control-range", "form-check-inline", "form-row"]

    if BootstrapClasses.objects.filter(category="form").count() <= 0:
        for x in Form:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="form")
            save_image_classes.save()

    Dropdown = ["dropdown", "dropdown-menu", "dropdown-item", "dropdown-toggle", "dropdown-divider",
                "dropdown-toggle-split", "dropup", "dropend", "dropstart", "dropdown-item-text", "acrive", "disabled",
                "dropdown-menu-end", "dropdown-menu-lg-right", "dropdown-menu-sm-right", "dropdown-menu-md-right",
                "dropdown-menu-xl-right", "dropdown-menu-lg-left", "dropdown-menu-sn-left", "dropdown-menu-md-left",
                "dropdown-menu-xl-left"]

    if BootstrapClasses.objects.filter(category="dropdown").count() <= 0:
        for x in Dropdown:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="dropdown")
            save_image_classes.save()

    Input = ["form-control", "form-check-input", "form-control-lg", "form-control-sm", "form-control-plaintext",
             "form-control-color"]

    if BootstrapClasses.objects.filter(category="input").count() <= 0:
        for x in Input:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="input")
            save_image_classes.save()

    text = ["text-justify", "form-control", "text-center", "text-right", "text-left", "text-lowercase",
            "text-uppercase", "text-capitalize", "font-weight-bold", "font-weight-bolder", "font-weight-normal",
            "font-weight-light", "font-weight-lighter", "text-monospace"]

    if BootstrapClasses.objects.filter(category="text").count() <= 0:
        for x in text:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="text")
            save_image_classes.save()

    label = ["form-check-label"]

    if BootstrapClasses.objects.filter(category="label").count() <= 0:
        for x in label:
            save_image_classes = None
            save_image_classes = BootstrapClasses.objects.create(class_name=x, category="label")
            save_image_classes.save()

    return HttpResponse(BootstrapClasses.objects.filter().count())


def payments(request):
    files = File.objects.filter(user_id=request.user.id).filter(isProfile=1)
    plan = Payments.objects.filter(user_id=request.user.id).first()
    name = request.user.first_name
    data = []
    for file in files:
        data.append(file.get_download_url)
    return render(request, 'user/payments.html', context={'url': data, 'name': name.split()[0],'plan':plan})


def userInfo(request):
    files = File.objects.filter(user_id=6)
    print(request.user.id)
    # print(file)
    # print(file.get_download_url)
    # data={
    #     'url':file.get_download_url
    # }
    data = []
    for file in files:
        data.append(file.get_download_url)
    return render(request, 'user/step2.html', context={'url': data})


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        username = request.POST.get('username', 'default')
        password = request.POST.get('password', 'default')
        confirmPass = request.POST.get('confirmPass', 'default')
        image = request.POST.get('image', 'default')
        images = request.FILES.getlist('images')
        # get_all_images = File.objects.all()
        if name != "" or email != "" or username != "" or password != "" or confirmPass != "":
            data = User.objects.filter(username=username)
            if data.count() == 0:
                if password == confirmPass:
                    record = User.objects.create_user(username, email, password)
                    record.first_name = name
                    for image in images:
                        photo = File.objects.create(
                            name=image,
                            file=image,
                            isProfile=True,
                            user_id=record.id
                        )
                        photo.save()
                    record.save()
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                    return render(request, 'user/step3.html')
                else:
                    messages.error(request, " Passwords do not match")
                    return redirect('index')
            else:
                messages.error(request, " Username is already taken")
                return redirect('index')
    return render(request, 'user/step3.html')
        # else:
        #     photo = File.objects.create(
        #         name=image,
        #         file=image,
        #         # user_id=request.user.id
        #     )
        #     photo.save()


@csrf_exempt
def uploadImage(request):
    image = request.FILES.get('file')

    # images = request.GET.get('form', 'default')
    print("Image Title ", image)
    if image:
        photo = File.objects.create(
            name=image,
            file=image,
            isProfile=False,
            user_id=request.user.id
        )
        photo.save()
    file = File.objects.filter(user_id=request.user.id).order_by('-created_at').first()
    data = []
    data.append(file.get_download_url)
    print("Image Data ", data)
    return HttpResponse(data)


def paymentMethod(request):
    return render(request, 'user/step3.html')


def templates(request):
    return render(request, 'user/finalStep.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('name', 'default')
        password = request.POST.get('password', 'default')
        print(username)
        print(password)
        if username != "" and password != "":
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('userdashboard')
            else:
                messages.error(request, "Invalid Credentials, Please try again")
                return redirect('index')
        else:
            return render(request, "user/index.html")
    else:
        return HttpResponse("404 Page Not Found")


def userLogout(request):
    logout(request)
    return redirect('index')


def temp(request):
    return render(request, 'user/temp.html')


@csrf_exempt
def ajaxcall(request):
    test = request.GET.get('salman', 'default')
    print("hello ajax call ")
    f = open("testfile.txt", "a")
    f.write(test)
    f.close()

    # open and read the file after the appending:
    # f = open("demofile2.txt", "r")
    # print(f.read())
    return HttpResponse(test)


@csrf_exempt
def ajaxreadcall(request):
    print("hello ajax call ")
    if file_exists('testfile.txt'):
        f = open("testfile.txt", "r")
        test = f.read()
        f.close()
    else:
        test = "no file"
    return HttpResponse(test)


@csrf_exempt
def savingData(request):
    test = request.GET.get('salman', 'default')
    f = open("testfile.txt", "r+")
    f.truncate(0)
    f.close()
    f = open("testfile.txt", "w")
    f.write(test)
    f.close()
    return HttpResponse(test)


@csrf_exempt
def saveHtmlData(request):
    html = request.GET.get('html', 'default')
    file = request.GET.get('file_name', 'default')
    file = file + '.html'
    f = open("testfile.txt", "w")
    f.write(html)
    f.close()
    f = open(file, "w")
    f.write(html)
    f.close()
    return HttpResponse(html)


def switchPage(request):
    html = request.GET.get('fileName', 'default')
    if html == 'home':
        f = open("home.html", "r")
        data = f.read()
        f.close()
        f = open("testfile.txt", "w")
        f.write(data)
        f.close()
        return HttpResponse(data)
    elif html == 'about':
        f = open("about.html", "r")
        data = f.read()
        f.close()
        f = open("testfile.txt", "w")
        f.write(data)
        f.close()
        return HttpResponse(data)
    elif html == 'services':
        f = open("services.html", "r")
        data = f.read()
        f.close()
        f = open("testfile.txt", "w")
        f.write(data)
        f.close()
        return HttpResponse(data)
    elif html == 'contact':
        f = open("contact.html", "r")
        data = f.read()
        f.close()
        f = open("testfile.txt", "w")
        f.write(data)
        f.close()
        return HttpResponse(data)


def downloadCode(request):
    imgId = request.GET.getlist('imageID[]', 'default')
    parms = {}
    f = open("home.html", "r")
    homePage = f.read()
    if homePage != "":
        parms.update({'home':homePage})
    f.close()
    f = open("about.html", "r")
    aboutPage = f.read()
    if aboutPage != "":
        parms.update({'about': aboutPage})
    f.close()
    f = open("services.html", "r")
    servicesPage = f.read()
    if servicesPage != "":
        parms.update({'services': servicesPage})
    f.close()
    f = open("contact.html", "r")
    contactPage = f.read()
    if contactPage != "":
        parms.update({'contact': contactPage})
    f.close()
    json_object = json.dumps(parms)
    print(json_object)
    # params = ["homePage", "aboutPage", "servicesPage", "contactPage"]
    # return render(request, 'user/editor.html', context=params)
    return HttpResponse(json_object)


def clearfileajax(request):
    print("hello ajax call ")
    if file_exists('testfile.txt'):
        f = open("testfile.txt", "w")
        f.write("")
        f.close()
        test = "file cleared"
    else:
        test = "no file"
    return HttpResponse(test)

def imageData(request):
    imgId = request.GET.getlist('imageID[]', 'default')
    imgIDs = []
    for x in imgId:
        data = File.objects.filter(id=x).first()

        imgIDs.append(str(data.file))
        imgIDs.append(" ")
    # print(imgIDs)
    # json_obj=[]
    # json_obj.append({'data':json.dumps(imgIDs)})
    # return HttpResponse(json.dumps(imgIDs),contentType='application/json')
    return HttpResponse(imgIDs)
