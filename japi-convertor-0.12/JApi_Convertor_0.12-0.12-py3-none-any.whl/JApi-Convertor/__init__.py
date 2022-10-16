import json
import os
import re

class Convertor():
    def __init__(self):
        self.data = {}
        self.variable_type_to_moodel_field = {
            int: "models.IntegerField(blank=True,null=True)",
            str: "models.TextField(blank=True,null=True)",
            float: "models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)",
            bool: "models.BooleanField(default=False)"
        }
        self.primary_keys = {}
        self.path = ''
        
    def validString(self, dataString):
        specialCharacters = "[^a-zA-Z0-9_]"

        if len(dataString) == 0:
            return False
        elif dataString[0].isdigit():
            return False
        elif len(re.findall(specialCharacters, dataString)) != 0 :
            return False
        return True
    
    def write_to_file(self):
        data = {
            'path' : self.path,
            'data' : self.data,
            'primary_keys' : self.primary_keys
        }
        with open('initData.json','w') as file:
            json.dump(data, file)

    def load_from_file(self):
        if os.path.exists('initData.json'):
            with open('initData.json', 'r') as file:
                dic = json.load(file)
                self.path = dic['path']
                

    def ask_or_append(self,json_data,class_name,primary_key=None):
        class_name = class_name.title()
        if class_name in self.data.keys():
            print('Class with the same name already exists!!')
            choice = input('Do you want to overwrite it (y|n) : ').lower()
            if choice=='y' or choice=='yes':
                for k in self.data.keys():
                    if not self.validString(k):
                        print(f'Json key {k} doesnt follow correct nomenclature')
                        return
                self.append(json_data,class_name)
            else:
                print('Aborting operation')
                return
            
        else:
            for k in self.data.keys():
                if not self.validString(k):
                    print(f'Json key {k} doesnt follow correct nomenclature')
                    return
            self.append(json_data,class_name)
        if primary_key:
            del self.data[class_name]['id']
            prev_val = self.data[class_name][primary_key]
            new_val = prev_val.split('(')[0]+'(primary_key=True,editable=False)'
            self.data[class_name][primary_key] = new_val
            self.primary_keys[class_name] = primary_key
        else:
            self.primary_keys[class_name] = "id"
        
    def append(self,json_data,class_name):
        class_dic = {
            "id": "models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)",
            "created_on" : "models.DateTimeField(auto_now_add=True,editable=False)",
            "last_modified" : "models.DateTimeField(auto_now=True)"
        }
        for k,v in json_data.items():
            class_dic[str(k)] = self.variable_type_to_moodel_field[type(v)]
        self.data[class_name.title()] = class_dic

    def create_model_string(self):
        string_data = "from django.db import models\nimport uuid\n\n"
        for class_name,class_dic in self.data.items():
            string_data+=f'class {class_name.title()}(models.Model):\n'
            for k,v in class_dic.items():
                string_data+=f'\t{k} = {v}\n'
            string_data+='\n'
        return string_data
            
    def create_serialiser_string(self):
        string_data = "from rest_framework import serializers\n"
        string_data += "from .models import *\n\n"
        for class_name in self.data.keys():
            string_data+=f'class {class_name.title()}Serializer(serializers.ModelSerializer):\n'
            string_data+=f'\tclass Meta:\n'
            string_data+=f'\t\tmodel = {class_name}\n'
            string_data+=f"\t\tfields = '__all__'\n\n"
        return string_data
    
    def create_views_string(self):
        
        def check_existence(class_name):
            string_data = f"\t\ttry:\n"
            string_data += f"\t\t\t{class_name.lower()} = {class_name}.objects.get({self.primary_keys[class_name]}=pk)\n"
            string_data += f"\t\texcept:\n"
            string_data += f"\t\t\treturn Response({{'detail':'{class_name} does not exist.'}},status=status.HTTP_400_BAD_REQUEST)\n"
            return string_data
        
        def add_put_or_patch(class_name,partial):
            isPartial = "True" if partial else "False"
            fun_name = "patch" if partial else "put"
            string_data = f"\tdef {fun_name}(self,request,pk):\n"
            string_data += check_existence(class_name)
            string_data += "\t\tdata = request.data\n"
            string_data += f"\t\tserialized = {class_name}Serializer({class_name.lower()},data=data,partial={isPartial})\n"
            string_data += f"\t\tif serialized.is_valid():\n"
            string_data += f"\t\t\tserialized.save()\n"
            string_data += f"\t\t\treturn self.get(request=request,pk=pk)\n"
            string_data += f"\t\treturn Response({{'detail':'Some error occured check field names'}},status=status.HTTP_400_BAD_REQUEST)\n\n"
            return string_data
        
        string_data = "from rest_framework.decorators import api_view\n"
        string_data += "from rest_framework.views import APIView\n"
        string_data += "from rest_framework.response import Response\n"
        string_data += "from rest_framework import status\n"
        string_data += "from .models import *\n"
        string_data += "from .serializers import *\n\n"
        for class_name in self.data.keys():
            string_data += "@api_view(['GET'])\n"
            string_data += f"def get_all_{class_name.lower()}(request):\n"
            string_data += f"\t{class_name.lower()}s = {class_name}.objects.all()\n"
            string_data += f"\tserialized = {class_name}Serializer({class_name.lower()}s,many=True)\n"
            string_data += f"\treturn Response(serialized.data,status=status.HTTP_200_OK)\n\n"
            string_data += "@api_view(['POST'])\n"
            string_data += f"def create_{class_name.lower()}(request):\n"
            string_data += "\tdata = request.data\n"
            if self.primary_keys[class_name]=="id":
                string_data += f"\t{class_name.lower()} = {class_name}.objects.create()\n"
            else:
                string_data += "\ttry:\n"
                string_data += f"\t\t{class_name.lower()} = {class_name}.objects.create({self.primary_keys[class_name]}=data['{self.primary_keys[class_name]}'])\n"
                string_data += "\texcept:\n"
                string_data += f"\t\treturn Response({{'detail':'{self.primary_keys[class_name]} should be prvided to create {class_name}'}},status=status.HTTP_400_BAD_REQUEST)\n"
            string_data += f"\tserialized = {class_name}Serializer({class_name.lower()},data=data,partial=True)\n"
            string_data += f"\tif serialized.is_valid():\n"
            string_data += f"\t\tserialized.save()\n"
            string_data += f"\t\treturn Response(serialized.data,status=status.HTTP_200_OK)\n\n"
            string_data += f"\treturn Response({{'detail':'Some error occured check field names'}},status=status.HTTP_400_BAD_REQUEST)\n\n"
            string_data += f"class {class_name}APIView(APIView):\n"
            string_data += f"\tdef get(self,request,pk):\n"
            string_data += check_existence(class_name)
            string_data += f"\t\tserialized = {class_name}Serializer({class_name.lower()},many=False)\n"
            string_data += f"\t\treturn Response(serialized.data,status=status.HTTP_200_OK)\n\n"
            string_data += add_put_or_patch(class_name,False)
            string_data += add_put_or_patch(class_name,True)
            string_data += "\tdef delete(self,request,pk):\n"
            string_data += check_existence(class_name)
            string_data += "\t\ttry:\n"
            string_data += f"\t\t\t{class_name.lower()}.delete()\n"
            string_data += "\t\t\treturn Response({'Message':'Deleted Successfully'},status=status.HTTP_200_OK)\n"
            string_data += "\t\texcept:\n"
            string_data += "\t\t\treturn Response({'detail':'Some error occured while deleting'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)\n\n"
        return string_data
    
    def create_urls_string(self):
        string_data = "from django.urls import path\nfrom . import views\n\n"
        string_data += "urlpatterns = [\n"
        for class_name in self.data.keys():
            string_data += f"\tpath('{class_name.lower()}',views.get_all_{class_name.lower()}),\n"
            string_data += f"\tpath('{class_name.lower()}/create',views.create_{class_name.lower()}),\n"
            string_data += f"\tpath('{class_name.lower()}/<slug:pk>',views.{class_name}APIView.as_view()),\n"
        string_data += ']'
        return string_data