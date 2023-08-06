# Smart Notebook
A connected e-paper "smart notebook" on a Raspberry Pi Pico with a Waveshare display. Captures notebook pages, processes the images, and renders summaries to the screen.
- `startProcedure/` – startup monitoring + summary compiler
- `imageProcessing/`, `magickTest/` – page capture and image conversion
- `htmlLayouts/`, `webHost/` – web front-end and host
- `compressionTest/` – image-compression experiments (C)
- `printedParts/` – 3D-printed enclosure
Vendored libraries and build binaries are excluded.
