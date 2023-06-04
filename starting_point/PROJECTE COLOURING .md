<a name="br1"></a> 

UNIVERSITAT AUTÒNOMA DE BARCELONA

PROJECTE

COLOURING

Xarxes neuronals i aprenentatge profund

Yasmin L’Harrak(1603496), Nuria Salvador(1605592),

Amal El Hammoudi (1608672)

31 de maig del 2023



<a name="br2"></a> 

ÍNDEX

**INTRODUCCIÓ........................................................................................................................2**

**OBJECTIUS.............................................................................................................................3**

**DATASETS.............................................................................................................................. 4**

**STARTING POINT................................................................................................................... 5**

ARQUITECTURA DEL MODEL......................................................................................... 5

ALPHA VERSION.............................................................................................................. 6

BETA VERSION.................................................................................................................6

**DESENVOLUPAMENT............................................................................................................8**

**RESULTATS.......................................................................................................................... 10**

Dataset Pradera............................................................................................................... 10

Gràfica de pèrdues..................................................................................................... 11

Execució..................................................................................................................... 11

Dataset Rural................................................................................................................... 12

Gràfica de pèrdues.....................................................................................................13

Execució.....................................................................................................................13

Dataset Banana................................................................................................................14

Gràfica de pèrdues.....................................................................................................15

Execució.....................................................................................................................15

**GIF VERSION........................................................................................................................ 16**

Gràfica de pèrdues.....................................................................................................18

Execució.....................................................................................................................18

**CONCLUSIONS.....................................................................................................................19**

Datasets..................................................................................................................... 19

Imatges.......................................................................................................................20

Vídeo..........................................................................................................................20

Millores.......................................................................................................................20

**BIBLIOGRAFIA..................................................................................................................... 22**

1



<a name="br3"></a> 

INTRODUCCIÓ

La coloració d’imatges (image colorization en anglès) consisteix en donar color a fotografies

en blanc i negre. Aquest procès pot semblar senzill, ja que per nosaltres, els humans, és

relativament comú veure els colors reals que tenen els diferents elements, com el mar o la

gespa, que apareixen en una imatge en blanc i negre.

Aquest tema en qüestió ha captat una atenció considerable i ha estat objecte d'ampli debat i

anàlisi en diversos cercles artístics, com ara la restauració d'imatges antigues de baixa

qualitat o millora de la representació visual. No obstant això, no és l'únic àmbit en el qual

s'aplica aquesta tecnologia, també s'utilitza per acolorir elements multimèdia, obrint noves

possibilitats en la restauració de videos històrics, pel·lícules en blanc i negre i altres

continguts audiovisuals en camps cinematogràfics, la televisió…

Amb els avenços tecnològics del deep learning, l'àmbit del processament d'imatges ha

experimentat avenços significatius, donant lloc a reptes com afegir color a imatges en

escala de grisos. Amb tècniques especialitzades de l'aprenentatge profund, com les capes

de les xarxes neuronals convolucionals (CNN), la xarxa és capaç d'aprendre a capturar

patrons, il·luminació, color i textures de les imatges. Amb un entrenament previ utilitzant un

conjunt d'imatges a color, la xarxa pot recrear una versió vívida i acolorida de les imatges

del conjunt de proves.

Dit d’una altra manera, mitjançant l'entrenament previ, la xarxa adquireix la capacitat

d'aprendre a relacionar els píxels de les imatges en escala de grisos amb els seus

equivalents en color, permetent tenir com a resultat una imatge amb una gran precisió de

colors i tons.

En aquest informe, es presenta un projecte que aborda aquest tema. En primer lloc,

s’estableixen els objectius proposats. Després, s’explica la base del projecte, el starting

point, el qual es divideix en dues versions, alpha i beta version, explicant les

característiques i funcionalitats de cadascuna. Seguidament, s’aborda el model utilitzat amb

l’arquitectura de la xarxa neuronal. Es detallen les capes, els paràmetress i el

desenvolupament, incloent els canvis realitzats en el codi, les proves realitzades i les

millores al llarg del procés.

