---
title: Jeszcze nowsza strona
cover: /covers/jeszcze-nowszy-wyglad-strony.png
coverCaption: Gdyby był to screenshot tego właśnie artykułu, powstałby fraktal.
categories: [meta]
tags: [design, gradient, markdown]
---

Wbrew krążącej wśród niektórych opinii, zdawałem sobie sprawę z tego, że moja strona wyglądała zupełnie inaczej od większości innych w internecie. Nie przeszkadzało mi to zbytnio, ponieważ zawartość też była w niepowtarzalny sposób jakby przeciwna temu, żeby czytało ją dużo osób.

Ale kilka tygodni temu natrafiłem na imponująco (dla mnie) popularną [stronę mojej koleżanki z klasy z gimnazjum](https://bthegreat.pl) i zdałem sobie sprawę z tego, że tak wcale nie musi być. Staram się nie przejmować za bardzo opinią innych wytworzoną na podstawie m.in. mojej strony -- chociaż obecnie mam pewne wątpliwości co do praktyczności takiego założenia, OK. Ale w żaden sposób nie oznacza to, że na każdym kroku muszę upewniać się, że wszyscy potencjalni czytelnicy wiedzą, że nimi się nie przejmuję.

Celem strony jest, żeby jej tworzenie było dla mnie _fajne_. Ale jeżeli mam dwa interesujące mnie tematy, nic nie stoi na przeszkodzie, żebym przy pisaniu artykułu czy wpisu wybrał ten, który jest ciekawszy dla osób innych niż ja. Poza tym, co jeżeli tworzenie jak najpopularniejszej strony jest _najfajniejszą_ rzeczą jaką można ze stroną zrobić? Na razie mam z pięciu prawie-regularnych czytelników, ale to się może zmienić.

## Moja obecna koncepcja

Istnieje pewien konsensus, że pisanie w losowych momentach na całkowicie losowe tematy nie pomaga w utworzeniu grona stałych odbiorców.

Dlatego staram się ustalić niszę, którą będę próbował moimi wpisami wypełnić. W tej chwili mam pomysł, żeby w przystępny sposób opisywać mniej znane idee i teorie kierujące działaniami społeczeństwa i jego części, w szczególności tego jak odnoszą się do polskiej młodzieży. Przykładowe tematy:

- Jaki jest cel lektur szkolnych i kiedy uczniowie nie będą musieli czytać Mickiewicza?
- Skąd biorą się obecne zasady języka polskiego?
- Czy opinie innych osób o nas są nam niepotrzebne?
- Czego Ministerstwo Edukacji oczekuje od informatyki w szkołach?
- Dlaczego w IPA ⟨sz⟩ to /ʂ/, a nie /ʃ/, inaczej niż ⟨sh⟩ w angielskim? <!-- PS: właśnie to sprawdziłem i to po prostu są dwa różne dźwięki. Całe życie w błędzie! Ale o czym ja napiszę ten artykuł? -->
- Czy esperanto jest narzędziem komunistów w osiąganiu światowej dominacji?
- Czy samobójstwo może być racjonalnym wyborem?

Będę oczywiście również zawsze otwarty na sugestie. I tak nie na wszystkie te pytania jestem w stanie samemu od razu odpowiedzieć, więc jest to też dla mnie stała okazja, żeby dowiedzieć się czegoś nowego.

Jeżeli mimo oczekiwań by to dobrze poszło, mogłoby to ewoluować do czegoś na wzór dziennikarstwa, które zamiast rozpraszać się na jakichś osobistych skandalach pojedynczych polityków skupiłoby się bardziej na aspektach ich ogólniejszych światopoglądów.

Wydaje się to tak dobrym pomysłem, że pewnie ktoś już na niego dawno temu wpadł. Ale ja nigdy na nic takiego nie trafiłem, a byłbym bardzo zainteresowany. Stąd wniosek, że jest miejsce na przynajmniej jeden kolejny taki blog.

## Szczegóły designowe

Projektując pierwotny wygląd mojej strony, zacząłem od białego tła i czarnego szeryfowego tekstu. Następnie po kolei próbowałem dodać każdy element jaki można by umieścić na blogu, i przy każdym dochodziłem do wniosku, że nie da się go wkomponować bez zniszczenia idealnego balansu jednej kolumny tekstu. Dlatego ostatecznie na stronie był tytuł, data, moje nazwisko i duży blok tekstu, teoretycznie z obrazkami, ale w praktyce żadnych nie było.

Nie dało się zaprzeczyć, że wyglądało to bardzo estetycznie i oryginalnie. Więc nazwałem to "minimalizmem" i czując się usatysfakcjonowanym, przeszedłem do upewniania się, że wszystko co napiszę na stronie jest dostatecznie niezrozumiałe.

Ale chcąc pozwolić stronie dać szansę stać się popularną, przeglądałem sobie poradniki "jak zrobić najpopularniejszego bloga ever w 10 prostych krokach" i mimo mojego sceptyzmu co do niektórych tam zawartych "porad", doszedłem do wniosku, że brakiem przejrzystej nawigacji czy jakiegoś opisu o czym w ogóle są na stronie artykuły, do regularnego czytelnictwa w istocie nie zachęcam.

Co do konkretnego wyglądu: chciałem coś "odważnego", jednak eleganckiego. Dlatego pomyślałem o kolorowym gradiencie. Po długich poszukiwaniach inspiracji w internecie, natrafiłem na [Stellar](https://html5up.net/uploads/demos/stellar/), darmowy szablon od [HTML5 UP](https://html5up.net) wyglądający moim zdaniem idealnie. Więc skopiowałem sobie wszystkie kolory i na tej podstawie zbudowałem coś, co mi się podoba. I mam nadzieję, że wam też. 💜

## Szczegóły techniczne

Do tej pory używałem [samodzielnie skonstruowanego skryptu]({{< ref "2019-09-06-moj-system-tworzenia-strony.md" >}}) zamieniającego pliki [Markdowna](https://commonmark.org/help/) w pliki HTML tworzące stroną internetową, a [GitHub Pages](https://pages.github.com) uprzejmie za darmo je hostował z [mojego repozytorium](https://github.com/Aleshkev/aleshkev.github.io) na swoich serwerach.

Ale praca nad tym skryptem była bardzo nieprzyjemna. Postanowiłem przenieść się więc na jakiś profesjonalny system. Przetestowałem [Jekylla](https://jekyllrb.com), ale mi się niezbyt podobał. Więc ostatecznie używam [Hugo](https://gohugo.io).

Ogólnie całego procesu nie polecam. Jeżeli ktoś nie chce poświęcać ogromnej ilości czasu na ledwie funkcjonującą stronę, radzę użyć Wordpressa albo czegoś podobnego.

---

Nie jestem w stanie powiedzieć jak pójdzie mi realizowanie swoich celów i jaka będzie ostateczna jakość czy przydatność moich wpisów. Ale mam nadzieję, że od tej pory uprzyjemnię choć minimalnie moją stroną życie nie tylko sobie samemu. 😊
