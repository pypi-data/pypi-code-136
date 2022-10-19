import os
from typing import Dict

import streamlit.components.v1 as components
import streamlit as st

# Toggle this to False for local development
_RELEASE = True

if _RELEASE:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _viewer = components.declare_component("pollination_streamlit_viewer", path=build_dir)
else:
    _viewer = components.declare_component(
        "pollination_streamlit_viewer", url="http://localhost:3001"
    )

def viewer(
    key: str, *, 
    content: bytes = None,
    toolbar: bool = True, 
    sidebar: bool = True,
    subscribe: bool = False,
    clear: bool = True,
    action_stack: list = [],
    style: Dict = None,
    screenshot_name: str = None
):
    """Pollination Streamlit Viewer component.

    Args:
        key: A unique string for this instance of the viewer.
        content: A VTKJS file content.
        toolbar: A boolean to show or hide the toolbar in the viewer. Default is set to True.
        sidebar: A boolean to show or hide the sidebar in the viewer. Default is set to True.
        subscribe: A boolean to subscribe or unsubscribe the VTKJS camera and renderer content.
        clear: A boolen to clear the current contents from the viewer when loading the
            new content. Default is set to True.
        action_stack: Action stack
        style: A dictionary to set the style for the viewer. The key and values can be
            any CSS style attribute. Default {"border": "1px solid #d0d7de", "borderRadius": "2px"}
        screenshot_name: string
            An optional string that will be the default name for a screenshot
    """

    style = style or {"border": "1px solid #d0d7de", "borderRadius": "2px"}
    return _viewer( 
        key=key,
        content=content, 
        toolbar=toolbar, 
        sider=sidebar, 
        subscribe=subscribe, 
        action_stack=action_stack, 
        clear=clear, 
        style=style, 
        screenshot_name=screenshot_name,
    )


EXAMPLES = [
  "bidirectional_editing",
  "get_display",
  "grid",
  "minimal"
]

if not _RELEASE:
    path = f'../examples/apps/{EXAMPLES[3]}.py'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), path))
    exec(open(path).read())