from PIL import Image, ImageOps
from glob import glob
import os
import re

# ORMH - Occlusion, Roughness, Metallic, Height
# Mask - Metalness, Occlusion, Roughness, Gloss

# =============================================

file_type = "TGA"
path = "./source/**/*." + file_type

regex_ormh = r"ORMH|ORM|Roughness"

mask_filename = "uMask"
height_filename = "uHeight"

# =============================================

files = glob(path, recursive=True)


def convertORMH(file):
    a = False
    map_file = os.path.splitext(file)

    img = Image.open(file)

    try:
        r, g, b, a = img.split()
    except:
        r, g, b = img.split()

    img = Image.merge("RGBA", (b, r, g, ImageOps.invert(g)))

    img.save(re.sub(regex_ormh, mask_filename, file, re.IGNORECASE), file_type)
    if a:
        a.save(re.sub(regex_ormh, height_filename,
                      file, re.IGNORECASE), file_type)

    os.remove(file)


for img in files:
    if re.search(regex_ormh, img, re.IGNORECASE):
        convertORMH(img)
