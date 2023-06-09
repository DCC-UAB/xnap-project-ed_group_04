## CONTRIBUTORS
Yasmin L'Harrak: 1603496@uab.cat

Nuria Salvador: 1605592@uab.cat

Amal El Hammoudi 1608672@uab.cat

Xarxes Neuronals i Aprenentatge Profund -Grau de Data Engineering UAB, 2023

Aquest repositori conté el conjunt de codis utilitzats per a la coloració automàtica d'imatges i vídeos en blanc i negre, així com els conjunts de dades utilitzats i resultats obtinguts en aquest procés.

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



## STARTING POINT

Per començar, es va utilitzar el repositori “starting_point” com a base per al projecte. Aquest repositori proporciona tres versions diferents, però només es van utilitzar les dues primeres (alpha i beta). La tercera versió, que era un model molt pesat, no era viable a causa de les limitacions de memòria disponibles.


## ARQUITECTURA DEL MODEL

Per afrontar aquesta qüestió, s’ha decidit utilitzar una Xarxa Neuronal Convolutional (Convolutional Neural Network, CNN). Es basa en l’arquitectura d’un autoencoder.
        
Un autoencoder és una xarxa neuronal que consta de dues parts: un encoder i un decoder. 

L’enconder és la primera part, es compon de diverses capes convolucionals i s’encarrega d’extreure les característiques més importants de les imatges en blanc i negre. Aquest procès permet que el model aprengui a capturar els patrons, textures, etc per a la posterior coloració.

El decoder és la segona part, s’encarrega de reconstruir l’entrada original a partir de la representació generada per l’encoder. Aquesta arquitectura seqüencial permet aprendre patrons i textures de les imatges per aconseguir una coloració precisa i realista.


## ALPHA VERSION
La versió alpha treballa sobre una única imatge, la qual, passa de RGB a LAB on la component 'L' (Lluminositat) serà la 'X' i les components 'A' i 'B' (canals de colors), es normalitzen dividint-se entre 128 i seran la variable 'Y'.

S'utilitza una xarxa neuronal seqüencial, ja que el problema no és massa complex. Aquest model té capes convolucionals 'Conv2D' amb activació ReLU, ja que amb ReLU s’evita el problema de desaparició del gradient i aporta no linealitat a la xarxa per tal d’aprendre altres patrons i característiques.
A les capes convolucionals es troba padding 'same' per no modificar la mida de la imatge de entrada, es a dir, que la mida de l’entrada i la de la sortida siguin la mateixa, i strides=2, reduint així la sortida de la capa convolucional a la meitat de les dimensions que la capa d'entrada. 

També s'usen capes d'upsampling per augmentar les dimensions de la imatge per poder reconstruir caracteristiques que s’han reduit degut a l’us de l’stride=2 i una capa convolucional final amb activació per tangent hiperbòlica. S’usa l’activació per tanh perquè la sortida es normalitza entre -1 i 1 i aixó es favorable per representar els colors a l’espai LAB.

Per optimitzar el model, s’utilitza l’optimitzador rmsprop amb una leaning rate de 0.001 i la funció de pèrdua d’error mitjà quadrat (MSE). 

Es fa un fit del model passant la 'X' i la 'Y' que s'han creat anteriorment. Finalment, s'avalua el model i es fa la predicció multiplicant la sortida per 128 per tal de retornar la imatge predita amb els colors adients.


## BETA VERSION

La versió beta segueix el mateix procediment que l’alpha version, encara que aquest treballa sobre un train d’imatges a color, i les converteix de l’escala RGB a LAB, on la component L serà la X i les components A i B (canals de colors), es normalitzen i es divideixen entre 128, sent la variable Y.

En aquest cas, es construeix un model seqüencial, i es comença afegint una capa d’entrada (InputLayer) amb una dimensió de 256x256. Aquesta dimensió és la mateixa que “L”, que representa la imatge en escala de grisos.

A continuació, s’afegeixen diversos blocs convolucionals que formen la part de l’encoder del model. El primer bloc consisteix en una capa convolucional amb 63 filtres de mida 3x3, activada per la funció d’activació ReLu (Rectified Linear Unit) per introduir no linealitats, i s’aplica un padding “same” als marges, per mantenir la mida original de la imatge.

