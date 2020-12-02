#!/usr/bin/env python3

# write the models

from lmfit import Minimizer, Parameters, report_fit
import numpy as np
import pandas as pd

# AIC and BIC function
def calcAic(l, RSS, lp):
    """
    Calculates AIC manually

    Parameters:
        l     (int): number of datapoints
        lp    (int): number of parameters from model
        RSS (float): residual sum of squares

    Returns:
        AIC (float): aic value
    """
    aic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(RSS) + 2 * lp

    return aic

def calcBic(l, RSS, lp):
    """
    Calculates AIC manually

    Parameters:
        l     (int): number of datapoints
        lp    (int): number of parameters from model
        RSS (float): residual sum of squares

    Returns:
        AIC (float): aic value
    """
    bic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(RSS) + np.log(l) * lp

    return bic

##########################
### fitted OLS using lmfit
##########################

# objective function to minimize, the residuals
def residLin(params, t, data):
    """
    Calculate residuals from linear model by subtracting data

    Parameters:
        params (parameter object): parameter of object containing coefficients
                                   a, b, c and d
        t                (vector): vector of independent variable, time
        data   (pandas dataframe): dataframe containing the t and N values

    Returns:
        residual values from subtracting data from model prediction
    """
    a = params["a"]
    b = params["b"]
    c = params["c"]
    d = params["d"]

    # cubic model
    model = a*t**3 + b*t**2 + c*t + d

    return model - data # return the residuals
    # remember residuals = model - data

###############################
### fitted logistic using lmfit
###############################

def residLogi(params, t, data):
    """
    Calculate residuals from logistic model by subtracting data


    Parameters:
        params (parameter object): parameter of object containing starting 
                                   values N_0, N_max and r_max
        t                (vector): vector of independent variable, time
        data   (pandas dataframe): dataframe containing the t and N values

    Returns:
        residual values from subtracting data from model prediction
    """
    N_0 = params["N_0"]
    N_max = params["N_max"]
    r_max = params["r_max"]

    # logistic model
    model = N_0 * N_max * np.exp(r_max * t) / \
        (N_max + N_0 * (np.exp(r_max * t) - 1))

    return model - data # return the residuals

####################
# gompertz model fit
####################
def residGom(params, t, data):
    """
    Calculate residuals from gompertz model and subtract data
        Calculate residuals from logistic model by subtracting data

    Parameters:
        params (parameter object): parameter of object containing starting 
                                   values N_0, N_max, r_max and t_lag
        t                (vector): vector of independent variable, time
        data   (pandas dataframe): dataframe containing the t and N values

    Returns:
        residual values from subtracting data from model prediction
    """
    N_0 = params["N_0"]
    N_max = params["N_max"]
    r_max = params["r_max"]
    t_lag = params["t_lag"]
    
    # gompertz model
    model = np.exp(N_0 + (N_max - N_0) * \
        np.exp(-np.exp(r_max * np.exp(1) * (t_lag - t) / \
                     ((N_max - N_0) * np.log(10)) + 1)))
    
    # return residuals
    return model - data

# ###################
# # baranyi model fit
# ###################
# def residBar(params, t, data):
#     """
#     Calculate residuals from Baranyi model and subtract data
#         Calculate residuals from logistic model by subtracting data

#     Parameters:
#         params (parameter object): parameter of object containing starting 
#                                    values N_0, N_max, t_lag and r_max
#         t                (vector): vector of independent variable, time
#         data   (pandas dataframe): dataframe containing the t and N values

#     Returns:
#         residual values from subtracting data from model prediction
#     """
#     N_0 = params["N_0"]
#     N_max = params["N_max"]
#     r_max = params["r_max"]
#     t_lag = params["t_lag"]

#     h_0 = 1 / (np.exp(t_lag * r_max) - 1)
#     A_t = t + 1 / r_max * np.log((np.exp(-r_max * t) + h_0) / (1 + h_0))
#     model = N_0 * A_t - np.log(1 + (np.exp(r_max * A_t) - 1) / np.exp(N_max - N_0))

#     # return residuals
#     return model - data

def getStartVal(ini_r_max, ini_t_lag):
    r_max = np.random.normal(ini_r_max, 0.2, 300)
    t_lag = np.random.normal(ini_t_lag, 0.2, 300)
    startVal = np.array([r_max, t_lag])

    return startVal

