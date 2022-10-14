"""Generate type annotated python from SQL."""

from pprint import pprint
from importlib.resources import read_text

import black
from lark import Lark, Transformer, UnexpectedToken # type: ignore
from jinja2 import Template, StrictUndefined, TemplateSyntaxError


class SqlPyGenTransformer(Transformer):
    """Transform the parse tree for code generation."""

    CNAME = str
    MODULE_NAME = str
    RTYPE_OPT = str
    RETURN_OPT = str

    def SQL_STRING(self, t):
        return t.strip().rstrip(";").strip()

    def module(self, ts):
        (name,) = ts
        return ("module", name)

    def pname_ptype(self, ts):
        pname, ptype = ts
        return (pname, ptype)

    def params(self, ts):
        fn_params = [f"{pname}: {ptype}" for pname, ptype in ts]
        fn_params = ", ".join(fn_params)
        fn_params = "connection: ConnectionType, " + fn_params

        query_args = [f'"{pname}": {pname}' for pname, _ in ts]
        query_args = ", ".join(query_args)
        query_args = f"{{ {query_args} }}"

        explain_args = [f'"{pname}": None' for pname, _ in ts]
        explain_args = ", ".join(explain_args)
        explain_args = f"{{ {explain_args} }}"

        return (
            "params",
            {
                "fn_params": fn_params,
                "query_args": query_args,
                "explain_args": explain_args,
                "has_params": True,
            },
        )

    def rtype_opt(self, ts):
        rtype = ts[0]
        return f"Optional[{rtype}]"

    def rtype_not_opt(self, ts):
        rtype = ts[0]
        return rtype

    def returnone(self, ts):
        ts = ", ".join(ts)
        return_ = f"Optional[tuple[{ts}]]"

        return (
            "return_",
            {
                "return_": return_,
                "returns_one": True,
                "does_return": True,
            },
        )

    def returnmany(self, ts):
        ts = ", ".join(ts)
        return_ = f"Iterable[tuple[{ts}]]"

        return (
            "return_",
            {
                "return_": return_,
                "returns_one": False,
                "does_return": True,
            },
        )

    def schema(self, ts):
        name, sql = ts
        return ("schemas", {"name": name, "sql": sql})

    def query(self, ts):
        name, sql = ts[0], ts[-1]
        params = {
            "fn_params": "connection: ConnectionType",
            "query_args": None,
            "explain_args": None,
            "has_params": False,
        }
        return_ = {
            "return_": "None",
            "returns_one": None,
            "does_return": False,
        }
        for typ, val in ts[1:-1]:
            if typ == "params":
                params = val
            elif typ == "return_":
                return_ = val
            else:
                raise ValueError(f"Unexpected child type: {typ=} {val=}")

        return (
            "queries",
            {"name": name, "params": params, "return_": return_, "sql": sql},
        )

    def start(self, ts):
        ret = {
            "module": None,
            "schemas": [],
            "queries": [],
        }
        for grp, val in ts:
            if grp == "module":
                ret["module"] = val
            else:
                ret[grp].append(val)

        return ret


def get_parser() -> Lark:
    """Return the parser."""
    grammar = read_text("sqlpygen", "sqlpygen.lark")
    parser = Lark(grammar, parser="lalr")
    return parser


def get_template() -> Template:
    """Return the code generation template."""
    tpl_text = read_text("sqlpygen", "sqlpygen.jinja2")
    try:
        tpl_obj = Template(
            tpl_text, trim_blocks=True, lstrip_blocks=True, undefined=StrictUndefined
        )
    except TemplateSyntaxError as e:
        raise ValueError(f"Syntax error in template line {e.lineno}") from e
    return tpl_obj


def generate(text: str, verbose: bool = False) -> str:
    """Generate python from annotated sql."""
    parser = get_parser()
    transformer = SqlPyGenTransformer()
    template = get_template()

    try:
        parse_tree = parser.parse(text)
    except UnexpectedToken as e:
        line, col = e.line - 1, e.column - 1
        col_m1 = max(0, col)
        err_line = text.split("\n")[line]
        err_marker = "-" * col_m1 + "^"
        msg = f"Error parsing input:\n{e}\n{err_line}\n{err_marker}"
        raise RuntimeError(msg)

    if verbose:
        print("Parse tree")
        print("-" * 80)
        print(parse_tree.pretty())

    trans_tree = transformer.transform(parse_tree)

    if verbose:
        print("Transformed tree")
        print("-" * 80)
        pprint(trans_tree)

    rendered_tree = template.render(**trans_tree)
    rendered_tree = black.format_str(rendered_tree, mode=black.Mode())
    return rendered_tree
