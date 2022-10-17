import asana
import json
import os
# import request
import pandas as pd
import time
pd.options.display.width = 0

# pandas set max column width
pd.set_option('display.max_colwidth', 75)


def user_select_option(message, options):
    option_lst = list(options)
    print_(message)
    for i, val in enumerate(option_lst):
        print_(i, ': ' + val['name'])
    index = int(input("Enter choice (default 0): ") or 0)
    return option_lst[index]

def get_client():
    with open(os.path.expanduser('~/.dt_config.json')) as f:
        config = json.load(f)
        api_key = config['asana_api_key']
        
    # create asana client
    client = asana.Client.access_token(api_key)
    return client


def asana_list_todos(workspace_name,filtering):
    if filtering is None: filtering = 'due'
    
    df = asana_get_todos(workspace_name,filtering)
    df = df[['gid','name',"due_on", "completed", "notes"]] # projects
    
    if filtering == 'done':
        df = df[df['completed'] == True]
        print(df)
        
    if filtering == 'due':
        df = df[df['completed'] == False]
        print(df)
    
    if filtering == 'all':
        print(df)
        
    if filtering == 'everyone':
        df = asana_get_todos(workspace_name,filtering)
        print(df)
        
def asana_get_todos(workspace_name,filtering):
     # read api key from ~/.dt_config.json
    client = get_client()
    (url, state) = client.session.authorization_url()
        
    me = client.users.me()
    workspace_id = me['workspaces'][0]['gid']
    
    # {'param': 'value', 'param': 'value'}
    # https://developers.asana.com/docs/get-tasks-from-a-project
    # print requests that python is making

    opt_fields='name,due_on,completed,projects,notes'
    if filtering!='everyone':
        tasks = list(client.tasks.find_all({"opt_fields":opt_fields}, 
                                           workspace=workspace_id, assignee='me'))
    else:
        project_id = list(client.projects.get_projects_for_workspace(workspace_id))[0]['gid']
        tasks = list(client.tasks.find_all({"opt_fields":opt_fields, "project_id": project_id}, 
                                           project=project_id))
    df = pd.DataFrame(tasks)
    return df
    
def add_todo(task_text, expected_duration, workspace_id, project_name):
    tm = time.localtime()
    
    if expected_duration is None:
        tar_date = f"{tm.tm_year}-{tm.tm_mon:02d}-{tm.tm_mday+1:02d}"
    else:
        day = tm.tm_mday+int(expected_duration)
        tar_date = f"{tm.tm_year}-{tm.tm_mon:02d}-{day:02d}"
    
    
    client = get_client()
    me = client.users.me()
    
    if workspace_id is None: workspace_id = me['workspaces'][0]['gid']
    
    
    projects = list(client.projects.get_projects_for_workspace(workspace_id))
    if project_name is 0:
        # here project_name is id
        project_id = projects[int(project_name)]['gid']
    else:
        project_name = 'Daily'
        project_id = [ w['gid'] for w in projects if w['name'] == project_name][0]
        
    # docs https://developers.asana.com/docs/create-a-task
        
    data =  {'name': task_text,
        "resource_subtype": "default_task",
        "assignee": me['gid'],
        "due_on": tar_date,
        "projects": project_id,
        # 'notes': 'Note: This is a test task created with the python-asana client.',
        # 'projects': [workspace_id]
    }
    
    if project_name == '-1':
        del data['projects']
        
    print("posting", data)
    result = client.tasks.create_in_workspace(workspace_id, data)

    print(json.dumps(result, indent=4))
    
def done_todo(task_id):
    client = get_client()
    data =  {'completed': True}
    result = client.tasks.update_task(task_id, data)
    print(json.dumps(result, indent=4))

def fix_past_due(workspace_name):
    df = asana_get_todos(workspace_name,None)
    client = get_client()
    
    # select all that are past due
    df = df[df['completed'] == False]
    df = df[df['due_on'].notnull()]
    df['due_on'] = pd.to_datetime(df['due_on'])
    df = df[df['due_on'] < pd.Timestamp.today()]
    
    # asana update task to today
    all_tasks = []
    
    for i in df.index:
        task_id = df.loc[i,'gid']
        data =  {'due_on': pd.Timestamp.today().strftime("%Y-%m-%d")}
        result = client.tasks.update_task(task_id, data)
        # print(json.dumps(result, indent=4))
        all_tasks.append(result)
        
    df = pd.DataFrame(all_tasks)
    cols = ['gid', 'completed', 'due_on', 'name', 'notes']
    print(df[cols])