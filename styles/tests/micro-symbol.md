# Micro Symbol Test

## Should fire (bad examples)

Add 10 uL of buffer. <!-- vale-expect: nucleus.micro-symbol -->

Dilute to 500 uM final concentration. <!-- vale-expect: nucleus.micro-symbol -->

The bead diameter is 2 um. <!-- vale-expect: nucleus.micro-symbol -->

Mix 0.5 uL with 100 uM stock. <!-- vale-expect: nucleus.micro-symbol -->

Dilute tRNA stocks to 35 ug / uL. <!-- vale-expect: nucleus.micro-symbol -->

Dilute tRNA stocks to 35 ug/uL. <!-- vale-expect: nucleus.micro-symbol -->

Dilute tRNA stocks to 0.5 ug / uL. <!-- vale-expect: nucleus.micro-symbol -->

Dilute tRNA stocks to 35 ug / uL / uM. <!-- vale-expect: nucleus.micro-symbol -->

## Mixed representation in compound units (should fire on wrong part)

Dilute tRNA stocks to 35 µg / uL. <!-- vale-expect: nucleus.micro-symbol -->

Dilute tRNA stocks to 35 ug / µL. <!-- vale-expect: nucleus.micro-symbol -->

## Should NOT fire (correct µ symbol)

Add 10 µL of buffer. <!-- vale-clean -->

Dilute to 500 µM final concentration. <!-- vale-clean -->

The bead diameter is 2 µm. <!-- vale-clean -->

Dilute tRNA stocks to 35 µg/µL. <!-- vale-clean -->

## Should NOT fire (non-unit uses of 'um')

Um, that's a good question. <!-- vale-clean -->

Add to the medium before proceeding. <!-- vale-clean -->

The maximum volume is 25 µL. <!-- vale-clean -->

Enzyme activity was measured in units per mg. <!-- vale-clean -->

## Should NOT fire (milli units, not micro)

Dilute to 3.5 mg/mL. <!-- vale-clean -->

Add 100 mM NaCl. <!-- vale-clean -->
