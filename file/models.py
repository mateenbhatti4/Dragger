from django.db import models
from django.urls import reverse



class File(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='documents/')
    user = models.ForeignKey('auth.User',null=True,default=None,on_delete=models.CASCADE)
    isProfile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


    def __str__(self):
        return f'{self.name}'

    @property
    def get_download_url(self):
        return reverse('file:download', args=[self.pk])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.name:
            self.name = self.file.name
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    @property
    def full_path(self):
        return f'{self.name}'

    @property
    def extension(self):
        return str(self.name).split('.')[-1]

    @property
    def icon(self):
        if self.extension == 'txt':
            return '-alt'
        elif self.extension == 'pdf':
            return '-pdf'
        elif self.extension in ['doc', 'docs', 'docx', 'odt', 'dot', 'dotm', 'dotx']:
            return '-word'
        elif self.extension in ['xls', 'xlsx', 'xlt']:
            return '-excel'
        elif self.extension in ['ppt', 'pptx', 'ppsx']:
            return '-powerpoint'
        elif self.extension in ['png', 'jpg', 'jpeg']:
            return '-image'
        elif self.extension in ['mp4', 'mkv', 'flv', 'vob', 'avi', 'wmv']:
            return '-video'
        elif self.extension in ['mp3', 'aa', 'aac', 'act', 'mmf', 'mpc']:
            return '-audio'
        elif self.extension in ['py', 'js', 'java', '\p'
                                                    'hp', 'rb', 'html', 'css', 'htm']:
            return '-code'
        elif self.extension in ['zip', 'rar', 'iso', '7z', 'apk']:
            return '-archive'
        elif self.extension == 'csv':
            return '-csv'
        else:
            return ''