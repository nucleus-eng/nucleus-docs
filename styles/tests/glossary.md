# Glossary Test

## Collapses — the refused word denotes something else (error)

Encapsulate the cargo in a liposome. <!-- vale-clean -->

Encapsulate the cargo in a vesicle. <!-- vale-expect: glossary.collapses -->

A Conflict is computed from a sensitivity and an imposition. <!-- vale-clean -->

The CPRG incompatibility was asserted on nine pages. <!-- vale-expect: glossary.collapses -->

## Prefer — house consistency, case-insensitive (warning)

DevStudio ran for three weeks. <!-- vale-clean -->

DevCell Studio ran for three weeks. <!-- vale-expect: glossary.prefer -->

Resuspend in ultrapure water. <!-- vale-clean -->

Resuspend in milliQ water. <!-- vale-expect: glossary.prefer -->

Resuspend in MilliQ water. <!-- vale-expect: glossary.prefer -->

Each integration path was walked once. <!-- vale-clean -->

Each leg was walked once. <!-- vale-expect: glossary.prefer -->

## Prefer, case-sensitive — Node is a proper noun (warning)

The Chicago Node built it. <!-- vale-clean -->

The Chicago node built it. <!-- vale-expect: glossary.prefer-cased -->

The Chicago-node built it. <!-- vale-expect: glossary.prefer-cased -->

## Why that rule names a Node: a diagram node is not one, and 7 of 9 uses meant the diagram

It is not yet a diagram node. <!-- vale-clean -->

Follow the ALG node in the process-dependency graph. <!-- vale-clean -->

Each node carries its own edge into this one. <!-- vale-clean -->

## Refused in the glossary, deliberately never a rule — each collides with a heading, a filename or ordinary English

Every module page carries an Expected Behavior section. <!-- vale-clean -->

The composition source is spec.yml, beside spec.md. <!-- vale-clean -->

The London demo used a different lipid composition. <!-- vale-clean -->

This is an Analyte, so it is not a constituent of anything. <!-- vale-clean -->

It belongs under Prerequisite Documentation. <!-- vale-clean -->
