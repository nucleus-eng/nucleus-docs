# Grow and Induce Expression Strains

<aside>
<img src="https://www.notion.so/icons/light-bulb_gray.svg" alt="https://www.notion.so/icons/light-bulb_gray.svg" width="40px" /> **Getting Started**

</aside>

You want to purify proteins. First, you’re going to have to make some. We make proteins using bacterial strains that carry our protein of interest on an expression plasmid (here: pET28a). These expression plasmids put a gene of interest under the transcription of an inducible promoter (e.g., pT7). This allows us to first (1) grow our bacteria quickly to a high density, without the metabolic load of making a lot of proteins, then to (2) induce the overexpression of our protein of interest. Making so much protein is toxic to the cells, so we only want to induce expression once our culture is grown out (OD600 ~0.5).

<aside>
<img src="https://www.notion.so/icons/wrench_gray.svg" alt="https://www.notion.so/icons/wrench_gray.svg" width="40px" /> **Materials and Equipment**

</aside>

| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| ***Media*** |  |  |  |  |  |  |
| LB | Luria Broth (Miller's LB Broth), Non-Sterile, 6.8 - 7.2, Molecular Biology Grade, suitable for regular E.coli culture, Powder | Sigma-Aldrich | L3522-1KG | $221 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/l3522)] |
| IPTG | Isopropyl β-D-thiogalactoside (IPTG), Powder, ≥99% (TLC), ≤0.1% Dioxane | Sigma-Aldrich | I6758-1G | $89.90 | -25C to -15C | [[link](https://www.sigmaaldrich.com/US/en/product/sial/i6758)] |
| Kanamycin | BioReagent Kanamycin sulfate, 
≥750 ug/mg, From Streptomyces kanamyceticus, Suitable for cell culture, 
Suitable for plant cell culture, Powder | Sigma-Aldrich | K1377-1G | $47.70 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/sigma/k1377)] |
|  |  |  |  |  |  |  |
| ***Consumables*** |  |  |  |  |  |  |
| Culture tubes | Culture Tube, PS, 14mL, 18x95mm, Sterile, TC Treated, w/ Snap (Vent) Cap | Greiner Bio-One | 191160 | $258.15 | 4C to 30C | [link] |
| 50 mL conical tubes | Corning® 50 mL Polypropylene Centrifuge Tubes, Sterile, Racked, CentriStar™ Cap | Corning | 430828 | $436.88 | 4C to 30C | [[link](https://ecatalog.corning.com/life-sciences/b2b/US/en/Liquid-Handling/Tubes%2C-Liquid-Handling/Centrifuge-Tubes/Corning%C2%AE-50-mL-Centrifuge-Tubes/p/430828)] |
|  |  |  |  |  |  |  |
| ***Flasks*** |  |  |  |  |  |  |
| 250 mL baffled flasks | PYREX® 250 mL Delong Shaker Erlenmeyer Flask with Baffles | Pyrex | 4444-250 | $188.26 | 4C to 30C | [[link](https://ecatalog.corning.com/life-sciences/b2c/US/en/Bioprocess-and-Scale-up/Erlenmeyer-Flasks/Erlenmeyer-Flasks,-Glass/PYREX%C2%AE-Flask-with-Baffles/p/4444-250)] |
| flask closures | Chemglass Life Sciences Closure, 38mm, Stainless Steel | Chemglass Life Sciences | Chemglass Life Sciences Closure, 38mm, Stainless Steel | $100.75 | 4C to 30C | [[link](https://www.fishersci.com/shop/products/sst-closure-38mm-lanced-1/501215156)] |
|  |  |  |  |  |  |  |
| ***Equipment*** |  |  |  |  |  |  |
| Shaking incubator | New Brunswick Innova 4430 Incubator Shaker | New Brunswick | - | - | 4C to 30C | discontinued |
| Microvolume spectrophotometer | DeNovix DS-11+ Spectrophotometer | DeNovix | DS-11+ | unlisted | 4C to 30C | [[link](https://www.denovix.com/products/ds-11-fx-spectrophotometer-fluorometer/)] |
| Bench centrifuge | Sorvall X4R Pro-MD, IVD Certified | Sorvall | 75009521 | $18,270.00 | 4C to 30C | [[link](https://www.thermofisher.com/order/catalog/product/75009521)] |
| -20C Freezer | TSX Series High-Performance -20°C Manual Defrost Freezers | Thermo Scientific | TSX2320FA | unlisted | 4C to 30C | [[link](https://www.thermofisher.com/order/catalog/product/TSX2320FA)] |
| -80C Freezer | TSX Series Ultra-Low Freezers | Thermo Scientific | TSX60086A | unlisted | 4C to 30C | [[link](https://www.thermofisher.com/order/catalog/product/TSX60086A)] |

<aside>
<img src="https://www.notion.so/icons/merge_gray.svg" alt="https://www.notion.so/icons/merge_gray.svg" width="40px" /> **Prerequisite Protocols**

</aside>

- [ ]  Prepare selective media and inducer: [Make Protein Purification Buffers and Media](https://www.notion.so/Make-Protein-Purification-Buffers-and-Media-9d2ac519c37e4300b7e2c01bf74515a6?pvs=21).

<aside>
<img src="https://www.notion.so/icons/iterate_gray.svg" alt="https://www.notion.so/icons/iterate_gray.svg" width="40px" /> **Protocol**

</aside>

- [ ]  Prep overnight cultures.
    - [ ]  Add 5 mL LB + Kanamycin (50 ug / mL) to 15 mL culture tubes and label.
    - [ ]  Innoculate your tubes with your expression strain working stock using a pipette tip.
    - **Notes - you can use glycerol stocks OR fresh colonies as working stocks**
        
        We first need to prepare bacterial cultures to induce. We will work from 5 mL overnight cultures of our expression strains and backdilute them the next day. In order to prepare these overnight cultures, we need stocks of bacteria.
        
        We work from 100 uL aliquots of our glycerol stocks, frozen in PCR strip tubes. When seeding our overnights with bacteria, we poked each glycerol stock with a pipette tip and ejected the tip into culture tubes (more details below).
        
        Optionally, you can work from individual colonies by streaking out your bacterial stocks onto selective plates (here: Kanamycin at 50 ug / mL). Working from colonies assures that your bulk outgrowth will have come from a single colony forming unit, which may improve plasmid stability over the course of protein expression.
        
    - [ ]  Incubate cultures overnight at 37C / 225 rpm for between 12 hrs and 16 hrs.
- [ ]  Perform bulk outgrowth.
    - [ ]  Back dilute overnight cultures 1:1000 into fresh media (e.g., add 100 uL of overnight and 100 mL LB with Kanamycin to 250 mL Erlenmeyer flasks).
    - **Notes: leave ≥ 2.5x culture volume in headroom!**
        
        Bacteria need breathing room! Oxygenation matters, plus shaking can spill overfilled flasks. Make sure to leave at 2.5 culture volumes worth of headroom. E.g., 
        
        100 mL culture in a 250 mL flask
        
        500 mL culture in a 2 L flask
        
    - [ ]  Incubate back diluted cultures at 37C / 225 rpm / to mid-log phase (OD600 between 0.4 and 0.6 ~ 3.5 hrs).
- [ ]  Induce protein expression.
    - [ ]  At mid-log phase, induce your cultures with IPTG to 500 uM (e.g., add 100 uL of IPTG (0.5M) to a 100 mL culture).
    - [ ]  Incubate induced cultures at 37C / 225 rpm / 4 hr to allow cells to express proteins.
- [ ]  Centrifuge cells and freeze pellets.
    - [ ]  While incubating your induced cultures, pre-chill your centrifuge and rotor to 4C.
    - [ ]  Harvest your cultures by centrifuging at 3200 rcf / 4C / 30 min.
    - [ ]  Decant supernatant and reserve pellets.
    - [ ]  Weigh pellets to calculate your biomass yield (gDCM / L).
    - [ ]  Store pellets at -80C and allow to freeze (at least overnight)
    - **Notes: take a break!**
        
        Frozen bacterial pellets can be stored at -80C for extended periods (up to at least 3 months). There is no need to rush directly into purifying proteins from these pellets. We find that a nice workflow for making PURE proteins is to take two weeks to make 36 bacterial pellets, then purify those pellets at a later point.
        

<aside>
<img src="https://www.notion.so/icons/book_gray.svg" alt="https://www.notion.so/icons/book_gray.svg" width="40px" /> **Resources and References**

</aside>

- Papers
    - Original PURE paper
    
    [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802)
    
    - OnePot PURE
    
    [A Simple, Robust, and Low-Cost Method To Produce the PURE Cell-Free System](https://doi.org/10.1021/acssynbio.8b00427)
    
    [OnePot PURE Cell-Free System | Text Page](https://dx.doi.org/10.3791/62625)
    

<aside>
<img src="https://www.notion.so/icons/megaphone_gray.svg" alt="https://www.notion.so/icons/megaphone_gray.svg" width="40px" /> **Credits**

</aside>

Yan Zhang, Zoila Jurado, and Miki Yun (Richard Murray Lab, Caltech)

- Developers
    - [Murray Lab](https://www.notion.so/Murray-Lab-498206a6c19444f7a1cee90a528f72d4?pvs=21)
    - [Freemont Lab](https://www.notion.so/Freemont-Lab-290158f216024a6f862037ebd7d23183?pvs=21)
    - [Shimizu lab](https://www.notion.so/Shimizu-lab-501c98e185a048c988f8a9ee0a5cb38a?pvs=21)