#!/usr/bin/env python3

# applying models to datasets

from lmfit import Minimizer, Parameters, report_fit
import numpy as np
import pandas as pd
from models import calcAic, calcBic, polycubic, polyfour, residLogi, bestFitsLogi, getStartVal
import multiprocessing

# profile speed
import cProfile
import pstats

# profile speed
profStats = cProfile.Profile()
profStats.enable()

# set seed for testing
np.random.seed(1995)

# import dataset
df = pd.read_csv("../Data/PreppedLGD.csv")

# list of unique IDs
uniqueID = np.unique(df['numID'])
len(uniqueID)

def parallelFit(i):
    """
    describe function


    """
    # initialize empty dataframe to store fit statistics for each unique ID
    fitStats = pd.DataFrame(columns = ["ID", "Temp", "Medium","3a", "3b", "3c",\
                                    "3d", "3polyRSS", "3polyAIC", "3polyBIC",\
                                    "4a", "4b", "4c", "4d", "4e", "4polyRSS",\
                                    "4polyAIC", "4polyBIC", "Logi_N_0", \
                                    "Logi_N_max", "Logi_r_max", "LogiRSS",\
                                    "LogiAIC", "LogiBIC"]) 
                                    #, "Gom_N_0", "Gom_N_max",\
                                    # "Gom_r_max", "Gom_t_lag", "GomRSS",\
                                    # "GomAIC", "GomBIC"])
                                    #    , "Bar_N_0",\
                                    #    "Bar_N_max", "Bar_r_max", "Bar_t_lag",\
                                    #    "BarRSS", "BarAIC", "BarBIC"],)
    
    # to loop through every data subset
    dfSubset = df[df['numID'] == i]
    # set time and population variable
    t = dfSubset['Time']
    N = dfSubset['PopBio']
    N0 = min(N)
    Nmax = max(N)

    # cube fit
    cubePolyFit = polycubic(t, N)

    if cubePolyFit is None:
        print("Error at ID", i, "cubic fit unsuccessful")
    else:
        # RSS for cubic fit
        cubePolyRSS = cubePolyFit[1][0]
        # calculate AIC and BIC for cube fit
        l = len(dfSubset)
        lpCube = len(cubePolyFit[0]) # length of parameters
        cubeAic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(cubePolyRSS)\
             + 2 * lpCube
        cubeBic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(cubePolyRSS)\
             + np.log(l) * lpCube

        # set ID equal unique ID
        fitStats.loc[0, "ID"] = i
        # set Temp and Medium
        fitStats.loc[0, "Temp"] = dfSubset.iloc[0,6]
        fitStats.loc[0, "Medium"] = dfSubset.iloc[0,10]
        # extract fit parameters
        fitStats.loc[0, "3a"] = cubePolyFit[0][0]
        fitStats.loc[0, "3b"] = cubePolyFit[0][1]
        fitStats.loc[0, "3c"] = cubePolyFit[0][2]
        fitStats.loc[0, "3d"] = cubePolyFit[0][3]
        fitStats.loc[0, "3polyRSS"] = cubePolyRSS
        fitStats.loc[0, "3polyAIC"] = cubeAic
        fitStats.loc[0, "3polyBIC"] = cubeBic

    # power four fit
    fourPolyFit = polyfour(t, N)

    if fourPolyFit is None:
        print("Error at ID", i, "power four fit unsuccessful")
    else:
        # RSS for power four fit
        fourPolyRSS = fourPolyFit[1][0]
        # calculate AIC and BIC for power four fit
        lpFour = len(fourPolyFit[0]) # length of parameters
        fourAic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(fourPolyRSS)\
             + 2 * lpFour
        fourBic = l + 2 + l * np.log((2 * np.pi) / l) + l * np.log(fourPolyRSS)\
             + np.log(l) * lpFour
        fitStats.loc[0, "4a"] = fourPolyFit[0][0]
        fitStats.loc[0, "4b"] = fourPolyFit[0][1]
        fitStats.loc[0, "4c"] = fourPolyFit[0][2]
        fitStats.loc[0, "4d"] = fourPolyFit[0][3]
        fitStats.loc[0, "4e"] = fourPolyFit[0][4]
        fitStats.loc[0, "4polyRSS"] = fourPolyRSS
        fitStats.loc[0, "4polyAIC"] = fourAic
        fitStats.loc[0, "4polyBIC"] = fourBic

    # rolling regression to find rmax, use 3 consecutive datapoints at a time
    # also used to find tlag by intersecting fitted line with x-axis
    for j in range(len(t)-2):
        rmaxTemp = 0
        fitLin1 = np.polyfit(t[j: j+2], N[j : j+2], 1, full = True)
        # poly = np.poly1d(fitLin1)
        # plt.plot(poly(t))
        if fitLin1[0][0] > rmaxTemp:
            rmaxTemp = fitLin1[0][0]
            tlagTemp = fitLin1[0][1]

    ini_rmax = rmaxTemp
    ini_tlag = tlagTemp
    
    # setup starting values sample
    # ini_rmax and ini_tlag but no ini_tlag as of now
    startVal = getStartVal(ini_rmax, ini_tlag)

    # fit logi
    logiFit = bestFitsLogi(dfSubset, t, N, N0, Nmax, startVal)
    # solve problem of logi not fitting
    # note any IDs where logistic model fit was unsuccessful
    if logiFit is None:
        print("Error at ID", i, "logistic fit unsuccessful")
    else:
        fitStats.loc[0, "Logi_N_0"] = logiFit.iloc[0, 0]
        fitStats.loc[0, "Logi_N_max"] = logiFit.iloc[0, 1]
        fitStats.loc[0, "Logi_r_max"] = logiFit.iloc[0, 2]
        # fitStats.loc[0, "Logi_t_lag"] = logiFit.iloc[0, 3]
        fitStats.loc[0, "LogiRSS"] = logiFit.iloc[0, 3]
        fitStats.loc[0, "LogiAIC"] = logiFit.iloc[0, 4]
        fitStats.loc[0, "LogiBIC"] = logiFit.iloc[0, 5]

    # # fit gom
    # gomFit = bestFitsGom(dfSubset, t, N, N0, Nmax, startVal)

    # # note any IDs where logistic model fit was unsuccessful
    # if gomFit.empty:
    #     print("Error at ID", i, "gompertz fit unsuccessful")
    # else:
    #     fitStats.loc[0, "Gom_N_0"] = gomFit.iloc[0, 0]
    #     fitStats.loc[0, "Gom_N_max"] = gomFit.iloc[0, 1]
    #     fitStats.loc[0, "Gom_r_max"] = gomFit.iloc[0, 2]
    #     fitStats.loc[0, "Gom_t_lag"] = gomFit.iloc[0, 3]
    #     fitStats.loc[0, "GomRSS"] = gomFit.iloc[0, 4]
    #     fitStats.loc[0, "GomAIC"] = gomFit.iloc[0, 5]
    #     fitStats.loc[0, "GomBIC"] = gomFit.iloc[0, 6]

    # fit bar
    # barFit = bestFitsBar(dfSubset, t, N, N0, Nmax, startVal)

    # # note any IDs where logistic model fit was unsuccessful
    # if barFit is None:
    #     print("Error at ID", i, "baranyi fit unsuccessful")
    # else:
    #     fitStats.loc[0, "Bar_N_0"] = barFit.iloc[0, 0]
    #     fitStats.loc[0, "Bar_N_max"] = barFit.iloc[0, 1]
    #     fitStats.loc[0, "Bar_r_max"] = barFit.iloc[0, 2]
    #     fitStats.loc[0, "Bar_t_lag"] = barFit.iloc[0, 3]
    #     fitStats.loc[0, "BarRSS"] = barFit.iloc[0, 4]
    #     fitStats.loc[0, "BarAIC"] = barFit.iloc[0, 5]
    #     fitStats.loc[0, "BarBIC"] = barFit.iloc[0, 6]

    return fitStats

