from urllib.parse import urlparse


def get_path_referer(request):
    # gets the url where this url was invoked.
    referer_path = request.META.get('HTTP_REFERER', None)
    path = urlparse(referer_path).path if referer_path else '/'
    return path