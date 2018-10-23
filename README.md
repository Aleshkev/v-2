# aleshkev.github.io

My personal website. 

I created my own build process. Its source code is under [MIT License](LICENSE.md), while all of [content/](content/) is under [exclusive copyright](content/LICENSE.md).

Website is hosted live on Github pages, see [aleshkev.github.io](https://aleshkev.github.io). I might buy myself some nice custom domain in the future.

The site is statically built into the `a/` folder. I set up an `index.html` file, which redirects immediately from `https://aleshkev.github.io/` to `https://aleshkev.github.io/a/`.

To build, simply use `build.py` or `build.py release`. The `release` mode uses absolute url, while the default uses only relative links (so the changes can be previewed by simply opening them in the browser). \
The PyCharm project files already have these two configurations.