Seguidament, s’augmenta el nombre de filtres en els blocs convolucionals posteriors. S’utilitzen capes amb 128, 256 i 512 filtres, mantenint la mateixa mida de filtre (3x3) i la funció d’activació ReLU. Algunes d’aquestes capes estan seguides de capes de strides, per reduir la dimensionalitat de la imatge.

Després dels blocs convolucionals, s’afegeixen les capes de reconstrucció (decoder), per generar la imatge en color. Aquestes capes inclouen una capa d’UpSampling2D, per augmentar la resolució de la imatge, per compensar els strides aplicats anteriorment. També inclou capes convolucionals amb un nombre reduïts de filtres (64 i 32) i activació ReLU. 
Finalment, s’afegeix una capa convolucional amb 2 filtres i activació tangent hiperbòlica (tanh) per generar la imatge en color. La capa de sortida té una dimensió de 256z256x2, on els dos canals representen els valors de color, els canals A i B.

Per optimitzar el model, s’utilitza l’optimitzador Adagrad amb una leaning rate de 0.001 i la funció de pèrdua d’error mitjà quadrat (MSE).

Per comprovar el procès de coloració, el primer que es fa és llegir les imatges del test i s’ajusta la mida de les imatges a 256x256. Després de la redimensió i comprovació de que les imatges tinguin 3 canals, es converteixen a l’espai LAB utilitzant la funció rgb2lab.

A continuació, s’aplica el model entrenat a les imatges, utilitzant la funció predict. Aquesta funció el que fa és retornar les prediccions, que són les imatges en color generades pel model. Seguidament, es crea una matriu buida de mida 256x256x3 per representar la imatge final en color. El que es fa és assignar els valors de la capa L de la imatge original (entrada) a la capa L de la nova imatge i, després s’assignen les prediccions del model a les capes A i B.

Finalment, s’aplica la conversió inversa de l’espai de color LAB a RGB, utilitzant la funció lab2rgb.


## GIF VERSION

En el marc d'aquest projecte, s'ha decidit ampliar-ne l'abast per incloure la coloració de vídeos en format GIF en blanc i negre i no només imatges.

La idea ha estat utilitzar les mateixes tècniques d'aprenentatge profund que s'ha utilitzat, ja que les xarxes neuronals convolucionals han mostrat resultats bastant satisfactoris. De tal manera que s'ha seguit la mateixa idea i procés, per recrear el color en el següent GIF (starting_point/Beta-version/video-paisatge.gif)


Si bé és cert, no es va tractar el GIF com a vídeo, ja que es va tractar com una seqüència de frames individuals, i cada frame es va considerar com una imatge independent. 

Primerament, es va entrenar un model seqüencial utilitzant un conjunt de dades d'entrenament específic que consistia en més de 100 imatges temàtiques del directori "beach".

Un cop el model seqüencial va ser entrenat amb les imatges del train del directori "beach", es passa a la fase test, en la que s’utilitza els frames del GIF en format LAB.  Aquesta representació LAB, permet separar la informació de la imatge en lluminositat (L) i dos canals de colors (A i B) . 

Aquesta separació va bé per tal de poder fer la predicció, ja que per cada frame individual, es passa el canal lluminositat (L) com a entrada del model predictiu i genera un output corresponent al canals de color (A, B). 

Acabat el procés de predicció per cada frame individual, es reconstrueixen les imatges finals. Per fer-ho, primerament, s’uneixen els tres canals (L, A, B), els del output i el de l’entrada del predict, creant la imatge resultat en format LAB. Per acabar de recrear la imatge resultant la passem al model de representació RGB.


Aquest procés es repeteix per a tots els frames del GIF, fins a obtenir la seqüència completa de frames en color. Finalment, es reconstrueix el GIF acolorit unint tots els frames processats.

Es va fent el mateix per tots els frames, fins a tenir-los tots, un cop acabat aquest procés, reconstruim el GIF acolorit unint els frames.
