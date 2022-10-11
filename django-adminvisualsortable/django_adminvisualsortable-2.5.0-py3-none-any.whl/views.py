import django
from django.shortcuts import render
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.apps import apps
from django.db.models import ForeignKey
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import HttpResponse, get_object_or_404
from django.http import Http404, HttpResponseForbidden
from django.urls import reverse
import simplejson as json
import copy

def get_fk_name(model):
    ''' Get The First ForeignKey Field Name '''
    fields = model._meta.get_fields()
    for field in fields:
        if isinstance(field, ForeignKey):
            return field.name
    return None

def model_has_inlines(modelname):
    ''' Check if Model has Inline(s) from his Model Admin '''
    inline_list = get_model_inlines(modelname)
    if len(inline_list) > 0:
        return True
    return False

def get_model_inlines(modelname):
    ''' Get Inline Models from Model Admin '''
    inline_list = []
    for k,v in admin.site._registry.items():
        if v.inlines:
            for i in v.inlines:
                if k.__name__.lower() == modelname.lower():
                    inline_list.append(i.model)
    return inline_list

@staff_member_required
def sortable_inlines_detail(request, app, modelparentname, model_id, modelname, fkfield=None):
    ''' Sort Element from Inline Model'''
    preview_field = False
    has_image_json = False
    image_json_path = ['image', 'small', 'url', 'regular']
    TargetModelParent = apps.get_model('{}.{}'.format(app, modelparentname))
    TargetModel = apps.get_model('{}.{}'.format(app, modelname))
    if model_id == 0: # Could Be A SingleTone Admin Model
        parent_instance = TargetModelParent.objects.first()
    else:
        parent_instance = TargetModelParent.objects.get(id=model_id)
    ordering_field = TargetModel._meta.ordering[0]
    if fkfield is None:
        # se non indicato proviamo a pescarlo in autonomia
        fkfield = get_fk_name(TargetModel)
    queryset = TargetModel.objects.filter(**{fkfield: parent_instance})
    res = []
    fields = TargetModel._meta.get_fields()
    fields_name = [f.name for f in fields]
    for parent_model, parent_admin in admin.site._registry.items():
        if parent_model == TargetModelParent:
            if parent_admin.inlines:
                for v in parent_admin.inlines:
                    if v.model == TargetModel:
                        if getattr(v, 'visualsortable_image_json', False):
                            has_image_json = True
                            preview_field = 'image_json'
                        elif getattr(v, 'visualsortable_field', False):
                            for f in fields:
                                if f.name == getattr(v, 'visualsortable_field', None):
                                    if getattr(f, 'attr_class', None) == django.db.models.fields.files.ImageFieldFile:
                                        preview_field = getattr(v, 'visualsortable_field')
                            if preview_field:
                                break
    if preview_field is False:
        for field in fields:
            if getattr(field, 'attr_class', None) == django.db.models.fields.files.ImageFieldFile:
                preview_field = field.name
                break
    idx_list = []
    warning_dups = False
    for q in queryset:
        if preview_field:
            if preview_field == 'image_json':
                image_json_url = getattr(q, preview_field, {})
                try:
                    for x in image_json_path:
                        if x in image_json_path:
                            image_json_url = image_json_url[x]
                except KeyError:
                    print('Visual Sortable - KeyError on Image Json')
                    image_json_url = None
                except TypeError:
                    print('Visual Sortable - TypeError on Image Json')
                    image_json_url = None
                if image_json_url:
                    image_url = { 'url': image_json_url }
                else:
                    image_url = 'NOIMAGE'
                res.append({'ord': getattr(q, ordering_field, 0), 'obj': q,
                            'img': image_url })
            else:
                res.append({'ord': getattr(q, ordering_field, 0), 'obj': q,
                            'img': getattr(q, preview_field, 'NOIMAGE') })
        else:
            res.append({'ord': getattr(q, ordering_field), 'obj': q,
                        'img': 'NOIMAGE' })
        if getattr(q, ordering_field, 0) in idx_list:
            warning_dups = True
            break
        else:
            idx_list.append(getattr(q, ordering_field, 0))
    if warning_dups:
        from django.core.management import call_command
        call_command('reorder', '{}.{}'.format(app.lower(), modelname.lower()))
        return HttpResponseRedirect(request.path)

    parent_is_sortable = False
    for k,v in admin.site._registry.items():
        if k.__name__.lower() == modelparentname:
            if getattr(v, 'is_adminvisualsortable', False):
                parent_is_sortable = True
    inline_list = []
    for k,v in admin.site._registry.items():
        if v.inlines:
            for i in v.inlines:
                if k.__name__.lower() == modelparentname:
                    if getattr(i, 'is_adminvisualsortable', False):
                        inline_list.append(i.model)
    parent_multi_inlines = True if len(inline_list) > 1 else False
    parent_pivot_url = reverse('adminvisualsortable:sortable inlines', kwargs={'app': app, 'modelparentname': modelparentname, 'model_id': model_id})
    parent_sort_url = reverse('adminvisualsortable:sort models', kwargs={'app': app, 'modelname': modelparentname, })
    context = {
        'res': res,
        'parent_instance': parent_instance,
        'ordering_field': ordering_field,
        'app': app,
        'modelname': modelname,
        'targetModel':  { 'name': TargetModel.__name__,
                         'verbose_name_plural': TargetModel._meta.verbose_name_plural,
                        },
        'parentModel' : { 'name': TargetModelParent.__name__,
                         'verbose_name_plural': TargetModelParent._meta.verbose_name_plural,
                        },
        'preview_field': preview_field,
        'parent_multi_inlines': parent_multi_inlines,
        'parent_pivot_url': parent_pivot_url,
        'parent_is_sortable': parent_is_sortable,
        'parent_sort_url': parent_sort_url if parent_is_sortable else None,
        'site_header': admin.site.site_header
    }
    return render(request, 'adminvisualsortable/sort-inline-models.html', context)

