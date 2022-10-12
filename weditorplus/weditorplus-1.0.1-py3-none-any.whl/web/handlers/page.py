# coding: utf-8
#

import base64
import io
import json
import os
import traceback

import tornado
from logzero import logger
from PIL import Image
from tornado.escape import json_decode

from ..device import connect_device, get_device
from ..version import __version__

import requests
pathjoin = os.path.join


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Credentials",
                        "true")  # allow cookie
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, DELETE, OPTIONS')

    def options(self, *args):
        self.set_status(204)  # no body
        self.finish()

    def check_origin(self, origin):
        """ allow cors request """
        return True


class VersionHandler(BaseHandler):
    def get(self):
        ret = {
            'name': "weditor",
            'version': __version__,
        }
        self.write(ret)


class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")


class DeviceConnectHandler(BaseHandler):
    def post(self):
        platform = self.get_argument("platform").lower()
        device_url = self.get_argument("deviceUrl")

        try:
            id = connect_device(platform, device_url)
        except RuntimeError as e:
            self.set_status(500)
            self.write({
                "success": False,
                "description": str(e),
            })
        except Exception as e:
            logger.warning("device connect error: %s", e)
            self.set_status(500)
            self.write({
                "success": False,
                "description": traceback.format_exc(),
            })
        else:
            ret = {
                "deviceId": id,
                'success': True,
            }
            if platform == "android":
                ws_addr = get_device(id).device.address.replace("http://", "ws://") # yapf: disable
                ret['screenWebSocketUrl'] = ws_addr + "/minicap"
            self.write(ret)


class DeviceHierarchyHandler(BaseHandler):
    def get(self, device_id):
        d = get_device(device_id)
        self.write(d.dump_hierarchy())


class DeviceHierarchyHandlerV2(BaseHandler):
    def get(self, device_id):
        d = get_device(device_id)
        self.write(d.dump_hierarchy2())


class WidgetPreviewHandler(BaseHandler):
    def get(self, id):
        self.render("widget_preview.html", id=id)


class DeviceWidgetListHandler(BaseHandler):
    __store_dir = os.path.expanduser("~/.weditor/widgets")

    def generate_id(self):
        os.makedirs(self.__store_dir, exist_ok=True)
        names = [
            name for name in os.listdir(self.__store_dir)
            if os.path.isdir(os.path.join(self.__store_dir, name))
        ]
        return "%05d" % (len(names) + 1)

    def get(self, widget_id: str):
        print("widget_id:::",widget_id)
        data_dir = os.path.join(self.__store_dir, widget_id)
        with open(pathjoin(data_dir, "hierarchy.xml"), "r",
                  encoding="utf-8") as f:
            hierarchy = f.read()

        with open(os.path.join(data_dir, "meta.json"), "rb") as f:
            meta_info = json.load(f)
            meta_info['hierarchy'] = hierarchy
            self.write(meta_info)

    def json_parse(self, source):
        with open(source, "r", encoding="utf-8") as f:
            return json.load(f)

    def put(self, widget_id: str):
        """ update widget data """

        data = json_decode(self.request.body)
        target_dir = os.path.join(self.__store_dir, widget_id)
        with open(pathjoin(target_dir, "hierarchy.xml"), "w",
                  encoding="utf-8") as f:
            f.write(data['hierarchy'])

        # update meta
        meta_path = pathjoin(target_dir, "meta.json")
        meta = self.json_parse(meta_path)
        meta["xpath"] = data['xpath']
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(meta, indent=4, ensure_ascii=False))

        self.write({
            "success": True,
            "description": f"widget {widget_id} updated",
        })

    def post(self):
        data = json_decode(self.request.body)
        widget_id = self.generate_id()
        target_dir = os.path.join(self.__store_dir, widget_id)
        os.makedirs(target_dir, exist_ok=True)

        image_fd = io.BytesIO(base64.b64decode(data['screenshot']))
        im = Image.open(image_fd)
        im.save(pathjoin(target_dir, "screenshot.jpg"))

        lx, ly, rx, ry = bounds = data['bounds']
        im.crop(bounds).save(pathjoin(target_dir, "template.jpg"))

        cx, cy = (lx + rx) // 2, (ly + ry) // 2
        # TODO(ssx): missing offset
        # pprint(data)
        widget_data = {
            "resource_id": data["resourceId"],
            "text": data['text'],
            "description": data["description"],
            "target_size": [rx - lx, ry - ly],
            "package": data["package"],
            "activity": data["activity"],
            "class_name": data['className'],
            "rect": dict(x=lx, y=ly, width=rx-lx, height=ry-ly),
            "window_size": data['windowSize'],
            "xpath": data['xpath'],
            "target_image": {
                "size": [rx - lx, ry - ly],
                "url": f"http://localhost:17311/widgets/{widget_id}/template.jpg",
            },
            "device_image": {
                "size": im.size,
                "url": f"http://localhost:17311/widgets/{widget_id}/screenshot.jpg",
            },
            # "hierarchy": data['hierarchy'],
        } # yapf: disable

        with open(pathjoin(target_dir, "meta.json"), "w",
                  encoding="utf-8") as f:
            json.dump(widget_data, f, ensure_ascii=False, indent=4)

        with open(pathjoin(target_dir, "hierarchy.xml"), "w",
                  encoding="utf-8") as f:
            f.write(data['hierarchy'])

        self.write({
            "success": True,
            "id": widget_id,
            "note": data['text'] or data['description'],  # 备注
            "data": widget_data,
        })


