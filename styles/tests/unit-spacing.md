# Unit Spacing Test

## Should fire (spaces around '/' in compound unit expressions)

Dilute tRNAs to 40 ng / µL in nuclease-free water. <!-- vale-expect: nucleus.unit-spacing -->

Prepare a 20 ng / µL sample from stock. <!-- vale-expect: nucleus.unit-spacing -->

Dilute to 35 µg / µL as a 10x working stock. <!-- vale-expect: nucleus.unit-spacing -->

The conversion factor is 40 mg / mL per A260 unit. <!-- vale-expect: nucleus.unit-spacing -->

Add substrate at 10 µM / mL to the reaction. <!-- vale-expect: nucleus.unit-spacing -->

Stock concentration is 100 ng / mL. <!-- vale-expect: nucleus.unit-spacing -->

## Should NOT fire (correct — no spaces around '/')

Dilute tRNAs to 40 ng/µL in nuclease-free water. <!-- vale-clean -->

Prepare a 20 ng/µL sample from stock. <!-- vale-clean -->

Dilute to 35 µg/µL as a 10x working stock. <!-- vale-clean -->

The conversion factor is 40 mg/mL per A260 unit. <!-- vale-clean -->

## Should NOT fire (non-unit expressions with '/')

Pre-run gels at 100 V / 30 min. <!-- vale-clean -->

Run the gel at 125V / 2.5 hr. <!-- vale-clean -->

Incubate at 65°C / 3 min then hold at 4°C. <!-- vale-clean -->

See Figure 2 / Panel B for details. <!-- vale-clean -->

Mix at a ratio of 1 / 10 dilution. <!-- vale-clean -->
