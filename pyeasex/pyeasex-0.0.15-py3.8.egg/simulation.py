class Task():
  def __init__(self, project_uuid, api, task_data=None):
    self.project_uuid = project_uuid
    self.api = api
    self.task_data = task_data
    self.output = {}

  def prepare(self):
    pass

  def run(self):
    pass

  def complete(self):
    pass

  def get_output(self):
    return self.output

  def terminate(self, exception_code):
    pass