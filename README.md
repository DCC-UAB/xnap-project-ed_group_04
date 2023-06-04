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


DESENVOLUPAMENT 

Un dels primers canvis que es van realitzar va ser passar el model a la GPU de la màquina virtual per tal de poder executar a major velocitat.

Un segon canvi va ser aplicar un resize a totes les imatges per a que totes tinguessin una mida de (256,256) i així, no hi hagués cap conflicte a l’hora d’operar amb aquestes.

També es mira que totes les fotografies tinguin tres dimensions, en el cas de no ser així, és a dir, que siguin en blanc i negre, s’afegeixen dues dimensions més.

Seguidament, a la part del codi del Data Augmentation, per tal d’afegir variabilitat i més característiques a les imatges, hi havia diverses opcions de canvis que s’apliquen a algunes imatges, dues d’aquestes opcions eren flips, aquests es van descartar ja que no interessa que s’alteri la naturalesa de la composició de les imatges.

Les modificacions d’imatges que s’han mantingut són el shear_range que aplica una deformació a la imatge amb un angle màxim de 0.2 radians, el zoom_range que apropa o allunya la imatge com a màxim en un 0.2 i finalment, el rotation_range que realitza una rotació aleatoria com a màxim de 20 graus. Aquesta última modificació afegeix variabilitat però no arriba a distorsionar la naturalesa de la composició de la imatge tant com els flips.

El Data Augmentations és important en aquest projecte degut a que els datasets que s’usen no són massa grans, per tant, afegir característiques modificant les imatges, fa que s’enriqueixi l’entrenament del model.

Una altra modificació del codi ha sigut aplicar més capes convolucionals al model. Aquest canvi es va aplicar per obtenir una major capacitat d’aprenentatge de característiques ja que cada capa extra pot aprendre característiques més complexes i abstractes que les capes anteriors.

Al afegir més capes convolucionals també augmentem la no linealitat de la xarxa, el que permet aprendre relacions i patrons no lineals en les dades. Al augmentar la profunditat de la xarxa, s’augmenta la capacitat per processar relacions no lineals més complexes entre les dades.

No sempre es recomenable aquest canvi ja que si s’afegeixen moltes, la xarxa es pot tendir a l’overfitting i a més pot causar problemes de memòria, per això, per aquest model només s’han afegit tres capes convolucionals extres.

Després es van canviar l’optimitzador i el learning rate. Experimentalment, el millor optimitzador ha sigut Adagrad amb un learning rate de 0.001. Adagrad és un bon optimitzador ja que quan els gradients varien de manera considerable entre dimensions, Adagrad treballa bé. 

Després es van canviar el batch_size, les epochs i els steps_per_epoch. El batch_size és el número d’elements del train que s’utilitzen en una iteració abans d’actualitzar els pesos del model. Per tal d’utilitzar un batch_size optim, s’ha d’observar el numero d’elements que hi ha al train, com els datasets que s’utilitzen en aquest projecte són petits, el batch size adient es troba al voltant de 15.

Per les epochs, que és la quantitat de cops que el model passa per tot el train, també s’ha tingut en compte la mida del train, com els trains acostumen a no ser massa grans, 350 epochs són suficients per a que el model eviti l’overfitting.
Els steps per epoch són el número de pasos que es faràn en cada època, entent passos com la realització d’un càlcul per actualitzar els pesos del model. En aquest cas els steps que han mostrat millors resultats han estat al voltant dels 50.

Finalment, per tal de comprovar si el model fa overfitting de manera gràfica, s’ha guardat el fit_generator del model en la variable ‘history’ afegint per paràmetre el validation_data que és la part del conjunt X que s’usa com a test. Del history extraiem la ‘loss’, que representa la loss del train, i la ‘val_loss’ que representa la loss del conjunt de validació. Per poder visualitzar aquests resultats i comprovar si es fa overfitting, es fan plots d’aquests resultats i com VisualStudio no te interfície gràfica, es guarda el resultat dels plots com a arxiu png.









