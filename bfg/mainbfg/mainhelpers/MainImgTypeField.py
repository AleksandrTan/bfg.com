from django.db.models import FileField
from django.forms import forms


"""
    Custom type for field 'main_img' in table Sentence
    https://blog.bixly.com/accept-only-specific-file-types-in-django-file-upload
"""
class MainImgTypeField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types.
        Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file
        size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(MainImgTypeField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(MainImgTypeField, self).clean(*args, **kwargs)
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError(('Превышен размер загружаемого файла'))
            else:
                raise forms.ValidationError(('Расширение файла не поддерживается.'))
        except AttributeError:
            pass
        return data
