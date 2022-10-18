from pathlib import Path
import os
import streamlit as st
from pollination_streamlit_io import get_hbjson
from honeybee.model import Model
from honeybee_vtk.model import Model as VTKModel
# viewer is taken from __init__.py context
from pollination_streamlit_viewer import viewer

# create a folder where save files
FOLDER = Path(__file__).parent.joinpath('data').resolve()
if not os.path.isdir(FOLDER):
    os.makedirs(FOLDER)

# session variables
if 'count' not in st.session_state:
    st.session_state.count = 0

@st.cache
def model_from_path(path):
    vtk_model = VTKModel.from_hbjson(path)
    vtk_path = vtk_model.to_vtkjs(folder=FOLDER, 
        name=model.identifier)
    return vtk_path

hbjson_data = get_hbjson(key='hbjson_data')

content = None
if hbjson_data is not None:
    model = Model.from_dict(hbjson_data['hbjson'])
    path = model.to_hbjson(folder=FOLDER, name=model.identifier)
    content = Path(model_from_path(path)).read_bytes()

viewer(
    content=content,  
    key='vtkjs-viewer',
    subscribe=False,
    style={
        'height' : '640px'
    }
)
st.session_state.count += 1
st.warning(f'I ran n.{st.session_state.count} times.')