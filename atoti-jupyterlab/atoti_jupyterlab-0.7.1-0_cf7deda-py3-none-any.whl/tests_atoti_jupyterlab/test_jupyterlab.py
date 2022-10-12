import re

import pytest
from atoti_core import MissingPluginError

import atoti as tt


def test_visualize_without_jupyterlab_plugin(session: tt.Session):
    with pytest.raises(MissingPluginError):
        session.visualize()


@pytest.mark.jupyterlab
def test_visualize_with_jupyterlab_plugin(session: tt.Session):
    session.visualize()


@pytest.mark.jupyterlab
def test_runtime_typechecking(session: tt.Session):
    with pytest.raises(
        TypeError,
        match=re.escape(
            'type of argument "name" must be one of (str, NoneType); got int instead'
        ),
    ):
        session.visualize(2020)  # type: ignore
