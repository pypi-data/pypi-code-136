import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st

CONFIG = read_config()

st.set_page_config(
    page_title="Connections",
    page_icon="🔗",
)
hide_st(st)
if check_password(st):
    num = 10

    tab_strings = [f"Connection {i}" for i in range(1, num + 1)]

    tabs = st.tabs(list(tab_strings))

    for i in range(num):
        with tabs[i]:
            con = i + 1
            st.write(f"Configure connection {con}")

            CONFIG.forwards[i].source = st.text_input(
                f"Source for con:{con}", value=CONFIG.forwards[i].source
            ).strip()
            st.write("only one source is allowed in a connection")
            CONFIG.forwards[i].dest = get_list(
                st.text_area(
                    f"Destinations for con:{con}",
                    value=get_string(CONFIG.forwards[i].dest),
                )
            )
            st.write("Write destinations one item per line")

    if st.button("Save"):
        write_config(CONFIG)
