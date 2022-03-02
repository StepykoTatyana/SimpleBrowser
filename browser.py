import argparse
import os
import sys

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
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.'''
nytimes_com = '''This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
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
site = input()
while site != 'exit':
    if site == 'bloomberg.com':
        file = open(folder_browser + '\\bloomberg', 'w')
        file.write(bloomberg_com)
        file = open(folder_browser + '\\bloomberg', 'r')
        print(file.read())
        file.close()
    elif site == 'nytimes.com':
        file = open(folder_browser + '\\nytimes', 'w')
        file.write(nytimes_com)
        file = open(folder_browser + '\\nytimes', 'r')
        print(file.read())
        file.close()
    elif site == 'bloomberg' and os.access(folder_browser + '\\bloomberg', os.F_OK) == 1:
        file = open(folder_browser + '\\bloomberg', 'r')
        print(file.read())
        file.close()
    elif site == 'nytimes' and os.access(folder_browser + '\\nytimes', os.F_OK) == 1:
        file = open(folder_browser + '\\nytimes', 'r')
        print(file.read())
        file.close()
    else:
        print("Error: Incorrect URL")
    print()
    site = input()