Un cop finalitzat el desenvolupament, es presenten els resultats finals obtinguts, i

seguidament, es tracten les millores podrien implementar per obtenir millors resultats i es

presenten les conclusions del projecte, per concloure aquest projecte.

2



<a name="br4"></a> 

OBJECTIUS

L'objectiu principal d'aquest projecte és utilitzar les tècniques d'aprenentatge profund i capes

especialitzades de xarxes neuronals convolucionals (CNN) per desenvolupar un sistema

eficient i precís que sigui capaç d'afegir color automàticament a imatges en escala de grisos.

Una de les principals consideracions en aquest projecte és assegurar que el sistema pugui

afegir color de manera realista i amb qualitat. Per aconseguir això, s'usen capes

convolucionals especialitzades que s'han entrenat amb un conjunt de dades d'imatges en

color per aprendre els patrons i les relacions entre els píxels en les imatges.

Addicionalment, el projecte s'ha ampliat per incloure acolorir vídeos en format GIF. Això

implica l'aplicació de les mateixes tècniques de capes convolucionals per recrear el color en

cada imatge individual de la seqüència de vídeo. Amb aquest enfocament, s'aspira a

proporcionar una solució completa per a la restauració de vídeos en blanc i negre.

3



<a name="br5"></a> 

DATASETS

L’elecció de conjunts de dades és important en l’entrenament de models CNN per que

influeix en la capacitat d'aprendre del model i en la generalització dels colors de les imatges

resultants. Alguns aspectes que s’han tingut en compte són la mida i diversitat del dataset.

Aquests aspectes són importants ja que un conjunt de dades amb molta variabilitat de

dades proporciona al model molts exemples per aprendre i generalitzar correctament els

colors. Com més variat sigui el conjunt, s’obtindran millors resultats i més precisos.

El primer dataset que es va utilitzar va ser els conjunts ‘Pradera-train’ i ‘Pradera-test’ que

tenen imatges de prats verds. Aquest conjunt és un recull de diverses fotografies de prats,

que en general, son bastant similars. Al principi és interesant probar el model amb un

dataset homogeni ja que d’aquesta manera es pot fer una avaluació inicial, ja que al

treballar amb imatges semblants, és més facil la comparació de resultats i l’estudi de

patrons que realitza el model, això pot ser util per comprendre el comportament del model.

Pradera-train té 54 imatges i Pradera-test té 10 imatges.

El segon dataset que es va utilitzar van ser els conjunts ‘Rural-train’ i ‘Rural-test’ que

contenen imatges de l’ambient rural. Aquestes imatges tenen una major variabilitat en

comparació amb el dataset anterior ja que cadascuna té diferents elements rurals. En

algunes es poden veure animals, altres tractors, rius, etc. Aquest dataset segueix la

tendencia de l’anterior però amb més variabilitat, això és interessant a l’hora d’entrenar una

xarxa neuronal per colorejar imatges ja que les diferencies entre les imatges aportan

consistencia al model aprenent patrons específics a la vegada que reforça la capacitat de

generalitzar i produir resultats més robustos.

‘Rural-train’ compta amb 36 imatges i ‘Rural-test’ compta amb 10 imatges.

Per tal de veure com reacciona el model en un cas completament diferent als anteriors, es

va sel·leccionar un dataset de plàtans, on predominen els colors grocs i on no hi ha cap

paisatge al fons. Amb aquest dataset es volia comprobar la capacitat de generalització del

model. Aquest dataset compta amb un total de 43 imatges.

Figura 1: Imatge Dataset Pradera

Figura 2: Imatge Dataset Rural

Figura 3: Imatge Dataset Banana

4



<a name="br6"></a> 

STARTING POINT

Per començar, es va utilitzar el repositori “starting\_point” com a base per al projecte. Aquest

repositori proporciona tres versions diferents, però només es van utilitzar les dues primeres

(alpha i beta). La tercera versió, que era un model molt pesat, no era viable a causa de les

limitacions de memòria disponibles.

ARQUITECTURA DEL MODEL

Per afrontar aquesta qüestió, s’ha decidit utilitzar una Xarxa Neuronal Convolutional

