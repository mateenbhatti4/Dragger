from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    # path('get_data/',views.get_data,name='get_data'),
    # path('edit/',views.edit,name='edit'),
    # path('delete/',views.delete,name='delete'),
    # path('saveUpdation/',views.saveUpdation,name='saveUpdation'),
    # path('show/',views.show,name='show'),
    path('editor/',views.editor,name='edit'),
    path('temp/',views.temp,name='temp'),
    path('gallery/',views.gallery,name='gallery'),
    path('profile/',views.profile,name='profile'),
    path('change_password/',views.ChangePassword,name='change_password'),
    # path('allsides/',views.allsides,name='allsides'),
    # path('uploadfile/',views.uploadfile,name='uploadfile'),
    path('payments/',views.payments,name='payments'),
    # path('qna/',views.qna,name='qna'),
    path('userInfo/',views.userInfo,name='userInfo'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.userLogin,name='userLogin'),
    path('paymentMethod/',views.paymentMethod,name='paymentMethod'),
    path('templates/',views.templates,name='templates'),
    path('ajax/',views.ajaxcall,name='ajax'),
    path('ajaxread/',views.ajaxreadcall,name='ajaxread'),
    path('clearfileajax/',views.clearfileajax,name='clearfileajax'),
    path('savingData/',views.savingData,name='savingData'),
    path('userLogout/',views.userLogout,name='userLogout'),
    path('uploadImage/',views.uploadImage,name='uploadImage'),
    path('saveHtmlData/',views.saveHtmlData,name='saveHtmlData'),
    path('insertClasses/',views.insertClasses,name='insertClasses'),
    path('switchPage/',views.switchPage,name='switchPage'),
    path('downloadCode/',views.downloadCode,name='downloadCode'),
path('imageData/',views.imageData,name='imageData')

]
