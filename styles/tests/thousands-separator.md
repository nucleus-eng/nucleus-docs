# Thousands Separator Test

## Should fire (comma separator, or ungrouped >= 5 digits, near a unit)

Lysozyme, protein ≥40,000 units/mg, lyophilized powder. <!-- vale-expect: nucleus.thousands-separator -->

Pellet nucleic acids at 43721 g for 15 min. <!-- vale-expect: nucleus.thousands-separator -->

## Should NOT fire (NIST-correct, currency, or non-unit numbers)

Lysozyme, protein ≥40 000 units/mg, lyophilized powder. <!-- vale-clean -->

Spin at 4372 g for 10 min. <!-- vale-clean -->

Pellet cultures at 16 000 rcf / 4 °C / 10 min. <!-- vale-clean -->

SimpliAmp Thermal Cycler — $6,580.00. <!-- vale-clean -->

Bench centrifuge, part number 75009521. <!-- vale-clean -->
