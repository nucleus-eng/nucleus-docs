# Chemical Notation Tests

## ion-charges.yml — should fire (inline-number ion charges)

The reaction requires 8 mM Mg2+.
This module is highly sensitive to [Mg2+].
The buffer contains Mg++ ions.
The resin is Ni2+ charged.
Add Ca2+ to stabilize.
Use Na+ buffer at pH 7.
Use K+ buffer at pH 7.

## ion-charges.yml — should NOT fire (correct Unicode superscripts)

The reaction requires 8 mM Mg²⁺.
The buffer contains Ni²⁺ resin.
Use Na⁺ buffer.
Use K⁺ buffer.

## ion-charges.yml — should NOT fire (non-ion uses)

Transform into BL21(DE3) cells.
Grade A+ purity reagents.

## chemical-notation.yml — should fire (absorbance / OD wavelength labels)

Measure OD600 before harvesting.
The ratio A260/A280 should be above 1.8.
Check A260 to quantify RNA.
The A230 reading was elevated.

## chemical-notation.yml — should fire (molecular formulae with ASCII digits)

Resuspend in ddH2O.
Add 1 mL H2O to dissolve.
H2O2 was used to quench the reaction.
Prepare 50 mM MgSO4 solution.
Add MgCl2 to 10 mM final.
Add CaCl2 to the buffer.
Supplement with CO2.

## chemical-notation.yml — should NOT fire (already correct subscript forms)

Measure OD₆₀₀ before harvesting.
The ratio A₂₆₀/A₂₈₀ should be above 1.8.
Resuspend in ddH₂O.
The formula is H₂O₂.
Prepare 50 mM MgSO₄.

## chemical-notation.yml — should NOT fire (non-chemical tokens)

Transform into BL21(DE3) cells.
The pET28a vector was used.
Express from PURET7-3 promoter.
Growth in M9 minimal medium.
Strain A19 was used.
Connect port A2 to the pump.
Lane O2 shows the control.
The value is K1 in the table.
