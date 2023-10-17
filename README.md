Alma Mater Studiorum - Università di Bologna       Dipartimento Informatica - Scienza e Ingegneria - DISI Laurea Magistrale in Informatica

Corso di Intelligenza Artificiale

**Modelli di classificazione per la diagnostica della SARS-CoV-2 in un’ottica di ecosostenibilità**

**Gabriele Fogu - 0001101637 - gabriele.fogu@studio.unibo.it Martina Daghia - 0001097932 - martina.daghia@studio.unibo.it Martina Zauli - 0001097933 - martina.zauli@studio.unibo.it Riccardo Spini - 0001084256 - riccardo.spini@studio.unibo.it**

*17 ottobre 2023        Anno scolastico 2022-2023*

**Indice**

**1 Introduzione 3**

**2 Descrizione del problema 5**

1. [Soluzioni proposte ](#_page6_x85.04_y123.48). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1. [Miglioramento dei materiali di produzione del test . ](#_page6_x85.04_y295.72). . . . . . . . . 6
1. [Miglioramento sul trasporto ](#_page6_x85.04_y597.34). . . . . . . . . . . . . . . . . . . . . . 6
1. [Smaltimento .](#_page8_x85.04_y544.23) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2. [Descrizione del prodotto finale .](#_page9_x85.04_y585.45) . . . . . . . . . . . . . . . . . . . . . . . . 9
3. [Descizione del dataset ](#_page10_x85.04_y253.49). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

**3 Dati inquinamento tamponi NAAT per SARS-CoV-2 12**

1. [Produzione del test kit ](#_page12_x85.04_y789.53). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1. [Trasporto ](#_page13_x85.04_y321.06). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1. [Processo di estrazione dell’RNA ](#_page13_x85.04_y526.08). . . . . . . . . . . . . . . . . . . . . . . . 13
1. [Trattamento dei rifiuti .](#_page13_x85.04_y727.61) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1. [Impatti ambientali per il test dell’acido nucleico COVID-19 . .](#_page14_x85.04_y585.86) . . . . . . . 14

**4 Metodo d’approccio 18**

1. [Organizzazione del lavoro di gruppo .](#_page18_x85.04_y178.73) . . . . . . . . . . . . . . . . . . . . . 18
1. [Revisione della letteratura .](#_page18_x85.04_y524.38) . . . . . . . . . . . . . . . . . . . . . . 18
1. [Dati e strumenti disponibili ](#_page19_x85.04_y145.15). . . . . . . . . . . . . . . . . . . . . . 19
2. [Progettazione e sviluppo ](#_page19_x85.04_y294.55). . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3. [Applicazione al caso specifico ](#_page20_x85.04_y275.82). . . . . . . . . . . . . . . . . . . . . . . . . 20
1. [Modellazione del Dataset .](#_page20_x85.04_y422.81) . . . . . . . . . . . . . . . . . . . . . . . 20
1. [Estrazione delle features ](#_page21_x85.04_y142.82). . . . . . . . . . . . . . . . . . . . . . . . 21
4. [Training del modello e misurazione delle performance .](#_page26_x85.04_y640.34) . . . . . . . . . . . 26
5. [Limitazioni ](#_page27_x85.04_y361.84). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

**5 Risultati sperimentali 28**

1. [Studio di ablazione: comparazione tra diverse configurazioni .](#_page28_x85.04_y738.63) . . . . . . . 29
1. [Selezione delle features ](#_page30_x85.04_y87.53). . . . . . . . . . . . . . . . . . . . . . . . . 30
1. [Soglia per la positività di una predizione .](#_page32_x85.04_y659.71) . . . . . . . . . . . . . . 32

22

3. [Configurazione migliore .](#_page35_x85.04_y797.79) . . . . . . . . . . . . . . . . . . . . . . . . 36
2. [Studio di comparazione: comparazione con le soluzioni presenti in letteratura 36](#_page36_x85.04_y432.24)

**6 Costi ambientali del modello 39**

1. [Costo in spazio, tempo ed energia .](#_page39_x85.04_y399.63) . . . . . . . . . . . . . . . . . . . . . . 39
1. [Costo in emissioni ](#_page40_x85.04_y474.15). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

**7 Conclusione e progetti futuri 42**

[7.1 Progetti futuri .](#_page42_x85.04_y674.78) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

**Bibliografia 44 Matrici di confusione 45 Boxplots 49**

1  **Introduzione**

La<a name="_page3_x85.04_y87.53"></a> pandemia da COVID-19, causata dal coronavirus SARS-CoV-2, ha scosso il mondo intero dal suo scoppio nel 2019, trasformando radicalmente la nostra società e lasciando un’impronta indelebile sulla salute pubblica, sull’economia globale e sulla vita di miliar- di di persone in tutto il mondo. Questa crisi sanitaria senza precedenti ha richiamato l’attenzione dell’intera comunità internazionale, ponendo una serie di sfide complesse e mettendo alla prova la resilienza delle nazioni. La diffusione del virus ha imposto una serie di sfide significative nel campo della diagnostica e del monitoraggio della malattia; al fine di contenerla, è stato necessario identificare rapidamente e accuratamente le persone affette da COVID-19. I test diagnostici si basano principalmente su campioni biologici, come i tamponi nasofaringei, che richiedono personale sanitario specializzato e strutture dedicate. A tal proposito, risulta di fondamentale importanza sottolineare l’enorme im- patto ambientale che l’utilizzo a larga scala di questi strumenti ha portato in termini di emissioni inquinanti prodotte da ciascun test e dai loro smaltimenti.

Il presente elaborato si propone di esplorare un approccio innovativo per il rilevamento del COVID-19, utilizzando un dataset di file audio etichettati. L’ipotesi di base è che il virus SARS-CoV-2 possa influenzare le caratteristiche acustiche del sistema respira- torio umano, generando specifici segnali sonori che possono essere rilevati e analizzati. Questo metodo potrebbe offrire un’alternativa non invasiva e conveniente per la diagnosi precoce, la sorveglianza della malattia e per un impatto ambientale meno invasivo. Sa- ranno qui esaminate diverse metodologie di analisi dei file audio, tra cui l’estrazione di tratti acustici rilevanti, l’utilizzo di algoritmi di machine learning per la classificazione e l’elaborazione dei dati per identificare modelli distintivi correlati al COVID-19. Non saranno prese in considerazione le sfide legate alla raccolta dei dati audio, poiché reperiti dal nostro tutor supervisionante Stefano Pio Zingaro. Aspetto cruciale di questa ricerca sarà la validazione dei risultati ottenuti attraverso l’utilizzo di un dataset di controllo e la comparazione dei risultati con i test diagnostici tradizionali. Saranno altresì prese in considerazione le metriche di precisione, sensibilità e specificità per valutare l’affidabilità e l’efficacia del metodo proposto. L’obiettivo finale di questa tesi è fornire una valutazio- ne completa dell’approccio di rilevamento del COVID-19 attraverso l’analisi di file audio etichettati. Questa metodologia potrebbe avere importanti implicazioni per la diagnosi e la sorveglianza del COVID-19, consentendo una risposta più tempestiva ed efficiente alla diffusione del virus e contribuendo a limitare gli impatti ambientali, sociali ed economici derivanti dalla pandemia.

2  **Descrizione del problema**

L’emergere<a name="_page5_x85.04_y87.53"></a> del virus SARS-CoV-2 ha avuto un impatto significativo sulla salute uma- na, ma ha anche generato conseguenze inaspettate sull’ambiente. Tra le molte misure adottate per contrastare la diffusione del virus, l’uso diffuso dei tamponi molecolari per il rilevamento del COVID-19 ha avuto un ruolo cruciale. Tuttavia, l’aumento della pro- duzione e dell’uso di questi tamponi ha suscitato preoccupazioni riguardo al loro impatto ambientale. In questa discussione, esploreremo l’impatto ambientale dei tamponi moleco- lari utilizzati durante la pandemia di COVID-19.

Da un lato, i tamponi molecolari sono diventati uno strumento essenziale nella diagnosi del COVID-19, in quanto consentono di identificare il virus con una buona precisione. Tuttavia, è importante comprendere che questi tamponi sono costituiti da materiali che richiedono una produzione e una gestione adeguata per minimizzare il loro impatto sul- l’ambiente. Ad esempio, i tamponi molecolari contengono plastica, tra cui tubi e tappi, nonché reagenti chimici necessari per il processo di analisi. L’uso su larga scala dei tampo- ni molecolari ha portato a un aumento significativo della produzione di rifiutibiomedici, in particolare di plastica monouso. La gestione inadeguata di questi rifiutipotrebbe compor- tare impatti negativi sull’ambiente, come l’inquinamento dei suoli e delle acque, nonché la produzione di gas serra. Inoltre, la produzione di tamponi molecolari richiede l’utilizzo di risorse naturali, energia e acqua. L’estrazione e la lavorazione di queste risorse possono contribuire all’esaurimento delle risorse naturali e all’inquinamento associato. È fonda- mentale valutare la sostenibilità dei processi produttivi e cercare soluzioni che riducano l’impatto ambientale complessivo. Per mitigare l’impatto ambientale dei tamponi mole- colari, sono state proposte diverse iniziative, come il metodo che proponiamo in questo elaborato.

Noi, come team di ricerca, abbiamo scelto di concentrarci sull’analisi dell’impatto am- bientale dei tamponi molecolari perché riteniamo che sia una questione di fondamentale importanza per la salvaguardia del nostro pianeta. Il nostro impegno per l’analisi del- l’impatto ambientale dei tamponi molecolari nasce dalla consapevolezza delle sfide che il mondo affronta in termini di cambiamenti climatici, degrado ambientale e perdita di biodiversità, e riteniamo che sia nostro dovere contribuire alla ricerca di soluzioni che minimizzino l’impatto delle attività umane sull’ecosistema.

Ci auguriamo che i risultati della nostra ricerca possano contribuire a sensibilizzare e in-

formare le decisioni future riguardo all’utilizzo responsabile dei tamponi molecolari e alla gestione sostenibile dei rifiuti biomedici.

1. **Soluzioni<a name="_page6_x85.04_y123.48"></a> proposte**

Al finedi attenuare il problema dell’impatto ambientale causato dalla produzione di messa dei tamponi molecolari, ricercatori hanno avanzato diverse proposte di miglioramento [6] al fine di risolvere il problema legato all’inquinamento proposto nel capitolo precedente. Vedremo soluzioni ecosotenibili proposte per il packaging del test, il trasporto fino al punto di analisi e lo smaltimento (processo con un impatto sull’ambiente più elevato, come osservato nel capitolo [3).](#_page12_x85.04_y87.53)

1. **Miglioramento<a name="_page6_x85.04_y295.72"></a> dei materiali di produzione del test**

In primo luogo nella Tabella [1 descriviamo](#_page7_x85.04_y90.76) i componenti principali e relativi ingredienti per la produzione del kit di test.

È consigliabile dunque, partendo dalla tabella proposta, cambiare i materiali utilizzati per la produzione intera del test (packaging e materiali di produzione):

- **Packaging** : sostituzione delle scatole in carta patinata con scatole in carta Kraft biodegradabile e riciclabile;
- **Imballaggio** : l’imballaggio in plastica biodegradabile è selezionato come materiale sostitutivo per i sacchetti a chiusura lampo;
- **Tampone** : l’asta del tampone faringeo è realizzata in legno di betulla anziché in plastica, causa il basso grado di degradazione.
2. **Miglioramento<a name="_page6_x85.04_y597.34"></a> sul trasporto**

Nel capitolo [3 ](#_page12_x85.04_y87.53)vediamo uno studio [\[2\] ](#_page44_x85.04_y205.72)che dimostra come il trasporto sia un fattore di inquinamento molto influente, parliamo infatti di circa il 13*.*3% di gas ad effetto serra sul totale, circa il 20% della produzione di metalli pesanti, circa il 4% di agenti inquinanti scaricate nell’acqua e quasi il 25% di inquinanti atmosferici. Questi dati sono stati presi tenendo conto di un furgone rappresentativo con motore Diesel.

Per sovvenire a tale problema i ricercatori hanno proposto la soluzione di utilizzare **fur- goni elettrici** . Abbiamo scelto come campione un furgone elettrico con un’autonomia



|<a name="_page7_x85.04_y90.76"></a>**Componenti**|**Ingredienti**|
| - | - |
|Scatola di carta|Carta rivestita in un film di plastica|
|Tubo di plastica|*Copolimero stirene* − *acrilonitrile*|
|Acqua sterile deionizzata||
|Tampone per la gola|<p>Testa soffice di *nylon*</p><p>*Copolimero stirene* − *acrilonitrile*</p>|
|VTM|Sieroalbumina bovina Liquido di Hank|
|Liquido di Hank|<p>*NaCl MgSO*4*.*7*H*2*O KCl MgCl*2*.*6*H*2*O CaCl*</p><p>*H*2*O Na*2*HPO*4*.*12*H*2*O KH*2*PO*4</p>|
|Reagente di estrazione dell’acido nucleico|<p>*Lisato*</p><p>*GuSN*</p><p>*H*2*O*</p><p>*SLS*</p><p>*Triton X*-*100 Liquido solvente GuSN*</p><p>*KCl*</p><p>*Etanolo*</p><p>*Eluant*</p>|
|Miscela PCR|<p>*Acqua ultrapura Tris Hcl*</p><p>*KCl*</p><p>*MgSO*4</p><p>*Primer*</p>|
|Taqman|<p>*H*2*O*</p><p>(*NH*4)2*SO*4 *KH*2*PO*4 *MgSO*4 *CH*4*N*2*O Nacl*</p><p>*Tris Hcl NaOH HNO*3</p>|
|Soluzione tampone|*Tris Hcl KC MgCl*2 *H*2*O*|

Tabella 1: Componenti principali per la produzione e impacchettamento di un test

dell’acido nucleico. [\[6\]](#_page44_x85.04_y459.36)

di guida a pieno carico di 390 km e una capacità della batteria di 98*,*09 kWh, che ha un consumo energetico a pieno carico di 0*,*25 kWh/km in condizioni ideali a confronto dei 948*,*72 MJ/km di un furgone Diesel nelle stesse condizioni.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.001.png)

<a name="_page8_x85.04_y153.53"></a>Figura 1: Distanza e tempo medio di trasporto dei kit di test molecolare per le province

di Beijing, Tianjin, Hebei.

Nella figura [2 ](#_page8_x85.04_y376.49)possiamo notare quanto un furgone Diesel sia notevolmente più inquinante di un furgone elettrico tenendo conto della distanza media di trasporto per un singolo kit di test, riportata nella Figura 1.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.002.png)

<a name="_page8_x85.04_y376.49"></a>Figura 2: Confronto degli impatti ambientali tra il trasporto con furgoni diesel (DV) e

quello con furgoni elettrici (EV) per le province cinesi di Beijing, Tianjin, Hebei.

3. **Smaltimento**

<a name="_page8_x85.04_y544.23"></a>Lo smaltimento è la prima causa di inquinamento derivato dai tamponi molecolari come notiamo dalla Figura 9[ e](#_page16_x85.04_y80.31) [10, ](#_page16_x85.04_y394.69)giunge quindi fondamentale ovviare delle metriche di ecoso- stenibilità per il trattamento dei rifiuti. Il metodo sottostante esplica come funziona la maggior parte dello smaltimento dei rifiuti sanitari. Riprenderemo meglio questa figura nel capitolo [3.](#_page12_x85.04_y87.53)

![ref1]

<a name="_page9_x85.04_y80.31"></a>Figura 3: Riassunto della produzione del test NAAT

Un primissimo approccio è quello di utilizzare un modello integrato di trattamento dei rifiuti con apparecchiature di incenerimento a microonde. In questo scenario, i rifiuti sanitari vengono prima sterilizzati e disinfettati mediante irradiazione a microonde assi- stita da riscaldamento a vapore, per poi essere inviati all’inceneritore. Sviluppando tale metodo modificheremo la Figura 3[ nella](#_page9_x85.04_y80.31) Figura 4[ che](#_page9_x85.04_y405.43) segue:

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.004.png)

<a name="_page9_x85.04_y405.43"></a>Figura 4: Sistema integrato di trattamento dei rifiuti sanitari.

2. **Descrizione<a name="_page9_x85.04_y585.45"></a> del prodotto finale**

Quello che vogliamo produrre con la nostra attività di ricerca e sviluppo è un’applicazione mobile che possa essere impiegata da aziende, uffici pubblici e più in generale luoghi di lavoro e di aggregazione, che possa essere una valida alternativa all’impiego di tamponi rapidi o molecolari per i test di *routine*. Non abbiamo la pretesa di ottenere un modello predittivo che superi qualitativamente le performance e l’accuratezza dei test fisici e che dunque li sostituisca, il nostro impegno è piuttosto da intedersi come un tentativo di creare un algoritmo affidabile e leggero che possa soddisfare la necessità di mantenere monitorata la situazione sanitaria all’interno di contesti pubblici. Poniamo caso che,

malauguratamente, divampi una nuova pandemia: sarebbe auspicabile per chiunque si veda costretto a frequentare un ambiente pubblico, sia esso lavorativo o didattico, una monitorazione quotidiana dello stato di infezione di lavoratori e studenti, per impedire quando possibile la nascita di focolari infettivi.

I tamponi nasofaringei sono strumenti di test invasivi, costosi e inquinanti. La nostra teoria è che per un controllo quotidiano e superficiale si possa impiegare un modello predittivo che seppur meno preciso, sia facile da utilizzare, accessibile tramite smartphone, non invasivo e notevolmente meno inquinante.

3. **Descizione<a name="_page10_x85.04_y253.49"></a> del dataset**

Nel giorno martedì 18 Aprile 2022 ci è stato inviato una cartella dal nome " **KDD\_paper\_data** " di grandezza 1.63 GB siffatta:

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.005.png)

Figura 5: Cartella iniziale contenente sottocartelle che includono gli audio.

Notiamo subito che la cartella si divide in due macro-gruppi:

- Audio reperiti con dispositivi ***Android***.
- Audio reperiti via ***Web***.

Per ognuno di questi insiemi grandi insiemi abbiamo dei dati audio che indicano:

- Audio di persone presi da dispositivi **Android** e dal **Web** che hanno **Asma** e **Tosse** e **non hanno Covid** ;
- Audio di persone presi da dispositivi **Android** e dal **Web** che **hanno Covid** e **hanno Tosse** ;
- Audio di persone presi da dispositivi **Android** e dal **Web** che **hanno Covid** e **non hanno Tosse** ;
- Audio di persone presi da dispositivi **Android** e dal **Web** che **non hanno Covid** e **nessun Sintomo** ;
- Audio di persone presi da dispositivi **Android** e dal **Web** che **non hanno Sintomi** e **hanno Tosse** .

Oltre alle cartelle di audio sopra descritte, compaiono anche dei file *json* contenenti in- formazioni sugli audio. Noi abbiamo utilizzato in particolare il file nominato "*files.json*", in cui vi erano tutti i nomi dei files audio già divisi per etichette.

Tutte le collezioni di dati audio reperiti con dispositivi Android hanno due sotto-cartelle già ben definite prodotte dagli stessi campioni. Quindi per ogni persona abbiamo:

- **cough** : audio di solo colpi di tosse;
- **breath** : audio di solo respiro.

A differenza dei file reperiti da dispositivi Android, i file presi dal Web erano organizzati in sotto cartelle definite dal giorno dell’acquisizione dei file audio di tosse e respiro.

Con l’intento di creare un’applicazione software per *mobile* abbiamo deciso di lavorare, seppur con meno dati, unicamente con i dati campionati tramite dispositivi Android (536 audio).

3  **Dati inquinamento tamponi NAAT per SARS-CoV-2**

<a name="_page12_x85.04_y87.53"></a>L’impatto ambientale dei tamponi molecolari durante la pandemia di COVID-19 è un argomento di crescente preoccupazione e interesse. Sebbene i tamponi molecolari siano stati fondamentali per il rilevamento e la diagnosi del virus, il loro utilizzo su larga scala ha generato impatti significativi sull’ambiente. Sebbene i tamponi rapidi basati sull’antigene siano maggiormente utilizzati, questi hannno una sensibilità del 61% per tale ragione abbiamo utilizzato per il nostro motivo di studio i tamponi dell’acido nucleico NAAT (Test di amplificazione degli acidi nucleici) che hanno una precisione di **accuratezza dei veri positivi che varia dall’87% al 97%** . [\[3\]](#_page44_x85.04_y301.72) Pertanto, costruiamo un inventario dettagliato del ciclo di vita (LCI - Life Cicle Impulse) per COVID-19 NAAT approcciandolo dalla sua nascita al suo smaltimento (approccio "cradle-to-grave") e valutiamo quantitativamente più categorie di impatti ambientali che ne derivano.

Poiché è difficile ottenere informazioni accurate sulla distanza, il tempo e la modalità di trasporto per la consegna dei kit di test in tutto il mondo, consideriamo la Cina come caso di studio, per cui è più facile reperire dati ufficiali.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.006.jpeg)

<a name="_page12_x85.04_y443.15"></a>Figura 6: Approccio "cradle-to-grave" dell’LCI di un tampone NAAT. [6]

Partendo dalla Figura 6[ eseguiremo](#_page12_x85.04_y443.15) dei calcoli sull’impatto ambientale portato dai tam- <a name="_page12_x85.04_y789.53"></a>poni eseguiti in Cina.

1. **Produzione del test kit**

Il kit di test fornisce i materiali chiave per i test diagnostici COVID-19, che includono:

- **VTM** (Virale Trasport Medium): una soluzione utilizzata per raccogliere, traspor- tare e conservare campioni biologici contenenti virus;
- Reagente di estrazione dell’acido nucleico;
- Miscela di reazione a catena della polimerasi (PCR - polymerase chain reaction);
- Acqua deionizzata sterile e materiali di imballaggio;
- Accessori come carta patinata, sacchetti sigillanti e tamponi faringei.
2. **Trasporto**

<a name="_page13_x85.04_y321.06"></a>In questo caso teniamo conto dei trasporti su strade nazionali cinesi il che implica che i kit di test vengono spediti direttamente dai produttori ai centri di test senza distribuzione

e stoccaggio, altri modelli di consegna come gli aerei non sono considerati. I test devono essere tarsportati con una temperatura di -20°C, questo è possibile grazie all’ausilio di incubatori refrigeranti. Ad esempio: un furgone diesel rappresentativo (7,6m × 2,45m × 2,5m) a pieno carico potrebbe trasportare 208 incubatori e ogni incubatore può immagaz- zinare 264 kit di test.

Un simile furgone diesel a pieno carico richiede 948,72 MJ per kilometro.

3. **Processo<a name="_page13_x85.04_y526.08"></a> di estrazione dell’RNA**

Le principali apparecchiature utilizzate nei processi di estrazione sono:

- Un sistema di estrazione dell’acido nucleico con una potenza di 800 VA;
- Un refrigeratore con una potenza 900 VA.

Il consumo di energia elettrica è calcolato in base al tempo di funzionamento e alla potenza massima erogata, ciò comporta che l’utilizzo di elettricità utilizzata per test viene stimata <a name="_page13_x85.04_y727.61"></a>in modo equo.

4. **Trattamento dei rifiuti**

Dato che i rifiuti sanitari sono classificati come rifiuti pericolosi a causa del rischio che comportano di contenere agenti infettivi, il riciclaggio dei materiali non è considerato in questo lavoro.

Nella pratica corrente, la disinfezione viene eseguita su tutti i rifiuti della diagnostica COVID-19 mediante disinfettanti al cloro seguiti da sterilizzazione a vapore ad alta tem- peratura [\[2\].](#_page44_x85.04_y205.72) In seguito avviene lo smaltimento in un inceneritore ad alta temperatura (850 – 1200 °C). Infine, il processo si conclude con lo scarico sicuro dei fumi dopo la tempra. Gli impatti ambientali del trasporto dei rifiuti sanitari, dai luoghi sanitari agli impianti di trattamento dei rifiuti, sono esclusi perché tali dati non sono disponibili e variano notevolmente.

La Figura [7 ](#_page14_x85.04_y376.94)riassume i componenti principali e l’ampia gamma di ingredienti generati ed utilizzati per lo smaltimento dei kit di test [\[6\].](#_page44_x85.04_y459.36)

![ref1]

<a name="_page14_x85.04_y376.94"></a>Figura 7: Riassunto della produzione del test NAAT

5. **Impatti<a name="_page14_x85.04_y585.86"></a> ambientali per il test dell’acido nucleico COVID-19**

La Figura [9 ](#_page16_x85.04_y80.31)mostra la quantità di emissioni di gas a effetto serra e inquinanti per NAT COVID-19 e la Figura [10 ](#_page16_x85.04_y394.69)illustra una ripartizione dettagliata per ciascun processo per identificare i principali apporti negativi all’ambiente. Entrambe le figure sono state prese dal lavoro *["Potential Life-Cycle Environmental Impacts of the COVID-19 Nucleic Acid Test"*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9469759/)* di Ling Ji, Yongyang Wang, Yulei Xie, Ming Xu, Yanpeng Cai, Shengnan Fu, Liang Ma, e Xin Su. [\[6\]](#_page44_x85.04_y459.36) **Le emissioni totali di gas serra (GHG) per test sono pari a 612,90g** (precisamente 92,7% *CO*2, 7,3% *CH*4). Riportiamo la tabella con i dati relativi alle emissioni per ogni test dell’elaborato precedentemente citato.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.007.png)

Figura 8: Tabella con dati delle emissioni della Cina

La Figura [9 ](#_page16_x85.04_y80.31)mostra che l’impatto del trattamento dei rifiutiè il più pronunciato con 71,3% delle emissioni di gas serra (435,63g *CO*2). Durante questo processo, i rifiuti sanitari (in particolare i puntali delle pipette) sono il principale inquinante responsabile di oltre il 60,0% di *CH*4. Un ulteriore 23,6% delle emissioni di GHG deriva dall’utilizzo di energia per la disinfezione e il trattamento a vapore dei rifiuti sanitari contagiosi. Seguiti dal trattamento dei rifiuti, la produzione e il trasporto dei kit di test contribuiscono rispetti- vamente al 14,5% e al 13,3% delle emissioni totali di gas a effetto serra. Nel processo di produzione del kit di test, il VTM ha più impatto rispetto ad altri componenti principali

con 60,5g di *CO*2. Anche altri materiali ausiliari come canna di plastica (23,3 g *CO*2) e tamponi faringei (5,5g *CO*2) contribuiscono per il 32% alle emissioni di gas serra della produzione del kit di test.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.008.jpeg)

<a name="_page16_x85.04_y80.31"></a>Figura 9: Abbreviazioni: TK, produzione di kit di test; TP, trasporto; RE, estrazione

dell’RNA; TE, test; e WT, trattamento dei rifiuti.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.009.jpeg)

<a name="_page16_x85.04_y394.69"></a>Figura 10: Ripartizione delle emissioni GHG e inquinanti per ciascun processo.

Possiamo affermare che **la maggior parte dei GHG causati dalla produzione dei tamponi dell’acido nucleico (NAAT) sono originati da quello che è lo smalti- mento** di questi. L’impatto sul riscaldamento globale di tale processo è definito nell’isto- gramma [11.](#_page17_x85.04_y80.31)

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.010.png)

<a name="_page17_x85.04_y80.31"></a>Figura 11: Abbreviazioni: TR\_RI, trattamento rifiuti; E\_RNA, processo di estrazione

RNA

Forti di queste considerazioni, il nostro team di ricerca ha pensato ad un’applicazione che permetta di risolvere il problema dei tamponi come spiegato nel paragrafo 2.2.

Sebbene è stato quindi costatato essere molto inquinanti, come detto in precedenza, i tamponi NAAT sono attualmente il metodo più preciso con una **accuratezza del 87- 97%**.

Nel prossimo capitolo quindi introduciamo il metodo d’approccio utilizzato per l’imple- mentazione del prodotto finale.

4  **Metodo d’approccio**

<a name="_page18_x85.04_y87.53"></a>In questo capitolo esploriamo ed analizziamo le fasi di formulazione del problema, analisi dei dati, progettazione della soluzione e le tecniche pratiche implementative impiegate per lo svolgimento di questo lavoro di ricerca.

1. **Organizzazione<a name="_page18_x85.04_y178.73"></a> del lavoro di gruppo**

La prima fase del nostro lavoro è stata quella di formulare collettivamente in maniera formale il problema che avevamo decciso di affrontare, e successivamente l’organizzazione efficace della forza lavoro.

***Definizione formale del problema**: Vogliamo creare un algoritmo che possa esse- re implementato da un’applicazione mobile, che sia di facile utilizzo e che sia preciso ed efficace quanto più possibile nella diagnosi dell’infezione da SARS-CoV-2. L’obiettivo di questo algoritmo non è quello di essere più preciso dei tamponi, ma di essere abbastanza affidabile da poterli sostituire in un ottica di sostenibilità ambientale e di sicurezza nel- l’ambiente di lavoro.*

Il gruppo, formato da 4 persone, si è diviso la **fase di ricerca e studio della let- teratura** esistente in materia (cap. [4.1.1) ](#_page18_x85.04_y524.38)e la fase di **analisi dati e studio degli strumenti e delle tecnologie disponibili** (cap. [4.1.2).](#_page19_x85.04_y145.15)

1. **Revisione<a name="_page18_x85.04_y524.38"></a> della letteratura**

La letteratura che costituisce la base di conoscenze da cui il gruppo di studio partiva consisteva nel lavoro di tesi di Laurea Magistrale di Vanigli L. [\[10\] riv](#_page44_x85.04_y626.98)elatosi presto in- sufficiente a guidarci in maniera completa al lavoro che dovevamo svolgere. Il gruppo che si è dedicato allo studio della letteratura ed al conseguente apliamento della base di conoscenze, ha iniziato cercando paper ed articoli scentifici [4][ ](#_page44_x85.04_y353.71)[\[8\] ](#_page44_x85.04_y565.00)che trattassero il pro- blema della classificazione degli audio tramite algoritmi di ML e che fossero guide valide nel muovere i nostri primi passi in questo contesto. Successivamente le ricerche sono state più mirate e si sono concentrate nello studio delle tecniche più diffuse di analisi dei file audio, in maniera da allinearci agli standard vigenti [9][ ](#_page44_x85.04_y595.99)[\[12\]. ](#_page44_x85.04_y731.97)In ultima istanza abbiamo cercato letteratura che fosse strattamente correlata all’analisi di file audio con lo scopo di diagnosticare la SARS-CoV-2 e con grande sorpresa abbiamo trovato lo studio [1] [che ](#_page44_x85.04_y111.89)costituisce la base del lavoro effettuatoda Vanigli L. e che si è rivelato essere più completo sotto il punto di vista tecnico.

2. **Dati<a name="_page19_x85.04_y145.15"></a> e strumenti disponibili**

L’analisi dei dati a disposizione, le cui conclusioni sono state trattate nel capitolo dedicato al dataset (cap. [2.3),](#_page10_x85.04_y253.49) è mirata a capire quali fra le tecnologie e gli strumenti esistenti scegliere sulla base delle necessità e delle opportunità derivanti dalla struttura del nostro materiale. Questo studio e le ricerche effettuate sulla letteratura esistente hanno portato

i due gruppi a convergere all’idea di utilizzare [librosa.](https://librosa.org/)

2. **Progettazione<a name="_page19_x85.04_y294.55"></a> e sviluppo**

Il dataset che abbiamo scelto ci forniva audio di diversa natura, provenienti da soggetti diversi, i quali potevano essere o meno infetti dal virus SARS-CoV-2. Questa informazione è fondamentale e ci ha spinti ovviamente ad utilizzare un algoritmo di classificazione basato su un modello ad apprendimento supervisionato. Nello specifico, abbiamo deciso di utilizzare più algoritmi di classificazione in modo da poter confrontare i diversi risultati ottenuti, nello specifico:

- **Logistic Regression** : un modello di regressione non lineare utilizzato quando la variabile dipendente è di tipo dicotomico, cioè ha valore 0 o 1. L’obiettivo del modello è di stabilire la probabilità con cui un’osservazione può generare uno o l’altro valore della variabile dipendente; può inoltre essere utilizzato per classificare le osservazioni, in base alla caratteristiche di queste, in due categorie.
- **SVM** (Support-Vector Machines): sono dei modelli di apprendimento supervisio- nato associati ad algoritmi di apprendimento per la regressione e la classificazione. Dato un insieme di esempi per l’addestramento, ognuno dei quali etichettato con la classe di appartenenza fra le due possibili classi, un algoritmo di addestramento per le SVM costruisce un modello che assegna i nuovi esempi a una delle due classi, ottenendo quindi un classificatore lineare binario non probabilistico.

Il nostro algoritmo di classificazione prevede come input due file audio, uno per la tosse ed uno per il respiro, li unisce in un unico elemento e cerca di classificare non l’audio della tosse o l’audio del respiro come infetti da SARS-CoV-2, ma bensì l’unione dei due. In altri termini, l’algoritmo, a logica, classifica i pazienti e non gli audio che forniscono. Nella pratica, l’algoritmo non fa distinzione fra colpi di tosse e suono emesso dal respiro, trattando tutto come un unico dataset e li elabora tramite l’estrazione delle medesime features. Per affrontare questi problemi è stato necessario rielaborare il dataset ed estrar- re delle features che fossero significative dagli audio che possedevamo; in modo tale da identificare in maniera coerente e oggettiva la relazione fra gli indicatori sonori, fisici e matematici, ed l’infezione da SARS-CoV-2 (per una descrizione dettagliata delle features scelte, rimandiamo al cap. [4.3.2).](#_page21_x85.04_y142.82)

3. **Applicazione<a name="_page20_x85.04_y275.82"></a> al caso specifico**

Partendo dai presupposti esposti nella sezione precedente, la prima parte del lavoro è stata la definizione della struttura del nostro dataset e il conseguente adattamento dei dati alla struttura proposta. In seconda battuta è stato necessario definire quali features impiegare all’interno del nostro modello.

1. **Modellazione<a name="_page20_x85.04_y422.81"></a> del Dataset**

Come già detto in precedenza, i dati degli audio campionati con sistemi Android erano ben organizzati, abbiamo quindi sfruttato la struttura già presente in modo da ottenere come descrittore del dataset audio, un vettore di oggetti ognuno dei quali, rappresentante un audio e caratterizzato come segue:

- **filename** : una stringa contenente il nome del file di riferimento;
- **covid** : un intero fra 0 e 1 che indica se il soggetto dell’audio ha il covid oppure no, la *label* dei nostri dati;
- **audio\_features** : un oggetto contentente le features selezionate per la risoluzione del problema.

Questi tre campi, descrivono un singolo audio, tuttavia, ci è sembrato opportuno trattare ogni caso di predizione di covid, come descritto da una coppia di audio tosse e respiro (*cough* e *breath*) entrambi appartenenti ad uno stesso soggetto, quindi, ad esempio, l’u- tente identificato dalla stringa " **0c4dx8rU5G** " sarà associato a due audio. Per definire quali fosserò le features da impiegare nella ricerca della soluzione è stato necessario far riferimento alla letterature ed ai lavori simili già pubblicati in precedenza (cap. [4.1.1).](#_page18_x85.04_y524.38)

2. **Estrazione<a name="_page21_x85.04_y142.82"></a> delle features**

Siamo stati guidati principalmente da un articolo [1][ pubblicato](#_page44_x85.04_y111.89) da C. Brown e colleghi nel quale esploravano il campo della diagnosi di covid tramite crowdsourcing e analisi di segnali audio che ci ha portato a ritenere ragionevole l’impiego delle seguenti features:

- **Durata** : la durata dell’audio dopo aver eliminato il silenzio iniziale e quello finale.
- **Onset** : rappresenta il punto iniziale di un evento sonoro distintivo o di una nota musicale. L’onset è una caratteristica importante per l’analisi e la comprensione dei segnali audio, in quanto può fornire informazioni sul ritmo, sull’articolazione delle note, sulle transizioni di timbro e su altri aspetti temporali della musica o del suono.
- **Tempo** : valore scalare ottenuto da un singolo audio. Misura il numero di battiti che avvengono ad intervalli regolari di tempo. Viene inoltre impiegata per la capacità di identificare i picchi.
- **Period** : in un segnale audio, il periodo rappresenta il tempo impiegato per un ciclo completo della forma d’onda del segnale.
- **RMS Energy** : la *root-mean-square* (radice della media dei quadrati), è la misura statistica dell’energia contenuta nel segnale sonoro. Rappresenta l’ampiezza media del segnale audio nel tempo.
- **Spectral Centroid** o **Frequenza di centroide** : è una misura che fornisce un’in- dicazione della distribuzione spettrale delle frequenze di un segnale audio. Rappre- senta la "posizione" spettrale media delle frequenze presenti nel segnale. Lo spectral centroid rappresenta la "posizione" media delle frequenze nello spettro. Valori più bassi indicano che le frequenze concentrate sono principalmente nella parte bassa dello spettro, mentre valori più alti indicano che le frequenze sono distribuite su una gamma più ampia. Lo spectral centroid può essere utilizzato per caratterizzare le proprietà timbriche di un segnale audio.
- **Frequenza di Rolloff** o **di Cutoff** : è una misura che indica la frequenza al di sotto della quale cade una determinata percentuale dell’energia totale dello spettro di un segnale audio. È utilizzata per determinare il limite superiore dello spettro di frequenza rilevante del segnale.
- **Zero-crossing** : indica la frequenza con la quale un segnale attraversa lo zero in un determinato intervallo di tempo.
- **MFCC** : (*Mel-Frequency Cepstral Coefficients* ) Gli MFCC catturano informazioni importanti sulle caratteristiche spettrali del segnale audio, come le forme d’onda periodiche, le risonanze vocali e altre caratteristiche correlate al parlato. Sono ampiamente utilizzati in applicazioni di elaborazione del parlato. Usiamo le prime 13 componenti.
- ∆**-MFCC** : differenziali sul tempo (delta) del MFCC. Sono una estensione degli MFCC che catturano le variazioni temporali delle caratteristiche spettrali rispetto al tempo.
- ∆**2-MFCC** : differenziali sul delta del MFCC (coefficenti di accellerazione). Forni- scono informazioni sulle variazioni accelerate delle frequenze tra i frame consecutivi di un segnale audio.

La maggior parte delle features estratte restituisce delle serie temporali, poco adatte al nostro scopo.

È stato dunque necessario elaborare ulteriormente tutte le features definite come se-

rie temporali, ovvero: **RMSE** , **Spectral Centroid** , **Rolloff** , **Zero Crossing Rate** , **MFCC** / **MFCC** ∆/ **MFCC** ∆**2**.

Per ognuna di queste serie sono stati estratti degli indicatori statistici. Nel caso delle varianti di MFCC, le quali erano descritte da vettori di vettori, abbiamo ottenuto dei vettori di oggetti contenenti suddetti indicatori statistici.

Nello specifico sono stati estratti:

23

1. **Media** : somma di tutti i valori diviso il numero di elementi.
1. **Deviazione standard** : è un indi- ce riassuntivo delle differenze dei va- lori di ogni osservazione rispetto alla media della variabile.
1. **Minimo**
1. **Massimo**
1. **Valore mediano**
1. **Skewness** : misura dell’asimmetria della distribuzione.
1. **Kurtosis** : misura dell’allontanamen- to dalla normalità distributiva.
8. **1° quartile** o **percentile al 25%** : in- dica il valore al di sotto del quale cade il 25% dei dati in un insieme ordinato.
8. **2° quartile** o **percentile al 75%** : in- dica il valore al di sotto del quale cade il 75% dei dati in un insieme ordinato.
8. **Radice della media dei quadra- ti**: utilizzata per misurare la poten- za o l’energia media di un segnale nel tempo (le nostre serie).
8. **Scarto interquartile** : lo scarto in- terquartile (IQR, Interquartile Range)

è una misura statistica della dispersio- ne dei dati. Rappresenta la differenza tra il terzo quartile e il primo quartile in un insieme di dati.

32

In sintesi, ogni audio è descritto da **4 valori scalari** , **11 indicatori statistici ottenuti da ognuna delle 4 serie temporale semplici** ed altri **11 indicatori per ognuna delle 13 componenti utilizzate delle 3 varianti di MFCC** , per un totale di

**4** + **4** × **11** + **3** × **13** × **11 = 477 features** . Sostanzialmente, ogni utente, è descritto da due audio, tosse e respiro, i quali sono descritti da 477 features l’uno. Dunque, ogni utente è descritto da **477** + **477** = **954 features** .

Fatto ciò è stato necessario eseguire un ultimo passaggio prima di poter effettivamente impiegare il dataset all’interno del nostro modello. A questo punto della sperimentazione, il nostro dataset descriveva ogni audio come segue, nel caso del respiro ad esempio:

{

"filename\_breath": "...", "covid": ..., "audio\_features": {

...

}

}

Tuttavia, l’oggetto audio\_features non è ancora omogeneo in quanto costituito in parte da coppie chiave-scalare, in parte da coppie chiave-oggetto e in parte da coppie chiave-vettore dove ogni oggetto è costituito dagli 11 indicatori statistici e tali oggetti sono gli stessi che popolano i vettori.

Le features di un audio sono quindi elementi di questo tipo:

audio\_features: {

    duration: scalar,
    
    ...,
    
    onset: scalar,
    
    rmse: {
    
    mean: scalar,
    
    ...,
    
    iqr: scalar
    
    },
    
    ...,
    
    zc: {...},
    
    mfcc: [
    
        {
        
        mean: scalar,
        
        ...
        
        iqr: scalar
        
        }, ..., {
        
        mean: scalar, ...,
        
        iqr: scalar
        
        }
    
    ],
    
    mfcc\_d: [
    
        ...
    
    ], mfcc\_d2: [
    
        ...
    
    ]

}

Per semplicità di presentazione, le features e gli indicatori sono stati disposti nell’ordine con cui sono stati presentati durante questo trattato e l’oggetto appena descritto è da intendersi parziale e da completare con le restanti features/indicatori statistici.

La soluzione che abbiamo impiegato per uniformare i nostri oggetti all’interno del dataset consiste in un "appiattimento" degli oggetti e dei vettori tramite la seguente logica:

- Le coppie chiave-oggetto rmse: {

    "mean": scalar, ...,
    
        "iqr": scalar
    
    }
  diventano
    
    "rmse\_mean": scalar, ...
    
    "rmse\_iqr": scalar,

- Le coppie chiave-vettore, come il vettore mfcc formato da 13 elementi:

mfcc: [

    {
    
        "mean": scalar, ...,
        
        "iqr": scalar,
    
    }

]       
diventano:

"mfcc\_0\_mean": scalar, ...

"mfcc\_0\_iqr": scalar,

...

"mfcc\_12\_mean": scalar,

...

"mfcc\_12\_iqr": scalar

Ultimato questo passaggio di "appiattimento" dei vettori di features, abbiamo deciso di unire i due file appartententi ad ogni campione in un unico vettore di features, antepo- nendo le *keyword* "breath\_" e "cough\_" a tutte le features degli audio. Ottenendo degli oggetti come questo:

"filename\_breath": "breaths\_0c4dx8rU5G\_1586982341272.wav", "filename\_cough": "cough\_0c4dx8rU5G\_1586982341281.wav", "covid": 1,

"audio\_features": {

    "breath\_duration": 13.793560090702949,
    
    "breath\_tempo": 129.19921875,
    
    "breath\_period": 7425.0,
    
    ...
    
    "cough\_duration": 6.353560090702948,
    
    "cough\_tempo": 75.99954044117646,
    
    "cough\_period": 4674.0,
    
    ...

}

L’estrazione delle features, la loro organizzazione eterogenea all’interno di un dizionario e la successiva trasformazione delle features non scalari sono tutte operazioni che all’interno del codice vengono eseguite in un modulo dedicato: load\_dataset.py, il quale deve essere eseguito solo in fase di compilazione. Fatto ciò, finalmente i nostri audio sono descritti da 477 valori scalari organizzati uniformemente come valori all’interno di un oggetto *dictionary-like* come coppie chiave-valore e possiamo passare all’impiego del dataset, risultante dall’unione di audio di tosse ed audio di respiro per ogni utente, per l’effettivo training del modello.

4. **Training<a name="_page26_x85.04_y640.34"></a> del modello e misurazione delle performance**

Una volta ottenuto un dataset adatto alle esigenze di progettazione, siamo passati alla

fase di training dei modelli scelti.

Come prima cosa viene eseguita una divisione del dataset nella quale l’ **80%** degli ele- menti viene dedicato al *training* dei modelli. Dopo aver eseguito il training si passa alla parte di test dove viene richiesto al modello appena istruito (sia esso **SVM** o **Logistic**

**Regression** ) di predirre i risultati del *test-set*. Abbiamo inoltre ritenuto opportuno stan- dardizzare i dati, ovvero trasformarli in modo che avessero una distribuzione con media zero e deviazione standard unitaria. Questa trasformazione è utile quando i dati hanno scale diverse o distribuzioni non normali ed è una tecnica particolarmente diffusa ed im- piegata nel campo del machine learning.

La misurazione delle performance è stata eseguita tramite l’analisi delle metriche di va- lutazione standard, quali *Precision*, *Recall*, *Accuracy* e *F1-score*.

Sono inoltre state visualizzate le matrici di confusione dei test eseguiti per poi paragonate tutte queste metriche fra loro nelle diverse configurazioni adottate per il sistema. Nel capitolo [5.1 ](#_page28_x85.04_y738.63)viene analizzato approfonditamente il sistema e le modifiche che sono state fatte nei diversi tentativi di ottenere la configurazionemigliore, come queste configurazioni sono state decise di volta in volta e quali sono i risultati ottenuti.

5. **Limitazioni**

<a name="_page27_x85.04_y361.84"></a>Una delle principali limitazioni incontrate durante lo svolgimento del progetto riguardava la comprensione delle caratteristiche delle features utilizzate, poiché queste trattavano un ambiente di studio mai toccato prima da nessuno di noi.

È stata quindi una sfida comprendere appieno il significato e l’impatto di ciascuna feature e stabilire quali di queste fossero migliori e peggiori di altre in relazione agli obiettivi del progetto.

Oltre alla difficile comprensione delle features, data dalla loro natura, è stato difficile anche capire il loro significato rispetto al risultato restituito dal nostro metodo.

La difficoltànell’interpretazione delle features ha reso necessario un approfondimento teo- rico e un’analisi accurata per comprendere appieno la loro rilevanza e applicazione. Ulteriori limitazioni sono state date dalla raccolta di audio e nella sua organizzazione in generale:

- Annidamento dei dei file audio in cartelle non etichettate;
- Numero limitato di audio su cui poter lavorare;
- Stessi audio con formati differenti che creavano ridondanza nel dataset.
5  **Risultati sperimentali**

<a name="_page28_x85.04_y87.53"></a>Lo studio dei risultati ottenuti è stato fondamentale per comprendere errori e punti di forza all’interno del nostro lavoro. Dapprima abbiamo notato delle performance ecces- sivamente positive nelle nostre predizioni, il che, ci ha consentito di analizzare il codice ed i dati e ci ha permesso di capire che avevamo considerato come valida una feature che conteneva in se la risposta alla predizione: una categoria derivante dal nome della cartella che conteneva l’audio che se posta ad 1 o 2 implicava la presenza di covid mentre, se posta a valore 3 o 4 significava assenza di Covid nell’audio. Notato l’errore abbiamo rielaborato il dataset ed eliminato suddetta feature in quanto ovviamente non l’avremmo avuta a disposizione nel caso di audio ottenuti dagli utenti dell’applicazione finale.

Dopo di che le performance si sono abbassate drasticamente, il che ci ha portato ad ese- guire un cambio di rotta molto importante nella modalità di approccio alla risoluzione del problema: inizialmente infatti, data la poca esperienza, abbiamo peccato di lungimiranza e abbiamo deciso di organizzare il dataset per singoli audio. Sostanzialmente, un utente che avesse dato in input un audio di tosse ed uno di respiro avrebbe ottenuto due risposte diverse, in altre parole avevamo caratterizzato il problema come:

- *"**Questo audio** manifesta presenza di Covid?"*

e non come

- *"**Questo utente, rappresentato da questi due audio**, manifesta presenza di Covid?"*

L’approccio errato impiegato inizialmente depotenziava notevolmente le capacità del mo- dello, fornedogli di fatto la metà delle informazioni che aveva a disposizione per ogni utente e trattando ogni audio come un caso a se stante e non come parte di un caso più completo rappresentato da tosse e respiro.

Anche in questo caso abbiamo rielaborato la struttura del dataset unendo gli audio di tosse e respiro in un **oggetto che concettualmente è un utente** .

A questo punto le performance erano nella media, nulla di ottimo o pessimo, e abbiamo p<a name="_page28_x85.04_y738.63"></a>otuto iniziare a manipolare la configurazione del modello per ottimizzare i risultati.

1. **Studio di ablazione: comparazione tra diverse configurazioni**

Data la scarsità di elementi nel dataset, non abbiamo voluto verificare il cambio di per- formance che deriva dalla modifica del rapporto tra *training-set* e *test-set*, mantenendo stabile la configurazione **80%** del dataset per il **training-set** e **20%** per il **test-set** . Per prima cosa abbiamo visualizzato tramite un grafico a barre l’importanza delle featu- res all’interno del modello, i valori di importanza sono stati calcolati tramite la funzione mutual\_info\_classif della libreria [scikit-learn (](https://scikit-learn.org/stable/)sklearn). L’analisi del grafico risultan-

te ci ha mostrato come alcune delle features che avevamo definito non incidevano affatto sul risultato finale. Oltre a questo, la presenza di 954 features necessariamente produceva rumore all’interno del modello, dunque abbiamo deciso di ridurne il numero mantenendo le prime *N* features più importanti ed osservando le differenze nei risultati al variare di *N*.

1. **Selezione<a name="_page30_x85.04_y87.53"></a> delle features**

La seguente tabella riassume le prestazioni dei modelli LR e SVM al variare del numero di features impiegate:



|***N* features**|**LR**|**SVM**|**Valore al taglio**|
| - | - | - | - |
|954|Precision: 0.83 Recall: 0.75 F1-score: 0.78|Precision: 0.76 Recall: 0.80 F1-score: 0.77|0|
|800|Precision: 0.78 Recall: 0.79 F1-score: 0.78|Precision: 0.82 Recall: 0.77 F1-score: 0.79|0|
|700|Precision: 0.76 Recall: 0.75 F1-score: 0.75|Precision: 0.83 Recall: 0.76 F1-score: 0.79|0\.003265238832288464|
|600|Precision: 0.78 Recall: 0.78 F1-score: 0.78|Precision: 0.86 Recall: 0.77 F1-score: 0.81|0\.013183603234907526|
|500|Precision: 0.75 Recall: 0.75 F1-score: 0.74|Precision: 0.84 Recall: 0.75 F1-score: 0.79|0\.023942279686540502|
|400|Precision: 0.77 Recall: 0.79 F1-score: 0.77|Precision: 0.84 Recall: 0.74 F1-score: 0.79|0\.03499205264865424|
|300|Precision: 0.75 Recall: 0.78 F1-score: 0.76|Precision: 0.82 Recall: 0.75 F1-score: 0.78|0\.04814974536078087|
|200|Precision: 0.74 Recall: 0.74 F1-score: 0.74|Precision: 0.83 Recall: 0.75 F1-score: 0.79|0\.06713930776059573|
|100|Precision: 0.72 Recall: 0.74 F1-score: 0.72|Precision: 0.83 Recall: 0.76 F1-score: 0.79|0\.10296531938080355|
|50|Precision: 0.71 Recall: 0.72 F1-score: 0.71|Precision: 0.82 Recall: 0.75 F1-score: 0.78|0\.12542305439311274|
|10|Precision: 0.73 Recall: 0.74 F1-score: 0.73|Precision: 0.82 Recall: 0.73 F1-score: 0.77|0\.15931705110364125|

Tabella 2: Nella configurazione di partenza, se la previsione di un elemento ha probabilità >= 51% di rientrare in una classe, esso viene inserito nella classe. Questa configurazione verrà successivamente modificata.

Evinciamo da questi dati che la configurazione più promettente è quella nella quale ven- gono impiegate **600 features** per il modello SVM. Notiamo anche che il modello LR, nonostante ottenga un valore di precisione più alto quando la totalità delle features ven- gono impiegate, quando ne vengono utilizzate 600 ottiene valori fra i migliori di tutte le altre configurazioni.

Di conseguenza, fissamo *N* a 600 e procediamo a modificare la soglia di *threshold* di ca- tegorizzazione sulla base della probabilità.

Di seguito riportati **i boxplot delle migliori 6 features del dataset** in relazione alla target. Essi forniscono una rappresentazione grafica delle distribuzioni dei valori della feature per ciascuna categoria target. Il boxplot mostra la mediana come linea orizzontale

nel rettangolo centrale, il primo quartile (25%) come limite inferiore del rettangolo, il terzo quartile (75%) come limite superiore del rettangolo e i valori minimi e massimi come linee esterne (whisker). Questa visualizzazione permette di confrontare le distribuzioni delle feature per diverse categorie della target, evidenziando eventuali differenze o pattern.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.011.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.012.png)

(a) cough\_mfcc\_0\_max (b) breath\_mfcc\_d\_2\_root\_mean\_sqr

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.013.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.014.png)

(c) breath\_mfcc\_d\_2\_std\_dev (d) cough\_sc\_perc\_75

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.015.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.016.png)

(e) breath\_mfcc\_8\_perc25 (f) breath\_mfcc\_0\_perc25

*N.B.: È disponibile la raccolta completa di matrici di confusione alla fine del trattato.*

2. **Soglia per la positività di una predizione**

<a name="_page32_x85.04_y659.71"></a>La nostra priorità, in quanto alle prese con un problema di natura medica, è quella di ottenere il minor numero possibile di **Falsi Negativi** . Preferiamo un numero più alto, se pur contenuto, di **Falsi Positivi** con *trade-off* sulla precisione del modello.

34

Ricordiamo infatti che la precisione è definita come:

*Precision* = *V eriPositivi/*(*V eriPositivi* + *FalsiPositivi*)

ed indica il rapporto fra predizioni positive corrette e predizioni positive totali effettuate. Procediamo a modificare il threshold in modo da ottenere meno falsi negativi possibili. Procedendo per logica, un comportamento adatto al contesto sarebbe quello di valuta- re un caso come negativo solo se si ha una certezza che esso lo sia davvero di almeno l’80%.

***Def.***:![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.017.png)

*Threshold Positivo = X%* =⇒ *L’elemento rientra nella categoria covid se ci appartiene con una probabilità superiore o uguale all’ X%.![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.018.png)*

Partendo da questa base, vediamo come si comportano le matrici di confusione quando si va a modificare il valore di threshold positivo. Ricordiamoci che **0** sta per **Non Covid** mentre **1** significa che **Ha il Covid** , come mostrato nella tabella sottostante. Il numero di campioni nel **Test Set** è **54**.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.019.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.020.png)

(g) Matrice di confusione per LR (h) Matrice di confusione per SVM

Figura 12: **Threshold positivo all’70%** .



|**Model**|**Veri Positivi**|**Veri Negativi**|**Falsi Positivi**|**Falsi Negativi**|
| - | - | - | - | - |
|**LR**|∼29.62%|∼42.59%|∼16.66%|∼11.11%|
|**SVM**|∼38.88%|∼40.74%|∼18.51%|∼1.85%|

Tabella 3: Valori percentuali per LR e SVM configurati con threshold positivo al posto

70%.
36

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.021.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.022.png)

(a) Matrice di confusione per LR (b) Matrice di confusione per SVM

Figura 13: **Threshold positivo all’80%** .



|**Model**|**Veri Positivi**|**Veri Negativi**|**Falsi Positivi**|**Falsi Negativi**|
| - | - | - | - | - |
|**LR**|∼35.18%|∼40.74%|∼18.51%|∼5.55%|
|**SVM**|∼30.74%|∼37.03%|∼22.22%|0%|

Tabella 4: Valori percentuali per LR e SVM configurati con threshold positivo posto

all’80%.

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.023.png) ![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.024.png)

(a) Matrice di confusione per LR (b) Matrice di confusione per SVM

Figura 14: **Threshold positivo all’90%** .



|**Model**|**Veri Positivi**|**Veri Negativi**|**Falsi Positivi**|**Falsi Negativi**|
| - | - | - | - | - |
|**LR**|∼38.88%|∼41.29%|∼35.18%|∼1.85%|
|**SVM**|∼40.74.%|∼27.77%|∼31.48%|0%|

Tabella 5: Valori percentuali per LR e SVM configurati con threshold positivo posto al 90%.
37

*N.B.: È disponibile la raccolta completa di matrici di confusione alla fine del trattato.* Osserviamo che:




- **Falsi Negativi** alla Threshold;
- **Falsi Positivi** alla Threshold.

e **Veri Negativi** e **Veri Positivi**

sono in rapporto **direttamente proporzionale** sono in rapporto **inversamente proporzionale**


38

Questo è il comportamento che ci aspettavamo: alzando la soglia oltre la quale una probabilità è 1 (ovvero *covid*), stiamo dicendo all’algoritmo di scegliere più spesso 0 (*non- covid*).

Andiamo a verificare come cambiano le metriche di misura delle performance per ogni configurazione, fatto ciò sarà sufficiente decidere quale sia la configurazione che meglio risponde alle nostre necessità.



|**Threshold**|**Precision**|**Recall**|**F1-score**|
| - | - | - | - |
|**70%**|68%|77%|72%|
|**80%**|66%|86%|75%|
|**90%**|61%|91%|73%|

Tabella 6: Valori delle metriche di misurazione delle performance al variare delle

configurazioni per LR.

Vogliamo recall alta nella classificazione *covid* limitando il tradeoff sulla precisione, per far si che vengano commessi il minor numero possibile di errori sui falsi negativi, mante- nendo comunque bassi gli errori sui falsi positivi, **in modo tale che l’applicazione dia la priorità a non sbagliare sull’identificazione dei positivi, pur non restituendo**

**troppi falsi allarmi e rimanga quindi affidabile** .



|**Threshold**|**Precision**|**Recall**|**F1-score**|
| - | - | - | - |
|**70%**|68%|95%|79%|
|**80%**|65%|100%|79%|
|**90%**|56%|100%|72%|

Tabella 7: Valori delle metriche di misurazione delle performance al variare delle

<a name="_page35_x85.04_y797.79"></a>configurazioni per SVM.


54

3. **Configurazione migliore**

In base ai risultati restituiti osserviamo che **SVM si comporta meglio in generale** : fissiamo il threshold all’ **80%** in quanto possiamo notare che fornisce i risultati più bi- lanciati e adatti alle nostre necessità. A fronte di ∼ 1% di precisione in meno rispetto alla controparte LR nella classificazione del covid, SVM esibisce una Recall del **100% nella classificazione del covid** e una precisione del **100% nella classificazione di non-covid** , evidenziando come che **SVM ha performance migliori rispetto a LR** . Dunque come sintesi di questa analisi, il nostro mostra le performance ottimali rispetto alle nostre necessità quando è impostato per utilizzare **600 features su 954** e un **thre- shold positivo all’80%** .

*N.B.: La scelta del thrashold positivo all’80% è una scelta che va contestualizzata a quello che il nostro gruppo di ricerca ha valutato essere di fondamentale importanza per il nostro algoritmo, si potrebbe preferire una soglia più bassa o più alta a seconda di quelle che sono le esigenze del contesto.*

2. **Studio<a name="_page36_x85.04_y432.24"></a> di comparazione: comparazione con le soluzioni pre- senti in letteratura**

Alla luce dei nostri risultati possiamo mettere ora a parargone gli esiti del nostro lavoro con lo studio affrontato da Brown, introdotto nel paragrafo [4.1.1. \[1\]](#_page18_x85.04_y524.38)

È da tenere in considerazione che gli obbiettivi del nostro elaborato e quello di Brown sono diversi seppur abbia la stessa logica di fondo. Il loro scopo è creare un modello di classificazione che riesce a distinguere un paziente affetto da COVID-19 da uno sano utilizzando come input le registrazioni audio. In particolare sono stati studiati tre casi:

1. (*COVID-positive* vs. *non-COVID* ) Distinzione tra utenti che hanno dichiarato di essere risultati positivi al COVID-19 e utenti che non hanno dichiarato di essere risultati positivi al COVID-19, hanno una storia medica pulita, non hanno mai fumato e non hanno sintomi;
1. (*COVID-positive with cough* vs. *non-COVID with cough*) Distinzione tra utenti che hanno dichiarato di essere risultati positivi al COVID-19 e hanno la tosse come sintomo e utenti che hanno dichiarato di non essere risultati positivi al COVID-19, hanno una storia medica pulita, non hanno mai fumato e hanno la tosse;
3. (*COVID-positive with cough* vs. *non-COVID with asthma cough*) Distinzione tra utenti che hanno dichiarato di essere risultati positivi al COVID-19 e hanno la tosse come sintomo e utenti che hanno dichiarato di non essere risultati positivi al COVID-19, hanno riportato l’asma nella loro storia medica e hanno la tosse.

attraverso ad un metodo promosso dall’Università di Cambridge riassunto in questa pipeline [\[10](#_page44_x85.04_y626.98)]:

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.025.png)

Figura 15: Pipeline per il modello utilizzato da Brown e il suo team di ricerca.

In questo studio, hanno diviso il dataset per raggiungere l’obbiettivo di ogni task nella seguente suddivisione:

- il task n. 1 è stato sperimentato con registrazioni sia di respirazioni sia di colpi di tosse (cough+breath) con 141 esempi da 62 utenti per l’esito positivo (*COVID- positive*) e 298 esempi da 220 utenti per l’esito negativo (*non-COVID* );
- il task n. 2 è stato sperimentato con registrazioni di colpi di tosse (cough) con 54 esempi da 23 utenti per l’esito positivo (*COVID-positive with cough*) e 32 esempi da 29 utenti per l’esito negativo (*non-COVID with cough*);
- il task n. 3 è stato sperimentato con registrazioni di respirazioni (breath) con 54 esempi da 23 utenti per l’esito positivo (*COVID-positive with cough*) e 20 esempi da 18 utenti per l’esito negativo (*non-COVID with asthma cough*).

Nel nostro elaborato invece come visto nel paragrafo [2.3 la](#_page10_x85.04_y253.49)voriamo solamente con 536 audio diviso in 268 elementi audio di tosse e 268 audio di respiro, per un totale di 268 utenti.

La nostra **task** ( differente da quella dello studio di Brown) tratta uno studio sull’eco- sostenibilità del nostro algoritmo e sull’implementazione di un applicazione mobile che possa rimpiazzare i tamponi, non sulla sua riuscita effettiva in termini di precisione e performance.

In seguito metteremo quindi a paragone i risultati dei due studi:

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.026.png)

Figura 16: Risultati dello studio di Brown per ogni task. [1]



<table><tr><th colspan="1" valign="top"><b>Task</b></th><th colspan="1" valign="top"><b>Modalità</b></th><th colspan="1" valign="top"><b>Esempi(utenti)</b></th><th colspan="1" valign="top"><b>Modelli</b></th><th colspan="1" valign="top"><b>Precision</b></th><th colspan="1" valign="top"><b>Recall</b></th><th colspan="1" valign="top"><b>F1-Score</b></th></tr>
<tr><td colspan="1" rowspan="3" valign="top"><p>Predirre Covid</p><p>da Audio Android</p></td><td colspan="1" rowspan="3" valign="top">C+B</td><td colspan="1" rowspan="3" valign="top">158(0)/110(1)= 268</td><td colspan="1" valign="top"><i>LR</i></td><td colspan="1" valign="top">66%</td><td colspan="1" valign="top">88%</td><td colspan="1" valign="top">75%</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td colspan="1" valign="top"><i>SVM</i></td><td colspan="1" valign="top">65%</td><td colspan="1" valign="top">100%</td><td colspan="1" valign="top">75%</td></tr>
</table>

Tabella 8: Risultati ottenuti dalla **configurazione migliore** : 80% trashold positivo, 600 features.

Nel capitolo che segue andremo a calcolare l’impatto ambientale che ha il nostro algoritmo nel dispositivo mobile standard più venduto nel 2020: *Iphone 12*.

6  **Costi ambientali del modello**

<a name="_page39_x85.04_y87.53"></a>Alla luce dei risultati ottenuti, dobbiamo discutere le differenze in termini di costi am- bientali fra il nostro algoritmo nella sua configurazione migliore e l’impiego di tamponi fisici per la diagnosi preventiva di SARS-CoV-2. I fattori che terremo in considerazione per determinare il **costo ambientale** del nostro algoritmo sono:

1. Costo in **spazio** .
1. Costo in **tempo** .
1. Costo **energetico** in *KWatt* rapportata al tipo di energia impiegata.
1. Costo in **emissioni di** *CO*2.

Procediamo dunque all’analisi nella quale calcoleremo i costi sopra elencati in riferimento all’algoritmo e non all’applicazione completa che lo implementa, in quanto essa non esiste al giorno della stesura di questa ricerca.

1. **Costo<a name="_page39_x85.04_y399.63"></a> in spazio, tempo ed energia**

**Spazio**

Per ottenere il costo in spazio del nostro algoritmo è sufficiente verificare lo spazio utiliz- zato per la memorizzazione dei file di codice di interesse e del dataset:

- **Peso dataset** : 14*.*376 KB.
- **Peso file di codice** : main.py 17*,*23 KB, svm\_model.py 2*,*03 KB.

L’occupazione di spazio totale è dunque pari a 12.81926 KB, ovvero ∼12,8 MB.

**Tempo**

Per il calcolo del tempo impiegato dall’algoritmo per classificare un singolo elemento, abbiamo tracciato il tempo impiegato dall’algoritmo per eseguire la classificazione dei 54 elementi del test-set, pari a 0,003000497817993164*s* ≈ 0,30004978179*ms*. A questo punto ci basta dividere per la cardinalità del test-set per ottenere una media del tempo impiegato per classificare un singolo elemento tramite la formula

*TempoTotale TempoClassificazione* =

*ElementiTotali*

ovvero

0*,* 30004978179*ms*

≈ 0*,*00555647744*ms*

54

**Energia**

Per quanto riguarda l’energia, possiamo solo effettuare una stima basata sull’assunzione della potenza del sistema su cui viene eseguito. Secondo un articolo di Statistics and Data [\[7\]](#_page44_x85.04_y534.02) il telefono più venduto al mondo nel 2020 è stato *l’iPhone 12* e *l’iPhone 12 Mini* (Apple) con 38 milioni di copie vendute. Prendiamo l’iPhone 12 come hardware di riferimento. Sappiamo che un telefono standard consuma in media 4,5W l’ora, ipotizziamo che iPhone 12 consumi 5W [\[5\],](#_page44_x85.04_y406.37) di conseguenza, l’energia impiegata per eseguire una classificazione è

5*W* ·0*,*30004978179*ms* convertiamo i *W* in *kW* ed i *ms* in *h* ed otteniamo:

5*W* ·0*,*30004978179*ms*

1\*.*000 3*.*600*.*000

ovvero:

0*,*5 ·10− 2 ·0*,*8335·10− 7 ≈ 0*.*415·10− 9

*kW h kW/h*

2. **Costo<a name="_page40_x85.04_y474.15"></a> in emissioni**

Abbiamo impiegato la libreria *[CodeCarbon.io*,](https://codecarbon.io/)* libreria creata specificatamente per misu- rare le emissioni di *CO*2 degli algoritmi di Machine Learning. Abbiamo quindi eseguito l’algoritmo SVM con il test\_set da 54 elementi con la sua configurazione migliore e ne abbiamo calcolarto i consumi in termini ambientali.

Il report generato dalla libreria è riassumibile nei seguenti dati:

EmissionsData(

... run\_id=’c64854b3-5f23-4b8f-b0f5-b495c5cbc1cf’, duration=0.07477235794067383, emissions=3.374447892963441e-07, emissions\_rate=4.5129617226205555e-06,

...

energy\_consumed=1.4918247418006688e-06, country\_name=’Italy’,

...

|<p>
    CO **LCI di un tampone NAAT**</p><p>
    2</p>|<p>
    CO **di un ciclo di test di SVM**</p><p>
    2</p>|
| - | - |
|
    612, 90g|<p>
    0, 625 ·10−**2**</p><p>
    g</p>|

[^1])

We apply an energy mix of 226 g.CO2eq/kWh for Italy

Per eseguire la classificazionedi 54 elementi sono stati emesse 3.374447892963441·10−**7 tonnellate di** CO 2. Inoltre la libreria ci informa che per misurare questa quantità è stata assunto che in Italia venga utilizzato un mix energetico con una intensità di carbonio pari a **226 grammi di** *CO*2 equivalente emessa per ogni kilowattora (kWh) di energia prodotta.

Il campo emissions\\_rate indica l’emissione media generata dal codice al secondo in tonnellate di *CO*2 equivalenti.

Il nostro algoritmo **per singolo test** avrà un emissione di *CO*2 in grammi pari a:

3*,*374447892963441·10*T* ≈ 0*,*37445 =

−7

1000000* [^2]

= 0*,* 3744554 *g* ≈ 0*,* 37445*g* ≈ 0.625 · 10−g **2**

In conclusione possiamo osservare come sia evidente che il nostro algoritmo abbia un impatto sensibilmente minore a livello ambientale prendendo in considerazione i dati del capitolo [3.](#_page12_x85.04_y87.53)

7  **Conclusione e progetti futuri**

<a name="_page42_x85.04_y87.53"></a>Il nostro elaborato si è concentrato sullo sviluppo di un algoritmo innovativo che mira a identificare la presenza della SARS-CoV-2 attraverso l’analisi di audio di respiro e tosse acquisiti da dispositivi Android. Lo scopo principale di tale algoritmo è ridurre l’im- patto ambientale associato al largo utilizzo di tamponi NAAT, i quali richiedono risorse significative per la loro produzione, test, stoccaggio, trasporto e smaltimento. I risultati ottenuti durante lo sviluppo e la valutazione dell’algoritmo dimostrano che, nonostante

la sensibilità e l’accuratezza siano inferiori rispetto ai tamponi molecolari utilizzati oggi- giorno, il nostro approccio rappresenta comunque un’alternativa valida e sicuramente più ecosostenibile.

L’applicazione non dovrà essere sostituitiva dei tamponi molecolari bensì volta ad essere un azione di prevenzione quotidiana. Nel capitolo 3 [abbiamo](#_page12_x85.04_y87.53) osservato come la produzione di un solo test dell’acido nucleico emetta nell’atmosfera 612*,*90g di gas ad effetto serra (è una sottostima: non sono stati calcolate molte alte variabili), aumentando notevolmente l’impatto dell’inquinamento sul clima globale già destabilizzato da anni di afflizioni. Il nostro studio aveva l’intento di fornire una soluzione, alla portata di tutti, in grado di rilevare la SARS-Cov-2 in modo ecosostenibile, come misura di prevenzione ad un’altra futura pandemia causata dallo stesso virus.

I dati estratti dalle analisi che abbiamo eseguito, ci confermano che **un tampone mo- lecolare dell’acido nucleico NAAT** (secondo il modello "*cradle-to-grave*") **rilascia nell’atmosferma circa** 612*.*90*g* **di gas serra contro i 0.** 00625*g* **di GHG per ogni test del nostro algoritmo** .

Nonostante questo dato fattuale, non converrebbe sostituire il tampone NAAT al nostro algoritmo in quanto, quest’ultimo nella sua configurazione migliore, rileva i veri positivi

e i veri negativi con un accuratezza del 40*,*74% e 27*.*77%, bensì rileva i falsi negativi con una accuratezza del 100% con il fine di non espandere l’epidemia se si dovesse ripresentare di<a name="_page42_x85.04_y674.78"></a> nuovo.

**7.1 Progetti futuri**

Uno dei miglioramenti futuri con cui la nostra applicazione può essere perfezionata è di espandere i dispositivi su cui può essere utilizzata (PC, smartwatch) e rendere possibile **l’aggiunta di altri formati audio** grazie all’ausilio di algoritmi di denoising dedicati.

Sebbene sia diffcile, con miglioramenti specializzati sarà possibile rilevare il COVID-19 attraverso un audio non solo di tosse e respiro ma di **interi campioni di parlato** . Attraverso un **interfaccia** sarà possibile avere un contatto del proprio medico, le cure necessarie, contatti delle farmacie e dei centri specializzati più vicini alla persona infetta. Potrà essere implementato nell’applicazione anche il modo per tenere traccia della rete dei contatti che hanno avuto a che fare con persona infetta, avvertendoli preventivamente.

Sarà di fondamentale importanza **addestrare i modelli** aumentando il numero di audio del dataset, migliorando la sensibilità e la specificità. Infine potremmo aggiungere un altro metodo basato sulle reti neurali con l’aggiunta delle **features di VGGish** per perfezionare l’applicazione. [\[11\]](#_page44_x85.04_y678.98)

**Riferimenti bibliografici**

1. Chloë<a name="_page44_x85.04_y111.89"></a> Brown, Jagmohan Chauhan, Andreas Grammenos, Jing Han, Apinan Hastha- nasombat, Dimitris Spathis, Tong Xia, Pietro Cicuta, and Cecilia Mascolo. Exploring automatic diagnosis of COVID-19 from crowdsourced respiratory sound data. *CoRR*, abs/2006.05919, 2020.
1. Yang<a name="_page44_x85.04_y205.72"></a> Chen, Qiong Ding, Xiaoling Yang, Zhengyou Peng, Diandou Xu, and Qinzhong Feng. Application countermeasures of non-incineration technologies for medical waste treatment in china. *Waste Management & Research: The Journal for a Sustainable Circular Economy*, 31(12):1237–1244, 2013.
1. Ordine<a name="_page44_x85.04_y301.72"></a> dei Medici Chirurghi e Odontoiatri di Forlì-Cesena. Covid-19, quanto sono affidabili i tamponi rapidi per la rilevazione del virus?, Nov 2021.
1. Ketan<a name="_page44_x85.04_y353.71"></a> Doshi. Audio deep learning made simple: Sound classification, step-by-step, May 2021.
1. <https://www.energybot.com/energy-usage/telephone.html#:~:text=How%20many%20watts%20does%20a,%2C%20size%2C%20or%20other%20factors.>
1. <a name="_page44_x85.04_y406.37"></a>Ling<a name="_page44_x85.04_y459.36"></a> Ji, Yongyang Wang, Yulei Xie, Ming Xu, Yanpeng Cai, Shengnan Fu, Liang Ma, and Xin Su. Potential life-cycle environmental impacts of the covid-19 nucleic acid test. *Environmental Science & Technology*, 56(18):13398–13407, Sep 2022.
1. May<a name="_page44_x85.04_y534.02"></a> 2022.
1. Andy<a name="_page44_x85.04_y565.00"></a> Singer. Introduction to audio processing in python, May 2023.
1. Hasith<a name="_page44_x85.04_y595.99"></a> Sura. Audio classification, Jan 2020.
1. Lorenzo<a name="_page44_x85.04_y626.98"></a> Vainigli. Registrazioni vocali per la diagnosi di covid-19 con deep convolutional neural networks, 2019.
1. Video<a name="_page44_x85.04_y678.98"></a> features documentation, [https://iashin.ai/video_features/models/ vggish/.](https://iashin.ai/video_features/models/vggish/)
1. Cornellius<a name="_page44_x85.04_y731.97"></a> Yudha Wijaya. Top 3 python packages to learn audio data science project, Dec 2021.

**Matrici di confusione Logistic Regression**

**Matrice di confusione per LR con threshold![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.027.png)**

**positivo posto all’70%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.028.png)

**Matrice di confusione per LR con threshold![ref2]**

**positivo posto all’80%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.030.png)

**Matrice di confusione per LR con threshold![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.031.png)**

**positivo posto all’90%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.032.png)

**Support Vector Machine**

**Matrice di confusione per SVM con threshold![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.033.png)**

**positivo posto all’70%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.034.png)

**Matrice di confusione per SVM con threshold![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.035.png)**

**positivo posto all’80%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.036.png)

<a name="_page48_x85.04_y80.31"></a>**Matrice di confusione per SVM con threshold![ref2]**

**positivo posto all’90%** .

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.037.png)

**Boxplots**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.038.png)

Figura 17: Box Plot per la feature **cough\_mfcc\_0\_max**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.039.png)

Figura 18: Box Plot per la feature **breath\_mfcc\_d\_2\_root\_mean\_sqr**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.040.png)

Figura 19: Box Plot per la feature **breath\_mfcc\_d\_2\_std\_dev**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.041.png)

Figura 20: Box Plot per la feature **cough\_sc\_perc\_75**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.042.png)

Figura 21: Box Plot per la feature **cough\_mfcc\_8\_perc25**

![](Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.043.png)

Figura 22: Box Plot per la feature **cough\_mfcc\_0\_max**

[^1]: 

    
[^2]: 
[ref1]: Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.003.png
[ref2]: Aspose.Words.410d46e6-d804-4e10-8537-f37c2c40f9ad.029.png
