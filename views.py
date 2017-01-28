import re

from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template import RequestContext
from django.template import TemplateDoesNotExist
from django.template import loader

def health_check(request):
    response = HttpResponse('200 OK', status=200)
    return response

def generic_template_view(request, template_name, context_dict=None, content_type='text/html', missing_template_exception=Http404):
    try:
        template = loader.get_template(template_name)
        context_dict = context_dict or {}
        context = RequestContext(request, context_dict)
        response = HttpResponse(template.render(context), content_type=content_type)
    except TemplateDoesNotExist:
        response = None
        raise missing_template_exception
    return response

def google_site_verification(request, code):
    from htk.exceptions import MissingGoogleSiteVerificationFile
    template_name = 'site_verification/google%s.html' % code
    response = generic_template_view(
        request,
        template_name,
        missing_template_exception=MissingGoogleSiteVerificationFile
    )
    return response

def html_site_verification(request, code):
    from htk.exceptions import MissingHtmlSiteVerificationFile
    template_name = 'site_verification/%s--.html' % code
    response = generic_template_view(
        request,
        template_name,
        missing_template_exception=MissingHtmlSiteVerificationFile
    )
    return response

def bing_site_auth(request):
    from htk.exceptions import MissingBingSiteVerificationFile
    template_name = 'site_verification/BingSiteAuth.xml'
    response = generic_template_view(
        request,
        template_name,
        content_type='text/xml',
        missing_template_exception=MissingBingSiteVerificationFile
    )
    return response

def robots(request):
    template_name = 'robots.txt'
    context_dict = {
        'request' : {
            'request' : request,
            'host' : request.get_host(),
         },
    }
    response = generic_template_view(
        request,
        template_name,
        context_dict=context_dict,
        content_type='text/plain'
    )
    return response

def redir(request):
    url = request.GET.get('url', None)
    if url:
        if not re.match('^https?://', url):
            url = 'http://%s' % url
        else:
            pass
        response = redirect(url)
    else:
        response = redirect('/')
    return response

##################################################
# error pages

def error_view(request):
    path_no_slash = request.path[1:]
    response = generic_template_view(
        request,
        '%s.html' % path_no_slash
    )
    return response
