# Losses beyond the 27

The register is for faults and conditions you can find and fix. Some real losses are a different kind of thing. They
are not faults, or they are not caused by the plant. Keep them in a separate list so you don't chase them, and so nobody
reads the performance number as one long fault list. No list is complete, and I did not see every item below on this
plant.

| Loss | Why it isn't in the register | What I do |
|---|---|---|
| Grid outages and power failures | The plant is healthy but can't run or export. In the monsoon this was a real share of lost generation | Log outage hours separately and keep them out of the performance figure |
| Curtailment, export caps, zero-export limits | A control setting, not a defect | Log the limited hours and check the controller settings |
| Less sun: cloud, haze, smoke, monsoon | The resource itself | Compare against measured plane-of-array irradiance, not calendar months |
| Temperature, reflection and low-light losses, module tolerance, yearly degradation | Part of every plant | Put them in the expected-output model so they aren't mistaken for faults |
| Inverter efficiency, standby use, transformer and cable losses | Design losses | Check against the datasheets and act only if they exceed design |
| Site damage: nests under panels, animal damage to cables, lightning or surge damage, loose clamps in wind, weeds | Happens around the plant, outside the electrical design | Walk the roof each season and after storms. Photograph and log findings |
| Slow repair: no spares, slow response | Turns a small fault into days of lost generation | Keep critical spares and agree response times |
| Bad measurement: sensor drift, wrong irradiance data, meter scaling, clock errors | The plant is fine and the number is wrong | See the measurement checks in the field guide |

## Why it matters

When I corrected the expected-output model, the plant stopped looking like one big fault. Part of the gap was a fixed
loss from the azimuth, and part was availability from the grid. Only the rest could be recovered by maintenance. See
[azimuth and expected output](04-azimuth-and-expected-output.md).
