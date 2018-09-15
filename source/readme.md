# Jonas Aleshkevich's personal site

Well, the title explains it all.

To waste a large amount of time, I created my own build process in Python.

It follows the obvious and natural idea of making it simple, understandable and maintainable - an idea which some people decided for inexplicable reasons to name and attribute to their favourite piece of software (don't get me started on KISS).

I will now just list my personal notes relating to this project. 

Build process:
1. `root_url` is the root of the site, e.g. `aleshkevich.github.io` (without slash at the end)
1. `nav.md`, `footer.md` and `site-name.txt` are special
1. for each `.md` file in `content/`:
    1. read `.md` file, parse to AST
    1. apply transformations on AST:
        1. resolve local links
    1. render Markdown to HTML
    1. render Jinja2 template with rendered HTML, data from special files
    1. save `.html` file to `build/`
1. copy all files from `content/` to `build/` (currently including Markdown sources)

Planned features:
1. more typographic features 
    1. smart quotes
    1. correct word breaking: break most words, don't break people's names
    1. server-side auto-insertion of soft hyphens (strongly related to the point above)
    1. server-side auto-replacement of spaces with non-breaking spaces (before short words, `1 cm`, `page 17`)
1. self-hosted font, loaded only if not available on system (currently using Google Fonts)
