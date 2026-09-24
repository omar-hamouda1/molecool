"""Functions for visualization of molecules."""

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

from .atom_data import atom_colors


def draw_molecule(coordinates: np.ndarray, symbols: np.ndarray, draw_bonds: dict | None = None, save_location: str | None = None, dpi: int = 300):
    """Draw a molecule in 3D.

    Parameters
    ----------
    coordinates : np.ndarray
        The coordinates of the atoms.
    symbols : np.ndarray
        The atomic symbols of the atoms.
    draw_bonds : dict, optional
        Dictionary of bonds to draw.
    save_location : str, optional
        Where to save the figure.
    dpi : int, optional
        The DPI of the saved figure.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The axes object of the figure.
    """
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])

    size = np.array(plt.rcParams["lines.markersize"] ** 2) * 200 / (len(coordinates))

    ax.scatter(
        coordinates[:, 0],
        coordinates[:, 1],
        coordinates[:, 2],
        marker="o",
        edgecolors="k",
        facecolors=colors,
        alpha=1,
        s=size,
    )

    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]

            ax.plot(
                [coordinates[atom1, 0], coordinates[atom2, 0]],
                [coordinates[atom1, 1], coordinates[atom2, 1]],
                [coordinates[atom1, 2], coordinates[atom2, 2]],
                color="k",
                linewidth=2,
            )

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax


def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    """Draw a histogram of bond lengths.

    Parameters
    ----------
    bond_list : dict
        A dictionary of bonds (from build_bond_list).
    save_location : str, optional
        Where to save the figure.
    dpi : int, optional
        The DPI of the saved figure.
    graph_min : float, optional
        The minimum bond length for the histogram.
    graph_max : float, optional
        The maximum bond length for the histogram.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The axes object of the figure.
    """
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)

    bins = np.linspace(graph_min, graph_max)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.xlabel("Bond Length (angstrom)")
    plt.ylabel("Number of Bonds")

    ax.hist(lengths, bins=bins)

    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)

    return ax