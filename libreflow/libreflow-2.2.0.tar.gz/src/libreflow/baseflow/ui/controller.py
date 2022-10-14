import six
import sys


FILE_TYPE_NAMES = ['Inputs', 'Outputs', 'Works']


def get_icon_ref(icon_name, resource_folder='icons.flow'):
    if isinstance(icon_name, six.string_types):
        icon_ref = (resource_folder, icon_name)
    else:
        icon_ref = icon_name

    return icon_ref


class RevisionData:
    '''
    File revision data to be used by the task view.
    '''

    def __init__(self, session, oid, site_names):
        self.session = session
        self.oid = oid
        self.name = oid.split('/')[-1]
        properties = self.session.cmds.Flow.call(
            oid, 'get_properties', ['user', 'comment', 'date'], {}
        )
        self.data = [
            properties['user'],
            properties['comment'],
            properties['date'],
        ]
        exchange_status = self.session.cmds.Flow.call(
            oid, 'get_sync_status', [], dict(exchange=True)
        )
        self.statutes = [exchange_status] + [
            self.session.cmds.Flow.call(
                oid, 'get_sync_status', [name], {}
            )
            for name in site_names
        ]


class HistoryData:
    '''
    File history data to be used by the task view.
    '''

    def __init__(self, session, file_oid, site_names):
        self.revisions = [
            RevisionData(session, oid, site_names)
            for oid in reversed(
                session.cmds.Flow.get_mapped_oids(file_oid+'/history/revisions')
            )
        ]


class ActionData:
    '''
    Task action data to be used by the task view.
    '''

    def __init__(self, oid, ui):
        self.oid = oid
        self.icon = get_icon_ref(ui['icon'])
        self.label = ui['label'] or oid.rsplit('/', 1)[-1].replace('_', ' ').title()
        self.tooltip = ui['tooltip']


class FileData:
    '''
    Task file data to be used by the task view.
    '''
    
    def __init__(self, session, oid, activate_oid=None):
        self.session = session
        self.oid = oid
        self.label = self.session.cmds.Flow.get_value(oid+'/display_name')
        self.icon = get_icon_ref(self.session.cmds.Flow.call(oid, 'get_icon', [], {}))
        self.main_actions = None
        self.secondary_actions = None
        self.activate_oid = activate_oid
    
    def update_actions(self):
        display_order = self.session.cmds.Flow.get_value(self.oid+'/action_display_order') or {}
        visible_count = self.session.cmds.Flow.get_value(self.oid+'/visible_action_count') or 0

        # Sort actions by display priority
        actions = sorted(
            self.session.cmds.Flow.get_object_actions(self.oid),
            key=lambda a: display_order.get(a[2][0], sys.maxsize)
        )
        
        self.main_actions = [
            ActionData(a[3]['oid'], a[3]['ui'])
            for a in actions[:visible_count]
        ]
        self.secondary_actions = [
            ActionData(a[3]['oid'], a[3]['ui'])
            for a in actions[visible_count:]
        ]


class TaskData:
    '''
    Task data to be used by the task view.
    '''

    def __init__(self, session, oid):
        self.session = session
        self.oid = oid
        self.label = self.session.cmds.Flow.call(oid, 'get_display_name', [], {})
        self.icon = get_icon_ref(self.session.cmds.Flow.call(oid, 'get_icon', [], {}))
        self.color = self.session.cmds.Flow.call(oid, 'get_color', [], {})
        self.actions = None
        self.update_files()
        self.update_actions()
    
    def update_files(self):
        self.files = {n: [] for n in FILE_TYPE_NAMES}
        
        for oid in self.session.cmds.Flow.get_mapped_oids(self.oid+'/files'):
            _type = self.session.cmds.Flow.get_value(oid+'/file_type') or 'Works'
            activate_oid = self.session.cmds.Flow.call(oid, 'activate_oid', [], {}) or None
            self.files[_type].append(FileData(self.session, oid, activate_oid))
    
    def update_actions(self):
        self.actions = [
            ActionData(a[3]['oid'], a[3]['ui'])
            for a in self.session.cmds.Flow.get_object_actions(self.oid)
            if not a[3]['ui']['hidden']
        ]