@staff_member_required
def sort_models(request, app, modelname):
    ''' Sort Element from an Inline Model referring from Parent Model'''
    preview_field = False
    has_image_json = False
    image_json_path = ['image', 'small', 'url', 'regular']
    TargetModel = apps.get_model('{}.{}'.format(app, modelname))
    ordering_field = TargetModel._meta.ordering[0]
    queryset = TargetModel.objects.all()
    res = []
    idx_list = []
    fields = TargetModel._meta.get_fields()
    fields_name = [f.name for f in fields]
    for k,v in admin.site._registry.items():
        if k == TargetModel:
            if getattr(v, 'visualsortable_image_json', False):
                has_image_json = True
                preview_field = 'image_json'
            elif getattr(v, 'visualsortable_field', False):
                for f in fields:
                    if f.name == getattr(v, 'visualsortable_field'):
                        if getattr(f, 'attr_class', None) == django.db.models.fields.files.ImageFieldFile:
                            preview_field = getattr(v, 'visualsortable_field')
                if preview_field:
                    break

    if preview_field is False:
        for field in fields:
            if getattr(field, 'attr_class', None) == django.db.models.fields.files.ImageFieldFile:
                preview_field = field.name
                break
    warning_dups = False
    for q in queryset:
        if preview_field:
            if preview_field == 'image_json':
                image_json_url = getattr(q, preview_field, {})
                try:
                    for x in image_json_path:
                        if x in image_json_path:
                            image_json_url = image_json_url[x]
                except KeyError:
                    print('Visual Sortable - KeyError on Image Json')
                    image_json_url = None
                except TypeError:
                    print('Visual Sortable - TypeError on Image Json')
                    image_json_url = None
                if image_json_url:
                    image_url = { 'url': image_json_url }
                else:
                    image_url = 'NOIMAGE'
                res.append({'ord': getattr(q, ordering_field, 0), 'obj': q,
                            'has_sort_inlines': model_has_inlines(modelname),
                            'img': image_url })
            else:
                res.append({'ord': getattr(q, ordering_field, 0), 'obj': q,
                            'has_sort_inlines': model_has_inlines(modelname),
                            'img': getattr(q, preview_field, 'NOIMAGE') })
        else:
            res.append({'ord': getattr(q, ordering_field), 'obj': q,
                        'has_sort_inlines': model_has_inlines(modelname),
                        'img': 'NOIMAGE' })
        if getattr(q, ordering_field, 0) in idx_list:
            warning_dups = True
            break
        else:
            idx_list.append(getattr(q, ordering_field, 0))
    if warning_dups:
        from django.core.management import call_command
        call_command('reorder', '{}.{}'.format(app.lower(), modelname.lower()))
        return HttpResponseRedirect(request.path)
    context = {
        'res': res,
        'ordering_field': ordering_field,
        'modelInstance': TargetModel,
        'app': app,
        'modelname': modelname,
        'targetModel': { 'name': TargetModel.__name__,
                         'verbose_name_plural': TargetModel._meta.verbose_name_plural,
                         'id': TargetModel.id,
                         'app_name': app },
        'preview_field': preview_field,
        'site_header': admin.site.site_header
    }
    return render(request, 'adminvisualsortable/sort-models.html', context)

