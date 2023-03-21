from django.db import models

class BaseModel (models.Model) :
    added_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta :
        abstract = True