(Convolutional Neural Network, CNN). Es basa en l’arquitectura d’un autoencoder.

Un autoencoder és una xarxa neuronal que consta de dues parts: un encoder i un decoder.

L’enconder és la primera part, es compon de diverses capes convolucionals i s’encarrega

d’extreure les característiques més importants de les imatges en blanc i negre. Aquest

procès permet que el model aprengui a capturar els patrons, textures, etc per a la posterior

coloració.

El decoder és la segona part, s’encarrega de reconstruir l’entrada original a partir de la

representació generada per l’encoder. Aquesta arquitectura seqüencial permet aprendre

patrons i textures de les imatges per aconseguir una coloració precisa i realista.

Figura 4: Arquitectura Autoencoder

5



<a name="br7"></a> 

ALPHA VERSION

La versió alpha treballa sobre una única imatge, la qual, passa de RGB a LAB on la

component 'L' (Lluminositat) serà la 'X' i les components 'A' i 'B' (canals de colors), es

normalitzen dividint-se entre 128 i seran la variable 'Y'.

S'utilitza una xarxa neuronal seqüencial, ja que el problema no és massa complex. Aquest

model té capes convolucionals 'Conv2D' amb activació ReLU, ja que amb ReLU s’evita el

problema de desaparició del gradient i aporta no linealitat a la xarxa per tal d’aprendre altres

patrons i característiques.

A les capes convolucionals es troba padding 'same' per no modificar la mida de la imatge de

entrada, es a dir, que la mida de l’entrada i la de la sortida siguin la mateixa, i strides=2,

reduint així la sortida de la capa convolucional a la meitat de les dimensions que la capa

d'entrada.

També s'usen capes d'upsampling per augmentar les dimensions de la imatge per poder

reconstruir caracteristiques que s’han reduit degut a l’us de l’stride=2 i una capa

convolucional final amb activació per tangent hiperbòlica. S’usa l’activació per tanh perquè

la sortida es normalitza entre -1 i 1 i aixó es favorable per representar els colors a l’espai

LAB.

Per optimitzar el model, s’utilitza l’optimitzador rmsprop amb una leaning rate de 0.001 i la

funció de pèrdua d’error mitjà quadrat (MSE).

Es fa un fit del model passant la 'X' i la 'Y' que s'han creat anteriorment. Finalment, s'avalua

el model i es fa la predicció multiplicant la sortida per 128 per tal de retornar la imatge

predita amb els colors adients.

BETA VERSION

La versió beta segueix el mateix procediment que l’alpha version, encara que aquest

treballa sobre un train d’imatges a color, i les converteix de l’escala RGB a LAB, on la

component L serà la X i les components A i B (canals de colors), es normalitzen i es

divideixen entre 128, sent la variable Y.

En aquest cas, es construeix un model seqüencial, i es comença afegint una capa d’entrada

(InputLayer) amb una dimensió de 256x256. Aquesta dimensió és la mateixa que “L”, que

representa la imatge en escala de grisos.

A continuació, s’afegeixen diversos blocs convolucionals que formen la part de l’encoder del

model. El primer bloc consisteix en una capa convolucional amb 63 filtres de mida 3x3,

activada per la funció d’activació ReLu (Rectified Linear Unit) per introduir no linealitats, i

s’aplica un padding “same” als marges, per mantenir la mida original de la imatge.

6



<a name="br8"></a> 

Seguidament, s’augmenta el nombre de filtres en els blocs convolucionals posteriors.

S’utilitzen capes amb 128, 256 i 512 filtres, mantenint la mateixa mida de filtre (3x3) i la

funció d’activació ReLU. Algunes d’aquestes capes estan seguides de capes de strides, per

reduir la dimensionalitat de la imatge.

Després dels blocs convolucionals, s’afegeixen les capes de reconstrucció (decoder), per

generar la imatge en color. Aquestes capes inclouen una capa d’UpSampling2D, per

augmentar la resolució de la imatge, per compensar els strides aplicats anteriorment. També

