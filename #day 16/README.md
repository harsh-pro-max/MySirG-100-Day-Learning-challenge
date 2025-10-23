## Day 16 — Markdown to HTML (Python)

### Summary
Small utility to convert `.md` files into clean `.html` using Python, safe file I/O, and a reusable function.

### Features
- Read `.md` → convert to HTML → write `.html`
- Supports headings, lists, links, code blocks, tables (via extensions)
- Graceful errors for missing files/paths
- Easy to style later via a CSS link or template

### Requirements
- Python 3.8+
- Install: `pip install markdown`

### Quick Start
1) Save the script below as `md_to_html.py`.
2) Run:  
   `python md_to_html.py sample.md sample.html`
3) Open `sample.html` in a browser or VS Code preview.
