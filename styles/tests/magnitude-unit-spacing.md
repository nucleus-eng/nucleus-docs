# Magnitude–Unit Spacing Test

## Should fire (missing space between magnitude and unit)

Spin the lysate at 5000g for 15 min. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Pellet precipitated proteins at 14 000g. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Begin the starter culture at 6pm. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Begin the run at 12pm. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Elute with 500mL of buffer. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Filter through a 0.22µm membrane. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Dilute the stock to 50mM before use. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Incubate at 37°C for 30s on ice. <!-- vale-expect: nucleus.magnitude-unit-spacing, nucleus.space-before-degree -->

Run the SDS-PAGE at 200V for 1h. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Load 10µL of each sample. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Add 100µg of lysozyme to the lysis buffer. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

The protein runs at approximately 25kDa. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Centrifuge at 10000rcf for 10 min. <!-- vale-expect: nucleus.magnitude-unit-spacing, nucleus.thousands-separator -->

Measure absorbance at 660nm. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

Use a 30mm filter membrane. <!-- vale-expect: nucleus.magnitude-unit-spacing -->

## Should NOT fire (correct spacing, or non-targets)

Spin the lysate at 5000 g for 15 min. <!-- vale-clean -->

Pellet precipitated proteins at 14 000 g. <!-- vale-clean -->

Begin the starter culture at 6 pm. <!-- vale-clean -->

Begin the run at 12 pm. <!-- vale-clean -->

Add 50 mg of lysozyme. <!-- vale-clean -->

Dilute to 40 µg per reaction. <!-- vale-clean -->

Resuspend 3.6 gDCM of biomass. <!-- vale-clean -->

Use a 0.5 kg counterweight. <!-- vale-clean -->

Elute with 500 mL of buffer. <!-- vale-clean -->

Filter through a 0.22 µm membrane. <!-- vale-clean -->

Dilute the stock to 50 mM before use. <!-- vale-clean -->

Incubate at 37 °C for 30 s on ice. <!-- vale-clean -->

Run the SDS-PAGE at 200 V for 1 h. <!-- vale-clean -->

Load 10 µL of each sample. <!-- vale-clean -->

The protein runs at approximately 25 kDa. <!-- vale-clean -->

Centrifuge at 10 000 rcf for 10 min. <!-- vale-clean -->

Measure absorbance at 660 nm. <!-- vale-clean -->

Use the 10x buffer concentrate. <!-- vale-clean -->

Perform 3 wash steps. <!-- vale-clean -->