inclou capes convolucionals amb un nombre reduïts de filtres (64 i 32) i activació ReLU.

Finalment, s’afegeix una capa convolucional amb 2 filtres i activació tangent hiperbòlica

(tanh) per generar la imatge en color. La capa de sortida té una dimensió de 256z256x2, on

els dos canals representen els valors de color, els canals A i B.

Per optimitzar el model, s’utilitza l’optimitzador Adagrad amb una leaning rate de 0.001 i la

funció de pèrdua d’error mitjà quadrat (MSE).

Per comprovar el procès de coloració, el primer que es fa és llegir les imatges del test i

s’ajusta la mida de les imatges a 256x256. Després de la redimensió i comprovació de que

les imatges tinguin 3 canals, es converteixen a l’espai LAB utilitzant la funció rgb2lab.

A continuació, s’aplica el model entrenat a les imatges, utilitzant la funció predict. Aquesta

funció el que fa és retornar les prediccions, que són les imatges en color generades pel

model. Seguidament, es crea una matriu buida de mida 256x256x3 per representar la

imatge final en color. El que es fa és assignar els valors de la capa L de la imatge original

(entrada) a la capa L de la nova imatge i, després s’assignen les prediccions del model a les

capes A i B.

Finalment, s’aplica la conversió inversa de l’espai de color LAB a RGB, utilitzant la funció

lab2rgb.

7



<a name="br9"></a> 

DESENVOLUPAMENT

Un dels primers canvis que es van realitzar va ser passar el model a la GPU de la màquina

virtual per tal de poder executar a major velocitat.

Un segon canvi va ser aplicar un resize a totes les imatges per a que totes tinguessin una

mida de (256,256) i així, no hi hagués cap conflicte a l’hora d’operar amb aquestes.

També es mira que totes les fotografies tinguin tres dimensions, en el cas de no ser així, és

a dir, que siguin en blanc i negre, s’afegeixen dues dimensions més.

Seguidament, a la part del codi del Data Augmentation, per tal d’afegir variabilitat i més

característiques a les imatges, hi havia diverses opcions de canvis que s’apliquen a algunes

imatges, dues d’aquestes opcions eren flips, aquests es van descartar ja que no interessa

que s’alteri la naturalesa de la composició de les imatges.

Les modificacions d’imatges que s’han mantingut són el shear\_range que aplica una

deformació a la imatge amb un angle màxim de 0.2 radians, el zoom\_range que apropa o

allunya la imatge com a màxim en un 0.2 i finalment, el rotation\_range que realitza una

rotació aleatoria com a màxim de 20 graus. Aquesta última modificació afegeix variabilitat

però no arriba a distorsionar la naturalesa de la composició de la imatge tant com els flips.

El Data Augmentations és important en aquest projecte degut a que els datasets que s’usen

no són massa grans, per tant, afegir característiques modificant les imatges, fa que

s’enriqueixi l’entrenament del model.

Una altra modificació del codi ha sigut aplicar més capes convolucionals al model. Aquest

canvi es va aplicar per obtenir una major capacitat d’aprenentatge de característiques ja que

cada capa extra pot aprendre característiques més complexes i abstractes que les capes

anteriors.

Al afegir més capes convolucionals també augmentem la no linealitat de la xarxa, el que

permet aprendre relacions i patrons no lineals en les dades. Al augmentar la profunditat de

la xarxa, s’augmenta la capacitat per processar relacions no lineals més complexes entre

les dades.

No sempre es recomenable aquest canvi ja que si s’afegeixen moltes, la xarxa es pot tendir

a l’overfitting i a més pot causar problemes de memòria, per això, per aquest model només

s’han afegit tres capes convolucionals extres.

Després es van canviar l’optimitzador i el learning rate. Experimentalment, el millor

optimitzador ha sigut Adagrad amb un learning rate de 0.001. Adagrad és un bon

optimitzador ja que quan els gradients varien de manera considerable entre dimensions,

Adagrad treballa bé.

8



<a name="br10"></a> 

Després es van canviar el batch\_size, les epochs i els steps\_per\_epoch. El batch\_size és el

