# Chemical Notation Tests

## ion-charges.yml — should fire (inline-number ion charges)

The reaction requires 8 mM Mg2+. <!-- vale-expect: nucleus.ion-charges -->

This module is highly sensitive to [Mg2+]. <!-- vale-expect: nucleus.ion-charges -->

The buffer contains Mg++ ions. <!-- vale-expect: nucleus.ion-charges -->

The resin is Ni2+ charged. <!-- vale-expect: nucleus.ion-charges -->

Add Ca2+ to stabilize. <!-- vale-expect: nucleus.ion-charges -->

Use Na+ buffer at pH 7. <!-- vale-expect: nucleus.ion-charges -->

Use K+ buffer at pH 7. <!-- vale-expect: nucleus.ion-charges -->

## ion-charges.yml — should NOT fire (correct Unicode superscripts)

The reaction requires 8 mM Mg²⁺. <!-- vale-clean -->

The buffer contains Ni²⁺ resin. <!-- vale-clean -->

Use Na⁺ buffer. <!-- vale-clean -->

Use K⁺ buffer. <!-- vale-clean -->

## ion-charges.yml — should NOT fire (non-ion uses)

Transform into BL21(DE3) cells. <!-- vale-clean -->

Grade A+ purity reagents. <!-- vale-clean -->

## chemical-notation.yml — should fire (absorbance / OD wavelength labels)

Measure OD600 before harvesting. <!-- vale-expect: nucleus.chemical-notation -->

The ratio A260/A280 should be above 1.8. <!-- vale-expect: nucleus.chemical-notation -->

Check A260 to quantify RNA. <!-- vale-expect: nucleus.chemical-notation -->

The A230 reading was elevated. <!-- vale-expect: nucleus.chemical-notation -->

## chemical-notation.yml — should fire (molecular formulae with ASCII digits)

Resuspend in ddH2O. <!-- vale-expect: nucleus.chemical-notation -->

Add 1 mL H2O to dissolve. <!-- vale-expect: nucleus.chemical-notation -->

H2O2 was used to quench the reaction. <!-- vale-expect: nucleus.chemical-notation -->

Prepare 50 mM MgSO4 solution. <!-- vale-expect: nucleus.chemical-notation -->

Add MgCl2 to 10 mM final. <!-- vale-expect: nucleus.chemical-notation -->

Add CaCl2 to the buffer. <!-- vale-expect: nucleus.chemical-notation -->

Supplement with CO2. <!-- vale-expect: nucleus.chemical-notation -->

## chemical-notation.yml — should NOT fire (already correct subscript forms)

Measure OD₆₀₀ before harvesting. <!-- vale-clean -->

The ratio A₂₆₀/A₂₈₀ should be above 1.8. <!-- vale-clean -->

Resuspend in ddH₂O. <!-- vale-clean -->

The formula is H₂O₂. <!-- vale-clean -->

Prepare 50 mM MgSO₄. <!-- vale-clean -->

## chemical-notation.yml — should NOT fire (non-chemical tokens)

Transform into BL21(DE3) cells. <!-- vale-clean -->

The pET28a vector was used. <!-- vale-clean -->

Express from PURET7-3 promoter. <!-- vale-clean -->

Growth in M9 minimal medium. <!-- vale-clean -->

Strain A19 was used. <!-- vale-clean -->

Connect port A2 to the pump. <!-- vale-clean -->

Lane O2 shows the control. <!-- vale-clean -->

The value is K1 in the table. <!-- vale-clean -->
