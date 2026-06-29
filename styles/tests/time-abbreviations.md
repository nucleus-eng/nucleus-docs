# Time Abbreviations Test

## Should fire (unabbreviated time units)

Incubate at 37°C for 16 hours. <!-- vale-expect: nucleus.space-before-degree, nucleus.time-abbreviations -->

Rock at room temperature for 30 minutes. <!-- vale-expect: nucleus.time-abbreviations -->

Store frozen pellets for up to 3 months. <!-- vale-expect: nucleus.time-abbreviations -->

Microwave the gel for 30 seconds. <!-- vale-expect: nucleus.time-abbreviations -->

Cultures remain viable for 2 years. <!-- vale-expect: nucleus.time-abbreviations -->

Dry the pellet for 5 days. <!-- vale-expect: nucleus.time-abbreviations -->

## Should NOT fire (already abbreviated, or non-targets)

Incubate at 37 °C for 16 h. <!-- vale-clean -->

Incubate at 37 °C for 16 hr. <!-- vale-expect: nucleus.time-si-substitution -->

Rock at room temperature for 30 min. <!-- vale-clean -->

Store frozen pellets for up to 3 mo. <!-- vale-clean -->

Microwave the gel for 30 s. <!-- vale-clean -->

Microwave the gel for 30 sec. <!-- vale-expect: nucleus.time-si-substitution -->

Take two weeks to make 36 pellets. <!-- vale-clean -->