número d’elements del train que s’utilitzen en una iteració abans d’actualitzar els pesos del

model. Per tal d’utilitzar un batch\_size optim, s’ha d’observar el numero d’elements que hi

ha al train, com els datasets que s’utilitzen en aquest projecte són petits, el batch size adient

es troba al voltant de 15.

Per les epochs, que és la quantitat de cops que el model passa per tot el train, també s’ha

tingut en compte la mida del train, com els trains acostumen a no ser massa grans, 350

epochs són suficients per a que el model eviti l’overfitting.

Els steps per epoch són el número de pasos que es faràn en cada època, entent passos

com la realització d’un càlcul per actualitzar els pesos del model. En aquest cas els steps

que han mostrat millors resultats han estat al voltant dels 50.

Finalment, per tal de comprovar si el model fa overfitting de manera gràfica, s’ha guardat el

fit\_generator del model en la variable ‘history’ afegint per paràmetre el validation\_data que

és la part del conjunt X que s’usa com a test. Del history extraiem la ‘loss’, que representa la

loss del train, i la ‘val\_loss’ que representa la loss del conjunt de validació. Per poder

visualitzar aquests resultats i comprovar si es fa overfitting, es fan plots d’aquests resultats i

com VisualStudio no te interfície gràfica, es guarda el resultat dels plots com a arxiu png.

9



<a name="br11"></a> 

RESULTATS

En aquest apartat, es presenten els resultats obtinguts durant tot el desenvolupament.

Dataset Pradera

En aquest apartat, es mostren les imatges originals i les seves prediccions corresponents

generades pel model, per poder fer la comparativa de la recreació dels colors de les imatges

en escala de grisos.

S’ha utilitzat 350 èpoques d’entrenament, 50 passos per cada època i un batch size de 15.

Aquests paràmetres són els que han permès obtenir els millors resultats.

*Figura 5: Imatge Real*

*Figura 6: Imatge predita*

*Figura 7: Imatge Real*

*Figura 8: Imatge predita*

10



<a name="br12"></a> 

Gràﬁca de pèrdues

Per tal de visualitzar el procés d’entrenament tant en la fase de train com en la fase de test, s’ha

generat un gràfic de les pèrdues (losses), corresponents a ambdues fases.

*Figura 9: Gràfica loss del Train i Validació Pradera*

Analitzant la gràfica, es pot observar que les tendències de les pèrdues tant en el train com en el test

són similars. Aquesta similitud indica que el model no ha sobre après i que ha generalitzat bastant

adequadament els patrons i les característiques.

Si bé és cert que la fase de validació presenta una menor estabilitat i mostra alguns pics, al final

acaba amb un menor valor de pèrdua.

Això pot indicar que el model he pogut aprendre i generalitzar de manera correcta.

Execució

nom fitxer: Beta\_version.py

Dataset:

\-

\-

train: starting\_point/Beta-version/Pradera-train/

test: starting\_point/Beta-version/Pradera-test/

Epochs: 350

Steps per epochs:50

Batch size: 15

11



<a name="br13"></a> 

Dataset Rural

En aquest apartat, es mostren les imatges originals i les seves prediccions corresponents

generades pel model, per poder fer la comparativa de la recreació dels colors de les imatges

en escala de grisos.

S’ha utilitzat 350 èpoques d’entrenament, 50 passos per cada època i un batch size de 15.

Aquests paràmetres són els que han permès obtenir els millors resultats.

*Figura 10: Imatge real*

*Figura 11: Imatge predita*

*Figura 12: Imatge real*

*Figura 13: Imatge predita*

*Figura 14: Imatge real*

*Figura 15: Imatge predita*

12



<a name="br14"></a> 

Gràﬁca de pèrdues

Per tal de visualitzar el procés d’entrenament tant en la fase de train com en la fase de test, s’ha

generat un gràfic de les pèrdues (losses), corresponents a ambdues fases.

*Figura 9: Gràfica loss del Train i Validació Rural*

Analitzant aquesta gràfica es pot observar que la pèrdua de train presenta una tendència

