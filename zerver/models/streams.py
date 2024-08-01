from django.db import models

from zerver.models.realms import Realm
from zerver.models.users import UserProfile


class Stream(models.Model):
    realm = models.ForeignKey(Realm, on_delete=models.RESTRICT)
    creator = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
