
import pprint
import xml.etree.ElementTree as et

from contextlib import redirect_stdout


class Node:
    """
    """

    def __init__(self, value=None):

        if not value:
            raise Exception("Node should have value.")
        
        self.value = value
        self.children = []
    
    def __repr__(self):

        return str(self.value)
    
    def add_child(self, child):

        self.children.append(child)


class Graph:
    """
    """

    def __init__(self, root=None):
        
        if not root:
            raise Exception("Graph should have root node.")
        
        if not isinstance(root,Node):
            raise Exception("Graph root should be Node instance.")

        self.root = root

    def bfs(self):

        self.visited = []
        self.queue = []
        self.result = []

        self.visited.append(self.root)
        self.queue.append(self.root)

        while self.queue:
            
            tmp = self.queue.pop(0)
            self.result.append(tmp)
            
            for child in tmp.children:
                if child not in self.visited:
                    self.visited.append(child)
                    self.queue.append(child)
        
        return self.result


class UML2CODE:
    """
    """

    models = {}

    root = Node('root')
    graph = Graph(root)

    def __create_model(self, model_id):

        self.models[model_id] = {}
        self.models[model_id]['attrs'] = []
        self.models[model_id]['parents'] = []
        self.models[model_id]['relations'] = []
        self.models[model_id]['children'] = []

    def build_deps(self):
        """
        """

        for key, model in self.models.items():
            
            model_node = Node(key)

            if not model['parents']:
                self.root.add_child(model_node)
            
            if model['children']:
                for child in model['children']:
                    child_node = Node(child)
                    model_node.add_child(child_node)

    def export(self):
        """
        """

        with open('exported.json', 'w') as f:
            with redirect_stdout(f):
                pprint.pprint(self.models)
                
    def write(self):
        """
        """

        file = open('result.py', 'w')
        
        file.write('from django.db import models\n')
        file.write('from django.utils.translation import gettext as _\n')
        file.write('\n')
        
        for key in self.graph.bfs()[1:]:
            
            model = self.models[key.value]
            print(model)
            
            class_text = f'\nclass { model["label"] }'
            file.write(class_text)

            if model['parents']:
                
                parent_ids = list(map(lambda x: self.models[x]['label'], model['parents']))
                parent_label = ', '.join(parent_ids)
                file.write('(')
                file.write(parent_label)
                file.write(')')
            
            else:

                class_text = '(models.Model)'
                file.write(class_text)

            class_text = ':\n'
            file.write(class_text)
            
            if model['attrs']:

                file.write('\n')

                for attr in model['attrs']:

                    name = attr['label'].split(':')[0].strip()
                    type = attr['label'].split(':')[1].strip()
                    file.write('    ')
                    attr_text = f"{ name } = models.{ type }()\n"
                    file.write(attr_text)
            
            if model['relations']:
                
                file.write('\n')

                for relation in model['relations']:
                    
                    relation_text = f"{ relation['label'] } = models.RelationField('{ self.models[relation['target']]['label'] }')\n"
                    file.write('    ')
                    file.write(relation_text)
            

            if not model['attrs'] and not model['relations']:
                
                file.write('    pass')
            
            file.write('\n')
            
        file.close()



    def parse(self):
        """
        """
        
        tree = et.parse('exported.xml')
        iter = tree.iter()

        for node in iter:

            attributes = node.attrib
            
            if 'type' in attributes:

                if attributes['type'] == 'model':
                    
                    model_id = attributes.pop('id', None)

                    if model_id not in self.models:

                        self.__create_model(model_id)
                    
                    self.models[model_id]['label'] = attributes['label']

                if attributes['type'] == 'attribute':
                    
                    child = node.find('mxCell')

                    if child:
                        
                        parent_id = child.attrib.pop('parent', None)

                        if parent_id not in self.models:

                            self.__create_model(parent_id)

                        self.models[parent_id]['attrs'].append(attributes)
                
                if attributes['type'] == 'inheritance':

                    child = node.find('mxCell')

                    if child:
                        
                        source_id = child.attrib.pop('source', None)
                        target_id = child.attrib.pop('target', None)

                        if target_id not in self.models:
                            
                            self.__create_model(target_id)
                        
                        if source_id not in self.models:
                            
                            self.__create_model(source_id)

                        self.models[source_id]['parents'].append(target_id)
                        self.models[target_id]['children'].append(source_id)
                
                if attributes['type'] == 'relation':

                    child = node.find('mxCell')

                    if child:

                        source_id = child.attrib.pop('source', None)
                        target_id = child.attrib.pop('target', None)

                        if source_id not in self.models:
                            
                            self.__create_model(source_id)

                        if target_id not in self.models:
                            
                            self.__create_model(target_id)
                            
                        attributes['target'] = target_id
                        
                        self.models[source_id]['relations'].append(attributes)
                """
                else:

                    label = node.attrib.pop('label', None)
                    parent_id = node.attrib.pop('parent', None)

                    if not label and parent_id:

                        self.relations[parent_id]['attr'] = label
                """


if __name__ == '__main__':
    
    uml2code = UML2CODE()
    uml2code.parse()
    #uml2code.export()
    uml2code.build_deps()
    #uml2code.show()
    uml2code.write()