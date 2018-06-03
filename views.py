import urllib
from django.http import HttpResponse


def home(request):
    g = urllib.urlopen("http://www.google.com")
    google_status_code = g.getcode()
    g.close()
    t = urllib.urlopen("http://www.twitter.com")
    twitter_status_code = t.getcode()
    t.close()
    return HttpResponse(
        """Uptime Checker. google.com status={0}. twitter.com status={1}""".format(
            google_status_code, twitter_status_code))
