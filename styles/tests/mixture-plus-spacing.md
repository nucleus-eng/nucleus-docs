# Mixture Plus-Spacing Test

## Should fire (missing spaces around '+')

Resuspend in LB+KAN before induction. <!-- vale-expect: nucleus.house-casing, nucleus.mixture-plus-spacing -->

Equilibrate the resin in buffer+TCEP. <!-- vale-expect: nucleus.mixture-plus-spacing -->

Co-expression of GFP+aHly quenches fluorescence. <!-- vale-expect: nucleus.mixture-plus-spacing -->

## Should NOT fire (correct spacing, or non-targets)

Resuspend in LB + Kan before induction. <!-- vale-clean -->

Equilibrate the resin in buffer + TCEP. <!-- vale-clean -->

The reaction requires 8 mM Mg2+. <!-- vale-expect: nucleus.ion-charges -->

This module is sensitive to Mg++. <!-- vale-expect: nucleus.ion-charges -->
