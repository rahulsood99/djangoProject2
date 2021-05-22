from django.db import models


def user_directory_path_pdf(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_id/filename
    return 'pdfs/' + filename


def user_directory_path_cover(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_id/filename
    return 'covers/' + filename


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to=user_directory_path_pdf)
    cover = models.ImageField(upload_to=user_directory_path_cover, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