class DeviceScreenshotHandler(BaseHandler):
    def get(self, serial):
        logger.info("Serial: %s", serial)
        try:
            d = get_device(serial)
            buffer = io.BytesIO()
            d.screenshot().convert("RGB").save(buffer, format='JPEG')
            b64data = base64.b64encode(buffer.getvalue())
            response = {
                "type": "jpeg",
                "encoding": "base64",
                "data": b64data.decode('utf-8'),
            }
            self.write(response)
        except EnvironmentError as e:
            traceback.print_exc()
            self.set_status(500, "Environment Error")
            self.write({"description": str(e)})
        except RuntimeError as e:
            self.set_status(500)  # Gone
            self.write({"description": traceback.format_exc()})


class CaseEditHandler(BaseHandler):
    def post(self):

        # 获取serial

        # res = requests.get("http://localhost:17311/")

        # print(res.cookies)
        # serial = res.cookies["serial"]
        
        
        data = json_decode(self.request.body)
        seriel = data['serial']
        id = connect_device("android",seriel)
        d = get_device(id)

        print("data::::",data)
        page_dict = {}
        if data:
            file_path = data['file_path']
            json_file_save_dir = file_path if file_path[-1] =='/' else file_path +"/"
            img_file_save_dir = json_file_save_dir.replace("pages","data")+"element_picture"
            isExists=os.path.exists(img_file_save_dir)
            # 判断结果
            if not isExists:
                os.makedirs(img_file_save_dir) 
            page_dict["PageName"] = data['page_name']
            root_page = data['root_page']
            elements = data['elements']
            # 获取AppPackage，MainActivity
            packagename = elements[0][8]
            mainactivity = elements[0][5]
            # print(type(root_page))


            if root_page:
                page_dict["PageType"] = "Activity"
                page_dict["AppPackage"] = packagename
                page_dict["MainActivity"] = mainactivity
            else:
                page_dict["PageType"] = "Child"
            page_dict["Elements"] = {}
            for i in elements:

                img_status = i[12] if i[12] else "ON"
                # 保存元素对应的图片
                img_name = f"{img_file_save_dir}/{i[0]}_{img_status}.jpg"
                print(":",img_name)
                # d.screenshot(img_name)
                # image = d.screenshot() # default format="pillow"
                image = d._d.xpath(i[2]).screenshot()
                image.save(img_name) # or home.png. Currently, only png and jpg are supported
                page_dict["Elements"].update({
                    i[0]:{
                        "Description":i[1],
                        "Selector":"xpath=="+i[2],
                        "Text": i[3],
                        "Position":i[4],
                        "Activity":i[5],
                        "Index":i[6],
                        "Desc":i[7],
                        "Package":i[8],
                        "ResourceId":i[9],
                        "Coord":i[10],
                        "ClassName":i[11],
                        "Image":{
                            img_status:img_name,
                        }
                    }
                })
                # print("dd",page_dict,i)
            # 处理Function
            # 'functions': [[[None, 'FunctionName:dfdfed', 'None:', 'None:'], [None, 'LocalVar:dsfsf', 'GlobalVar:dfsdfs', 'None:'], [None, 'None:', 'None:', 'None:']], [[None, 'FunctionName:dfdfed', 'None:', 'None:'], [None, 'LocalVar:dsfsf', 'GlobalVar:dfsdfs', 'None:'], [None, 'None:', 'None:', 'None:']]]
            if data["functions"]:

                func_dict = {}
                for i in data["functions"]:
                    if "FunctionName" not in data["functions"][0]:
                        break
                    
                    function_dict = {}
                    function_dict["func_step"] = []
                    for j in i:
                        print("j::",j)
                        indent_cont = 0
                        tmp = {}
                        params = []
                        values = []
                        flag = False
                        for k in j[1:]:
                            print(k,type(k))
                            
                            if k and k !="None:":
                                flag = True
                                key,value = k.split(":")
                                tmp['Indent'] = indent_cont
                                if key =="FunctionName":
                                    function_dict["func_name"] = value       
                                
                                if key =="Param": 
                                    params.append(value)
                                elif key=="Value":
                                    values.append(value)
                                else:
                                    tmp[key] = value
                            else:
                                if not flag:
                                    indent_cont += 1
                        if values:
                            tmp["Value"] = values

                        if params:
                            tmp["Param"] = params

                        function_dict["func_step"].append(tmp)
                    
                    # 获取功能的参数
                    function_dict["func_param"] = function_dict["func_step"][0]["Param"] if function_dict["func_step"][0].get("Param") else []
                    # 去掉第一行 func_step
                    function_dict["func_step"] = function_dict["func_step"][1:]
                    func_dict[function_dict["func_name"]] = function_dict
                    # functions_list.append(function_dict)      
                    print("function_dict:",function_dict)
                        
            page_dict["Functions"] = func_dict

            # 处理父页面信息
            if data["parents"]:
                parent = data["parents"]
                page_dict["ParentPages"] ={
                    parent["select_parent_page"]:{
                        "Link": parent["select_parent_page"],
                        "Functions": [parent["select_parent_func"]],
                        "Params":parent["parms"]

                    }
                }




            
        print("page_dict::",page_dict)
        json_file_save_dir_file = json_file_save_dir + data['page_name']+".json"
        with open(json_file_save_dir_file,'w',encoding='utf-8') as f:
            json.dump(page_dict, f,ensure_ascii=False)
 
        response = {
                "success": "ok"      
            }
        self.write(response)
    
class GetFileInfoHandler(BaseHandler):
    def get(self):
        filedir = self.get_argument("file_path")
        # data = json_decode(self.request.body)
        # print(data)
        # filedirs = os.path.expanduser(filedir)
        # print(filedirs)
        page_list = []
        all_page_obj = []
        for name in os.listdir(filedir):
            print(name)
            page_list.append(name[:-5])
            with open(filedir+"/"+name,'r') as f:
                all_page_obj.append(json.load(f))
        
        response = {
                "success": "ok",
                "data":page_list,
                "all_page_obj":all_page_obj
            }
        self.write(response)
        


    