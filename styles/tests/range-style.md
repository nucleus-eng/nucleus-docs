# Range Style Test

## Should fire (bare hyphen in range before unit)

Wavelength range is 225-2400 nm for this detector. <!-- vale-expect: nucleus.range-style -->

Store samples between 4-8 °C during transport. <!-- vale-expect: nucleus.range-style -->

Elute with 50-100 mM imidazole gradient. <!-- vale-expect: nucleus.range-style -->

Run the gel for 45-60 min at 200 V. <!-- vale-expect: nucleus.range-style -->

The fragment is 500-1500 kDa by native PAGE. <!-- vale-expect: nucleus.range-style -->

## Should NOT fire (correct range style, or non-targets)

Wavelength range is 225 nm to 2400 nm for this detector. <!-- vale-clean -->

Store samples between 4 °C to 8 °C during transport. <!-- vale-clean -->

Elute with 50 mM to 100 mM imidazole gradient. <!-- vale-clean -->

Run the gel for 45 min to 60 min at 200 V. <!-- vale-clean -->

The fragment is (500–1500) kDa by native PAGE. <!-- vale-clean -->

The fragment is (225-2400) nm for this detector. <!-- vale-clean -->

Use catalog part number 14-660 for ordering. <!-- vale-clean -->

Add 1-2 drops of indicator solution. <!-- vale-clean -->
