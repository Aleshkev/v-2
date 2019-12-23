---
tags: meta, projekt, markdown, opinia
---

# Mój system tworzenia strony

Ponieważ mam blog i odczuwam potrzebę wypełnienia go nieinteresująco specyficznymi postami, zacznę od najprostszego możliwego tematu: programu, który samemu stworzyłem.

## Dlaczego renderuję strony?

Ostatnio popularne wśród deweloperów są [generatory statycznych stron](https://www.staticgen.com). Tworzą (_renderują_) one HTML gotowy do wysłania każdemu użytkownikomi, bez potrzeby zaawansowanego serwera -- wystarczy, że będzie on wysyłał odpowiednie pliki.

Oznacza to, że taki serwer jest wydajny, bezpieczny i tani -- w istocie na tyle tani, że niektóre firmy zapewniają darmowy każdemu użytkownikowi. Przykładem jest [GitHub Pages](https://pages.github.com), którego ja w tym momencie osobiście używam.
(Dlatego URL mojej strony zawiera "github.io", ale da się to łatwo zmienić wykupując własną domenę.)

W statycznych stronach nadal może być JavaScript wykonywany po stronie klienta, więc nie są statyczne pod wszystkimi względami.

Dla mnie najważniejsze jest to, że gdy raz wyrenderuję stronę, nic się nie może dalej zepsuć, nieważne jak beznadziejny mój kod jest. Serwer nie scrashuje w środku nocy pozbawiając świat moich światłych przemyśleń na jego temat.

### Dlaczego stworzyłem własny system renderowania stron zamiast użyć któregoś z tej długiej listy, do której przed chwilą zalinkowałem?

To bardzo dobre pytanie, ja byłbym gotowy na nie odpowiedzieć, ale ono nie było i nie jest zadawane -- nie ma takich wątpliwości, zapewne dzięki klarowności odpowiedzi -- jakby ktoś takie pytanie zadał, chętnie na nie odpowiem, ale, jak już wspomniałem lub wspominałem, jedni wolą w takich sytuacjach aspekt dokonany, inni niedokonany, ale co ciekawe istnieją czasowniki które mają oba, lub ściślej rzecz biorąc, mogą pełnić funkcję obu -- to by była ciekawa sytuacja gdybym mógł tu, w tym pytaniu, takiego użyć, ale takiego pytania nie ma; więc myślę, że prawdziwym, bo tak chyba rozwieję więcej wątpliwości, których, powtarzam, na razie nie ma, a jakby były, to małe, wręcz pomijalne biorąc pod uwagę kontekst, który za rzadko się uwzględnia w dzisiejszej dyskusji na ten temat, ale też inne- czy to zrozumiałe? tak czy nie? tak? pytaniem jest- to znaczy: jak mi poszło?

## Jak mi poszło?

Cóż.

Cały mój system opiera się na ustawionych na sobie hackach i bodge'ach, niczym dom z kart -- ale nie taki fajny, z prezydentem zabijającym dziennikarzy -- taki będący metaforą bardzo delikatnej architektury, zawalającej się gdy ktoś poza autorem jej dotknie.

Moją opinią jest, że naprawienie tego nie jest warte wysiłku; wszystko po prostu działa, zapewne oprócz rzadkich przypadków, które, ponieważ jestem autorem wszystkiego, będę umiał, mam nadzieję, samodzielnie naprawić gdy je napotkam. W ten sposób naturalna awersja do wysiłku połączona z nihilizmem świadomości, że pewnie i tak niedługo zmienię zdanie jak wszystko ma działać i cały wysiłek się zmarnuje, oddelegowuje cokolwiek co zostało z perfekcjonizmu do pilnowania końcowego HTML-a.

A końcowy HTML jest bardzo ładny. Każdy fragment tekstu ma oznaczony język -- ten język jest używany do automatycznego wstawiania znaków `&shy;` i `&nbsp;` w odpowiednich miejscach, żeby przeglądarki wiedziały, gdzie słowa można przenosić do nowej linii. Ratując tradycyjne praktyki polskiej typografii przed agresywną westernizacją, cudzysłowy są poprawne, a paragrafy nie są oddzielane odstępem, tylko wcięciem pierwszego wiersza.

Jedną z trudniejszych do dodania rzeczy były notatki na marginesie. Ale udało się; jeżeli ekran użytkownika jest dostatecznie duży i JavaScript jest włączony, wszystkie przypisy pojawiają się właśnie tam.

Jest jeszcze kilka rzeczy, które nadal można by poprawić, ale to by wymagało za dużo pracy w stosunku do wyniku -- kiedyś pewnie się za to i tak kiedyś zajmę, ale nie jest to krytyczne.

## Kod źródłowy

Treści piszę w [Markdownie](https://en.wikipedia.org/wiki/Markdown) z rozszerzeniami, parsowanym przez [MarkdownIt](https://github.com/markdown-it/markdown-it) z dodatkami. Nad strukturą strony panuje skrypt w Pythonie, decydujący które pliki są wymagane i jakich przekształceń potrzebują, a następnie przekłada wszystkie wygenerowane pliki do osobnego folderu.

Wszystko co samodzielnie napisałem jest [na moim GitHubie](https://github.com/Aleshkev/aleshkev.github.io).

### Dlaczego Markdown?

W odróżnieniu od HTML-a, treści w nim napisane są bardzo czytelne. Celem Markdowna, według niektórych, jest, żeby kod źródłowy tekstu wyglądał na tyle dobrze, że można go swobodnie czytać nawet bez zamiany na inny format:

```markdown
---
tags: meta, markdown
---

# Tytuł strony

Paragraf składa się z bezpośrednio następujących po sobie
linii tekstu -- jedna lub więcej pustych linii tworzą nowy
paragraf.

Tekst można pochylić -- lub, ściślej rzecz biorąc, oznaczyć
jako akcentowany -- _w ten_ sposób.

## Tytuł sekcji

Używane jest rozszerzenie do wyświetlania notatek na
marginesie.^[To jest przykładowa notatka.]

Formuła matematyczna: $x^2$

![Obrazek.](image.png) _Podpis._

Tworzenie list jest proste:

- punkt jeden;
- punkt dwa;
- punkt trzy.
```

Są oczywiście inne podobne systemy, zwłaszcza [ReStructuredText](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) oraz [AsciiDoc](https://asciidoctor.org/docs/what-is-asciidoc/). Ale ja -- mimo wszystkich jego wad -- wolę Markdowna.

Niektórym bardzo przeszkadza, że nie ma niektórych elementów i bardzo szybko zaczyna się pisać w tylko jednym z licznych dialektów, zabijając jakąkolwiek niezależność od implementacji -- i ja to rozumiem, sam miałem przez długi czas takie wątpliwości. Ale mi to daje możliwość stworzenia własnego dialektu Markdowna, sprawiając, że moja witryna jest jakby zamkniętym w sobie ekosystemem, stworzonym w całości przeze mnie.
