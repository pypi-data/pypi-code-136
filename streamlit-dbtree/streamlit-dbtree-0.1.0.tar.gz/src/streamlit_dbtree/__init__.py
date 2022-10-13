from pathlib import Path
from typing import Optional
import json
import streamlit as st
import streamlit.components.v1 as components
import snowflake.connector
import snow_obj as sno

frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_dbtree", path=str(frontend_dir)
)

# @st.cache(suppress_st_warning=True,hash_funcs={snowflake.connector.connection.SnowflakeConnection:lambda _: None})
def getAll(conn):
    return sno.get_database_list(conn) 

def streamlit_dbtree(
    conn,
    key: Optional[str] = None,
    backgroundColor:Optional[str] = "transparent",
    selectColor:Optional[str] = "#beebff",
    hoverColor:Optional[str] = "transparent",
    fontColor:Optional[str] = "grey",
    height:Optional[int] = 200,
):
    if st.session_state.get("alldbinfo") is None:
        res=  getAll(conn)
        st.session_state["alldbinfo"]=res
    component_value = _component_func(
        data=json.dumps(st.session_state["alldbinfo"]),key=key,backgroundColor=backgroundColor,fontColor=fontColor,height=height,selectColor=selectColor,hoverColor=hoverColor
    )

    return component_value