class Controller:

    def __init__(self, task_widget):
        self.task_widget = task_widget
        self.session = task_widget.session
        self.oid = task_widget.oid
        self.cache = None
        self.selected = None
        self.selected_history = None
        self.site_names = None
        self.exchange_name = None

        self.statutes_section = None
        self.history_sections = ['Revision', 'User', 'Comment', 'Date']

        self.update_cache()
    
    def task_label(self):
        return self.cache.label
    
    def task_icon(self):
        return self.cache.icon
    
    def task_color(self):
        return self.cache.color
    
    def task_file_count(self, file_type):
        return len(self.cache.files[file_type])
    
    def task_actions(self):
        return self.cache.actions
    
    def file_data(self, file_type, row):
        return self.cache.files[file_type][row]
    
    def selected_file(self):
        return self.selected
    
    def update_selected(self, file_type, row):
        # Clear selection of file lists of other types
        for _type in FILE_TYPE_NAMES:
            if _type != file_type:
                self.task_widget.view.file_lists.clear_list_selection(_type)
        
        # Invalidate history qmodel before updating cache
        self.task_widget.view.file_view.beginResetHistoryModel()
        self.selected = self.cache.files[file_type][row]
        self.selected_history = HistoryData(self.session, self.selected.oid, self.site_names)
        self.task_widget.view.file_view.endResetHistoryModel()
        self.task_widget.view.file_view.update()
        self.task_widget.view.file_view.setVisible(True)
    
    def clear_selected(self):
        # Check if an item is selected (selection already cleared or task view not yet instanciated otherwise)
        if self.selected is not None:
            self.task_widget.view.file_view.setVisible(False)
            self.task_widget.view.file_lists.clear_selection()
    
    def file_history_header(self, column):
        return self.history_sections[column]
    
    def file_statutes_header(self, column):
        return self.statutes_section[column]
    
    def selected_file_revision_count(self):
        if self.selected is not None:
            return len(self.selected_history.revisions)
        
        return 0
    
    def selected_file_revision_data(self, row, column=None):
        if self.selected is not None:
            data = self.selected_history.revisions[row]
            if column is None:
                return data
            elif column == 0:
                return data.name
            else:
                return data.data[column - 1]
        
        return None
    
    def selected_file_revision_status(self, row, column):
        if self.selected is not None:
            if column == 0:
                return self.selected_history.revisions[row].name
            else:
                return self.selected_history.revisions[row].statutes[column - 1]
        
        return None
    
    def toggle_file_statutes(self):
        if self.task_widget.view.file_view.isVisible():
            self.task_widget.view.file_view.toggle_file_statutes()
    
    def update_cache(self):
        self.cache = TaskData(self.session, self.oid)
        self.site_names = self.working_site_names()
        self.exchange_name = self.exchange_site_name()
        self.statutes_section = ['Revision', self.exchange_name] + self.site_names

    def working_site_names(self):
        return self.session.cmds.Flow.call(
            '/'+self.oid.split('/')[1]+'/admin/multisites/working_sites',
            'mapped_names', [], {}
        )
    
    def exchange_site_name(self):
        return self.session.cmds.Flow.get_value(
            '/'+self.oid.split('/')[1]+'/admin/multisites/exchange_site_name'
        )
    
    def site_count(self):
        return len(self.site_names) + 1
    
    def show_action_dialog(self, action_oid):
        self.task_widget.page.show_action_dialog(action_oid)
    
    def goto(self, oid):
        self.task_widget.page.goto(oid)
    # def get_file_display_name(self, file_type, row):
    #     oids = self.get_task_file_oids()
    #     # print(column)
    #     return self.cache[file_type].get(row, FileCache(self.session, oid))
    #     return self.session.cmds.Flow.get_value(oids[column]+'/display_name')

    # def get_task_file_oids(self):
    #     return self.session.cmds.Flow.get_mapped_oids(self.oid+'/files')
    
    # def get_file_type(self, oid):
    #     return self.session.cmds.Flow.get_value(oid+'/file_type')