més estable mentre que hi ha diverses irregularitats i pics en la pèrdua de validació.

Aquestes irregularitats en la pèrdua de validació poden ser causades per diversos motius,

com per exemple la variabilitat en les condicions de captura (il·luminació, angles, resolució)

o per la manca de diversitat en les dades d’entrenament.

To t i que es puguin observar irregularitats, el fet que la pèrdua vagi disminuint demostra que

el model està aprenent de manera bastant efectiva

Execució

nom fitxer: Beta\_version.py

Dataset:

\-

\-

train: starting\_point/Beta-version/Rural-train/

test: starting\_point/Beta-version/Rural-test/

Epochs: 350

Steps per epochs:50

Batch size: 15

13



<a name="br15"></a> 

Dataset Banana

En aquest apartat, es mostren les imatges originals i les seves prediccions corresponents

generades pel model, per poder fer la comparativa de la recreació dels colors de les imatges

en escala de grisos.

S’ha utilitzat 350 èpoques d’entrenament, 50 passos per cada època i un batch size de 15.

Aquests paràmetres són els que han permès obtenir els millors resultats.

14



<a name="br16"></a> 

Gràﬁca de pèrdues

Execució

nom fitxer: Beta\_version.py

Dataset:

\-

\-

train: starting\_point/Beta-version/Banana/train/

test: starting\_point/Beta-version/Banana/test/

Epochs: 350

Steps per epochs:50

Batch size: 15

15



<a name="br17"></a> 

GIF VERSION

Addicionalment, d'acolorir les imatges, com bé posa en l'apartat dels objectius, s'amplia el

projecte per incloure acolorir vídeos en format GIF que estan en blanc i negre.

La idea ha estat utilitzar les mateixes tècniques d'aprenentatge profund que s'ha utilitzat, ja

que les xarxes neuronals convolucionals han mostrat resultats bastant satisfactoris. De tal

manera que s'ha seguit la mateixa idea i procés, per recrear el color en el següent GIF:

*Figura : GIF onades blanc i negre*

Si bé és cert, no es va tractar el GIF com a vídeo, ja que es va tractar com una seqüència

de frames individuals, i cada frame es va considerar com una imatge independent.

*Figura : frame del GIF*

Primerament, es va entrenar un model seqüencial utilitzant un conjunt de dades

d'entrenament específic que consistia en més de 100 imatges temàtiques del directori

"beach".

*Figura : imatges dataset*

*beach*

16



<a name="br18"></a> 

Un cop el model seqüencial va ser entrenat amb les imatges del train del directori "beach",

es passa a la fase test, en la que s’utilitza els frames del GIF en format LAB. Aquesta

representació LAB, permet separar la informació de la imatge en lluminositat (L) i dos canals

de colors (A i B) .

Aquesta separació va bé per tal de poder fer la predicció, ja que per cada frame individual,

es passa el canal lluminositat (L) com a entrada del model predictiu i genera un output

corresponent al canals de color (A, B).

Acabat el procés de predicció per cada frame individual, es reconstrueixen les imatges

finals. Per fer-ho, primerament, s’uneixen els tres canals (L, A, B), els del output i el de

l’entrada del predict, creant la imatge resultat en format LAB. Per acabar de recrear la

imatge resultant la passem al model de representació RGB.

*Figura : frame del GIF en RGB*

Aquest procés es repeteix per a tots els frames del GIF, fins a obtenir la seqüència completa

de frames en color. Finalment, es reconstrueix el GIF acolorit unint tots els frames

processats.

Es va fent el mateix per tots els frames, fins a tenir-los tots, un cop acabat aquest procés,

reconstruim el GIF acolorit unint els frames.

*Figura : GIF resultant en RGB*

17



<a name="br19"></a> 

Gràﬁca de pèrdues

Per tal de visualitzar el procés d’entrenament tant en la fase de train com en la fase de test,

s’ha generat un gràfic de les pèrdues (losses), corresponents a ambdues fases.

*Figura : gràfica LOSS train test del GIF*

Es pot observar a la gràfica de Loss del train i el validation que ambdues tenen la mateixa

