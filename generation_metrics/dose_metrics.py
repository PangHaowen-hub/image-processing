#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from typing import Optional

class DoseMetrics():
    def __init__(self):
        #TODO
        # Define prescribed dose for brain (b) and pelvis (p)
        self.prescribed_dose = {'b': 2, 'p': 3}
        
    def mae_dose(self,
                 d_gt: np.ndarray, 
                 d_pred: np.ndarray,
                 roi: str,
                 threshold: Optional[float] = 1) -> float:
        """
        Compute Mean Absolute Error (MAE) for the dose distributions given a certain
        threshold [0,1] relative to the prescribed dose.
    
        Parameters
        ----------
        d_gt : np.ndarray
            Dose distribution of the ground truth CT
        d_pred : np.ndarray
            Dose distribution of the predicted synthetic CT.
        roi : str
            Which region is analyzed, either brain (b) or pelvis (p).
        threshold : float, optional
            Theshold for determining the included voxels relative to the prescribed
            dose. It can be a value beteen 0 and 1. The default is 1.
    
        Returns
        -------
        mae_dose_value : float
            Mean absolute dose difference relative to the prescribed dose.
    
        """
        # Threshold dose distributions
        abs_th = threshold * self.prescribed_dose[roi]
        d_pred = d_pred[d_gt >= abs_th]
        d_gt = d_gt[d_gt >= abs_th]
        n = len(d_gt)
        
        # Calculate MAE     
        mae_dose_value = np.sum(np.abs(d_gt - d_pred)/self.prescribed_dose[roi])/n
        return float(mae_dose_value)
    
    
    def dvh_metric(self, 
                   gt_dvh : dict, 
                   pred_dvh : dict) -> float:
        """
        Calculate the dose volume histogram (DVH) metric from the given DVH
        parameters.

        Parameters
        ----------
        gt_dvh : dict
            DVH parameters for the dose calculation on ground truth CT.
        pred_dvh : dict
            DVH parameters for the dose calculation on predicted synthetic CT.
            
        Returns
        -------
        DVH_metric : float
            One combined metric based on several DVH parameters for the SynthRAD 
            challenge.

        """
        
        # target metrics
        D98_target = ( np.abs(gt_dvh['D98_target']- pred_dvh['D98_target']) /
                      ( gt_dvh['D98_target'] + 1e-12 ) )
        V95_target = ( np.abs(gt_dvh['D98_target']- pred_dvh['D98_target']) /
                       ( gt_dvh['D98_target'] + 1e-12 ) )
        
        # OAR metrics
        D2_OAR, Dmean_OAR = [], []
        for i in range(1, 4):
            D2_OAR.append( ( np.abs(gt_dvh[f'D2_OAR{i}']- pred_dvh[f'D2_OAR{i}']) /
                             ( gt_dvh[f'D2_OAR{i}'] + 1e-12) ) )
            Dmean_OAR.append( ( np.abs(gt_dvh[f'Dmean_OAR{i}']- pred_dvh[f'Dmean_OAR{i}']) /
                                ( gt_dvh[f'Dmean_OAR{i}'] + 1e-12) ) )

        
        # Calculate sum
        DVH_metric = ( D98_target + V95_target + 
                       1/(len(D2_OAR)) * np.sum(D2_OAR) + 
                       1/(len(Dmean_OAR)) * np.sum(Dmean_OAR) )
        
        return float(DVH_metric)

        
    def gamma_index(self,
                    d_gt: np.ndarray, 
                    d_pred: np.ndarray) -> float:
        # TODO
        raise NotImplementedError
    