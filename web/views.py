from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from .models import ShortenedUrl
from .forms import UrlShortenerForm


def go(request):
    """
    Search the database for the original value of the given short URL and
    redirect the user automatically to the original URL.
    """
    # Retrieve just the path after the FQDN and strip any leading and trailing
    # slashes. Seems a bit hacky but couldn't think of a better solution at
    # the moment.
    url = request.path_info.strip('/')

    try:
        original_url = ShortenedUrl.objects.get(shortened=url).original
        if not original_url: original_url = '/'
    except ShortenedUrl.DoesNotExist:
        raise Http404

    return redirect(original_url)


def shorten(request):
    """
    Generates a short URL version of the given original URL.original_exists

    Checks:
        1. If the original URL already exists, don't create a new object and
        simply return the shortened value.
        2. If the user enters a URL in the original field that already exists
        as a shortened URL, let the user know.
    """
    form = UrlShortenerForm()

    already_shortened = False

    if request.POST:
        original = request.POST['original']

        original_exists = ShortenedUrl.objects.original_exists(original)
        already_shortened = ShortenedUrl.objects.already_shortened(
            original.replace('http://%s/' % request.get_host(),'').strip('/'))

        # Only create the object if it doesn't already exists and it's not
        # already shortened.
        if not already_shortened:
            if not original_exists:
                obj = ShortenedUrl.objects.create(
                    original=original,
                    shortened=ShortenedUrl.objects.shorten(original),
                )
            else:
                obj = ShortenedUrl.objects.get(original=original)

            form.fields['shortened'].initial = 'http://%s/%s' % (
                request.get_host(), obj.shortened)

        form.fields['original'].initial = original


    return render_to_response(
        'web/index.html',
        {'form': form, 'already_shortened': already_shortened},
        context_instance=RequestContext(request),
    )