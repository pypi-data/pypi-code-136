import json
from http import HTTPStatus

from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from cloudspotlicense.api import CloudspotLicense_API
from cloudspotlicense.constants.errors import BadCredentials
from cloudspotlicense.constants.responses import ResponseStatus

from .models import GlobalPermission, CloudspotCompany
from .helpers import revoke_permissions, grant_permissions

class LoginView(View):
    """ Authenticates the user against the Cloudspot License Server """
    
    template_name = 'auth/login.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        redirect_url = settings.LOGIN_REDIRECT_URL if hasattr(settings, 'LOGIN_REDIRECT_URL') else '/'
        login_url = settings.LOGIN_URL if hasattr(settings, 'LOGIN_URL') else '/'
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        # We authenticate using the License Server
        api = CloudspotLicense_API(settings.CLOUDSPOT_LICENSE_APP)
        try:
            api.authenticate(username, password)
        except BadCredentials:
            messages.error(request, _('Email or password incorrect'))
            return redirect(login_url)
        
        # Gather the additional user info from the API
        api.get_user()
        
        # First we check all the returned companies, and create them if they're not already present on our system
        
        returned_companies = []
        for company_perm in api.permissions.items():
            company = CloudspotCompany.objects.filter(id=company_perm.company_id).first()
            if not company: company = CloudspotCompany.objects.create(id=company_perm.company_id, name=company_perm.company_name)
            elif company.name != company_perm.company_name:
                company.name = company_perm.company_name
                company.save()
            
            # Add the id to an array that we use later
            returned_companies.append(company_perm.company_id)
        
       # Then we check if we know the user in our system
        UserModel = get_user_model()
        try:
            
            # Update the user with the new information
            user = UserModel.objects.get(username=username)
            user.first_name = api.user.first_name
            user.last_name = api.user.last_name
            user.license_token = api.token
            user.is_active = True
            user.save()
            
        except ObjectDoesNotExist:
            
            # We don't know the user, so we create them
            # Push it to the database
            user = UserModel.objects.create_user(username=username, email=username, password=password, **{
                'first_name' : api.user.first_name,
                'last_name' : api.user.last_name,
                'license_token' : api.token,
            })
            
            user.save()
            
        # Now that we know the user, we clear all the previously linked companies and reassign them to the companies that are included in the response
        user.available_companies.clear()
        for company_id in returned_companies: user.available_companies.add(company_id)
        
        # The user and companies are created, if not already present. We check if the user already has a company linked to them, from a previous login.
        if user.company:
            
            # If there is a company present, we check if the current company has also been returned in the response.
            
            if str(user.company.id) in returned_companies:
                
                # The current company is included in the response, so we set the appropriate permissions and log the user in.
        
                # Remove all existing permissions
                revoke_permissions(user)
                
                # Assign all the returned permissions
                permissions = []
                for perm in api.permissions.items():
                    if perm.company_id == user.company.id:
                        
                        for perm in perm.permissions:
                            permissions.append(perm)
                
                grant_permissions(user, permissions)
                
                # Finally, we log them in and redirect them
                login(request, user)
                
                return redirect(redirect_url)
            else:
                user.company = None
                user.save()
        
        # Else, if the user has no company OR the current company of the user is not included in the response, the users needs to select a new company.
        login(request, user)
        return redirect('select_company')
        
class SelectCompanyView(LoginRequiredMixin, View):
    """ Shows a list of all the available companies to a user to select from """
    
    template_name = 'auth/select_company.html'
    
    def get(self, request, *args, **kwargs):
        api = CloudspotLicense_API(settings.CLOUDSPOT_LICENSE_APP, token=request.user.license_token)
        api.get_permissions()
        context_data = { 'company_permissions' : api.permissions.items() }
        return render(request, self.template_name, context_data)

class SetCompanyView(LoginRequiredMixin, View):
    """ Sets the chosen company for a user and assigns the permissions """
    
    def get(self, request, *args, **kwargs):
        redirect_url = settings.LOGIN_REDIRECT_URL if hasattr(settings, 'LOGIN_REDIRECT_URL') else '/'
        
        user = request.user
        api = CloudspotLicense_API(settings.CLOUDSPOT_LICENSE_APP, token=user.license_token)
        
        # Set company
        user.company = self.company
        user.save()
        
        # Remove all existing permissions
        revoke_permissions(user)
        
        # Get permissions
        try:
            permissions = api.get_company_permissions(self.company.id)
        except Exception as e:
            messages.error(request, e)
            return redirect('select_company')
        
        # Assign all the returned permissions
        grant_permissions(user, permissions)
        
        return redirect(redirect_url)
    
    def dispatch(self, request, *args, **kwargs):
        self.company = CloudspotCompany.objects.filter(id=kwargs['company_id']).first()
        if not self.company: return HttpResponseBadRequest(_('The selected company does not exist'))
        return super().dispatch(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class WebhookView(View):
    """ Handles all the webhook events that the Cloudspot License Server server sends """
    
    def post(self, request, *args, **kwargs):
        
        req = json.loads(request.body)
        event = req['event']
        data = req['data']
        UserModel = get_user_model()
        
        if event == 'permissions.updated':
            token = data['token']
            
            try:
                user = UserModel.objects.get(license_token=token)
            except UserModel.DoesNotExist:
                return JsonResponse({ 'status' : ResponseStatus.NOT_FOUND, 'error' : { 'message' : 'No user matched the token.' }}, status=HTTPStatus.NOT_FOUND)
            
            permissions = data['permissions']
            company_id = data['company_id']
            
            try:
                company = CloudspotCompany.objects.get(pk=company_id)
            except CloudspotCompany.DoesNotExist:
                return JsonResponse({ 'status' : ResponseStatus.NOT_FOUND, 'error' : { 'message' : 'No company matched the id.' }}, status=HTTPStatus.NOT_FOUND)
            
            # Only update the user permissions if the current company is the company in the request
            # Otherwise, these permissions do not apply to this user at this moment
            # When the user switches companies, the new permissions get retrieved from the License Server anyway
            if user.company == company:
                revoke_permissions(user)
                grant_permissions(user, permissions)

            return JsonResponse({ 'status' : ResponseStatus.OBJECT_UPDATED })