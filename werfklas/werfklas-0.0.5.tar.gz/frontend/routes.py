from flask import Blueprint, request, flash
from flask import render_template
from src.modules.common import find_waiting_children
from src.classes.database import sessionSetup
exec(open('__version__.py').read())

session = sessionSetup()

# Blueprint Configuration
templates_bp = Blueprint(
    'templates_bp', __name__,
    template_folder='templates'
)


@templates_bp.route('/')
def index():
    _waiting_children = find_waiting_children()
    return render_template('index.html',
                           children=_waiting_children,
                           _PageTitle=f'Wachtlijst',
                           version=f'| {__version__}')
