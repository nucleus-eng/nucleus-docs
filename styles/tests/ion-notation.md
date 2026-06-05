# Ion Notation Test

## Should fire (bad examples)

The reaction requires 8 mM Mg++. <!-- vale-expect: nucleus.ion-notation -->

This module is highly sensitive to [Mg++]. <!-- vale-expect: nucleus.ion-notation -->

## Should NOT fire (correct notation)

The reaction requires 8 mM Mg2+. <!-- vale-clean -->

This module is highly sensitive to [Mg2+]. <!-- vale-clean -->
