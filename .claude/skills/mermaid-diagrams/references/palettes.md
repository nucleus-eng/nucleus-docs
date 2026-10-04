# Palettes

Load this only when the user has explicitly asked for colour. The default is
greyscale — see the main skill.

## Greyscale (default)

Two shades carry most diagrams:

```
    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
```

A third, for the node the page is about:

```
    classDef this     fill:#374151,stroke:#111827,color:#ffffff;
```

If you need more than three shades, the diagram is probably encoding something
that wants a second diagram instead.

## Colourblind-safe categorical palette

Okabe–Ito, which is distinguishable under the common forms of colour vision
deficiency. Fill, stroke, and text are given together because a light fill with
default black text fails contrast at small sizes.

| Hue | Fill | Stroke | Text |
| --- | --- | --- | --- |
| Blue | `#e3f0f8` | `#0072B2` | `#063a57` |
| Orange | `#fbe8dc` | `#D55E00` | `#7a2d00` |
| Green | `#def5ee` | `#009E73` | `#00402e` |
| Yellow | `#fdf3d9` | `#E69F00` | `#6b4a00` |
| Purple | `#f2e6f2` | `#CC79A7` | `#5c2a4a` |
| Neutral | `#f1efe8` | `#5f5e5a` | `#2c2c2a` |

```
    classDef groupOne fill:#e3f0f8,stroke:#0072B2,color:#063a57;
    classDef groupTwo fill:#fbe8dc,stroke:#D55E00,color:#7a2d00;
    classDef shared   fill:#def5ee,stroke:#009E73,color:#00402e;
```

## Rules for using colour at all

**Colour encodes exactly one distinction.** Pick the dimension — which group owns
a node, which subsystem it belongs to, confirmed versus proposed — and use hue
for that alone. Encoding two dimensions in hue produces a diagram nobody can
read without the legend open beside it.

**Never use hue as the only carrier of a status claim.** Status is already
carried by edge style and border dash, which survive greyscale printing,
screenshots, and colourblind viewers. Hue may reinforce it; it may not be the
sole signal.

**Abstract or generalised diagrams are always uniform grey.** Colour is for
meaningful distinctions between concrete things. An abstraction has none to show
— if a schematic is showing the *shape* of a system rather than a specific
instance, every node is the same shade.

**Match an existing diagram's palette before inventing one.** Two diagrams of the
same system in different palettes read as two different systems.

## Dark mode

Mermaid's own theming does not follow a site's dark mode reliably, and diagrams
authored for a light background can render close to unreadable against a dark
one. There is no clean fix inside Mermaid.

Two workarounds, in order of preference:

1. **Keep the diagram simple enough that the default theme works in both.** Fewer
   custom `fill` declarations means fewer things to go wrong. A diagram with no
   `classDef` at all inherits the theme and usually survives.
2. **For a diagram that genuinely must look right in both**, hand-author an inline
   SVG with CSS custom properties and a `prefers-color-scheme` block instead of
   using Mermaid. This costs the source-diffability that makes Mermaid worth
   using, so reserve it for a small number of high-visibility diagrams.

If you hit this, say so rather than shipping a diagram that is unreadable for
half the readers.
