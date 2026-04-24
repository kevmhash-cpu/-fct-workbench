# FCT Workbench (Prototype)

Graph-based analyst tool for detecting structure-driven credibility transfer in narrative artifacts.

## Why this matters

Analysts increasingly face narratives that appear coherent before they are evidentially supported.

This tool attempts to surface that gap structurally—highlighting when narrative structure may be driving perceived credibility more than underlying evidence.
---

## What this is

FCT Workbench is a prototype tool designed to help analysts identify when:

**narrative structure is generating perceived coherence faster than evidence supports it.**

This is a triage tool — not a truth engine.

---

## Core idea

Some artifacts appear convincing not because they are well-sourced, but because:

- anchors are real or emotionally salient  
- connections imply causality  
- structure creates internal coherence  
- scale overwhelms verification  

FCT Workbench attempts to detect those structural patterns.

---

## What the tool does

- Identifies anchor candidates  
- Measures structural transfer  
- Estimates recursion (micro / meso / macro)  
- Calculates claim-to-source ratio  
- Detects self-referential paths  
- Classifies topology (hub-spoke / hierarchical / lattice)  

---

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Important

- This does NOT determine truth  
- This does NOT prove deception  
- This does NOT replace analyst judgment  

It is a working analytic construct + prototype.

---

## Status

Prototype — April 2026  
Not validated doctrine

## Citation

Hollenbeck, Kevin M. (2026).  
*Fractal Credibility Transfer (FCT): A Structural Model for Detecting Coherence Without Evidence*.  
Zenodo. https://doi.org/10.5281/zenodo.19732661
