# The Canonical Firefly Luminosity Is Overestimated by 10³–10⁴-Fold

David H. Silver | 2025

---

## Summary

The commonly cited firefly brightness—"1/40 candlepower" from Ives and Coblentz (1924)—corresponds to 3×10¹⁴ photons per flash. This exceeds the theoretical maximum imposed by luciferase abundance and quantum yield by 10³–10⁴-fold.

Direct field measurements with a calibrated lux meter yield 10¹⁰–10¹¹ photons per flash, consistent with both the biochemical bound and reanalysis of historical and modern spectroscopic data.

---

## Key Results

| Source | Method | Photons/flash |
|--------|--------|---------------|
| Commonly cited | "1/40 candle" | 3 × 10¹⁴ |
| Coblentz (1912) original | Visual photometry | 3 × 10¹³ |
| Harvey & Stevens (1928) | Surface brightness | 6 × 10¹¹ |
| Goh et al. (2022) | Lux meter | 10¹⁰–10¹¹ |
| Biochemical bound | Enzyme × yield | 10⁸–4 × 10¹⁰ |
| **This work** | Lux meter | **10¹⁰–4 × 10¹¹** |

Four independent estimates converge on 10¹⁰–10¹¹ photons per flash. The 1924 value is an outlier by 10³–10⁴.

---

## The Two Errors

**Error 1: Transcription.** Coblentz's 1912 data state the predominant flash intensity was 1/400 candle (not 1/40). The value propagated through secondary literature is "1/40 candle"—either a transcription error (1/400 → 1/40) or a rounded maximum.

**Error 2: Methodological biases.** Visual nulling photometry applied to brief, spectrally narrow emissions introduces systematic biases:
- Observers match peak rather than time-integrated intensity (2–4× inflation)
- Candlepower assumes isotropic emission; firefly lanterns emit into 1–2 sr (6–12× inflation)
- 560 nm emission sits at peak human photopic sensitivity

These biases multiply.

---

## Biochemical Bound

```
N_photons = N_cells × N_enz × k_eff × Φ × t

         = 10⁵ photocytes
         × 10⁶ luciferase/cell
         × 0.01–1 s⁻¹ turnover
         × 0.41 quantum yield
         × 0.25 s flash

         = 10⁸ – 4×10¹⁰ photons
```

Even if every enzyme fires exactly once, maximum output is 4×10¹⁰ photons—four orders of magnitude below the canonical value.

---

## Field Measurements

Lux-meter data collected in Sungai Petani, Malaysia (November 2025) from wild-caught *Pteroptyx* fireflies:

| Distance | Mean ΔLux | Max ΔLux |
|----------|-----------|----------|
| 1 cm | 0.30 | 0.5 |
| 2 cm | 0.23 | 0.5 |
| 3 cm | 0.04 | 0.2 |

Peak flash: 0.5 lux at 1 cm → 10¹⁰–4×10¹¹ photons/flash (with geometric correction for directional emission).

---

## Repository Contents

- `luminescence_submission/` — Manuscript (main.tex, main.pdf) and references
- `25_FireflyBioluminescence/` — Book chapter source exploring the topic
- `firefly_calculations.py` — Computational analysis and figures
- `emails.txt` — Expert correspondence (Fallon, Faust)

---

## Citation

> Silver, D.H. (2025). The canonical firefly luminosity is overestimated by 10³–10⁴-fold. *In preparation.*

---

*2025*
