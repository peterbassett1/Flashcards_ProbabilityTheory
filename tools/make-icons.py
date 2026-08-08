# -*- coding: utf-8 -*-
"""Generate the PWA / apple-touch icons from the app's brand mark.
Navy field (#1c1a2e) with a signal-violet bell curve (#6c5ce7) on a baseline,
matching the in-app header glyph. Run: python tools/make-icons.py"""
from PIL import Image, ImageDraw
import math
import os

NAVY = (28, 26, 46)       # #1c1a2e
VIOLET = (108, 92, 231)   # #6c5ce7
BASE = (74, 59, 192)      # #4a3bc0
OUT = os.path.join(os.path.dirname(__file__), '..', 'icons')
os.makedirs(OUT, exist_ok=True)


def make(size, pad_frac):
    # supersample for crisp curves, then downscale
    s = size * 4
    img = Image.new('RGB', (s, s), NAVY)
    d = ImageDraw.Draw(img)
    pad = round(s * pad_frac)
    inner = s - 2 * pad
    left, right = pad, pad + inner
    base_y = pad + inner * 0.80          # baseline
    peak = inner * 0.72                  # curve height

    # Gaussian bell as a filled area under the curve
    pts = []
    n = 160
    for i in range(n + 1):
        x = left + inner * i / n
        z = (i / n - 0.5) * 6.0          # span roughly [-3, 3] sigma
        y = base_y - peak * math.exp(-0.5 * z * z)
        pts.append((x, y))
    area = pts + [(right, base_y), (left, base_y)]
    d.polygon(area, fill=VIOLET)

    # baseline
    lw = max(2, round(s * 0.012))
    d.line([(left, base_y), (right, base_y)], fill=BASE, width=lw)
    return img.resize((size, size), Image.LANCZOS)


# apple-touch + manifest "any": tighter framing
for sz in (180, 192, 512):
    make(sz, 0.18).save(os.path.join(OUT, 'icon-%d.png' % sz))
# maskable: extra padding so the glyph survives iOS/Android corner masks
make(512, 0.28).save(os.path.join(OUT, 'icon-512-maskable.png'))
# small favicon for the browser tab when installing
make(32, 0.14).save(os.path.join(OUT, 'icon-32.png'))
print('icons written to', os.path.normpath(OUT))
for f in sorted(os.listdir(OUT)):
    print('  ', f)
