# Luminescence Journal Submission

## Manuscript

**Title:** Reexamining Ives & Coblentz (1924): Evidence That the Canonical Firefly Luminosity Is Substantially Overestimated

**Target Journal:** *Luminescence* (Wiley)

**Submission Portal:** https://wiley.atyponrex.com/journal/BIO

---

## Files

| File | Description |
|------|-------------|
| `main.tex` | Main manuscript (LaTeX) |
| `main.pdf` | Compiled PDF for review |
| `references.bib` | Bibliography |
| `figures/` | Figure files (TIF or EPS format) |
| `graphical_abstract.txt` | Graphical TOC text (50-60 words) |

---

## Pre-Submission Checklist

### Required by Journal

- [ ] Abstract ≤250 words, no citations
- [ ] Keywords (≤5): firefly bioluminescence; photometry; *Photinus pyralis*; luciferase; photon flux
- [ ] Sections: Introduction, Experimental, Results, Discussion, Conclusions
- [ ] References: numbered, superscript square brackets
- [ ] SI units throughout
- [ ] Tables on separate pages after references
- [ ] Figures as separate files (300 dpi photos, 600+ dpi line art)
- [ ] Graphical abstract (50mm × 60mm, 50-60 words)
- [ ] Conflict of interest statement
- [ ] Data availability statement
- [ ] ORCID for submitting author

### To Complete Before Submission

- [ ] Add corresponding author email
- [ ] Generate figures from `firefly_calculations.py`
- [ ] Create graphical abstract image
- [ ] Compile final PDF
- [ ] Proofread

---

## Compiling

```bash
cd luminescence_submission
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

## Graphical Abstract

**Image:** 50mm × 60mm, showing comparison of estimates (bar chart or schematic)

**Text (50-60 words):**
> The canonical firefly luminosity of "1/40 candlepower" (Ives & Coblentz, 1924) implies 3×10¹⁴ photons per flash. Biochemical calculation, field lux-meter measurements, and an overlooked 1928 study converge on 10⁸–10¹¹ photons—a 10³–10⁶-fold discrepancy. This century-old overestimate has implications for bioenergetic models of bioluminescence.

---

## Key Numbers

| Estimate | Photons/flash |
|----------|---------------|
| Ives & Coblentz (1924) | 3 × 10¹⁴ |
| Harvey & Stevens (1928) | 6 × 10¹¹ |
| Biochemical calculation | 10⁸–10¹⁰ |
| Field lux-meter | 10¹⁰–10¹¹ |
| Goh & Wang (2022) | 1.7 × 10¹¹ |
| **Discrepancy** | **10³–10⁶-fold** |

---

## Contact

Corresponding author: David H. Silver

