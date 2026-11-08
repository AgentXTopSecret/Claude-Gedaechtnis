---
name: project-python-packages
description: "What is installed in the EU5 advisor's .venv, from where, and why (PySide6, numpy, Pillow, OpenCV)"
metadata:
  node_type: memory
  type: project
  originSessionId: 56f6d77e-886c-43cd-be82-e0946090ef56
  modified: 2026-10-23T19:27:02.069Z
---

The EU5 advisor's Python environment is `C:\Users\Kevin\Desktop\Claude EU 5 Mod\.venv` (Python 3.12). Python libraries live there, not in `C:\Users\Kevin\Tools` (they only work inside the project venv; see [[local-tools-folder]]).

- PySide6, numpy, Pillow: installed 2026-10-23 via pip from PyPI before the download rules were stated ([[download-confirmation-rules]]); the venv was later copied into the project folder, not re-downloaded.
- opencv-python-headless 5.0.0.93: confirmed by the user ("bestätigt") on 2026-10-23. Wheel `opencv_python_headless-5.0.0.93-cp37-abi3-win_amd64.whl` (43,825,962 bytes) from PyPI (official channel of github.com/opencv/opencv-python, Apache 2.0); SHA-256 829717b6…87e0e matched the PyPI-published digest; installed offline from that verified file with `--no-deps`. Used for automatic camera tracking (edge detection, distance transform, image alignment).

**How to apply:** If the venv is ever rebuilt, reinstall these from requirements.txt only after listing them again for the user, per the download rules.
