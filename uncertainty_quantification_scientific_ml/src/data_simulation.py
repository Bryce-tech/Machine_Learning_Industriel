"""Synthetic data generation for a small aerodynamic surrogate model."""

from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_aerodynamic_data(n_samples: int = 320, random_state: int = 42) -> pd.DataFrame:
    """Create a synthetic dataset with a simplified lift coefficient."""

    rng = np.random.default_rng(random_state)

    n_main = int(0.8 * n_samples)
    n_edge = n_samples - n_main

    angle_main = rng.uniform(-4.0, 10.0, size=n_main)
    angle_edge = rng.uniform(10.0, 15.0, size=n_edge)
    angle_of_attack_deg = np.concatenate([angle_main, angle_edge])

    mach_number = rng.uniform(0.25, 0.85, size=n_samples)
    temperature_k = rng.normal(loc=288.0, scale=12.0, size=n_samples)
    temperature_k = np.clip(temperature_k, 255.0, 320.0)
    geometry_factor = rng.uniform(0.85, 1.15, size=n_samples)

    alpha_rad = np.deg2rad(angle_of_attack_deg)
    noise_std = 0.018 + 0.014 * np.abs(angle_of_attack_deg - 4.0) / 16.0
    measurement_noise = rng.normal(loc=0.0, scale=noise_std)

    lift_coefficient = (
        0.18
        + 4.7 * alpha_rad
        - 1.45 * alpha_rad**2
        + 0.62 * mach_number
        - 0.28 * (mach_number - 0.55) ** 2
        + 0.0022 * (temperature_k - 288.0)
        + 0.32 * (geometry_factor - 1.0)
        + 0.09 * np.sin(3.0 * alpha_rad)
        - 0.07 * mach_number * alpha_rad
        + measurement_noise
    )

    data = pd.DataFrame(
        {
            "angle_of_attack_deg": angle_of_attack_deg,
            "mach_number": mach_number,
            "temperature_k": temperature_k,
            "geometry_factor": geometry_factor,
            "lift_coefficient": lift_coefficient,
        }
    )

    return data.sample(frac=1.0, random_state=random_state).reset_index(drop=True)
