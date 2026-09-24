"""Functions for manipulating pdb files."""

import numpy as np


def open_pdb(file_location: str) -> tuple[np.ndarray, np.ndarray]:
    """Read coordinates and atom symbols from a pdb file.

    Parameters
    ----------
    file_location : str
        The path to the pdb file to be read.

    Returns
    -------
    symbols : np.ndarray
        The atomic symbols of the atoms in the pdb file.
    coords : np.ndarray
        The coordinates of the atoms in the pdb file.
    """
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if "ATOM" in line[0:6] or "HETATM" in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords