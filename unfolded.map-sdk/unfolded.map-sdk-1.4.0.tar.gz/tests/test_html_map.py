from unittest.mock import patch

from unfolded.map_sdk.map.html import HTMLMap

from .fixtures.test_data import EARTHQUAKES_DF


class TestHTMLMap:
    @patch("unfolded.map_sdk.transport.html.__version__", "test")
    @patch("unfolded.map_sdk.transport.html.uuid4", lambda: "test-div")
    def test_template_rendering(self, snapshot):

        m = HTMLMap()
        m.add_dataset(data=EARTHQUAKES_DF, label="Earthquakes")
        m.set_view(zoom=7)
        snapshot.assert_match(m._repr_html_(), "map.html")

    def test_html_map_action_list(self):

        m = HTMLMap()
        transport = m.transport

        m.set_view(zoom=7)
        m.set_view_limits(min_zoom=5)

        assert transport.serialized_actions == [
            {"args": [{"zoom": 7}], "options": {"index": 0}, "funcName": "setView"},
            {
                "args": [{"minZoom": 5}],
                "options": {"index": 0},
                "funcName": "setViewLimits",
            },
        ]

        m.set_theme(preset="light")

        # action_list remembers all previous actions
        assert transport.serialized_actions == [
            {"args": [{"zoom": 7}], "options": {"index": 0}, "funcName": "setView"},
            {
                "args": [{"minZoom": 5}],
                "options": {"index": 0},
                "funcName": "setViewLimits",
            },
            {"args": [{"preset": "light", "options": {}}], "funcName": "setUiTheme"},
        ]
