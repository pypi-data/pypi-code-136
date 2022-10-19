#!/usr/bin/env python

"""API for modelling solar+storage dispatch over shorter timer periods."""

__author__ = "Allen Lawrence"
__credits__ = "Brian Knowles", "Michael Baker"
__version__ = "0.1.0"
__maintainer__ = "Allen Lawrence"
__email__ = "allen.lawrence@ccrenew.com"
__status__ = "Development"




import numpy as np

### BINARY LOGIC ###
def binDischarge(cue, batt_power, soc, inp, lim, discharge_eff):
    """
    Calculates battery discharge for a single time step.
    Adapted from Brian Knowles's (CCR) battery model.

    :param cue: binary to cue to signal discharge/charge (0 or 1)
    :param batt_power: max energy per time interval dischargeable or chargeable from the battery (from the perspective
        of the grid).
    :param soc: current state-of-charge of battery
    :param inp: current solar production (energy per time step)
    :param lim: the goal power
    :param discharge_eff: efficiency of battery discharge (fraction).
    :return: scalar discharge value.
    """
    if cue:
        return min(batt_power/discharge_eff, soc, max(lim - inp, 0))
    else:
        return 0


def binCharge(cue, inp, lim, charge_eff, batt_power, batt_energy, soc):
    """
    Calculates battery charge for a single time step.
    Adapted from Brian Knowles's (CCR) battery model.

    :param cue: binary to cue to signal discharge/charge (0 or 1)
    :param inp: current solar production (energy per time step)
    :param lim: the goal power
    :param charge_eff: efficiency of battery charge (fraction)
    :param batt_power: max energy per time interval dischargeable or chargeable from the battery (from the perspective
        of the grid).
    :param batt_energy: maximum state-of-charge of battery (kWh)
    :param soc: current state-of-charge
    :return: scalar charge value.
    """
    if cue:
        return min(max(charge_eff * (inp - lim), 0), charge_eff * batt_power, batt_energy - soc)
    else:
        return min(charge_eff * inp, charge_eff * batt_power, batt_energy - soc)
####################




class Battery(object):
    """
    Battery model. Contains methods for battery dispatch.

    :param self.limit: scalar battery goal power. This can be overwritten by a variable signal in dispatch methods.
    :param self.power: battery charge/discharge power.
    :param self.duration: amount of time during which battery can discharge at max power.
    :param self.charge_eff: efficiency of battery charge.
    :param self.discharge_eff: efficiency of battery discharge.
    :param self.energy: maximum stored energy (from battery perspective)
    """

    def __init__(self):

        self.limit = 0.
        self.power = 0.
        #self.duration = 0.
        self.charge_eff = 0.85
        self.discharge_eff = 1.0
        self.nameplate_duration = 0.
        # degradation hours is the number of hours since the ESUs
        # were PIS'd.  since batteries don't know about history, 
        # this needs to be set to an appropriate value for previous
        # charge/discharge cycling
        self.degradation_hours = 0.0
        # calculate hourly degradation rate from the 4% annual figure
        self.degradation_rate = 0.96**(1/8760.0)

    @property
    def duration(self):
        deg_coeff = min(self.degradation_rate ** self.degradation_hours, 1)
        return self.nameplate_duration * deg_coeff

    @property
    def energy(self):
        return (self.power*self.duration)/self.discharge_eff



    def binary(self, valueS, inpS, limitS=False, soc0=0.):
        """
        Dispatch method for discharging "on-peak" and charging "off-peak". Interprets "on" vs. "off-peak" from the
            value signal provided.

        :param valueS: 1D nump.ndarray time series of energy values. Typically in units of $/kWh. If this signal
            contains more than two different values, consider using another dispatch method.
        :param inpS: 1D numpy.ndarray time series of energy production. Typically in units of kWh. If production
            clipping is significant, consider using another dispatch method.
        :param limitS: 1D numpy.ndarray time series of goal power. The battery will discharge to try to meet these
            values, and charge with input energy in excess of these values.
        :param soc0: Scalar value of internal battery energy. This is the SOC at the start of the dispatch period.
        :return: dict of output signals.
        """

        n = inpS.shape[0]
        assert valueS.shape[0] == n

        if not limitS:
            limitS = self.limit * np.ones(n)
        else:
            assert limitS.shape[0]== n

        #### BUILD  CUES FROM VALUE SIGNAL ####
        cueS = np.zeros(n)
        cueS[valueS == valueS.max()] = 1

        socS = np.zeros(n+1)
        socS[0] = soc0
        dischargeS = np.zeros(n)
        chargeS = np.zeros(n)

        for i in range(n):
            self.degradation_hours += 1
            soc = socS[i]
            cue = cueS[i]
            inp = inpS[i]
            lim = limitS[i]
            dischargeS[i] = binDischarge(cue, self.power, soc, inp, lim, self.discharge_eff)
            chargeS[i] = binCharge(cue, inp, lim, self.charge_eff, self.power, self.energy, soc)
            socS[i + 1] = soc + chargeS[i] - dischargeS[i]


        g_chargeS = chargeS / self.charge_eff
        g_dischargeS = dischargeS * self.discharge_eff
        batt_outS = inpS - g_chargeS + g_dischargeS

        return {'solar+storage': batt_outS,
                'charge': g_chargeS,
                'discharge': g_dischargeS,
                'SOC': socS
                }




#    def perfect(self, valueS, inpS, limitS=False, soc0=0.):
#        #TODO: discuss with O&M how to handle edge effects... add soc1 parameter?
#        """
#        Dispatch method for maximizing value of solar+storage production signal, given value signal and production
#            signal of any form. Employs GLPK's simplex algorithm.
#
#        Because this method only covers one optimization period, it will neglect optimal preparation for the next
#            period. If you don't understand what I'm talking about, contact the maintainer.
#
#        :param valueS: 1D nump.ndarray time series of energy values. Typically in units of $/kWh.
#        :param inpS: 1D numpy.ndarray time series of energy production. Typically in units of kWh.
#        :param limitS: 1D numpy.ndarray time series of goal power. The battery will discharge to try to meet these
#            values, and charge with input energy in excess of these values.
#        :param soc0: Scalar value of internal battery energy. This is the SOC at the start of the dispatch period.
#        :return: dict of output signals.
#        """
#
#        n = inpS.shape[0]
#        assert valueS.shape[0] == n
#
#        if not limitS:
#            limitS = self.limit * np.ones(n)
#        else:
#            assert limitS.shape[0] == n
#
#
#        ######### CONSTRAINT MATRICES #########
#        # Only charge from solar production
#        A = np.zeros((7 * n, 3 * n))
#        for i in range(n):
#            #### SOC #####
#            A[i][0:i + 1] = -1; A[i][n:n + i + 1] = 1; A[i][2 * n:2 * n + i + 1] = 1
#            A[n + i][0:i + 1] = 1; A[n + i][n:n + i + 1] = -1; A[n + i][2 * n:2 * n + i + 1] = -1
#            #### DISCHARGE ####
#            A[2 * n + i][i] = 1
#            A[3 * n + i][i] = 1
#            #### PROCHARGE + CHARGE #######
#            A[4 * n + i][n + i] = 1; A[4 * n + i][2 * n + i] = 1
#            A[5 * n + i][n + i] = 1; A[5 * n + i][2 * n + i] = 1
#            #### PROCHARGE ######
#            A[6 * n + i][n + i] = 1
#        A = np.asmatrix(A)
#
#
#        dischargeS, chargeS, socS = optiBatt(A, n, valueS, inpS, limitS, self.power, self.energy, self.discharge_eff,
#                                              self.charge_eff, soc0)
#
#        g_chargeS = chargeS / self.charge_eff
#        g_dischargeS = dischargeS * self.discharge_eff
#        batt_outS = inpS - g_chargeS + g_dischargeS
#
#        return {'solar+storage': batt_outS,
#                'charge': g_chargeS,
#                'discharge': g_dischargeS,
#                'SOC': socS
#                }


    def forecast(self):
        """
        IN DEVELOPMENT
        Similar to perfect, but where scheduling and execution are different, due to forecast uncertainty.
        """
        pass




