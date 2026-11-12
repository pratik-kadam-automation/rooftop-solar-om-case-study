# Findings

Nine things I found, what they cost and what I did about them.

## 1. Cleaning had no plan
It happened about once a month, then about once in two months. Dirt built up between cleanings and nobody could say
what a cleaning actually recovered. I moved to a planned cycle of about twice a month and measured the effect with
before and after performance ratio (`tools/cleaning_gain.py`). The right interval is whatever your site's soiling
rate says. Don't copy mine.

## 2. No cable maintenance and no preventive maintenance
Nothing was inspected until it failed. I wrote a seasonal calendar (`templates/pm_calendar.csv`) and started keeping
a fault register (`templates/fault_register.csv`).

## 3. Summer overload and heat
The inverters ran hot and overloaded in summer. I added cooling units and put inverter temperature and derating on the
dashboard. No inverter has failed since.

## 4. String maintenance skipped before summer
Loose joints and connector problems went unnoticed until the heat found them. I lost inverters, and in one case a
connector had gone to ground. A pre-summer connector check now comes before the hot months.

## 5. Unresolved string faults come before an inverter failure
The inverters that failed had a history of several string faults left open for months. This is the pattern behind
`tools/inverter_risk.py`. It is a heuristic from one plant, not a validated model.

## 6. The monsoon grid
Power failures in the rainy season cut generation. That is an availability loss, not a plant fault. Log outages
separately and keep them out of the performance figure, or the plant looks worse than it is.

## 7. Strings that pick up late
Moist cable insulation, aged by sun, makes a string start late in the morning in wet weather. I found these by watching
which strings picked up late each day. With little manpower, I took the worst strings out, inspected them, fixed the
open connection or the water near the connector, and reconnected. See [string triage](03-string-triage.md).

## 8. The expected-output model was wrong
The original quote promised 95%. The array could never reach it. About 10% was lost because the panels face west
instead of south, a result of spacing. That moves the realistic ceiling to about 85%. Without that correction I would
have kept chasing a target that could not be met. See
[azimuth and expected output](04-azimuth-and-expected-output.md).

## 9. Monitoring that tells you what to do
I upgraded the solar SCADA to give an early indication of a fault, with the action next to it. See
[SCADA pre-indication](05-scada-pre-indication.md).
