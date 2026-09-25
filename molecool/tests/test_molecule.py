"""
Unit and regression tests for the molecule module.
"""

import numpy as np
import molecool
import pytest


def test_build_bond_list():
    """Test that build_bond_list finds the correct number of bonds."""

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_build_bond_list_failure():
    """Test that build_bond_list raises ValueError for negative min_bond."""

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, min_bond=-1)