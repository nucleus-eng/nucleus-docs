# Glossary Test

## Prefer — house consistency, case-insensitive (warning)

DevStudio ran for three weeks. <!-- vale-clean -->

DevCell Studio ran for three weeks. <!-- vale-expect: glossary.prefer -->

Resuspend in ultrapure water. <!-- vale-clean -->

Resuspend in milliQ water. <!-- vale-expect: glossary.prefer -->

Resuspend in MilliQ water. <!-- vale-expect: glossary.prefer -->

The assay is colorimetric. <!-- vale-clean -->

The assay is colormetric. <!-- vale-expect: glossary.prefer -->

## Prefer, case-sensitive — Node is a proper noun (warning)

The Chicago Node built it. <!-- vale-clean -->

The Chicago node built it. <!-- vale-expect: glossary.prefer-cased -->

The Chicago-node built it. <!-- vale-expect: glossary.prefer-cased -->

The London node built it. <!-- vale-expect: glossary.prefer-cased -->

## Why that rule names a Node: a diagram node is not one

It is not yet a diagram node. <!-- vale-clean -->

Follow the ALG node in the process-dependency graph. <!-- vale-clean -->

## Vesicle is the umbrella term and is never refused

Encapsulate the cargo in a vesicle. <!-- vale-clean -->

Encapsulate the cargo in a liposome. <!-- vale-clean -->

A giant unilamellar vesicle (GUV) is one size class of vesicle. <!-- vale-clean -->

Not every vesicle is a liposome. <!-- vale-clean -->

## Accepted or prose-only, deliberately never a rule

Each leg was walked once. <!-- vale-clean -->

The LacZ and theophylline incompatibility was asserted on one page. <!-- vale-clean -->

Every module page carries an Expected Behavior section. <!-- vale-clean -->

The composition source is spec.yml, beside spec.md. <!-- vale-clean -->

The London demo used a different lipid composition. <!-- vale-clean -->

This is an Analyte, so it is not a constituent of anything. <!-- vale-clean -->

It belongs under Prerequisite Documentation. <!-- vale-clean -->

## A quoted span is exempt

The notebook reads "the Chicago node built it" in the original entry. <!-- vale-clean -->