# set number of cpu cores for parallelization
pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())

# create parallelized for loop to fit all models to all data subsets
parallelFits = pool.map(parallelFit, uniqueID)

# wait for processes to finish then close loop
pool.close()
pool.join()

# initialize final dataframe to store all fit stats
finalStat = pd.DataFrame(columns = ["ID", "Temp", "Medium","3a", "3b", "3c",\
                                    "3d", "3polyRSS", "3polyAIC", "3polyBIC",\
                                    "4a", "4b", "4c", "4d", "4e", "4polyRSS",\
                                    "4polyAIC", "4polyBIC", "Logi_N_0", \
                                    "Logi_N_max", "Logi_r_max", "LogiRSS",\
                                    "LogiAIC", "LogiBIC"])
                                    #, "Gom_N_0", "Gom_N_max",\
                                    # "Gom_r_max", "Gom_t_lag", "GomRSS",\
                                    # "GomAIC", "GomBIC"])
                                    #    , "Bar_N_0",\
                                    #    "Bar_N_max", "Bar_r_max", "Bar_t_lag",\
                                    #    "BarRSS", "BarAIC", "BarBIC"],)

for fitStats in parallelFits:
    finalStat = finalStat.append(fitStats)

finalStat.to_csv("../Data/growthFits.csv")

