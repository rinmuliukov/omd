#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def step2_umbrella():
    print(
        'А Утка 🦆 сделала д/з по питону?? 🐍 '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if option == 'да':
        return step3_avito()
    return step3_no_avito()


def step2_no_umbrella():  
    print('Утка осталась дома смотреть сериал')
def step3_avito():
    print('☂️+🦆+🍺')
def step3_no_avito():
    print('Утка осталась делать домашку, бар подождет')



def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if option == 'да':
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()

