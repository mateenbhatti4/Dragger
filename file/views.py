import os
from wsgiref.util import FileWrapper
from django.views.generic.base import View
from django.http import HttpResponse
from django.urls import reverse
from file.models import File
from django.shortcuts import redirect


def UploadFile(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        # get_all_images = File.objects.all()
        for image in images:
            is_file_exist = File.objects.filter(name=str(image))
            if not is_file_exist:
                photo = File.objects.create(
                    name=image,
                    file=image,
                )
                photo.save()
            else:
                photo = File.objects.create(
                    name=image,
                    file=image,
                )
                photo.save()
            return redirect('')

    return HttpResponse("No input")

class FileDownloadView(View):

    def get(self, request, pk):
        file = File.objects.filter(pk=pk).first()
        filename = file.file.path
        wrapper = FileWrapper(file.file)
        response = HttpResponse(wrapper, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % file.name
        response['Content-Length'] = os.path.getsize(filename)
        return response