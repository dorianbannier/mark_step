# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:35:08 2022

@author: dorian.bannier
"""

def mark_step(marker_left = 'LHEE', marker_right = 'RHEE', plot = 0):
    """
    Mark the foot strike/contact and the foot off in the current session opened in Vicon Nexus.

    Parameters
    ----------
    marker_left : str, optional
        DESCRIPTION. The default is LHEE.
    
    marker_right : str, optional
        DESCRIPTION. The default is RHEE.
    
    plot : int, optional
        DESCRIPTION. The default is 0.
        A value fixed to 1 display a plot with the foot strike and the foot off of each side

    Returns
    -------
    None.

    """
    
    
    from viconnexusapi import ViconNexus
    from scipy.signal import find_peaks
    import matplotlib.pyplot as plt
    import numpy as np
    from IPython import get_ipython
    
    vicon = ViconNexus.ViconNexus()
    
    vicon.ClearAllEvents()
    
    lhee = np.asarray(vicon.GetTrajectory(vicon.GetSubjectNames()[0], 'LHEE'))[2]
    rhee = np.asarray(vicon.GetTrajectory(vicon.GetSubjectNames()[0], 'RHEE'))[2]
    
    lhee_peaks, _ = find_peaks(lhee, prominence = 30) # Foot Off Gauche
    rhee_peaks, _ = find_peaks(rhee, prominence = 30) # Foot Off Droit
    lhee_peaks_inverse, _ = find_peaks(lhee*-1, prominence = 40) # Foot Strike Gauche
    rhee_peaks_inverse, _ = find_peaks(rhee*-1, prominence = 40) # Foot Strike Droit
    
    [vicon.CreateAnEvent(vicon.GetSubjectNames()[0], 'Left', 'Foot Off', int(i), 0) for i in lhee_peaks]
    [vicon.CreateAnEvent(vicon.GetSubjectNames()[0], 'Right', 'Foot Off', int(i), 0) for i in rhee_peaks]
    [vicon.CreateAnEvent(vicon.GetSubjectNames()[0], 'Left', 'Foot Strike', int(i), 0) for i in lhee_peaks_inverse]
    [vicon.CreateAnEvent(vicon.GetSubjectNames()[0], 'Right', 'Foot Strike', int(i), 0) for i in rhee_peaks_inverse]
    
    if plot == 1:
        get_ipython().run_line_magic('matplotlib', 'qt')
        fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True)
        axes[0,0].plot(lhee)
        axes[0,0].plot(lhee_peaks, lhee[lhee_peaks], "x")
        axes[0,0].title.set_text('Foot Off - Gauche')
        
        axes[1,0].plot(lhee)
        axes[1,0].plot(lhee_peaks_inverse, lhee[lhee_peaks_inverse], "x")
        axes[1,0].title.set_text('Foot Strike - Gauche')
        
        axes[0,1].plot(rhee)
        axes[0,1].plot(rhee_peaks, rhee[rhee_peaks], "x")
        axes[0,1].title.set_text('Foot Off - Droit')
        
        axes[1,1].plot(rhee)
        axes[1,1].plot(rhee_peaks_inverse, rhee[rhee_peaks_inverse], "x")
        axes[1,1].title.set_text('Foot Strike - Droit')
        fig.show()
