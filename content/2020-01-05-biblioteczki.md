# Traktat o biblioteczkach

## Wstęp

Jak powiedział pewien filozof:

> NIe mogę walczyć o to, czego nie kocham. Nie mogę kochać czegoś, czego nie szanuję. Nie mogę szanować czegoś, czego nawet nie znam.

Dlatego postaram się przedstawić moje poglądy, które choć kontrowersyjne, są w miarę oczywiste i trzeba by zaprzeczać obiektywnym faktom, aby je "obalić" -- tak naprawdę tylko zaprzeczyć zdrowemu rozsądkowi.

Tradycyjnie, istniał konflikt pomiędzy zadaniami z biblioteczkami a zadaniami bez biblioteczek. Według koncepcji Hegla, jest to pewna teza i antyteza tworząca syntezę, swoistą dialektykę librariańską. Jako typowo modernistyczny sposób interpretacji rzeczywistości, taka symplistyczna teoria nie działa w rzeczywistości, podobnie jak galopujący liberalizm.

Mój poprzedni artykuł napisany był w formie ironii, co wydaje mi się wszyscy inteligentni czytelnicy zrozumieli i nie próbowali kopiować dokładnie tego samego wstępu zmieniając tylko niektóre słowa, żeby osiągnąć wrażenie zupełnie przeciwne. Byłoby to przejawem kompletnego braku takowego zrozumienia i skompromitowałoby taką osobę w oczach zarówno każdego pojedynczego człowieka jak i każdego potencjalnie istniejącego boga. (Należy pamiętać, że obowiązkiem każdego wykształconego człowieka jest _udawanie_, że wierzy się w boga, gdyż nasze społeczeństwo jest zbudowane na wartościach chrześcijańskich i ich brak spowoduje jego upadek -- czego przykładem jest Imperium Rzymskie.) Na szczęście takich ludzi nie ma.

Gdyby na Olimpiadzie Informatycznej nie trzeba było implementować algorytmów, byłby to konkurs polonistyczny, gdzie jedyną trudnością jest przeczytanie treści zadania. W dodatku by wymagał umiejętności matematycznych, co by się mijało z celem.

## Niezbędne definicje

Zdefiniujmy na początek kilka klas podmiotów w logice doksastycznej. Radzę dobrze zrozumieć tę sekcję, gdyż bez jej zrozumienia dalsza część traktatu może okazać się niezrozumiała dla niedoświadczonego odbiorcy. Jeżeli ktoś jednak jest zapoznany z tematem, może od razu pominąć te dwa akapity.

Język naturalny jest jakąś kpiną z komunikacji interpersonalnej. Najlepiej w ogóle nie powinien istnieć, ponieważ bardzo ciężko się w nim komunikować. Powinien być zastąpiony językiem symbolicznym, jak to chcieli zrobić w Wiedniu w XIX wieku. Tę wiedzę i ich postęp jednak ukryto przed społeczeństwem, ponieważ taki rozwój wydarzeń zniszczyłby koncepcję państwa narodowego.

Przez $[p]$ oznaczmy operator modalny _przekonania_, że $p$ jest prawdziwe. Podmiot _dokładny_ nigdy nie wierzy w coś, co nie jest prawdą, czyli $[p] \implies p$ . Podmiot _niedokładny_ wierzy w przynajmniej jedną nieprawdziwą propozycję, czyli $\exists [p] \land \lnot p$. Podmiot _zarozumiały_ wierzy, że jego wierzenia nigdy nie są niedokładne: $[\forall [p] \implies p]$. Podmiot jest _spójny_ jeżeli $[p] \implies \lnot [\lnot p]$. Podmiot jest _normalny_ jeżeli $[p] \implies [[p]]$. (Podmiot _osobliwy_: $\exists [p] \land [\lnot[p]]$.)

