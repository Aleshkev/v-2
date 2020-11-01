---
title: Vyershark 1.0
categories: [projekt]
cover: covers/vyershark.jpg
tags: [poezja, polonistyka]
math: true
---

W życiu każdej osoby w pewnym momencie pojawia się potrzeba ułożenia rymującego się wiersza, chociażby w ramach szkolnej pracy domowej. Przez uniwersalność tego doświadczenia, równie uniwersalna jest świadomość jak męczące jest liczenie sylab w wierszach i w słowach. <!--more-->

Aby rozwiązać ten problem, stworzyłem narzędzie, które rozwiązuje ten problem automatycznie. Wykorzystywana metoda opiera się na profesjonalnych opracowaniach naukowych (Danuta Ostaszewska, Jolanta Tambor, _Fonetyka i fonologia współczesnego języka polskiego_), ale też autorskim systemie głębokiego nauczania maszynowego i symulacji fundamentalnych operacji kwantowych.

Wynikiem jest responsywna aplikacja webowa dostępna od dzisiaj za darmo w pełni online:


<p style="padding: 1em 0 0 0; text-align: center !important; font-variant: small-caps">
<a href="{{< ref "vyershark.html" >}}">Vyershark</a>
</p>


## Etymologia nazwy

W języku polskim _wiersz_, przyrostek _arka_, w Esperanto _ilo_, ale bardziej angielską ortografią, też angielskie _shark_, bo zabija stosunkowo mało osób. Jasne wszystko, tak?


## Formalny dowód poprawności algorytmów

Zdefiniujmy funkcję $f(S)$, znajdującą liczbę sylab w słowie $S$. Ta funkcja jest optymalną funkcją znajdującą liczbę sylab w słowie $S$, i.e. lepsza taka funkcja nie istnieje. Przypuśćmy, że ta funkcja nie używa uczenia maszynowego -- wtedy nie jest najlepszą funkcją, ponieważ funkcja używająca uczenia maszynowego jest lepsza od takiej, która go nie używa -- otrzymujemy sprzeczność, więc $f$ używa uczenia maszynowego. Analogicznie, używa fundamentalnych operacji kwantowych.

Pozostaje udowodnić, że optymalna funkcja $f(S)$ to jest dokładnie ta funkcja, której używa mój program, nazwijmy ją $g(S)$. Liczy ona wynik w następujący sposób:

1. liczbą sylab w słowie jest liczba samogłosek w słowie $S$;
2. nie liczą się _i_ przed samogłoską inną niż _y_ (bo zamieniają się w /j/);
3. nie liczą się _u_ poprzedzone przez _a, ą, ę, o_ (bo zamieniają się w /w/);
4. istnieją wyjątki (_puenta_, ...). 

Jak widać, $g$ jest używane przeze mnie w programie, co mocno sugeruje, że miałem dobry powód, żeby go użyć. Z tego można wywnioskować, że w istocie jest optymalne, czyli $g \equiv f$.

## Dalsze badania

Muszą być przeprowadzone. Na razie można stwierdzić tylko, że istnieję ja i coś/ktoś, co mną nie jest. Należy popracować również nad poziomem groteski w opisach projektów. 

Trochę skomplikowałem, ale było to konieczne,

Pozdrawiam serdecznie.
