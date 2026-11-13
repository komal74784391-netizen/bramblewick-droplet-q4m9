"""Two-point calibration helpers for the Droplet dispenser."""

import json
import time


def measure_mass(balance_readings):
    if not balance_readings:
        raise ValueError("no balance readings")
    return sum(balance_readings) / len(balance_readings)


def fit_two_point(points):
    """Fit steps-per-microliter from (command_ul, measured_ul) pairs."""
    low, high = points[0], points[-1]
    if high[1] == low[1]:
        raise ValueError("calibration points are degenerate")
    slope = (high[0] - low[0]) / (high[1] - low[1])
    return {"steps_per_ul": slope, "offset_ul": low[0] - slope * low[1]}


def save(calibration, path="calibration.json"):
    with open(path, "w") as fh:
        json.dump(calibration, fh)
    print("calibration saved", calibration)


if __name__ == "__main__":
    points = [(0.0, 0.0), (10.0, 9.8), (50.0, 49.1)]
    save(fit_two_point(points))
