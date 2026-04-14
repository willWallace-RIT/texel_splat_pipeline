# Texel Splat Reconstruction Pipeline

This project converts video path pairs into a static scene and generates a texel splat field.

## 🧠 Core Concept: Aggregate Average Geometry Anchor (AAGA)

Instead of fully reconstructing dense geometry, we compute a lightweight evolving structure:

### AAGA Definition
A running estimate of scene geometry derived from temporal accumulation:
