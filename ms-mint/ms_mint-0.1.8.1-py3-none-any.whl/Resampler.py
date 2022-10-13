import pandas as pd


class Resampler:
    """Resample a chromatogram to have fixed time intervals.

    :param tau: Sampling interval, defaults to "50ms"
    :type tau: str
    :param unit: Time unit, defaults to "minutes"
    :type unit: str
    :param smooth: Whether or not to apply rolling average.
    :type smooth: bool
    """
    def __init__(self, tau: str="50ms", unit: str="minutes", smooth: bool=True):
        self._unit = unit
        self._tau = tau
        self._smooth = smooth

    def resample_unit_minutes(self, chrom):
        chrom = chrom.sort_index()
        chrom.index = pd.to_timedelta(chrom.index, unit=self._unit)
        chrom = chrom.resample(self._tau).nearest()
        if self._unit == "seconds":
            chrom.index = chrom.index.seconds + chrom.index.microseconds / 1000000
        if self._unit == "minutes":
            chrom.index = (
                chrom.index.seconds + chrom.index.microseconds / 1000000
            ) / 60
        if self._smooth:
            chrom = chrom.rolling(20, center=True).mean()
            chrom = chrom.rolling(5, center=True).mean()
        return chrom

    def resample(self, chrom):
        return self.resample_unit_minutes(chrom)
