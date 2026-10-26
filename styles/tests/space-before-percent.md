# Space Before Percent Test

## Should fire (missing space before the percent sign)

Add 25% glycerol to the stock. <!-- vale-expect: nucleus.space-before-percent -->

Keep the glycerol below ~5% of the volume. <!-- vale-expect: nucleus.space-before-percent -->

The result held at ≥ 90% across three runs. <!-- vale-expect: nucleus.space-before-percent -->

Works from 4–20% in the set gel. <!-- vale-expect: nucleus.space-before-percent -->

A small fraction (12%) was lost. <!-- vale-expect: nucleus.space-before-percent -->

At 0.25% the signal drops. <!-- vale-expect: nucleus.space-before-percent -->

25% of the reaction is pre-expressed protein. <!-- vale-expect: nucleus.space-before-percent -->

## Should NOT fire (correct, or not a unit value)

Add 25 % glycerol to the stock. <!-- vale-clean -->

Keep the glycerol below ~5 % of the volume. <!-- vale-clean -->

See the [catalog entry](https://example.com/Tubes%2C-Handling/Corning%C2%AE) for the part. <!-- vale-clean -->

The `100%` literal is code and is not linted. <!-- vale-clean -->

:width: 75% <!-- vale-clean -->
