import argparse
import os
import sys
import requests

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
        with open(os.path.join(folder_browser, site.replace('.com', '')), 'w', encoding='UTF-8') as f, open(
                os.path.join(folder_browser, site.replace('.com', '')), 'r', encoding='UTF-8') as f1:
            r = requests.get(site).text
            f.write(r)
            print(f1.read())
    elif site.__contains__('http') == 0:
        with open(os.path.join(folder_browser, site.replace('.com', '')), 'w', encoding='UTF-8') as f, open(
                os.path.join(folder_browser, site.replace('.com', '')), 'r', encoding='UTF-8') as f1:
            r = requests.get('https://' + site).text
            f.write(r)
            print(f1.read())
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
