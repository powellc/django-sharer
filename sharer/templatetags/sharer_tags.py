from urlparse import urljoin
import urllib
import simplejson as json


from django import template
from django.contrib.sites.models import Site
from django.template.defaultfilters import urlencode

from sharer.forms import EmailShareForm
from sharer.models import SocialNetwork
from sharer.settings import ENABLE_EMAILS, BITLY_LOGIN, BITLY_KEY

register = template.Library()


@register.inclusion_tag("sharer/includes/widget.html", takes_context=True)
def share(context, title="", url=""):
    """
    Renders the share widget
    """
    networks = SocialNetwork.objects.all()

    if not url:
        url = context.get("SHARE_URI", "")

    if url.startswith("/"):
        site = Site.objects.get_current()

        if site:
            url = urljoin("http://%s" % site.domain, url)

    return {
        "networks": networks,
        "title": title,
        "url": url,
        "ENABLE_EMAILS": ENABLE_EMAILS,
        "MEDIA_URL": context.get("MEDIA_URL", ""),
        "LANGUAGE_CODE": context.get("LANGUAGE_CODE", ""),
    }


@register.simple_tag
def share_url(network, title="", url=""):
    """
    Builds a network url with given variables
    """
    if network.isgd_shorten:
	page = urllib.urlopen('http://is.gd/api.php?longurl=%s' % url)    
	url = page.read()
    if network.bitly_shorten and BITLY_LOGIN:
        page = urllib.urlopen('http://api.bit.ly/shorten?version=2.0.1&longUrl=%s&login=%s&apiKey=%s&history=1' % (url, BITLY_LOGIN, BITLY_KEY))	
        response = json.load(page)
        url = results=response["results"][url]["shortUrl"]
    return network.url % {
        "url": urlencode(url),
        "title": urlencode(title),
    }
