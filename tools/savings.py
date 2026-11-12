"""Rough value of a maintenance programme against its cost.

Two ways to look at it:

1. Break-even: how many units a year the contract must recover to pay for itself.
   This needs only the contract cost and a tariff, so it is the safer number.
2. Recovered units (estimate): annual generation now, scaled by the change in
   performance ratio. This assumes the before and after percentages are on the same
   baseline and that irradiance was comparable. Replace it with real before and after
   generation (adjusted for sun) as soon as you have it.

The tariff should be the part of your bill that solar energy actually avoids. Demand
charges (MD) usually don't fall just because you generate more units.
"""
import argparse


def breakeven_units(amc_cost, tariff):
    return amc_cost / tariff


def recovered_units(annual_kwh_now, pr_now, pr_before):
    """Units a year you would not have without the improvement (same-basis assumption)."""
    return annual_kwh_now * (1.0 - pr_before / pr_now)


def lakh(x):
    return f"\u20b9{x / 1e5:,.2f} lakh"


def main():
    ap = argparse.ArgumentParser(description="Maintenance contract cost against units recovered")
    ap.add_argument("--amc", type=float, required=True, help="contract cost per year, rupees")
    ap.add_argument("--annual-kwh", type=float, required=True, help="annual generation now, kWh")
    ap.add_argument("--pr-now", type=float, required=True, help="performance now, 0 to 1")
    ap.add_argument("--pr-before", type=float, required=True, help="performance before, 0 to 1")
    ap.add_argument("--tariff", type=float, nargs="+", required=True, help="rupees per unit, one or more")
    a = ap.parse_args()
    rec = recovered_units(a.annual_kwh, a.pr_now, a.pr_before)
    print(f"Contract cost       {lakh(a.amc)} a year")
    print(f"Annual generation   {a.annual_kwh / 1e5:.2f} lakh kWh")
    print(f"Units recovered     {rec / 1e5:.2f} lakh kWh a year (PR {a.pr_before * 100:.0f}% to {a.pr_now * 100:.0f}%, same basis assumed)\n")
    print(f"{'tariff':>8} {'break-even units':>17} {'share of generation':>20} {'value of recovered':>19} {'net of contract':>16} {'benefit/cost':>13}")
    for t in a.tariff:
        be = breakeven_units(a.amc, t)
        val = rec * t
        print(f"{'Rs ' + format(t, 'g'):>8} {be:17,.0f} {be / a.annual_kwh * 100:19.1f}% {lakh(val):>19} {lakh(val - a.amc):>16} {val / a.amc:12.1f}x")


if __name__ == "__main__":
    main()
