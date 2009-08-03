from django.db import models
from django.utils.translation import ugettext_lazy as _

from sharer.managers import SocialNetworkManager


class SocialNetwork(models.Model):
    """
    A social network that can be used to share content
    """
    name = models.CharField(_("Name"), max_length=255)
    icon = models.ImageField(_("Icon"), upload_to="sharer/icons", blank=True, null=True)
    url = models.CharField(_("URL"), max_length=255)
    active = models.BooleanField(_("Active"), default=True)
    isgd_shorten = models.BooleanField(_("Shorten URL with is.gd"), default=False)
    bitly_shorten = models.BooleanField(_("Shorten URL with bit.ly"), default=False)

    admin_objects = models.Manager()
    objects = SocialNetworkManager()

    class Meta:
        verbose_name = _("Social Network")
        verbose_name_plural = _("Social Networks")

    def __unicode__(self):
        return self.name
