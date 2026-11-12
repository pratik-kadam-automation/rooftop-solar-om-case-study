"""Performance ratio and expected-energy helpers.

PR = final yield / reference yield
  final yield     = AC energy (kWh) / installed DC capacity (kWp)       -> hours
  reference yield = plane-of-array (POA) energy (kWh/m2) / 1 kW/m2     -> hours

Always say which POA data you used and where it was measured.
"""
import argparse

STC_KW_M2 = 1.0


def reference_yield(poa_kwh_m2):
    return poa_kwh_m2 / STC_KW_M2


def final_yield(ac_kwh, dc_kwp):
    return ac_kwh / dc_kwp


def performance_ratio(ac_kwh, dc_kwp, poa_kwh_m2):
    ry = reference_yield(poa_kwh_m2)
    if ry <= 0:
        raise ValueError("POA energy must be positive")
    return final_yield(ac_kwh, dc_kwp) / ry


def expected_energy(dc_kwp, poa_kwh_m2, target_pr):
    """AC energy (kWh) you should see at a given target PR."""
    return dc_kwp * reference_yield(poa_kwh_m2) * target_pr


def ceiling_with_structural_loss(quoted_pr, structural_loss):
    """Realistic PR ceiling when a fixed geometry loss was left out of the quote.

    Example: a quote of 0.95 with a 10% loss from a wrong azimuth gives about 0.855.
    """
    return quoted_pr * (1.0 - structural_loss)


def main():
    ap = argparse.ArgumentParser(description="Performance ratio for a period")
    ap.add_argument("--kwp", type=float, required=True, help="installed DC capacity, kWp")
    ap.add_argument("--ac-kwh", type=float, required=True, help="AC energy in the period, kWh")
    ap.add_argument("--poa-kwh-m2", type=float, required=True, help="POA irradiation in the period, kWh/m2")
    ap.add_argument("--target-pr", type=float, help="optional target PR (0 to 1) to compare against")
    a = ap.parse_args()
    fy = final_yield(a.ac_kwh, a.kwp)
    ry = reference_yield(a.poa_kwh_m2)
    pr = performance_ratio(a.ac_kwh, a.kwp, a.poa_kwh_m2)
    print(f"final yield      {fy:8.2f} h")
    print(f"reference yield  {ry:8.2f} h")
    print(f"performance ratio {pr * 100:7.1f} %")
    if a.target_pr:
        exp = expected_energy(a.kwp, a.poa_kwh_m2, a.target_pr)
        print(f"expected at {a.target_pr * 100:.0f}%   {exp:10.0f} kWh")
        print(f"shortfall        {exp - a.ac_kwh:10.0f} kWh")


if __name__ == "__main__":
    main()
