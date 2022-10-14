import os,subprocess,time,json

import os,subprocess,time,sys,django,json


def mq_init(base_url):
    file_path = os.path.join(base_url,'models.py')
    fp = open(file_path,'r')
    if 'DB_django_task_mq' in fp.read():
        print('已执行过该初始化，请不要重复执行，或删除掉models.py中的DB_django_task_mq类再执行！')
        fp.close()
        exit()
    fp = open(file_path,'a+')
    fp.writelines(['\n'*4,'class DB_django_task_mq(models.Model):','\n    topic = models.CharField(max_length=100,null=True,blank=True,default="")',
                   '\n    message = models.TextField(default="{}")','\n    status = models.BooleanField(default=True)','\n    def __str__(self):','\n        return self.topic'])
    fp.close()
    file_path = os.path.join(base_url,'admin.py')
    fp = open(file_path,'a+')
    fp.writelines(['\n'*4,'admin.site.register(DB_django_task_mq)'])
    fp.close()
    time.sleep(0.5)
    mp = os.path.join(base_url,'..','manage.py')
    subprocess.call('python3 %s makemigrations'%mp,shell=True)
    subprocess.call('python3 %s migrate'%mp,shell=True)

def mq_producer(base_url,topic,message,DB_django_task_mq):
    sys.path.append(base_url)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pressure.settings')
    django.setup()
    DB_django_task_mq.objects.create(topic=topic,message=json.dumps(message))

def mq_consumer(base_url,fun,DB_django_task_mq,topic):
    sys.path.append(base_url)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pressure.settings')
    django.setup()
    while True:
        time.sleep(1)
        mq = DB_django_task_mq.objects.filter(status=True,topic=topic).first()
        if mq:
            print('开始执行------:',mq.id,mq.topic,mq.message)
            mq.status = False
            mq.save()
            fun(mq.message)
            mq.delete()
            print('执行完毕')
        else: print('已无任务...')
