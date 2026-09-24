"""Functions for manipulating xyz files."""

import numpy as np


def open_xyz(file_location: str) -> tuple[np.ndarray, np.ndarray]:
    """Open an xyz file and return symbols and coordinates.

    Parameters
    ----------
    file_location : str
        The path to the xyz file to be read.

    Returns
    -------
    symbols : np.ndarray
        The atomic symbols of the atoms in the xyz file.
    coords : np.ndarray
        The coordinates of the atoms in the xyz file.
    """
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(float)
    return symbols, coords


def write_xyz(file_location: str, symbols: np.ndarray, coordinates: np.ndarray) -> None:
    """Write an xyz file given a file location, symbols, and coordinates.

    Parameters
    ----------
    file_location : str
        The path to save the xyz file.
    symbols : np.ndarray
        The atomic symbols of the atoms.
    coordinates : np.ndarray
        The coordinates of the atoms.

    Raises
    ------
    ValueError
        If the number of symbols and coordinates do not match.
    """
    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) "
            f"and number of coordinates ({len(coordinates)}) "
            f"must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write(
                "{}\t{}\t{}\t{}\n".format(
                    symbols[i],
                    coordinates[i, 0],
                    coordinates[i, 1],
                    coordinates[i, 2],
                )
            )