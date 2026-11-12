# String triage

How I protected the inverters when there wasn't enough manpower to fix everything at once.

> **Safety.** PV DC circuits can stay live in daylight. Isolate, lock out and test before touching anything, use
> approved instruments, follow your site procedure and the maker's instructions, and let only qualified people do
> the work.

## Steps

1. **Find the late strings.** Each day, look at when every string first carries current, compared with the other strings
   on the same inverter. `tools/string_pickup.py` does this from a CSV export.
2. **Rank them.** Strings that never start come first, then the ones that are late most often and by the most minutes.
3. **Isolate and inspect the worst first.** Look for an open connection, water collecting near the connector, damaged
   insulation or a loose joint.
4. **Repair, test, reconnect.** Test insulation resistance before putting the string back. Log what you found.
5. **Count repeats per inverter.** A string that keeps coming back, or several strings on one inverter, is the warning
   sign. `tools/inverter_risk.py` ranks inverters by open faults.

## The trade-off

While a string is out, you lose its energy. I accepted that to protect the inverter, because losing an inverter costs
more energy and more time than one string. Within about a year the plant came back up to around 75%. Weigh the same
trade-off for your own plant. Don't leave faults open and hope.

## Run it

```
python -m tools.string_pickup data/sample/string_currents.csv
python -m tools.inverter_risk data/sample/fault_log.csv --as-of 2025-06-10
```
