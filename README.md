## CONTRIBUTORS
Yasmin L'Harrak: 1603496@uab.cat

Nuria Salvador: 1605592@uab.cat

Amal El Hammoudi 1608672@uab.cat

Xarxes Neuronals i Aprenentatge Profund -Grau de Data Engineering UAB, 2023

## INTRODUCCIÓ

La coloració d'imatges (image colorization en anglès) consisteix a donar color a fotografies en blanc i negre. Aquest procés pot semblar senzill, ja que per nosaltres, els humans, és relativament comú veure els colors reals que tenen els diferents elements, com el mar o la gespa, que apareixen en una imatge en blanc i negre.

Aquest tema en qüestió ha captat una atenció considerable i ha estat objecte d'ampli debat i anàlisi en diversos cercles artístics, com ara la restauració d'imatges antigues de baixa qualitat o millora de la representació visual. No obstant això, no és l'únic àmbit en el qual s'aplica aquesta tecnologia, també s'utilitza per acolorir elements multimèdia, obrint noves possibilitats en la restauració de vídeos històrics, pel·lícules en blanc i negre i altres continguts audiovisuals en camps cinematogràfics, la televisió…

Amb els avenços tecnològics del deep learning, l'àmbit del processament d'imatges ha experimentat avenços significatius, donant lloc a reptes com afegir color a imatges en escala de grisos. Amb tècniques especialitzades de l'aprenentatge profund, com les capes de les xarxes neuronals convolucionals (CNN), la xarxa és capaç d'aprendre a capturar patrons, il·luminació, color i textures de les imatges. Amb un entrenament previ fent servir un conjunt d'imatges a color, la xarxa pot recrear una versió vívida i acolorida de les imatges del conjunt de proves.

Dit d'una altra manera, mitjançant l'entrenament previ, la xarxa adquireix la capacitat d'aprendre a relacionar els píxels de les imatges en escala de grisos amb els seus equivalents en color, permetent tenir com a resultat una imatge amb una gran precisió de colors i tons.

En aquest informe, es presenta un projecte que aborda aquest tema. En primer lloc, s'estableixen els objectius proposats. Després, s'explica la base del projecte, el starting point, el qual es divideix en dues versions, alpha i beta version, explicant les característiques i funcionalitats de cadascuna. Seguidament, s'aborda el model fet servir amb l'arquitectura de la xarxa neuronal. Es detallen les capes, els paràmetres i el desenvolupament, incloent-hi els canvis realitzats en el codi, les proves realitzades i les millores al llarg del procés.

Un cop finalitzat el desenvolupament, es presenten els resultats finals obtinguts, i seguidament, es tracten les millores podrien implementar per obtenir millors resultats i es presenten les conclusions del projecte, per concloure aquest projecte.


## OBJECTIUS

L'objectiu principal d'aquest projecte és utilitzar les tècniques d'aprenentatge profund i capes especialitzades de xarxes neuronals convolucionals (CNN) per desenvolupar un sistema eficient i precís que sigui capaç d'afegir color automàticament a imatges en escala de grisos.

Una de les principals consideracions en aquest projecte és assegurar que el sistema pugui afegir color de manera realista i amb qualitat. Per aconseguir això, s'usen capes convolucionals especialitzades que s'han entrenat amb un conjunt de dades d'imatges en color per aprendre els patrons i les relacions entre els píxels en les imatges.

Addicionalment, el projecte s'ha ampliat per incloure acolorir vídeos en format GIF. Això implica l'aplicació de les mateixes tècniques de capes convolucionals per recrear el color en cada imatge individual de la seqüència de vídeo. Amb aquest enfocament, s'aspira a proporcionar una solució completa per a la restauració de vídeos en blanc i negre.






## DATASETS
L’elecció de conjunts de dades és important en l’entrenament de models CNN per què influeix en la capacitat d'aprendre del model i en la generalització dels colors de les imatges resultants. Alguns aspectes que s’han tingut en compte són la mida i diversitat del dataset. Aquests aspectes són importants  ja que un conjunt de dades amb molta variabilitat de dades proporciona al model molts exemples per aprendre i generalitzar correctament els colors. Com més variat sigui el conjunt, s’obtindran millors resultats i més precisos.

El primer dataset que es va utilitzar va ser els conjunts ‘Pradera-train’ i ‘Pradera-test’ que tenen imatges de prats verds. Aquest conjunt és un recull de diverses fotografies de prats, que en general, són bastant similars. Al principi és interessant provar el model amb un dataset homogeni ja que d’aquesta manera es pot fer una avaluació inicial, ja que al treballar amb imatges semblants, és més fàcil la comparació de resultats i l’estudi de patrons que realitza el model, això pot ser útil per comprendre el comportament del model.
Pradera-train té 54 imatges i Pradera-test té 10 imatges.

El segon dataset que es va utilitzar van ser els conjunts ‘Rural-train’ i ‘Rural-test’ que contenen imatges de l’ambient rural. Aquestes imatges tenen una major variabilitat en comparació amb el dataset anterior ja que cadascuna té diferents elements rurals. En algunes es poden veure animals, altres tractors, rius, etc. Aquest dataset segueix la tendència de l’anterior però amb més variabilitat, això és interessant a l’hora d’entrenar una xarxa neuronal per acolorir imatges ja que les diferencies entre les imatges aporten consistència al model aprenent patrons específics a la vegada que reforça la capacitat de generalitzar i produir resultats més robustos.
‘Rural-train’ compta amb 36 imatges i ‘Rural-test’ compta amb 10 imatges.

Per tal de veure com reacciona el model en un cas completament diferent als anteriors, es va seleccionar un dataset de plàtans, on predominen els colors grocs i on no hi ha cap paisatge al fons. Amb aquest dataset es volia comprovar la capacitat de generalització del model. Aquest dataset compta amb un total de 43 imatges.







