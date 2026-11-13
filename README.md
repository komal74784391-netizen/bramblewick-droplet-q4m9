# Bramblewick Droplet

Open-source design package for the Droplet single-channel micro-dispenser.

## Implementation

Droplet uses a NEMA-8 stepper driven by a TMC2208 carrier, with a peristaltic
pump head and a magnetic home switch. The driver revision B board integrates
the stepper carrier, the RP2040 controller and a 12 V input protection stage on
one PCB.

- `hardware/` - KiCad schematic and board layout for driver revision B.
- `firmware/` - MicroPython control loop, calibration and plate routines.
- `enclosure/` - printable pump mount and reservoir bracket.
- `docs/` - assembly notes.

## Build

Flash `firmware/main.py` and `firmware/calibration.py` onto the RP2040 module,
then run the two-point calibration from the serial console. Calibration values
are stored in `calibration.json` on the controller.

The pump head and tubing are standard 3 mm silicone parts.
