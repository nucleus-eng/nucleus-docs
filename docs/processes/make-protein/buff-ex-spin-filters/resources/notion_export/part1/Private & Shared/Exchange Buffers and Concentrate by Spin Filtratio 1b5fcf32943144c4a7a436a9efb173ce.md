# Exchange Buffers and Concentrate by Spin Filtration

<aside>
<img src="https://www.notion.so/icons/light-bulb_gray.svg" alt="https://www.notion.so/icons/light-bulb_gray.svg" width="40px" /> **Getting Started**

</aside>

You have a sample of a biomolecule (e.g., T7RNAP, tRNA, ribosomes, plasmid, etc.) that is either (1) in the wrong buffer (e.g., has 500 mM Imidazole) or (2) is too dilute. 

You can use centrifugal spin filters to concentrate your sample and change its buffer. These filters allow buffer and small molecules to flow through them, retaining large molecules bigger than the filter’s specified molecular weight.

<aside>
<img src="https://www.notion.so/icons/wrench_gray.svg" alt="https://www.notion.so/icons/wrench_gray.svg" width="40px" /> **Materials and Equipment**

</aside>

We use two different volume spin filters, depending on how much sample volume we need to process: 15 mL or 0.5 mL.

| **Name** | **Product** | **Manufacturer** | **Part #** | **Price** | **Storage Conditions** | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| 15 mL spin filters (3 kDa cutoff) | Amicon® Ultra Centrifugal Filter, 3 kDa MWCO | Millipore Sigma | UFC9003 | $125 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/mm/ufc9003)] |
| 0.5 mL spin filters (3 kDa cutoff) | Amicon® Ultra Centrifugal Filter, 3 kDa MWCO | Millipore Sigma | UFC5003 | $63 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/mm/ufc5003)] |

<aside>
<img src="https://www.notion.so/icons/iterate_gray.svg" alt="https://www.notion.so/icons/iterate_gray.svg" width="40px" /> **Protocol**

</aside>

- [ ]  Dilute your sample ~10x with your new buffer (e.g., add 54 mL P3 Exchange Buffer to 6 mL eluted protein).
- [ ]  Load your sample onto a centrifugal filter column.
    - **Notes: use filter cutoffs 3x smaller than your sample.**
        
        Make sure your filter cutoff is at least 3x smaller than your protein size. Otherwise, your may lose your sample in the flowthrough. Using a smaller cutoff filter is fine, but will increase the time you need to spin your sample. If unsure, we recommend using 3 kDa filters for all samples.
        
- [ ]  Centrifuge samples at either 4000 rcf (4 mL or 15 mL filters) or 14 000 rcf (0.5 mL filters) at 4C until you’ve reached your target volume. Check on your sample volume in the first 10 min, then again as needed.
    - **Notes: if you have too much sample, load in tranches.**
        
        If you have more sample than you can fit onto your centrifugal filter column, you can load your sample in tranches. Fill your column, spin down your sample, and repeat. See instructions below for details on each spin step.
        
- [ ]  Continue to dilute and spin your sample, noting your sample volume and dilution volume at each step, until you’ve reached your target dilution factor (we recommend ≥ 300x).
    - **Notes: how to calculate dilution factor.**
        
        Each time you dilute your sample, note the volume of your concentrated sample ($V_{conc}$) and the volume of your sample after diluting ($V_{dilute}$) Calculate the dilution factor for that step ($f_n$) by dividing $V_{dilute}$ by $V_{conc}$. 
        
        $$
        f_n = \frac{V_{dilute}(n)}{V_{conc}(n)}
        $$
        
        To calculate the total dilution factor after multiple dilution steps ($f_{total}$), multiply the dilution factor for each step.
        
        $$
        f_{total} = \prod_n f_n = f_1 \times f_2 \times \dots \times f_n
        $$
        
- [ ]  Store columns for later use.
    - [ ]  Wash columns by loading with ddH2O and spinning.
    - [ ]  Load columns with EtOH 20% (v/v) and store at room temp.
- **Notes: If you see precipitate, dilute your sample immediately.**
    
    If you're protein precipitate out in any of the concentration steps, dilute the protein further before concentrating. The proteins are precipitating/aggregating out because of high salt concentrations; Therefore, diluting the proteins will reduces the chances of the protein to aggregate/ precipitate. 
    

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