tendència, però que el test experimenta dificultats en alguns punts, això es pot veure pels

pics que es formen en aquests. Aquest fenomen es pot donar perquè el model estigui fent

overfitting en aquelles etapes o perquè el conjunt de test sigui massa petit, la qual cosa no

suposaria un problema del model.

El més probable és que si s'executés amb un conjunt més gran d'imatges, els pics

acabarien desapareixent, ja que tindria més característiques que podria aprendre i se

solucionaria la falta de representació de dades en les etapes que provoquen els pics.

Execució

**nom fitxer**: colorization\_video.py

**Dataset**:

\-

\-

train: starting\_point/Beta-version/beach/train/

test: són els frames del video

**Epochs**: 150

**Steps per epochs**:50

**batch size**: 15

18



<a name="br20"></a> 

CONCLUSIONS

L'objectiu principal d'aquest projecte és utilitzar les tècniques d'aprenentatge profund i capes

especialitzades de xarxes neuronals convolucionals (CNN) per desenvolupar un sistema

eficient i precís que sigui capaç d'afegir color automàticament a imatges en escala de grisos.

Després de realitzar un extens seguit de proves en la coloració d'imatges i vídeos, hem

arribat a la conclusió que les capes convolucionals són una eina essencial per transformar i

colorejar les imatges amb una gran precisió i qualitat. Fent ús de les capes convolucionals

(CNN), hem aconseguit capturar i aprendre característiques, detalls, textures, a més

d'estructures, colors, voreres, patrons i relacions complexes entre els píxels de les imatges,

mitjançant el procés d'entrenament amb un conjunt de datasets.

Una de les raons per les quals hem usat les capes convolucionals ha estat per la seva

capacitat per processar les imatges de manera eficient, la qual cosa fa que l'execució no

tardi tant en comparació a possibles altres models.

To t i això, una execució ens podia tardar perfectament 3 hores.

En el cas dels vídeos, vam decidir fer servir les mateixes tècniques de xarxes neuronals,

perquè com estem tractant el GIF com un conjunt d'imatges, aquestes estan connectades

entre elles, per tant, una de les principals característiques de les CNN és que mantenen una

coherència, continuïtat i relació entre les imatges que utilitza per entrenar i aprendre.

Datasets

En relació als datasets emprats, hem arribat a la conclusió que és important tenir en compte

diferents conjunts de dades, per tal de no caure en el fenòmen de l’overfitting i que el codi

quedi més generalizable, ja que cada datasets té les seves peculiaritats i això fa que s’hagi

de reajustar el codi en cada cas.

Al final, per tal de veure si el model s’enriqueixia de noves característiques es va decidir

utilitzar un nou dataset “maduixes” semblant al de plàtans, però en aquest cas, les

execucions no van donar resultats satisfactoris, ja que no captava bé la intensitat del

vermell. Aquest dataset està compost per un conjunt de imatges de maduixes amb diferents

tonalitats de vermell i verd per la fulla.

Com que els datasets comentats abans en l’apartat de datasets, no tenen un gran volum de

dades, és va buscar un de balenes amb 252 imatges de test i 1104 imatges de train. Utilizar

datasets voluminosos ajuda al rendiment del model i millora la capacitat de reconèixer

patrons per realitzar prediccions més precises.

Malgrat això, la disponibilitat de memòria del tensor, és bastant limitada, de manera, que no

soporta una quantitat de dades tan gran, fent així que quedi revocat.

19



<a name="br21"></a> 

Imatges

Després de fer moltes proves i provar molts datasets, hem arribat a la conclusió que

l’augment d’èpoques en el procés d’entrenament té un impacte bastant positiu en els

resultats, ja que el model té l’oportunitat d’aprendre més característiques, patrons i generar

prediccions més precises i acurades en la recreació del color.

No obstant això, també hem observat que un excés d'èpoques porta al desaprenentatge.

Això és degut a que el model es sobreajusta massa a detalls que eprd l’enfoc general i per

tant retorna la imatge en escala de grisos.

Vídeo

