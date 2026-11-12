# SCADA pre-indication

I upgraded the solar SCADA so that a fault shows up before it becomes an outage, with the next action beside it. The
aim was simple: someone who doesn't know solar well can still act, because the faults are already identified and mapped.

| Indicator | What it usually means | First action |
|---|---|---|
| A string starts late versus its peers, on several days | Wet or aged insulation, water near a connector, a loose joint | Inspect the connector and gland. Test insulation resistance once isolated |
| A string never starts | Open fuse, open connector or isolator | Check the fuse, the isolator and the connector |
| Several open string faults on one inverter | Higher risk of inverter failure | Raise the priority and inspect within days |
| High inverter temperature with a derating flag | Cooling problem, dirty vents or overload | Check filters, fans and the cooling unit |
| Performance ratio falling against POA | Soiling | Plan a cleaning and compare before and after |
| Low generation only during a grid outage | Availability, not plant condition | Log the outage and keep it out of the performance figure |

## Design rules I followed

- Every indicator has a meaning, a first action and an owner.
- Show the time, the data quality and the source next to the value.
- Keep outages and curtailment separate from performance.
- Don't clear an alarm until you have confirmed the condition is fixed.
