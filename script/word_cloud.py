from pathlib import Path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = []

for f in Path("content/").glob("*.md"):
    if "paski-tvp" in f.name:
        continue  # Opposition, Law and justice want to take over the entire cloud :c
    text.append(f.read_text("utf-8"))

# It would be nice to normalize all text to nominative cases, but that'd require some dictionary.

cloud = WordCloud(width=1335, height=576, max_font_size=100,
                  # background_color="white",
                  colormap="Pastel1" # I wonder why there isn't a theme which would work with a white background?
                  # Maybe the theme knows when there is a bright background, but you have to tell it that??
                  ).generate("\n".join(text))

# This will be 1400 x 1400 px with some margin, so content can be 1335 px...?
# (I don't know matplotlib.)
plt.figure(figsize=(14, 14))  # I wonder what unit is it in? Hundreds of pixels? Or is it relative to something?
plt.imshow(cloud, interpolation="bilinear")  # Actually, I hope it won't scale.
plt.axis("off")  # Maybe this margin is just where the axes would've been??
plt.tight_layout()  # Does this do anything?

plt.show()