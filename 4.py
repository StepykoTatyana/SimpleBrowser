import argparse
import os
import sys

import colorama
import requests
from bs4 import BeautifulSoup
from colorama import Fore

colorama.init()


def get_to_site(site_value):
    try:
        f = open(os.path.join(folder_browser, site_value.replace('.com', '').replace('https://', '')), 'w',
                 encoding='UTF-8')
        r = requests.get(site_value)
        soup = BeautifulSoup(r.content, 'html.parser')
        body = (soup.find_all(['[document]', 'head', 'script', 'style',
                               'body', 'html', 'h1', 'h2', 'h3', 'h4', 'h5',
                               'h6', 'title',
                               'table', 'div', 'li', 'form',
                               'img', 'tr', '\n']))
        for a in body:
            if a.name == "a":
                f.write((Fore.BLUE + a.text) + '\n')
            else:
                f.write(a.text + '\n')
        f.close()
        f1 = open(os.path.join(folder_browser, site_value.replace('.com', '').replace('https://', '')), 'r',
                  encoding='UTF-8')
        for j in f1:
            colorama.init()
            print(j.replace('\n', ''))
        f1.close()
    except requests.ConnectionError:
        print('Incorrect URL')


parser = argparse.ArgumentParser(description="This program open cites")
bloomberg_com = '''The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker?s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.'''
nytimes_com = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created ?soft? magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
important female and minority scientists in less than two 
years.'''

args = sys.argv
folder_browser = args[1]
if os.access(folder_browser, os.F_OK) == 1:
    pass
else:
    os.makedirs(folder_browser)
stack = []
history = []
i = 0
site = input()

while site != 'exit':
    if site.__contains__('http') == 1:
        get_to_site(site.replace('https://', ''))
    elif site.__contains__('http') == 0:
        site_new = 'https://' + site
        get_to_site(site_new)
    elif site == 'back':
        if len(stack) != 0:
            file = open(folder_browser + '\\' + stack.pop(), 'r')
            print(file.read())
            file.close()
    else:
        print("Error: Incorrect URL")
    if len(history) > 1:
        while i < len(history) - 1:
            stack.append(history[0])
            i += 1
    print()
    site = input()
