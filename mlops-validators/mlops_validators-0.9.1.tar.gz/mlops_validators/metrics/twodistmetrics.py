

class TwoDistMetrics:

    def get_metric_name(self):
        return NotImplementedError("Method get_metric_name must be implemented")

    def get_metric_table(self):
        return NotImplementedError("Method get_metric_table must be implemented")

    def get_metric(self):
        return NotImplementedError("Method get_metric must be implemented")

    def fit(self, **kwargs):
        return NotImplementedError("Method fit must be implemented")