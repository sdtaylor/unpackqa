---
layout: default
title: About
nav_order: 1
has_children: false
---

# pyUnpackQA  
Methods for unpacking all common remote sensing QA bands which are stored in bit-wise values.

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (full scenes).
- The same methods are used for all sensors, with specific product flags specified via arguments.
- No file reading or writing.
- numpy is the only dependecy.

# Installaion

Install via pip directly from the github repo:

```
pip install git+git://github.com/sdtaylor/pyUnpackQA
```