# function to generate starting values for each of the parameters
def bestFitsLogi(df, t, N, N0, Nmax, startVal):
    """
    Generates starting values by sampling from a Gaussian distribution with mean
    from the initial estimates
    Fits the models to each sample and calculate the AIC and BIC
    Choses the models with lowest AIC and BIC for each dataset

    Parameters:
        
        

    Returns:
        logiStats (pandas dataframe): dataframe containing optimal starting 
                                      values for logistic model
    """

    # initialize empty dataframe to store values
    logiStats = pd.DataFrame(columns = ["N_0", "N_max", "r_max", "RSS", "AIC", "BIC"])
 
    for row in startVal:
        params = Parameters()
        params.add_many(('N_0', N0, True, None, Nmax/10, None, None),
                        ('N_max', Nmax, True, N0, 1.3 * Nmax, None, None),
                        ('r_max', row[0], True, 0, None, None, None))
                        # ('t_lag', row[1], True, 0, float(0.5 * max(t)), None, None))
        # try:
        minner = Minimizer(residLogi, params, fcn_args = (t, N), nan_policy = "propagate")
        fitLogi = minner.minimize()
        # catch any unsuccessful runs and save to a list
        # except ValueError:
            # continue # continue to next set of values
        # append all starting parameters, resulting RSS, AIC and BIC to a dataframe
        aic = calcAic(len(N), fitLogi.chisqr, len(fitLogi.params))
        bic = calcBic(len(N), fitLogi.chisqr, len(fitLogi.params))
        logiStats = logiStats.append({"N_0": fitLogi.params["N_0"].value,
                                      "N_max": fitLogi.params["N_max"].value,
                                      "r_max": fitLogi.params["r_max"].value,
                                    #   "t_lag": "Not Used",
                                      "RSS": fitLogi.chisqr,
                                      "AIC": aic,
                                      "BIC": bic},
                                      ignore_index = True)
       
        logiStats = logiStats.dropna()   
    if len(logiStats) == 0:
        return None # return None for IDs not fitted
    else:
        bestFitLogi = logiStats[logiStats.AIC == min(logiStats.AIC)] # select lowest AIC for best fit
        return bestFitLogi

# function to generate starting values for each of the parameters
def bestFitsGom(df, t, N, N0, Nmax, startVal):
    """
    Generates starting values by sampling from a Gaussian distribution with mean
    from the initial estimates
    Fits the models to each sample and calculate the AIC and BIC
    Choses the models with lowest AIC and BIC for each dataset

    Parameters:
        df (pandas dataframe): dataframe contains the t and N values to be
                               fitted, and initial estimates for N_0, N_max, 
                               r_max and t_lag
        maxiters    (numeric): number of samples to draw

    Returns:
        gomStats (pandas dataframe): dataframe containing optimal starting 
                                     values for gompertz model
    """

    # initialize empty dataframe to store values
    gomStats = pd.DataFrame(columns = ["N_0", "N_max", "r_max", "t_lag", "RSS", "AIC", "BIC"])
    
    for row in startVal:
        params = Parameters()
        params.add_many(('N_0', N0, True, 0, Nmax/10, None, None),
                        ('N_max', Nmax, True, N0, 1.3 * Nmax, None, None),
                        ('r_max', row[0], True, 0, None, None, None),
                        ('t_lag', row[1], True, 0, None, None, None))
        # try:
        minner = Minimizer(residGom, params, fcn_args = (t, N), nan_policy = "propagate")
        fitGom = minner.minimize()
        # catch any unsuccessful runs and save to a list
        # except ValueError:
            # continue # continue to next set of values
        # append all starting parameters, resulting RSS, AIC and BIC to a dataframe
        aic = calcAic(len(N), fitGom.chisqr, len(fitGom.params))
        bic = calcBic(len(N), fitGom.chisqr, len(fitGom.params))
        gomStats = gomStats.append({"N_0": fitGom.params["N_0"].value,
                                    "N_max": fitGom.params["N_max"].value,
                                    "r_max": fitGom.params["r_max"].value,
                                    "t_lag": fitGom.params["t_lag"].value,
                                    "RSS": fitGom.chisqr,
                                    "AIC": aic,
                                    "BIC": bic},
                                    ignore_index = True)
    if len(gomStats) == 0:
        return None # return None for IDs not fitted
    else:
        bestFitGom = gomStats[gomStats.AIC == min(gomStats.AIC)] # select lowest AIC for best fit
        return bestFitGom

