from rats.core.session_data_tracker import SessionDataTracker
from rats.core.rats_data_tracker import RatsDataTracker
from rats.core.RATS_CONFIG import packagepath, cachepath, dfpath, PlotBanks
from rats.core.rats_parser import RatsParser
from dash_extensions.enrich import DashProxy, MultiplexerTransform, TriggerTransform, Output
import dash_bootstrap_components as dbc
import dash_uploader as du


app = DashProxy(__name__, external_stylesheets=[dbc.themes.FLATLY],
                suppress_callback_exceptions=True,
                transforms=[MultiplexerTransform(),
                            TriggerTransform()])

# Initialise the relevant utilities
du.configure_upload(app, str(packagepath / cachepath), use_upload_id=False)
session_data = SessionDataTracker(data_directory=str(packagepath / cachepath), parser=RatsParser)
rats_data = RatsDataTracker(str(packagepath / dfpath))

# imports here which depend on app being initialised.
from rats.core import rats_constructor
import rats.core.corecallbacks as core_callbacks
from rats.modules.error_detection import error_detection_callbacks, error_detection_view
from rats.modules.scope import scope_callbacks, scope_view
from rats.modules.jitter_analysis import jitter_analysis_callbacks, jitter_analysis_view
from rats.modules.data_management import data_management_callbacks, data_management_view

# Set the title of the browser tab
app.title = 'RATS'

# Configure which modules are to be included in the app. The second field in the tuple must align with the relevant enum
# field name in RATS_CONFIG.PlotBanks
app.layout = rats_constructor.create_rats_application([(error_detection_view, 'Error_detection'),
                                                       (scope_view, 'Scope'),
                                                       (jitter_analysis_view, 'Jitter_analysis'),
                                                       (data_management_view, 'Data_management')])

# After the layout is set, register the callbacks with the app
core_callbacks.register_callbacks(app)
error_detection_callbacks.register_callbacks(app, PlotBanks.Error_detection.number_of_plot_banks,
                                             PlotBanks.Error_detection.designation)
scope_callbacks.register_callbacks(app, PlotBanks.Scope.number_of_plot_banks, PlotBanks.Scope.designation)
jitter_analysis_callbacks.register_callbacks(app, PlotBanks.Jitter_analysis.number_of_plot_banks,
                                             PlotBanks.Jitter_analysis.designation)
data_management_callbacks.register_callbacks(app, PlotBanks.Data_management.designation)

# Launch RATS!
app.run_server()
