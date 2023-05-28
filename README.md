## CONTRIBUTORS
Yasmin L'Harrak: 1603496@uab.cat

Nuria Salvador: 1605592@uab.cat

Amal El Hammoudi 1608672@uab.cat

Xarxes Neuronals i Aprenentatge Profund -Grau de Data Engineering UAB, 2023


## 1. INTRODUCCIÓ

Amb els avenços tecnològics de deep learning, l'àmbit del processament d'imatges ha avançat de manera significativa, donant pas a reptes com ara afegir color a imatges a escala de grisos.

Amb tècniques especialitzades, d'aprenentatge profund, com ara capes de xarxes neuronals convolucionals (CNN), permetem que la xarxa aprengui a capturar patrons, il·luminació, color, textures de les imatges i que juntament amb l'entrenament previ amb un conjunt d'imatges a color, pugui recrear una versió de la imatge del conjunt test de manera viva i acolorida.

Dit d’una altra manera, mitjançant l'entrenament previ, la xarxa adquireix la capacitat d'aprendre a relacionar els píxels de les imatges en escala de grisos amb els seus equivalents en color, permetent tenir com a resultat una imatge amb una gran precisió de colors i tons.

Aquest tema en qüestió ha captat una atenció considerable i ha estat objecte d'ampli debat i anàlisi en diversos cercles artístics, com ara la restauració d'imatges antigues de baixa qualitat o millora de la representació visual.

No obstant això, no és l'únic àmbit en el qual s'aplica aquesta tecnologia, també s'utilitza per acolorir elements multimèdia, obrint noves possibilitats en la restauració de videos històrics, pel·lícules en blanc i negre i altres continguts audiovisuals en camps cinematogràfics, la televisió…



## 2. OBJECTIUS

L’objectiu d’aquest treball és utilitzar les tècniques d'aprenentatge profund i capes especialitzades de xarxes neuronals convolucionals (CNN) per desenvolupar un sistema capaç d'afegir color automàticament a imatges en escala de grisos de manera realista i amb qualitat. 

Addicionalment, hem decidit estendre el sistema a l’àmbit dels vídeos. Utilitzant les mateixes tècniques de capes convolucionals, recreem el color en imatges amb seqüència de manera realista i d'alta qualitat també. 




## 3. COLOURING D’IMATGES

En aquest apartat explicarem amb més detall el colouring d’imatges, amb les tècniques de aprenentatge profund. 


## 3.1 CONTEXT

Primerament, explicarem els fitxers que hem utilitzat i la seva finalitat. Hem optat per utilitzar com a base el repositori "starting_point" de GitHub, ja que aquest contenia els fitxers necessaris per començar a plantejar el sistema de "colouring".

Com el projecte "starting_point" estava estructurat en 3 nivells, vam començar pel més senzill i vam anar progressant a mesura que avançàvem.

En primer lloc, ens vam centrar en el directori "alpha", el qual contenia una única imatge que s'utilitzava tant per a l'entrenament com per a les proves de la xarxa neuronal convolucional.

Un cop vam verificar que tot funcionava correctament i que la imatge resultava ser igual que l'original, vam passar a treballar amb el directori "beta", i posteriorment amb el "full-version". Aquest últim era excessivament gran i ocupava més memòria del que teníem disponible, per la qual cosa vam optar per continuar amb el "beta", que treballava amb més imatges en comparació amb l'alpha i també tenia més capes per al procés d'aprenentatge del sistema.

Per a realitzar proves més exhaustives, vam decidir utilitzar altres conjunts de dades que havíem creat nosaltres mateixos. Com a conjunt de dades, hem utilitzat dos directoris: "paisaje_train" per a l'entrenament i "paisajes2" per a les proves. Tots dos directoris contenien paisatges amb prats verds, però amb diferents tonalitats de verd i intensitats, amb l'objectiu de permetre a la xarxa neuronal entrenar-se i oferir-nos representacions de colors més precises.

Hem pres la decisió de no abordar aquesta tasca amb un conjunt de imatges d’entrenament extens, per la principal raó que la nostra xarxa no té una gran dimensionalitat i a més, perquè ens volem enfocar en la qualitat de l’entrenament de la xarxa neuronal convolucional (CNN). 

A més de tot això, quan es treballa amb un conjunt més petit d'imatges, podem garantir amb certesa que la xarxa apren fins al detall de les imatges entrenades i processa amb més precisió, sense caure en el fenòmen del sobreajustament (overfitting). 




## 3.2 DESENVOLUPAMENT 

## 3.3 RESULTATS







