import random
import string
from django.db import IntegrityError
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import RedirectView, View, DetailView, ListView
from tinyurl.index.forms import UrlTinifyForm
from tinyurl.index.models import InternalUrl

str_generator = lambda N: ''.join(random.choice(string.letters + string.digits) for _ in range(N))


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        domain = 'http://%s' % self.request.META['HTTP_HOST']
        recent_urls = InternalUrl.objects.all()[:20]
        return {'domain': domain, 'recent_urls': recent_urls}


    def get(self, request, *args, **kwargs):
        context = self.get_context()
        context['form'] = UrlTinifyForm()
        return render(request, self.template_name,
                      context)

    def post(self, request, *args, **kwargs):
        form = UrlTinifyForm(request.POST)
        context = self.get_context()
        context['form'] = form

        if not form.is_valid():
            return render(request, self.template_name, context)

        url = request.POST.get('url')
        obj, created = InternalUrl.objects.get_or_create(external_url=url)

        if created:
            _valid_slug = False
            while not _valid_slug:
                try:
                    random_slug = str_generator(10)
                    obj.slug = random_slug
                    obj.save()
                    _valid_slug = True
                except IntegrityError:
                    _valid_slug = False

        return redirect('detail', slug=obj.slug)


class UrlDetail(DetailView):
    model = InternalUrl
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(UrlDetail, self).get_context_data(**kwargs)
        context['domain'] = 'http://%s' % self.request.META['HTTP_HOST']
        return context


class UrlRedirect(RedirectView):
    query_string = True

    def get_redirect_url(self, slug, *args, **kwargs):
        url = get_object_or_404(InternalUrl, slug=slug)
        url.visit()
        return url.external_url


class UrlList(ListView):
    model = InternalUrl
    template_name = 'urlslist.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UrlList, self).get_context_data(**kwargs)
        context['domain'] = 'http://%s' % self.request.META['HTTP_HOST']
        return context


@csrf_protect
def url_api(request):
    try:
        method = request.POST['method']
        slug = request.POST['slug']

        if method == 'DEL':
            get_object_or_404(InternalUrl, slug=slug).delete()
            return HttpResponse(200)
    except:
        raise Http404
