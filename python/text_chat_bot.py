#-*- coding: utf-8-*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

convI = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'bom dia, como vai?',
        'estou bem']
convF = ['que filmes você gosta?', 'eu gosto de John Wick.']


bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)

while True:
    quest = input('Você: ')
    answer = bot.get_response(quest)

    print('Bot: ', answer)
