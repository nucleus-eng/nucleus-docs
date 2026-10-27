# Default Unit Required Test

## Should fire (percent weight per volume with no default unit before it)

Dissolve agarose to 1.1 % w/v in water. <!-- vale-expect: docs.default-unit-required -->

Dissolve agarose to 1.2 % (w/v) in water. <!-- vale-expect: docs.default-unit-required -->

Dissolve agarose to 1.3% (w/v) in water. <!-- vale-expect: docs.default-unit-required, nucleus.space-before-percent -->

Dissolve agarose to 1.4 %w/v in water. <!-- vale-expect: docs.default-unit-required -->

A 28 mg/mL stock, 2.9 % w/v, is diluted. <!-- vale-expect: docs.default-unit-required -->

30 % w/v sucrose is layered under the sample. <!-- vale-expect: docs.default-unit-required -->

1.5 % w/v is the stock. <!-- vale-miss: docs.default-unit-required (a decimal at the start of a block, followed by more text, is not matched) -->

## Should NOT fire (default unit first, or not a w/v percent)

Use 10 mg/mL (1.6 % w/v) agarose. <!-- vale-clean -->

Use 11 mg/mL (1.7 % (w/v)) agarose. <!-- vale-clean -->

Stock is 28 mg/mL (2.8 % w/v) and final is 7 mg/mL (0.7 % w/v). <!-- vale-clean -->

Use 13 mg/mL (15 % w/v) agarose. <!-- vale-clean -->

Use 12 mg/mL agarose, no percent. <!-- vale-clean -->

Add 5 % v/v glycerol. <!-- vale-clean -->

Add 0.2 % casamino acids. <!-- vale-clean -->
