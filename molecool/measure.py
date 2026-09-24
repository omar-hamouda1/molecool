"""Functions for performing measurements."""

import numpy as np


def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.
    """
    dist_vec = rA - rB
    distance = float(np.linalg.norm(dist_vec))

    return distance


def calculate_angle(rA: np.ndarray, rB: np.ndarray, rC: np.ndarray, degrees: bool = False) -> float:
    """Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point.
    degrees : bool, optional
        If True, return the angle in degrees. Default is False (radians).

    Returns
    -------
    theta : float
        The angle between the three points.
    """
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta