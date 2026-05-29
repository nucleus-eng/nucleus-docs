// pubmatter pinned to 0.2.2 — 0.2.0 panics under typst >=0.8 (its `load`
// does string-based `type()` comparisons that newer typst broke). See #10.
#import "@preview/pubmatter:0.2.2"

#let bnextTitle = "Nucleus Protocols";
#let bnextLogo = image("logo.png");

#let leftCaption(it) = context {
  set text(size: 8pt)
  set align(left)
  set par(justify: true)
  text(weight: "bold")[#it.supplement #it.counter.display(it.numbering)]
  "."
  h(4pt)
  set text(fill: black.lighten(20%), style: "italic")
  it.body
}

#let fullwidth(it) = {
  place(top, dx: -30%, float: true, scope: "parent",
  box(width: 135%, it))
}

#let smallTableStyle = (
  map-cells: cell => {
    if (cell.y == 0) {
      return (..cell, content: strong(text(cell.content, 5pt)))
    }
    (..cell, content: text(cell.content, 5pt))
  },
  auto-vlines: false,
  map-hlines: line => {
    if (line.y == 0 or line.y == 1) {
      line.stroke = gray + 1pt;
    } else {
      line.stroke = 0pt;
    }
    return line
  },
)

#let template(
  frontmatter: (),
  heading-numbering: "1.1.1",
  kind: none,
  paper-size: "us-letter",
  // The path to a bibliography file if you want to cite some external works.
  page-start: none,
  max-page: none,
  // The paper's content.
  body
) = {
  let fm = pubmatter.load(frontmatter)
  let dates;
  //if ("date" in fm and type(fm.date) == datetime) {
  //  dates = ((title: "Published", date: fm.date),)
  // } else if (type(date) == dictionary) {
  //   dates = (date,)
  //} else {
  //  dates = date
  //}

  // Set document metadata.
  set document(title: fm.title, author: fm.authors.map(author => author.name))
  let theme = (color: rgb("#006837"), font: "Noto Sans")
  if (page-start != none) {counter(page).update(page-start)}
  state("THEME").update(theme)
  set page(
    paper: paper-size,
    margin: (left: 25%),
    header: pubmatter.show-page-header(fm),
    footer: block(
      width: 100%,
      stroke: (top: 1pt + gray),
      inset: (top: 8pt, right: 2pt),
      context [
        #set text(font: theme.font, size: 9pt, fill: gray.darken(50%))
        //#pubmatter.show-spaced-content((
        //  if("venue" in fm) {emph(fm.venue)} //,
        // if("date" in fm and fm.date != none) {fm.date.display("[month repr:long] [day], [year]")}
        //))
        #h(1fr)
        #counter(page).display()
      ]
    ),
  )
  let logo = [
    #bnextLogo
    #v(-13pt)
    #align(center)[
      #text(size: 15pt, weight: "bold", fill: theme.color, font: theme.font, bnextTitle)
    ]
    #v(13pt)
  ]

  show link: it => [#text(fill: theme.color)[#it]]
  show ref: it => {
    if (it.element == none)  {
      // This is a citation showing 2024a or [1]
      show regex("([\d]{1,4}[a-z]?)"): it => text(fill: theme.color, it)
      it
      return
    }
    // The rest of the references, like `Figure 1`
    set text(fill: theme.color)
    it
  }

  // Set the body font.
  set text(font: theme.font, size: 9pt)
  // Configure equation numbering and spacing.
  set math.equation(numbering: "(1)")
  show math.equation: set block(spacing: 1em)

  // Configure lists. Lab-ready protocols are checklists: render every list
  // marker as an empty checkbox so each step/substep can be ticked at the bench.
  set enum(indent: 10pt, body-indent: 9pt)
  set list(
    indent: 10pt,
    body-indent: 9pt,
    marker: box(width: 0.7em, height: 0.7em, stroke: 0.6pt + black, radius: 1pt, inset: 0pt),
  )

  // Configure headings.
  set heading(numbering: heading-numbering)
  show heading: it => context {
    let loc = here()
    // Find out the final number of the heading counter.
    let levels = counter(heading).at(loc)
    set text(10pt, weight: 400)
    if it.level == 1 [
      // First-level headings are centered smallcaps.
      // We don't want to number of the acknowledgment section.
      #let is-ack = it.body in ([Acknowledgment], [Acknowledgement],[Acknowledgments], [Acknowledgements])
      // #set align(center)
      #set text(if is-ack { 10pt } else { 12pt })
      #show: smallcaps
      #show: block.with(above: 20pt, below: 13.75pt, sticky: true)
      #if it.numbering != none and not is-ack {
        numbering(heading-numbering, ..levels)
        [.]
        h(7pt, weak: true)
      }
      #it.body
    ] else if it.level == 2 [
      // Second-level headings are run-ins.
      #set par(first-line-indent: 0pt)
      #set text(style: "italic")
      #show: block.with(above: 15pt, below: 13.75pt, sticky: true)
      #if it.numbering != none {
        numbering(heading-numbering, ..levels)
        [.]
        h(7pt, weak: true)
      }
      #it.body
    ] else [
      // Third level headings are run-ins too, but different.
      #show: block.with(above: 15pt, below: 13.75pt, sticky: true)
      #if it.level == 3 {
        numbering(heading-numbering, ..levels)
        [. ]
      }
      _#(it.body)_
    ]
  }
  if (logo != none) {
    place(
      top,
      dx: -33%,
      float: false,
      box(
        width: 27%,
        {
          if (type(logo) == content) {
            logo
          } else {
            image(logo, width: 100%)
          }
        },
      ),
    )
  }


  // Title and subtitle
  pubmatter.show-title-block(fm)

  let corresponding = fm.authors.filter((author) => "email" in author).at(0, default: none)
  let margin = (
    if corresponding != none {
      (
        title: "Correspondence to",
        content: [
          #corresponding.name\
          #link("mailto:" + corresponding.email)[#corresponding.email]
        ],
      )
    },
//    (
//      title: [Open Access #h(1fr) #pubmatter.show-license-badge(fm)],
//      content: [
//        #set par(justify: true)
//        #set text(size: 7pt)
//        #pubmatter.show-copyright(fm)
//      ]
//    ),
    if fm.at("github", default: none) != none {
      (
        title: "Data Availability",
        content: [
          Source code available:\
          #link(fm.github, fm.github)
        ],
      )
    },
  ).filter((m) => m != none)

  place(
    left + bottom,
    dx: -33%,
    dy: -10pt,
    box(width: 27%, {
      set text(font: theme.font)
      if (kind != none) {
        show par: set par(spacing: 0em)
        text(11pt, fill: theme.color, weight: "semibold", smallcaps(kind))
        parbreak()
      }
      if (dates != none) {
        let formatted-dates

        grid(columns: (40%, 60%), gutter: 7pt,
          ..dates.zip(range(dates.len())).map((formatted-dates) => {
            let d = formatted-dates.at(0);
            let i = formatted-dates.at(1);
            let weight = "light"
            if (i == 0) {
              weight = "bold"
            }
            return (
              text(size: 7pt, fill: theme.color, weight: weight, d.title)//,
              //text(size: 7pt, d.date.display("[month repr:short] [day], [year]"))
            )
          }).flatten()
        )
      }
      v(2em)
      grid(columns: 1, gutter: 2em, ..margin.map(side => {
        text(size: 7pt, {
          if ("title" in side) {
            text(fill: theme.color, weight: "bold", side.title)
            [\ ]
          }
          set enum(indent: 0.1em, body-indent: 0.25em)
          set list(indent: 0.1em, body-indent: 0.25em)
          side.content
        })
      }))
    }),
  )

  show par: set par(spacing: 1.4em, justify: true)

  show raw.where(block: true): (it) => {
      set text(size: 6pt)
      set align(left)
      block(sticky: true, fill: luma(240), width: 100%, inset: 10pt, radius: 1pt, it)
  }
  show figure.caption: leftCaption
  show figure.where(kind: "table"): set figure.caption(position: top)
  set figure(placement: none)

  set bibliography(title: text(10pt, "References"), style: "ieee")
  show bibliography: (it) => {
    set text(7pt)
    set block(spacing: 0.9em)
    it
  }

  // Display the paper's contents.
  body
}
