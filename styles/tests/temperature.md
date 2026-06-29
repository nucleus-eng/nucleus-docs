# Temperature Test

## Simple tests

Incubate at 37 degC for 1 hour. <!-- vale-expect: nucleus.time-abbreviations, nucleus.units -->

Cool samples to 4 degrees C before proceeding. <!-- vale-expect: nucleus.units -->

Store at -20 degrees Celsius overnight. <!-- vale-expect: nucleus.units -->

The reaction runs at 30 deg C. <!-- vale-expect: nucleus.units -->

Set the thermocycler to 95C for denaturation. <!-- vale-miss: nucleus.degrees-symbol (bare digit+C not yet detected by rule) -->

Hold at 72 C for extension. <!-- vale-miss: nucleus.degrees-symbol (bare digit+C not yet detected by rule) -->

We use vitamin C in the buffer. <!-- vale-clean -->

See option C for details. <!-- vale-clean -->

The correct way: incubate at 37 °C. <!-- vale-clean -->

## No false positives on figure/step labels (correctly not flagged)

See Figure 2C for the gel image. <!-- vale-clean -->

Refer to Step 1C in the protocol. <!-- vale-clean -->

Lane 3C shows the control band. <!-- vale-clean -->