# function to generate starting values for each of the parameters
# def bestFitsBar(df, t, N, N0, Nmax, startVal):
#     """
#     Generates starting values by sampling from a Gaussian distribution with mean
#     from the initial estimates
#     Fits the models to each sample and calculate the AIC and BIC
#     Choses the models with lowest AIC and BIC for each dataset

#     Parameters:
#         df (pandas dataframe): dataframe contains the t and N values to be
#                                fitted, and initial estimates for N_0, N_max, 
#                                r_max and t_lag
#         maxiters    (numeric): number of samples to draw

#     Returns:
#         gomStats (pandas dataframe): dataframe containing optimal starting 
#                                      values for gompertz model
#     """

#     # initialize empty dataframe to store values
#     barStats = pd.DataFrame(columns = ["N_0", "N_max", "r_max", "t_lag", "RSS", "AIC", "BIC"])
    
#     for row in startVal:
#         params = Parameters()
#         params.add_many(('N_0', N0, True, 0, (0.3 * Nmax), None, None),
#                         ('N_max', Nmax, True, (0.7 * Nmax), (1.3 * Nmax), None, None),
#                         ('r_max', row[0], True, (0.5 * row[0]), (1.5 * row[0]), None, None),
#                         ('t_lag', row[1], True, 0, float(0.5 * max(t)), None, None))
#         # try:
#         minner = Minimizer(residBar, params, fcn_args = (t, N), nan_policy = "propagate")
#         fitBar = minner.minimize()
#         # catch any unsuccessful runs and save to a list
#         # except ValueError:
#             # continue # continue to next set of values
#         # append all starting parameters, resulting RSS, AIC and BIC to a dataframe
#         aic = calcAic(len(N), fitBar.chisqr, len(fitBar.params))
#         bic = calcBic(len(N), fitBar.chisqr, len(fitBar.params))
#         barStats = barStats.append({"N_0": fitBar.params["N_0"].value,
#                                     "N_max": fitBar.params["N_max"].value,
#                                     "r_max": fitBar.params["r_max"].value,
#                                     "t_lag": fitBar.params["t_lag"].value,
#                                     "RSS": fitBar.chisqr,
#                                     "AIC": aic,
#                                     "BIC": bic},
#                                     ignore_index = True)
#     barStats = barStats.dropna()
#     if len(barStats) == 0:
#         return None # return None for IDs not fitted
#     bestFitBar = barStats[barStats.AIC == min(barStats.AIC)] # select lowest AIC for best fit
#     return bestFitBar
    
########################
### fitted using polyfit
########################

# cubic fit
def polycubic(t, N):
    """
    Fit a cubic model with parameters from the given dataset
    Use try and except to catch unsuccessful fits 
    If a fit is successful, return an object containing a ndarray of 
    coefficients and a list of statistics from the fit

    Parameters:
        t (vector): vector of independent variable, time
        N (vector): vector of  response variable, PopBio

    Returns:
        fit (object): ndarray of coefficients and a list of statistics from the
                      fit
        None        : None 
    """

    # try to fit cubic model to dataset
    try:
        fit = np.polyfit(t, N, 3, full = True)
    except ValueError:
        return None
    return None if fit[1].size == 0 else fit

# power four fit
def polyfour(t, N):
    """
    Fit a power four model with parameters from the given dataset
    Use try and except to catch unsuccessful fits 
    If a fit is successful, return an object containing a ndarray of 
    coefficients and a list of statistics from the fit

    Parameters:
        t (vector): vector of independent variable, time
        N (vector): vector of  response variable, PopBio

    Returns:
        fit (object): ndarray of coefficients and a list of statistics from the
                      fit
        None        : None 
    """

    # try to fit cubic model to dataset
    try:
        fit = np.polyfit(t, N, 4, full = True)
    except ValueError:
        return None
    return None if fit[1].size == 0 else fit