Després de veure el resultat final i comparar-lo amb la gràfica Loss de train i validation, hem

pogut veure que al resultat que retorna hi ha bastants pics, la qual cosa vol dir que o hi ha

outliers o que hi ha presència del fenomen overfitting.

Aquest fenomen es pot donar perquè el model estigui fent overfitting en aquelles etapes o

perquè el conjunt de test sigui massa petit, la qual cosa no suposaria un problema del

model.

Millores

Una possible millora en el context dels vídeos seria l'ús del model LSTM (Long Short-Term

Memory), ja que aquest és un model recursiu i pot arribar a ser bastant òptim, donat que

cada frame està connectat amb el frame anterior i posterior, així doncs aquest model pot

capturar millor les relacions seqüencials i temporals presents en el vídeo i recrear el color de

manera més gradual i real.

Un altre millora que ens hagués agradat realitzar és utilitzar el model amb datasets

notablement voluminós, ja que en algunes gràfiques de les funcions loss trobem pics que es

podrien solucionar si el model disposés de més característiques per aprendre. Creiem que

fent-ho, el model donaria resultats amb més qualitat.

20



<a name="br22"></a> 

Problemes

Per últim, volem afegir que el principal problema que hem tingut ha estat el tema de la

memòria, ja que si posàvem un batch size una mica més gran de l’habitual o posàvem més

capes a la xarxa neuronal, el tensor es quedava sense memòria disponible.

*Figura : imatge del error de memòria*

21



<a name="br23"></a> 

BIBLIOGRAFIA

images.cv | Image datasets for computer vision and machine learning. (s. f.).

<https://images.cv/>

Happywhale - Whale and Dolphin Identification | Kaggle. (s. f.).

<https://www.kaggle.com/competitions/happy-whale-and-dolphin/data>

Build software better, together. (s. f.). GitHub.

<https://github.com/topics/video-colorization>

Nayak, S., & Nayak, S. (2023). Image Colorization Using CNN With OpenCV. LearnOpenCV

– Learn OpenCV, PyTorch, Keras, Tensorflow with examples and tutorials.

[https://learnopencv.com/convolutional-neural-network-based-image-colorization-using-openc](https://learnopencv.com/convolutional-neural-network-based-image-colorization-using-opencv/)

[v/](https://learnopencv.com/convolutional-neural-network-based-image-colorization-using-opencv/)

KunalVaidya. (2020, 9 noviembre).

Image-Colorization-Using-Deep-Learning/ChromaGAN.ipynb at main

KunalVaidya99/Image-Colorization-Using-Deep-Learning. GitHub.

[https://github.com/KunalVaidya99/Image-Colorization-Using-Deep-Learning/blob/main/Chro](https://github.com/KunalVaidya99/Image-Colorization-Using-Deep-Learning/blob/main/ChromaGAN.ipynb)

[maGAN.ipynb](https://github.com/KunalVaidya99/Image-Colorization-Using-Deep-Learning/blob/main/ChromaGAN.ipynb)

Mandal, M. (2023). Introduction to Convolutional Neural Networks (CNN). Analytics Vidhya.

<https://www.analyticsvidhya.com/blog/2021/05/convolutional-neural-networks-cnn/>

Na, & Na. (2020). Convolutional Neural Networks: La Teoría explicada en Español | Aprende

Machine Learning. Aprende Machine Learning.

[https://www.aprendemachinelearning.com/como-funcionan-las-convolutional-neural-network](https://www.aprendemachinelearning.com/como-funcionan-las-convolutional-neural-networks-vision-por-ordenador/)

[s-vision-por-ordenador/](https://www.aprendemachinelearning.com/como-funcionan-las-convolutional-neural-networks-vision-por-ordenador/)

Convolutional Neural Networks (CNN) with Deep Learning. (2020, 28 enero).

HappiestMinds.

https://www.happiestminds.com/insights/convolutional-neural-networks-cnns/

Biswal, A. (2023). Convolutional Neural Network Tutorial. Simplilearn.com.

<https://www.simplilearn.com/tutorials/deep-learning-tutorial/convolutional-neural-network>

22

