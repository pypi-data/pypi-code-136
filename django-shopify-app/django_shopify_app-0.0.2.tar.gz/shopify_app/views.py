from django.views import View
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.clickjacking import xframe_options_exempt

import shopify

from shopify_app.utils import get_shop_model
from shopify_app.decorators import shopify_embed


class InitTokenRequestView(View):

    redirect_path_name = ''

    @xframe_options_exempt
    @shopify_embed
    def get(self, request, *args, **kwargs):

        shopify.Session.setup(
            api_key=settings.SHOPIFY_API_KEY,
            secret=settings.SHOPIFY_API_SECRET
        )

        shop_url = request.GET.get('shop')
        api_version = '2022-07'
        state = ''
        path = reverse(self.redirect_path_name)
        redirect_uri = f"{settings.SHOPIFY_APP_HOST}{path}"
        scopes = settings.SHOPIFY_APP_SCOPES

        newSession = shopify.Session(shop_url, api_version)
        auth_url = newSession.create_permission_url(
            scopes, redirect_uri, state
        )

        if request.GET.get('embedded'):
            context = {
                'api_key': settings.SHOPIFY_API_KEY,
                'host': request.GET.get('host'),
                'redirect': auth_url
            }
            return render(request, 'shopify_app/index.html', context=context)
        else:
            return redirect(auth_url)


class EndTokenRequestView(View):
    redirect_path_name = ''

    def get(self, request, *args, **kwargs):

        shop_url = request.GET.get('shop')

        shopify.Session.setup(
            api_key=settings.SHOPIFY_API_KEY,
            secret=settings.SHOPIFY_API_SECRET
        )

        session = shopify.Session(shop_url, '2022-07')

        access_token = session.request_token(request.GET.dict())

        Shop = get_shop_model()
        shop_record = Shop.objects.get_or_create(shopify_domain=session.url)[0]
        shop_record.shopify_token = access_token
        shop_record.access_scopes = session.access_scopes

        shop_record.save()

        host = settings.SHOPIFY_APP_HOST
        path = reverse(self.redirect_path_name)
        query = request.META['QUERY_STRING']

        return redirect(f"{host}{path}?{query}")
