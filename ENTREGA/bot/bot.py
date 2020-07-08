# importing Telegram API
import networkx as nx
import pickle
import matplotlib.pyplot as plt
from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
#t.me/LPQuizbot

# defining callback function for the /start command
def start(bot, update, user_data):
    username = update.message.chat.username
    missatge = "Hola %s" % (username)
    pickle_in = open('enq.pickle','rb')
    enquestes = pickle.load(pickle_in)
    pickle_in.close()
    if 'report' not in user_data:
        user_data['report'] = {}
    user_data['report'] = enquestes
    bot.send_message(chat_id=update.message.chat_id, text="Benvingut al QuizBot %s"%username)

def help(bot, update):
    info = '''
    Comandes del bot:
    /start
            Inicia la conversa amb el Bot.

    /help
            Llista totes les comandes possibles del bot
            amb una breu descripcio

    /author
            Mostra el nom complet de l'autor del projecte 
            i el seu correu electrònic de la facultat.

    /quiz <idEnquesta> 
            Inicia la enquesta seleccionada per ID.
            
    /bar <idPregunta>
            Diagrama de barres de les respostes a la pregunta donada.
            
    /pie <idPregunta>
            Grafica de formatgets amb el percentatge de les respostes a la pregunta donada.
            
    /report
            Taula amb el nombre de preguntes respostes per cada valor de cada pregunta.

    '''
    bot.send_message(chat_id=update.message.chat_id, text=info)

def author(bot, update):
    missatge = """
    David Carballo Montalbán
    (david.carballo@est.fib.upc.edu)"""
    bot.send_message(chat_id=update.message.chat_id, text=missatge)

def quiz(bot, update, args, user_data):
    if 'graph' not in user_data:
        user_data['graph'] = {}
    # Llegim el nostre graph
    graph = nx.read_gpickle("graph.gpickle")
    user_data['graph'] = graph
    enquestes = user_data['report']
    if 'enquesta' not in user_data:
        user_data['enquesta'] = {}
    if 'act_enquesta' not in user_data:
        user_data['act_enquesta'] = ""
    if 'act_question' not in user_data:
        user_data['act_question'] = "" 

    # Creació del pickle per la solucio
    if 'respostes' not in user_data:
        user_data['respostes'] = {} 

    # Obtenir l'enquesta solicitada

    id_enq = args[0]
    bot.send_message(chat_id=update.message.chat_id, text="Enquesta: %s" % (id_enq))
    
    succ = []
    for u,v,color in graph.edges.data('color'):
        if color == 'black':
            succ.append((u,v))

    sub = graph.edge_subgraph(succ)
    succ = nx.shortest_path(sub,id_enq,'END')
    succ.remove(id_enq)
    
    user_data['act_enquesta'] = id_enq
    user_data['enquesta'][id_enq] = succ
    
    # Fem la primera pregunta de l'enquesta
    quest = succ[0]
    if enquestes.get(quest) == None:
        enquestes[quest] = {}

    pregunta = " ".join(graph.nodes[quest]['content'])
    bot.send_message(chat_id=update.message.chat.id, text="E> %s" % (pregunta))
    user_data['act_question'] = quest

    for u,v in graph.edges(quest):
        if(graph[quest][v]['color'] == 'blue'):
                respostes = graph.nodes[v]['content']
                for cont,x in enumerate(respostes):
                    bot.send_message(chat_id=update.message.chat.id, text="%s: %s" % (cont," ".join(x)))

def answer(bot, update, user_data):
    enquestes = user_data['report']

    quest = user_data['act_question']
    if enquestes.get(quest) == None:
        enquestes[quest] = {}
    next_quest = quest
    id_enq = user_data['act_enquesta']
    graph = user_data['graph']

    # Actualitzar dades
    msg = update.message.text
    if enquestes[quest].get(msg) == None:
        enquestes[quest][msg] = 1
    else:
        enquestes[quest][msg] += 1
    #print(enquestes) 

    # Seguent pregunta
    succ = user_data['enquesta'][id_enq]
    #print(succ)
    succ.remove(quest)
    for u,v in graph.edges(quest):
        #print("%s,%s"%(u,v))
        if(graph[u][v]['color'] == 'green' and graph[u][v]['tag'] == msg):
            #print(graph[u][v]['tag'])
            succ.insert(0,v)
            next_quest = v

    if next_quest == quest:
        next_quest = quest = succ[0]

    if succ[0] == 'END':
        bot.send_message(chat_id=update.message.chat.id, text="Gràcies pel teu temps!")
        #print(enquestes)
        pickle_out = open('enq.pickle','wb')
        pickle.dump(enquestes,pickle_out)
        pickle_out.close()

    else:
        user_data['act_question'] = next_quest
        user_data['enquesta'][id_enq] = succ
        pregunta = " ".join(graph.nodes[next_quest]['content'])
        bot.send_message(chat_id=update.message.chat.id, text="E> %s" % (pregunta))

        for u,v in graph.edges(next_quest):
            if(graph[next_quest][v]['color'] == 'blue'):
                    respostes = graph.nodes[v]['content']
                    for cont,x in enumerate(respostes):
                        bot.send_message(chat_id=update.message.chat.id, text="%s: %s" % (cont," ".join(x)))

def bar(bot, update, args):
    try:
        pickle_in = open('enq.pickle','rb')
        enq = pickle.load(pickle_in)
        pickle_in.close()

        fitxer = "bar%s.png" % (args[0])
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        x = enq[args[0]].keys()
        y = enq[args[0]].values()
        ax.bar(x,y)
        plt.savefig(fitxer, bbox_inches='tight')
        bot.send_photo(chat_id=update.message.chat_id, photo=open(fitxer, 'rb'))
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='Error al crear la gràfica')

def pie(bot, update, args):
    try:
        pickle_in = open('enq.pickle','rb')
        enq = pickle.load(pickle_in)
        pickle_in.close()
        fitxer = "pie%s.png" % (args[0])

        total = sum(enq[args[0]].values())

        perc = [x/total for x in enq[args[0]].values()]
        labels = enq[args[0]].keys()
        explode = [0.05] * len(labels)
        fig,ax = plt.subplots()
        ax.pie(perc, labels=labels,explode=explode,shadow=True, autopct='%1.1f%%',startangle=90)
        ax.axis('equal')
        plt.savefig(fitxer, bbox_inches='tight')
        bot.send_photo(chat_id=update.message.chat_id, photo=open(fitxer, 'rb'))
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='Error al crear la gràfica')

def report(bot, update):
    try:
        pickle_in = open('enq.pickle','rb')
        enq = pickle.load(pickle_in)
        pickle_in.close()

        table = "*Pregunta*\t*Valor*\t*Respostes*\n"
        for question in enq:
            for u in enq[question]:
                table += "%s\t%s\t%s\n"%(question,u,enq[question][u])
        bot.send_message(chat_id=update.message.chat_id, text=table, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='Error al carregar el report')

# loading the access token from token.txt
TOKEN = open('token.txt').read().strip()

# call main Telegram objects
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# handling callbacks functions to the commands
dispatcher.add_handler(CommandHandler('start', start, pass_user_data=True))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('quiz', quiz, pass_args=True, pass_user_data=True))
dispatcher.add_handler(CommandHandler('bar', bar, pass_args=True))
dispatcher.add_handler(CommandHandler('pie', pie, pass_args=True))
dispatcher.add_handler(CommandHandler('report', report))

dispatcher.add_handler(MessageHandler(Filters.text, answer, pass_user_data=True))

# starting the bot
updater.start_polling()
