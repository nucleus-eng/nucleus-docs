# Time SI Substitution Test

## Should fire (non-SI time abbreviations following a number)

Vortex for 30s on / 10hr off cycle. <!-- vale-expect: nucleus.magnitude-unit-spacing, nucleus.time-si-substitution -->

Vortex for 30sec on ice. <!-- vale-expect: nucleus.time-si-substitution -->

Incubate at 37°C for 16hr. <!-- vale-expect: nucleus.space-before-degree, nucleus.time-si-substitution -->

Centrifuge at 4000 rcf for 30sec. <!-- vale-expect: nucleus.time-si-substitution -->

Allow 5hr equilibration time. <!-- vale-expect: nucleus.time-si-substitution -->

## Should NOT fire (SI abbreviations, or non-targets)

Vortex for 30 s on / 10 h off cycle. <!-- vale-clean -->

Incubate at 37 °C for 16 h. <!-- vale-clean -->

Centrifuge at 4000 rcf for 30 s. <!-- vale-clean -->

Rock at room temperature for 30 min. <!-- vale-clean -->

Store for up to 3 mo at -80 °C. <!-- vale-clean -->