@staff_member_required
def sortable_inlines(request, app, modelparentname, model_id):
    ''' If one Inline sortable show sortable layout '''
    ''' If more then one show or should show list of possible inlines to sort'''
    TargetModelParent = apps.get_model('{}.{}'.format(app, modelparentname))
    if model_id == 0: # SingleTone Admin
        parent_instance = TargetModelParent.objects.first()
    else:
        parent_instance = TargetModelParent.objects.get(id=model_id)
    inline_list = []
    for k,v in admin.site._registry.items():
        if v.inlines:
            for i in v.inlines:
                if k.__name__.lower() == modelparentname:
                    if getattr(i, 'is_adminvisualsortable', False):
                        inline_list.append(i.model)

    if len(inline_list) == 1:
        return HttpResponseRedirect(reverse('adminvisualsortable:sortable inlines detail', kwargs={
            'app': app,
            'modelparentname': modelparentname,
            'model_id': model_id,
            'modelname': inline_list[0].__name__.lower(),
        }))
    else:
        # Verificare se il padre è ordinabile
        parent_is_sortable = False
        for k,v in admin.site._registry.items():
            if k.__name__.lower() == modelparentname:
                if getattr(v, 'is_adminvisualsortable', False):
                    parent_is_sortable = True
        TargetModel = apps.get_model('{}.{}'.format(app, modelparentname))
        inline_list_res = []
        for i in inline_list:
            inline_list_res.append({ 'url': reverse('adminvisualsortable:sortable inlines detail',
                                        kwargs={'app': app, 'modelparentname': modelparentname,
                                                'model_id': model_id, 'modelname': i.__name__.lower(), }),
                                    'name': i.__name__ })
        context = {
            'app': app,
            'inlines': inline_list_res,
            'parent_is_sortable': parent_is_sortable,
            'parent_sort_url': reverse('adminvisualsortable:sort models',
                                        kwargs={'app': app, 'modelname': modelparentname, }),
            'model_id': model_id,
            'targetModel': { 'name': TargetModel.__name__,
                         'verbose_name_plural': TargetModel._meta.verbose_name_plural,
                         'id': model_id,
                         'app_name': app },
            'parent_instance': parent_instance,
            'site_header': admin.site.site_header
        }
        return render(request, 'adminvisualsortable/sort-models-pivot.html', context)

####################################################
################      API    #######################
####################################################

@staff_member_required
def api_sort_models(request):
    ''' Sorting API '''
    context_json = {}
    context_json['status'] = 'error'
    context_json['msg'] = 'Errore Generico'
    if request.method != 'POST':
        return HttpResponse(json.dumps(context_json), content_type="application/json")
    data = json.loads(request.body)
    # print(data)
    # id_from = data['id_from']
    # id_to = data['id_to']
    id_idx_dict = data['dict_id_idx']
    # print(id_idx_dict)
    model_name = data['model_name']
    app = data['app']
    parent_name = data.get('parentModel', None)
    if bool(parent_name) == False:
        TargetModel = apps.get_model('{}.{}'.format(app, model_name))
    ordering_field = TargetModel._meta.ordering[0]
    for el in id_idx_dict:
        TargetModel.objects.filter(id=el['id']).update(**{ordering_field: el['idx']})
    context_json['status'] = 'success'
    context_json['msg'] = 'Ordinamento aggiornato con successo'
    return HttpResponse(json.dumps(context_json), content_type="application/json")
