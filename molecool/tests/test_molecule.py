"""
Unit and regression tests for the molecule module.
"""

import numpy as np
import molecool
import pytest


@pytest.fixture
def methane_molecule():
    """Fixture for the methane molecule."""

    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4],
    ])

    return symbols, coordinates


def test_build_bond_list(methane_molecule):
    """Test that build_bond_list finds the correct number of bonds."""

    symbols, coordinates = methane_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == pytest.approx(1.4)


def test_build_bond_list_failure(methane_molecule):
    """Test that build_bond_list raises ValueError for negative min_bond."""

    symbols, coordinates = methane_molecule

    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, min_bond=-1)