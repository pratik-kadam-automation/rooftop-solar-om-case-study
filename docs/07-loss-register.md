# The loss register: 27 things to check

Each line is something to check for, not proof that it exists on a particular plant. Confirm at site before you count it.

## Modules, DC side and strings (01 to 14)

| # | What goes wrong | What I check |
|---|---|---|
| 01 | **Dust and dirt on the glass.** Dust, pollen and fallout cut the light reaching the cells. | Map dirt by roof zone. Compare a clean panel with a dirty one. Match against the cleaning log and rainfall. |
| 02 | **Hard bird droppings.** Opaque patches shade cells and can create hot areas. | Look for hot spots under deposits. Remove with the module maker's approved, non-abrasive method. |
| 03 | **Mud along the lower frame edge.** Shades the bottom cells and holds moisture. | Check the lower frame lip and drainage. Note zones where it keeps coming back. |
| 04 | **Shade from nearby objects.** Ducts, tanks, parapets, trees and new structures throw moving shadows. | Do a time-of-day shade survey. Compare with string layout and MPPT assignment. |
| 05 | **Light-induced degradation (LID).** Output settles lower after the first exposure to sun. | Compare against module type, warranty tolerance and initial flash data. |
| 06 | **Potential-induced degradation (PID).** Voltage, humidity and heat can drive leakage and loss. | Check string voltage, insulation and grounding. Look at the pattern of degradation across modules. |
| 07 | **Micro-cracks and snail trails.** Cracks from handling, foot traffic or vibration. | Keep people off the modules. Use EL testing when it is justified and compare with string output. |
| 08 | **Hot spots and failed bypass diodes.** Damaged or shaded cells heat up. A failed diode switches off part of a module. | IR scan in good sun and under load. Check the diode and module with the maker's procedure. |
| 09 | **EVA yellowing and delamination.** Ageing encapsulant lets moisture in and speeds corrosion. | Look for bubbles, colour change and edge lifting. Note the warranty position. |
| 10 | **Insulation resistance drop in the monsoon.** Aged or damaged DC insulation leaks when wet, and the inverter can start late. | Test before the monsoon with an approved insulation resistance method, isolated, by qualified people. |
| 11 | **Loose or mismatched MC4 connectors.** Poor crimps or cross-mated types heat up and can arc. | Confirm the same make and type. Inspect the crimp and look at the thermal image. |
| 12 | **String current mismatch.** Uneven dirt, module mismatch or ageing pulls one string down. | Trend string currents in steady sun. Compare strings with the same orientation. |
| 13 | **DC cable losses (I2R).** Long or undersized cable wastes power as heat. | Check conductor size, route length, joints and voltage drop against the design. |
| 14 | **Blown fuses and open isolators.** An open string can hide inside the inverter total. | Use string monitoring or a safe current check. Inspect fuses and isolators. |

## Inverter, AC, design and grid (15 to 27)

| # | What goes wrong | What I check |
|---|---|---|
| 15 | **Corroded AJB or DCDB busbars.** Moisture corrodes terminals and raises resistance. | Check enclosure seals, glands and condensation. Check terminal temperature. |
| 16 | **High earth resistance or a failed SPD.** Weak earthing or a dead surge protector reduces protection and can cause downtime. | Test the earth system. Inspect SPD status against the design and the maker's guidance. |
| 17 | **Inverter thermal derating.** Dusty heatsinks, failed fans or high ambient heat cut the output. | Trend inverter temperature, fan state, ambient conditions and the derating flag. |
| 18 | **DC-to-AC clipping.** Output is capped when DC power exceeds the inverter's AC limit. | Compare clipping time with the design DC/AC ratio. |
| 19 | **MPPT mismatch.** Different roof orientations or string types on one MPPT lose harvest. | Review string-to-MPPT mapping, voltage windows and orientation grouping. |
| 20 | **AC over-voltage trips.** High feeder voltage disconnects inverters at high generation and low load. | Trend voltage at the inverter terminals and the PCC. Review protection events. |
| 21 | **Zero-export or DG sync hunting.** Controller or reverse-power settings hold PV back as load or DG output changes. | Trend load, PV setpoint, DG kW, frequency, the reverse-power relay and controller mode. |
| 22 | **AC panel and transformer losses.** Loose terminations, cable losses and transformer losses. | Safe thermal checks of terminations. Review cable sizing, loading and transformer temperature. |
| 23 | **Sub-optimal tilt.** Tilt affects yearly sun capture, drainage and self-cleaning. | Compare installed tilt with the design yield model and roof limits. |
| 24 | **Azimuth and multi-face mismatch.** South, east, west and north faces have different generation curves. | Benchmark each roof face on its own. Allocate strings and MPPTs to match. |
| 25 | **Inter-row self-shading.** Tight row spacing shades panels when the sun is low. | Do a seasonal shading check and confirm the real shadow windows. |
| 26 | **Module temperature.** Hot cells lose power compared with rated conditions. | Trend module temperature against irradiance. Check rear ventilation and mounting gap. |
| 27 | **Reactive power and power factor.** Reactive demand can limit active power and affect billing. | Trend PF and kvar. Check the inverter capability curve and PCC measurements. |
