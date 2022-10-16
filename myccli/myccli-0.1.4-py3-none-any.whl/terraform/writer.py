import contextlib
import json
from typing import Optional, Dict, List

from myccli.terraform import TerraformItem
from myccli.terraform.resources import TerraformResource
from myccli.terraform.provider import TerraformProvider, AWSTerraformProvider
from myccli.terraform.common import JSONDocument, InlineBlock, ETFCall, ETF, ETFRawRef, TaggedInlineBlock, \
    JSONDocumentList

INDENT_SIZE = 2


def is_cname(s: str):
    return s.replace('_', '').isalnum()


class TerraformWriter:
    def __init__(self, f):
        self._f = f
        self._indent = 0
        self._should_pad = False
        self._json_depth = 0

    def write_indent(self):
        self._f.write(' ' * (self._indent * INDENT_SIZE))

    def write_line(self, s: Optional[str] = None, nl=True):
        s = s or ''
        self.write_indent()
        self._f.write(s + ('\n' if nl else ''))

    def write_arg_value(self, value: any, nl=False):
        if type(value) is int:
            self._f.write(str(value) + ('\n' if nl else ''))
            self._should_pad = False
        elif type(value) is str:
            self._f.write(f'"{value}"' + ('\n' if nl else ''))
            self._should_pad = False
        elif type(value) is bool:
            self._f.write(('true' if value else 'false') + ('\n' if nl else ''))
            self._should_pad = False
        elif isinstance(value, (JSONDocument, JSONDocumentList)):
            if isinstance(value, JSONDocument):
                start_delim, end_delim = '{', '}'
            else:
                start_delim, end_delim = '[', ']'
            self._f.write(f'jsonencode({start_delim}\n' if self._json_depth == 0 else f'{start_delim}\n')
            self._indent += 1
            self._json_depth += 1

            if isinstance(value, JSONDocument):
                for k, v in value.items():
                    self.write_arg(k, v)
            else:
                for v in value:
                    self.write_indent()
                    self.write_arg_value(v)
                    self._f.write(',\n')

            self._indent -= 1
            self._json_depth -= 1
            self.write_line(f'{end_delim})' if self._json_depth == 0 else end_delim, nl=nl)
            self._should_pad = True
        elif isinstance(value, (dict, InlineBlock, TaggedInlineBlock)):
            if isinstance(value, TaggedInlineBlock):
                self._f.write(' '.join(f'"{tag}"' for tag in value.tags) + ' ')

            self._f.write('{\n')
            self._indent += 1
            self._should_pad = False

            args = value.block if isinstance(value, TaggedInlineBlock) else value
            for k, v in args.items():
                self.write_arg(k, v)

            self._indent -= 1
            self.write_line('}', nl=nl)
            self._should_pad = True
        elif isinstance(value, list):
            self._f.write('[\n')
            self._indent += 1

            for v in value:
                self.write_line('', nl=False)
                self.write_arg_value(v, nl=False)
                self._f.write(',\n')

            self._indent -= 1
            self.write_line(']', nl=nl)
            self._should_pad = True
        elif isinstance(value, ETFCall):
            self._f.write(value.target + '(')
            for i, arg in enumerate(value.args):
                self.write_arg_value(arg, nl=False)
                if i != len(value.args) - 1:
                    self._f.write(', ')
            self._f.write(')' + ('\n' if nl else ''))
            self._should_pad = False
        elif isinstance(value, ETF):
            self._f.write(value.render() + ('\n' if nl else ''))
            self._should_pad = False
        elif isinstance(value, TerraformResource):
            self._f.write(value.get_self_ref().render() + ('\n' if nl else ''))
            self._should_pad = False
        else:
            raise NotImplementedError

    def write_arg(self, name: str, value: any):
        if not is_cname(name.strip()):
            name = f'"{name}"'

        if isinstance(value, list) and value and all(isinstance(v, (InlineBlock, TaggedInlineBlock)) for v in value):
            for block in value:
                self.write_arg(name, block)
            return

        if self._should_pad:
            self.write_line()

        if isinstance(value, (InlineBlock, TaggedInlineBlock)):
            prefix = name.strip() + ' '
        else:
            prefix = f'{name} = '

        self.write_line(prefix, nl=False)
        self.write_arg_value(value, nl=True)

    def write_args(self, **args: Dict[str, any]):
        if len(args) == 0:
            return

        max_len = max(len(k) for k in args.keys())

        sorted_items = sorted(args.items(), key=lambda p: p[0])
        sorted_items.sort(key=lambda p: isinstance(p[1], (InlineBlock, TaggedInlineBlock)))

        for k, v in sorted_items:
            self.write_arg(k + ' ' * (max_len - len(k)), v)

    def start_block(self, kind: str, *labels):
        if self._should_pad:
            self.write_line()

        str_labels = [f'"{label}"' for label in labels]
        self.write_line(f'{kind} {" ".join(str_labels) + " " if labels else ""}{{')
        self._indent += 1
        self._should_pad = False

    def end_block(self):
        self._indent -= 1
        self.write_line('}')
        self._should_pad = True

    @contextlib.contextmanager
    def in_block(self, kind: str, *labels):
        self.start_block(kind, *labels)
        try:
            yield
        finally:
            self.end_block()

    def _write_required_providers(self, providers: List[TerraformProvider]):
        if not providers:
            return

        if providers:
            with self.in_block('required_providers'):
                for p in providers:
                    self.write_arg(p.name, {
                        'source': p.source,
                        'version': p.version,
                    })

    def write_terraform_block(self, required_version: str, providers: List[TerraformProvider]):
        with self.in_block('terraform'):
            self._write_required_providers(providers)
            self.write_arg('required_version', required_version)

    def write_provider_block(self, provider: TerraformProvider):
        with self.in_block('provider', provider.name):
            if isinstance(provider, AWSTerraformProvider):
                self.write_arg('region', provider.region)
            else:
                pass

    def write_item_block(self, item: TerraformItem):
        prefix = 'resource' if isinstance(item, TerraformResource) else 'data'
        with self.in_block(prefix, item.kind, item.tf_name):
            all_args = dict(item.get_args())

            if item.lifecycle:
                assert 'lifecycle' not in all_args
                all_args['lifecycle'] = InlineBlock(item.lifecycle.to_dict())

            if item.dependencies:
                assert 'depends_on' not in all_args
                all_args['depends_on'] = list(map(ETFRawRef, item.dependencies))

            self.write_args(**all_args)
