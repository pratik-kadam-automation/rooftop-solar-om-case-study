# Cost and savings

What the annual maintenance contract (AMC) costs, and what it is worth in units on the electricity bill.

## Inputs

- AMC cost: about 7 lakh rupees a year.
- Tariff: about 15 to 17 rupees a unit all-in, my estimate for an industrial connection in Western India, including
  time-of-day and demand charges.
- Annual generation now: 13 to 16 lakh kWh.
- Performance: about 66% in 2020, about 85 to 89% now.

## Break-even, the safe number

The contract pays for itself if it recovers this many units a year. It needs only the cost and the tariff.

| Tariff | Break-even units a year | Share of annual generation |
|---|---|---|
| 15 rupees | about 46,700 | 2.9 to 3.6% |
| 17 rupees | about 41,200 | 2.6 to 3.2% |

That is roughly 115 to 130 units a day, about 3% of what the plant generates.

## Units recovered, an estimate

Scaling current generation by the change in performance (units recovered = annual units now x (1 - PR before / PR now)):

| Case | Generation now | PR now | Units recovered a year | Value at the matching tariff | Net of AMC |
|---|---|---|---|---|---|
| Low | 13 lakh | 85% | 2.91 lakh | 43.6 lakh at 15 rupees | 36.6 lakh |
| Middle | 14.5 lakh | 87% | 3.50 lakh | 52.5 lakh at 15 rupees | 45.5 lakh |
| High | 16 lakh | 89% | 4.13 lakh | 70.3 lakh at 17 rupees | 63.3 lakh |

On those assumptions the contract returns roughly 6 to 10 times its cost. Run it yourself:

```
python -m tools.savings --amc 700000 --annual-kwh 1450000 --pr-now 0.87 --pr-before 0.66 --tariff 10 15 17
```

## Read this before you quote it

- **Same basis.** The estimate assumes the before and after percentages are measured against the same expected-output
  model and that the sun was comparable. I corrected the model partway through, so this may not hold. Treat it as an
  estimate.
- **Better: real units.** Replace it with actual annual generation for 2020 and for now, adjusted for irradiance if you
  have it. The difference is the real number.
- **The tariff.** The 15 to 17 rupee figure includes demand (MD) charges. Solar units don't reliably reduce maximum demand,
  so the part of the bill that falls with each unit can be lower. Use the energy-linked part of your bill. The table above
  shows a 10 rupee case for that reason.
- **Not everything is the contract.** Some of the recovery came from my own triage, the cooling units and the SCADA
  upgrade, not only the AMC.
- **Break-even is the safe claim.** Even a small part of the recovery covers the contract.
