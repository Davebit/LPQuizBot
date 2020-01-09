# LPQuizBot

El projecte QuizBot per GEI-LP (edició tardor 2019). 
L’objectiu general de la pràctica consisteix en desenvolupar un chatbot que permeti recollir les dades d’enquestes definides mitjançant un compilador a través de telegram i consultar gràfiques simples i informes sobre les dades recollides.

## Començem

Aquestes instrucciones t'ajudaran a executar el projecte en la teva màquina local i testejar-lo.

### Prerequisits

Per realitzar la nostra pròpia gramàtica necessitem tenir instal·lat ANTLR4

A ms,es necessiten tenir instalades les següents llibreries de Python:

```
matplotlib -> per graficar dades.
networkx -> per a manipular grafs.
pickle -> per guardar i carregar estructures de dades en binari.
python-telegram-bot -> per interactuar amb Telegram.
```

### Instal·lant...

Per realitzar la instal·lació de ANTLR4:

Primer cal descarregar el arxiu jar [ANTLR4](https://www.antlr.org//):
* [jar file](https://www.antlr.org/download/antlr-4.7.1-complete.jar)
* [Getting started](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

Per realitzar la instal·lació de les llibreries:

```
pip3 install antlr4-python3-runtime
pip3 install matplotlib
pip3 install networkx
pip3 install python-telegram-bot
```

## Running the tests

Per executar el bot de Telegram, utilitzarem la següent comanda:

```
python3 bot.py input.txt
```
`input.txt` es el conjunt de respostes i preguntes que defineixen l'enquesta. Per utilitzar una altra enquesta, crear un nou arxiu i passar-lo com argument, o editar l'arxiu `input.txt`

### Bot de Telegram

Una vegada executat el programa, cal anar al bot en Telegram i iniciar una conversa amb el Bot.

### Comandes del bot

- `/start` inicia la conversa amb el Bot.
- `/help` el Bot ha de contestar amb una llista de totes les possibles comandes i
una breu documentació sobre el seu propòsit i ús.
- `/author` el Bot ha d’escriure el nom complet de l’autor del projecte i seu correu
electrònic oficial de la facultat.
- `/quiz <idEnquesta>` el Bot ha de iniciar un intèrpret similar al de la secció anterior realitzant
l’enquesta. A la secció següent s'amplia la informació.
- `/bar <idPregunta>` el Bot ha de tornar una gràfica de barres mostrant un diagrama de barres
de les respostes a la pregunta donada. A les seccions següents s'amplia la informació.
- `/pie <idPregunta>` el Bot ha de tornar una gràfica de formatget amb el percentatge de les respostes a la pregunta
donada. A les seccions següents s'amplia la informació.
- `/report` el Bot ha de tornar quelcom tipus taula amb el nombre de respostes obtingudes per cada valor de cada pregunta. A les seccions següents s'amplia la informació.

## Referències

* [Matplotlib](https://matplotlib.org/) - Per gràficar les dades
* [NetworkX](https://maven.apache.org/) - Per manipular grafs
* [Pickle](https://rometools.github.io/rome/) - Per guardar i carregar estructures de dades en binari.
* [Python-telegram-bot](https://python-telegram-bot.org/) - Per interactuar amb Telegram.

## Autor

* **David Carballo** - *david.carballo@est.fib.upc.edu*

## Enunciat

Aquest projecte s'ha realitzat segons les tasques demanades en l'enunciat de la [pràctica](https://gebakx.github.io/QuizBot/) 
