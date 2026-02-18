"""

Copyright (c) 2010-2020, Delft University of Technology
All rigths reserved

This file is part of the Tudat. Redistribution and use in source and
binary forms, with or without modification, are permitted exclusively
under the terms of the Modified BSD license. You should have received
a copy of the license with this file. If not, please or visit:
http://tudat.tudelft.nl/LICENSE.
"""
from __future__ import annotations
import numpy as np
from tudatpy.astro import two_body_dynamics
from tudatpy.dynamics import environment
import tudatpy.kernel.dynamics.environment
__all__: list[str] = ['calculate_lambert_arc_impulsive_delta_v', 'environment', 'np', 'two_body_dynamics']
def calculate_lambert_arc_impulsive_delta_v(bodies: tudatpy.kernel.dynamics.environment.SystemOfBodies, departure_body: str, target_body: str, departure_epoch: int, arrival_epoch: int, central_body: str = 'Sun') -> tuple[float]:
    """
     "
        This function solved Lambert's problem for a transfer from the `departure_body` (at departure epoch)
        to a `target_body` (at arrival epoch), with the states of the `departure_body` and the `target_body`
        defined by ephemerides stored inside the `bodies` (`SystemOfBodies` instance). Note that this solver
        assumes that the transfer departs/arrives to/from the center of mass of the departure and the target body.
    
        Parameters
        ----------
        bodies: environment.SystemOfBodies
            Body objects defining the physical simulation environment
        departure_body: str
            The name of the body from which the transfer is to be computed
        target_body: str
            The name of the body to which the transfer is to be computed
        departure_epoch: int
            Epoch at which the departure from the `target_body`'s center of mass is to take place
        arrival_epoch: int
            Epoch at which the arrival at he target body's center of mass is to take place
    
        Output
        ------
        ΔV_launch: float
            ΔV required for insertion into the Lambert transfer arc
        ΔV_arrival: float
            ΔV required for capture by the arrival body
        
    """