# profile speed
profStats.disable()
ps = pstats.Stats(profStats).print_stats()


    # # ######################################
    # # ### Plots
    # # ######################################

    # #### Plot results ####
    # plt.rcParams['figure.figsize'] = [20, 15]

    # # initiate time vector for smooth plots
    # tVec = np.linspace(min(t),
    #                 max(t),
    #                 1000)
    # # match N vector to same scale as tVec
    # NVec = np.ones(len(tVec))

    # # Linear
    # resultLin = N + fitLin.residual
    # plt.plot(t, resultLin, 'y.', markersize = 15, label = 'Linear')
    # residSmoothLin = residLin(fitLin.params, tVec, NVec)
    # plt.plot(tVec, residSmoothLin + NVec, 'yellow', linestyle = '--', linewidth = 1)

    # # Logistic
    # resultLogi = N + fitLogi.residual
    # plt.plot(t, resultLogi, 'b.', markersize = 15, label = 'Logistic')
    # # get a smooth curve by plugging a time vector to the fitted logi model
    # residSmoothLogi = residLogi(fitLogi.params, tVec, NVec)
    # plt.plot(tVec, residSmoothLogi + NVec, 'blue', linestyle = '--', linewidth = 1)
    # # plt.show()

    # # Gompertz
    # resultGom = N + fitGom.residual
    # plt.plot(t, resultGom, 'r.', markersize = 15, label = 'Gompertz')
    # residSmoothGom = residGom(fitGom.params, tVec, NVec)
    # plt.plot(tVec, residSmoothGom + NVec, 'red', linestyle = '--', linewidth = 1)

    # # Baranyi
    # resultBar = N + fitBar.residual
    # plt.plot(t, resultBar, 'g.', markersize = 15, label = 'Baranyi')
    # residSmoothBar = residBar(fitBar.params, tVec, NVec)
    # plt.plot(tVec, residSmoothBar + NVec, 'green', linestyle = '--', linewidth = 1)
    
    # # plot data points
    # plt.plot(t, N, 'k+', markersize = 15, markeredgewidth = 2, label = 'Data')
    # # plot legend
    # plt.legend(fontsize = 20)
    # plt.xlabel("Time", fontsize = 20)
    # plt.ylabel(r'$N_t$', fontsize = 20)
    # plt.ticklabel_format(style = 'scientific', scilimits = [0, 3])
    # plt.show()

    # if row == df.ID.unique()[1]:
    #     break

# print(fitStats)