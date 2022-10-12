def example_tree():
    """
    # Branches

    One call of `g.edge(node1, node2, node3, ...)` creates single chain of arrows.
    To make a branch, you need to call `g.edge` once again.
    """
    import os
    from typing import List, Optional

    from airium import Airium
    from grot import Grot, NodeVisit, Node

    this_dir_path = os.path.dirname(__file__)  # if run in console - remove 'directory' parameter below
    out_dir_path = os.path.join(this_dir_path, "out")

    font_face = "Monospace"  # "Courier New", "Helvetica"
    g = Grot(
        name="example_tree",
        format="png",
        directory=out_dir_path,
        graph_attrs={
            "fontname": font_face,
            "layout": "neato",
            "overlap": "scalexy",
            "mode": "ipsep",
            "sep": "+5",
        },
        node_attrs={
            "fontname": font_face,
            "penwidth": "1.1",
            "shape": "box",
            "width": "0",
            "height": "0",
            "margin": "0",
        },
        edge_attrs={
            "fontname": font_face,
            "penwidth": "0.80",
        },
    )

    def html_table_label(
        own_name: str, own_type: str, own_path: str, children: list[NodeVisit], fg_color: str, bg_color=str
    ) -> str:
        a = Airium(base_indent="")

        with a.table(border="0", bgcolor=bg_color):
            shaded_color = "#757575"
            with a.tr():
                with a.td(align="left").font(color=fg_color, **{"point-size": "29"}):
                    a(f" <b><u>{own_name}</u></b>")
                with a.td(align="right").font(color=fg_color):
                    types_ = " | ".join(sorted(set(c.type for c in children)))
                    types_ = f" [{types_[30:]}...]" if len(types_) > 36 else f" [{types_}]"
                    a(f"{own_type}{types_}")
            with a.tr():
                with a.td(colspan=2, align="center").font(color=shaded_color):
                    a(f"<i>{own_path}</i>")

            for visit in children:
                type_annotation = f'<font color="{shaded_color}"><b>{visit.type}</b> '
                sub_types = " | ".join(sorted(NodeVisit.children_types(visit.value)))
                if len(sub_types) > 36:
                    type_annotation += f"[{sub_types[:30]}...]"
                elif sub_types:
                    type_annotation += f"[{sub_types}]"
                type_annotation += "</font>"
                right = repr(visit.value)
                if len(right) < 55 and "<" not in right:
                    left = f"{visit.key}: {type_annotation}"
                    right = f" = {right}"
                else:
                    left = f"{visit.key}:"
                    right = type_annotation

                with a.tr():
                    a.td(align="left").font(_t=left, color=fg_color)
                    a.td(align="right").font(_t=right, color=fg_color)

            if not children:
                a.tr().td(colspan=2).font(_t="No children", color=fg_color)
        return str(a)

    def draw_node(node_object, path=("root",)) -> Optional[Node]:
        children: List[NodeVisit] = []
        for visit in NodeVisit.iter_tree_nodes(node_object):
            visit: NodeVisit
            visit.graph_node_id = draw_node(visit.value, (*path, visit.key))
            children.append(visit)

        if not children:
            return  # draw only containers not leafs
        fg_col = "#111111" if len(path) < 2 else "#112233" if len(path) % 2 else "#334433"
        bg_col = "#eeeeee" if len(path) < 2 else "#ddeedd" if len(path) % 2 else "#eee6dd"
        table_body: str = html_table_label(
            own_name=path[-1],
            own_type=type(node_object).__name__,
            own_path=NodeVisit.join_path_str(*path),
            children=children,
            fg_color=fg_col,
            bg_color=bg_col,
        )

        own_node: Node = g.html_node(table_body)

        for visit in children:
            if visit.graph_node_id:
                g.edge(own_node, visit.graph_node_id)

        return own_node

    my_nested_structure = {
        "web-app": {
            "servlet": [
                {
                    "servlet-name": "cofaxCDS",
                    "servlet-class": "org.cofax.cds.CDSServlet",
                    "init-param": {
                        "configGlossary:installationAt": "Philadelphia, PA",
                        "configGlossary:poweredBy": "Cofax",
                        "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
                        "dataStoreConnUsageLimit": 100,
                        "dataStoreLogLevel": "debug",
                        "maxUrlLength": 500,
                    },
                },
                {
                    "servlet-name": "cofaxEmail",
                    "servlet-class": "org.cofax.cds.EmailServlet",
                    "init-param": {"mailHost": "mail1", "mailHostOverride": "mail2"},
                },
                {"servlet-name": "cofaxAdmin", "servlet-class": "org.cofax.cds.AdminServlet"},
                {"servlet-name": "fileServlet", "servlet-class": "org.cofax.cds.FileServlet"},
                {
                    "servlet-name": "cofaxTools",
                    "servlet-class": "org.cofax.cms.CofaxToolsServlet",
                    "init-param": {
                        "templatePath": "toolstemplates/",
                        "log": 1,
                        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
                        "lookInContext": 1,
                        "adminGroupID": 4,
                        "betaServer": True,
                    },
                },
            ],
            "servlet-mapping": {
                "cofaxCDS": "/",
                "cofaxEmail": "/cofaxutil/aemail/*",
                "cofaxAdmin": "/admin/*",
                "fileServlet": "/static/*",
                "cofaxTools": "/tools/*",
            },
            "taglib": {"taglib-uri": "cofax.tld", "taglib-location": "/WEB-INF/tlds/cofax.tld"},
        }
    }
    draw_node(my_nested_structure)

    g.render()

    # example ends here
