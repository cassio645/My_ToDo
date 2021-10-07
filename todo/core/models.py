from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Título', max_length=50, null=False)
    description = models.TextField('Descrição', blank=True, null=True)
    done = models.BooleanField("Finalizada", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")

    class Meta:
        verbose_name_plural = "To Do"
        ordering = ['-created']

    def __str__(self):
        return self.title

