import discord
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
import feedparser
import tasks
import threading
import traceback
import tweepy
import summa
import django
from datetime import datetime
from time import mktime
import requests
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

client = discord.Client()

token = "your_token"

def openlink (url):
	print('opening link %s'%(url))
	html = urlopen(url)
	z = riplinks(html, url)
	print(z)
	return z

def riplinks (html, url):
	q = []
	print('ripping links')
	soup = BeautifulSoup(html, 'lxml')
	for a in soup.find_all('a', href=True):
		if '/article' in a['href']:
			q.append(url+a['href'])
			print('%i found.'%(len(q)))
	print('%i found.'%(len(q)))
	return q

def doall (site):
	print('starting')
	q = openlink(site)
	return q

client = discord.Client()

async def my_background_task():
    await asyncio.sleep(60)
    channel = discord.Object(id='636533302748119053')
    last_post = ""

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('--Burn-Bot--------')

@client.event
async def on_message(message):
	if (message.content.startswith('hello')):
		x = message.content.replace('bernie bot?', 'politics')
		if x == '':
			x = 10
		elif x[0] != ' ' :
			x = 10
		else:
			x = int(x.replace(' ', ''))
			
		links = doall("https://reuters.com/politics")
		await client.send_message(message.channel, 'Ehhh uhhh climate change is real damnit! https://tenor.com/view/bernie-trump-gif-5203774')
		print(links)
		print('Print all')
		for n in range(0, x):
		    await client.send_message(message.channel, '%s'%(links[n]))
	    
    #elif (message.content == 'NEWS MODULE'):
	#	await client.send_message(message.channel, 'News module shutting down')
	#	client.close()
	#	raise SystemExit

        #await asyncio.sleep(60)

client.loop.create_task(my_background_task())
client.run(token)
