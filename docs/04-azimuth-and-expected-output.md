# Azimuth and the expected-output model

"Performance" is only as honest as the expected-output model behind it.

## What happened

The original quote promised 95%. The array could never reach it. The panels were installed facing west instead of south
because of spacing, which costs about 10%. With that loss included, the realistic ceiling is about 85%.

```
python -c "from tools.pr import ceiling_with_structural_loss as c; print(c(0.95, 0.10))"
0.855
```

Once the target was realistic, the real gaps were visible: soiling, string faults and cooling.

## How to check your own plant

1. Measure the real azimuth and tilt on the roof, then compare with the design.
2. Estimate the size of the loss. This tool gives a clear-sky, relative figure to test a suspicion:

```
python -m tools.azimuth_penalty --lat 19 --lon 73 --tilt 15
latitude 19.0, tilt 15.0 deg, clear-sky, relative to due south
azimuth    90 deg     94.1 %   (-5.9 %)
azimuth   135 deg     98.3 %   (-1.7 %)
azimuth   180 deg    100.0 %   (+0.0 %)
azimuth   225 deg     98.3 %   (-1.7 %)
azimuth   270 deg     94.1 %   (-5.9 %)
```

At a 25 degree tilt the west-facing loss grows to about 9%. The figure I measured at the plant, about 10%, is in the same
range. It also depends on row spacing and shading, so don't read the tool as a yield simulation.

3. Recompute expected output from measured plane-of-array irradiance, not from the quote.
4. Separate two questions: is the plant underperforming, or was the target unrealistic?
5. Record the old and the new baseline, with the date. Don't change the baseline quietly.
