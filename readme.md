# aleshkev.github.io

Moja osobista strona: <https://aleshkev.github.io>.

Tutaj znajduje się jej kod źródłowy. Skonfigurowane jest [Travis CI](https://travis-ci.org/github/Aleshkev/aleshkev.github.io), które buduje stronę z `source` do `master`, skąd pliki hostuje [GitHub Pages](https://pages.github.com) ❤. Używane jest [Hugo](https://gohugo.io) z własnym szablonem wzorowanym lekko na [Stellar](https://html5up.net/stellar) od [@ajlkn](https://twitter.com/ajlkn) ([CC BY 3.0](https://html5up.net/license)). Treści są pisane w [Markdownie](https://www.markdownguide.org/getting-started/) rozszerzonym o [shortcodes](https://gohugo.io/content-management/shortcodes/). Po zbudowaniu strony przez hugo, wywoływany jest skrypt `enhance.py`, który mówi przeglądarkom jak myślnikować słowa, powstrzymuje pojedyncze literki na końcach linii, zamienia cudzysłowy na poprawne polskie.

## Notatki dla mnie samego

### Jak usuwa się ostatni commit

```sh
git reset --hard HEAD~1
git push --force
```

### TODO:

- [x] add katex math
- [ ] style code spans
- [ ] better SEO
  - look at yeast wp plugin?
- [ ] redirects from old links?
  - hard to do with static pages and nobody linked to me yet
- [ ] nicer gradient
  - something more fitting the content
  - independent from page height?
- [ ] better header
- [ ] footer
  - [ ] bio
  - [ ] next & previous articles
  - [ ] related & featured
  - [ ] newsletter
- [ ] more on the front page
  - [ ] smaller article cards?
  - [ ] bio?
- [ ] about section
- [ ] contact section
- [ ] some analytics
  - google analytics?
- [ ] custom domain
  - [ ] social sharing options
  - [ ] some comments
    - disqus comments?
- [ ] support for `series`
  - [ ] link to next/previous in series
  - maybe just us tags or categories for that, though?
- [ ] optimize images with `srcset` and hugo resources
- support for various markdown/html elements:
  - [ ] toc
  - [ ] tables
  - [ ] epigraphs (shortcode)
