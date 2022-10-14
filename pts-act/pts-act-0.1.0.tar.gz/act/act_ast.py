import textwrap


class ActDefinition:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def __repr__(self):
        return '<ActDefinition {}: {}>'.format(self.name, self.value)


class ActStatement:
    def __init__(self, statement=None):
        self.statement = statement

    def __repr__(self):
        return '<ActStatement {}>'.format(self.statement)


class ActBlock:
    def __init__(self, name=None, condition=None, contents=None):
        self.name = name
        self.condition = condition
        self.contents = contents

        self.data = {}
        for step in contents:
            if isinstance(step, ActDefinition):
                self.data[step.name] = step.value

    def __repr__(self):
        if self.condition:
            res = '<ActBlock {}: {}\n'.format(self.name, self.condition)
        else:
            res = '<ActBlock {}\n'.format(self.name)
        for c in self.contents:
            sub = repr(c)
            res += textwrap.indent(sub, '  ') + '\n'
        return res + '>'


class ActCondition:
    def __init__(self, a=None, b=None, method=None):
        self.a = a
        self.b = b
        self.method = method

    def __repr__(self):
        return '<ActCondition {} {} {}>'.format(self.a, self.method, self.b)


class ActReference:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<ActReference {}>'.format(self.name)
