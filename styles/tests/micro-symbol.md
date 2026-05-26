# Micro Symbol Test

## Should fire (bad examples)

Add 10 uL of buffer.
Dilute to 500 uM final concentration.
The bead diameter is 2 um.
Mix 0.5 uL with 100 uM stock.
Dilute tRNA stocks to 35 ug / uL.
Dilute tRNA stocks to 35 ug/uL.
Dilute tRNA stocks to 0.5 ug / uL.
Dilute tRNA stocks to 35 ug / uL / uM.

## Mixed representation in compound units (should fire on wrong part)

Dilute tRNA stocks to 35 µg / uL.
Dilute tRNA stocks to 35 ug / µL.

## Should NOT fire (correct µ symbol)

Add 10 µL of buffer.
Dilute to 500 µM final concentration.
The bead diameter is 2 µm.
Dilute tRNA stocks to 35 µg / µL.

## Should NOT fire (non-unit uses of 'um')

Um, that's a good question.
Add to the medium before proceeding.
The maximum volume is 25 µL.
Enzyme activity was measured in units per mg.

## Should NOT fire (milli units, not micro)

Dilute to 3.5 mg/mL.
Add 100 mM NaCl.
