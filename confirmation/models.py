from django.db import models

from zerver.models import Realm


class Confirmation(models.Model):
    realm = models.ForeignKey(Realm, on_delete=models.RESTRICT)