Podmiot _regularny_ jeżeli $p \implies q$ wierzy, że $[p] \implies [q]$. Formalnie rzecz biorąc, $[\forall (p \implies q) \implies [[p] \implies [q]]$. Podmiot _refleksywny_ dla każdej propozycji _p_ wierzy w jakąś propozycję _q_ tak, żeby $[q \iff ([q] \implies p)]$. Formalnie rzecz biorąc, $\forall_p \exists_q [q \iff ([q] \implies p)]$ Podmiot _ostrożny_ nie wierzy w $p$ jeżeli $p$ prowadzi do sprzecznego przekonania: $[[p] \implies [\perp]] \implies [\lnot p]$.

Podmiot typu $1$ wierzy w implikację i całość klasycznej logiki, czyli wcześniej lub później będzie wierzyć w każdą tautologię, a $[p \implies q] \land [p] \implies [q]$. Podmiot typu $1*$ dodatkowo wierzy, że wierzy w tę implikację: $[[p \implies q] \land [p] \implies [q]]$. Podmiot typu $4$ jest podmiotem typu $1$, który wierzy też, że $[([p] \land [p \implies q]) \implies q]$ oraz jest _normalny_ i wierzy, że jest _normalny_.

Zauważmy, że pierwsze 14 właściwości nic dla nas tutaj w zasadzie nie znaczą, jednak reszta naprawdę pozwala sobie zracjonalizować dalszą część. Przejdźmy więc od razu do konkretów.

## Konkrety

Obecne systemy wejścia są kompromisem pomiędzy wieloma czynnikami, niektóre sięgają najstarszych korzeni kultury europejskiej. Czytanie tekstu od lewej do prawej i ułamki dziesiętne są tylko jednym z przykładów elementów przenoszonych bezmyślnie z pokolenia na pokolenie.

Racjonalną rzeczą jest naprawić ten problem. Są dwa lub cztery rozwiązania:

1. zmienić kulturę europejską, żeby czytała tekst od prawej do lewej, co oczywiście zwiększy czytelność kodu;
2. zrobić żeby tylko w zadaniach liczby były pisane od prawej do lewej, co chociaż ułatwi wczytywanie tekstu, może spotkać się ze sprzeciwem ze strony środowiska za sprawą pojawienia się pewnej dychotomii kierunkowości myślenia;
3. zastąpienie wczytywania liczb po kolei poprzez wywołania funkcji, każda z nich by zwracała tylko jedną liczbę.

Rozwiązanie pierwsze ma pewne nieoczywiste wady: może okazać się, że niektóre starsze zadania mogą być ciężkie do przeczytania przez użytkowników przyzwyczajonych tylko do nowego systemu. Więc tutaj sukces będzie w paradoksalny sposób porażką. Coś takiego sugeruje jednak drugie rozwiązanie.

Drugie rozwiązanie natomiast wydaje się idealne, jednak jak już jest napisane wyżej, takie nie jest. Mimo wszystko jednak, jest lepsze od pierwszego. Nadal mimo tego, jest błędne.

Dlatego jedynym świetnym rozwiązaniem jest rozwiązanie trzecie. Postuluję zatem, aby wszystkie zadania wszystkie dane przekazywały jako wywołania funkcji. Zwiększa to czytelność:

```cpp
// Nieczytelne: nie wiemy co to są n, m, k czy w jakiej są kolejności.
cin >> n >> m >> k;

// Rozwiązanie 1 – słabe.
;ʞ << m << n << niɔ

// Rozwiązanie 2 – lepsze.
;n << m << ʞ << niɔ

// Rozwiązanie 3 – świetne:
get_n(), get_m(), get_k();
```

Nazwy w biblioteczkach są mało deskryptywne. Powinny więc się skommitować do jakiegoś targetu i stać się w pełni preskryptywne, wprowadzając pewien porządek. Cytując pewien traktat filozoficzny z lat 30. XX wieku:

> Tym, czym obyczaj dla życia, jest dla państwa prawo [...]. To i tylko to może pokonać chwiejne, ciągle kwestionowane intelektualne koncepcje i nadać im kształt, bez którego [...] nie może istnieć. W innym wypadku koncepcja metafizycznego poglądu na życie -- innymi słowy filozoficznej opinii -- nigdy z tego nie wyrosłaby. Dlatego atak przeciwko dogmatom jest bardzo podobny do walki przeciwko powszechnym, prawnym podstawom państwa i prowadzi do kompletnej anarchii, aż znajdzie swój koniec w beznadziejnym, religijnym nihilizmie.

Trzeba tutaj zwrócić uwagę na to, że każdy obecnie ma własne wyobrażenie o przeznaczeniu nazw funkcji w biblioteczkach, traktują je w sposób instrumentalny. Tylko przez przekwalifikowanie tego wszystkiego na niepodważalne wartości autoteliczne jesteśmy w stanie wziąć sprawy we własne, opiekuńcze ręce.

Dużo się mówi o różnicy pomiędzy `snake_case` oraz `CamelCase`. To o czym wam nie mówią, to pewne ukryte przez Uniwersytet Stanforda badania statystyczne potwierdzające, że jedna z opcji jest obiektywnie lepsze i o dziwo jest to zawsze ta sama, która jest w standardowej bibliotece szablonów języka. Jedynym wyjątkiem są tutaj języki bez wbudowanej standardowej biblioteki szablonów, tj. Python -- jest to jednak pewien żółtodziób wśród języków programowania i nie powinien być brany na poważnie, bo użytkownicy nie rozumieją roli interpretera. Są głupi i nie powinniśmy ich słuchać, co jest swego rodzaju wskaźnikiem poziomu samego języka tworzonego przez tę społeczność, więc Python jest głupi. Kontrowersyjna opinia zakończona, od teraz wracamy do obiektywnych faktów.

Kolejną moją opinią, która często jest źle rozumiana: zadania powinny być pisane w formacie tak zwanych manpage'ów funkcjonujących na zasadzie Linuxa. Wtedy w treść zadania wbudowane mogłoby być polecenie do wysyłania zgłoszeń, co znacznie zmniejszyłoby próg wejścia do programowania kompetetywnego, czyli olimpijskiego. Dałoby się za pomocą prostego użycia wywołań systemowych także sprawdzać rozwiązania na lokalnym komputerze, co znacznie obniży koszty utrzymania serwera ze strony organizatorów olimpiady. To jest też przy okazji kolejnym argumentem za moim wyjściem numer 3 w tekście wyżej.

## Konkluzja

Jeżeli się nie zgadzasz z powyższym tekstem -- bardzo dobrze, ale pamiętaj, twoja opinia nie jest jedyna i prawdopodobnie błędna jeśli opiera się tylko na ślepym podążaniu za ostatnimi trendami stylów programistycznym. Jeżeli chcesz odpowiedzieć, to odpowiedz, ale pamiętaj rozważyć wszystkie argumenty holistycznie, nie wyrywaj sobie jednego czy dwóch, które uważasz że łatwo obalić jak będą wyrwane z kontekstu. Stajesz się wtedy tylko takim żartem człowieka, taką parodią samego siebie, ludzie stworzą sobie opinię o tobie na podstawie, choć krzywdzącego, to prawdziwego, przesłania.
