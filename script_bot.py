import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import discord
from discord import Guild
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'mr.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv(dotenv_path="config")
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents =default_intents)
ma_liste=[]



@client.event
async def on_ready():
    print("Le bot est prêt.")
    global ma_liste
    ma_liste = client.guilds
    


@client.event
async def on_message(message):
    logging.info(f"{message.author} : {message.content} dans {message.channel.name}")

    if not message.channel.id == 911362696065200198:
        if not str(message.author)=="Yondaime#6523":
            await message.delete()
    
    if message.channel.id == 911081339892138004:
        await room00(message)

    if message.channel.id == 911243628851134554:
        await room01(message)

    if message.channel.id == 911357911916249128:
        await room02(message)

    if message.channel.id == 911357958762414120:
        await room03(message)
    
    if message.channel.id == 911415605402431558:
        await room04(message)

    if message.channel.id == 911986341129093140:
        await room05(message)
    
    if message.channel.id == 912868986276950017:
        await room06(message)

    if message.channel.id == 912872402793414747:
        await room07(message)
    
    if message.channel.id == 912872453901017191:
        await room08(message)
    
    if message.channel.id == 912872501187592212:
        await room09(message)

    if message.channel.id == 912872552542658620:
        await room10(message)
    
    if message.channel.id == 919004281888202782:
        await room11(message)

        
            
    #if message.content.lower()=="ping":
       # role = discord.utils.get(message.guild.roles, name="Player")
        #await message.author.add_roles(role)

    #if message.content.lower()=="room":
        #print('test')
        
    #if not str(message.author)=="Yondaime#6523":
        #await message.delete()

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(906330987506585684)
    await client.get_channel(911081339892138004).set_permissions(member,read_messages=True,send_messages=True)
    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")

async def room00(message):
    if message.content == str(message.author):
        await message.channel.set_permissions(message.author, overwrite=None)
        await client.get_channel(911243628851134554).set_permissions(message.author,read_messages=True,send_messages=True)
        role = discord.utils.get(message.guild.roles, name="New Player")
        await message.author.add_roles(role)
        

async def room01(message):
    if message.content == "1":
        await client.get_channel(911357911916249128).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(911243628851134554).set_permissions(message.author, overwrite=None)
        
async def room02(message):
    if message.content.lower() == "bravo":
        await client.get_channel(911357958762414120).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(911357911916249128).set_permissions(message.author, overwrite=None)

async def room03(message):
    r =['zhang ning', 'ning zhang']
    if message.content.lower() in r:
        await client.get_channel(911415605402431558).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(911357958762414120).set_permissions(message.author, overwrite=None)

async def room04(message):
    r=['frédéric chopin', 'chopin frédéric']
    if message.content.lower() in r:
        await client.get_channel(911986341129093140).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(911415605402431558).set_permissions(message.author, overwrite=None)    

async def room05(message):
    r=['area51', 'zone51', 'zone 51', 'area 51']
    if message.content.lower() in r:
        await client.get_channel(912868986276950017).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(911986341129093140).set_permissions(message.author, overwrite=None)    

async def room06(message):
    r=[f"a l'envers des nuages il y a toujours un ciel"]
    if message.content.lower() in r:
        await client.get_channel(912872402793414747).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(912868986276950017).set_permissions(message.author, overwrite=None)    

async def room07(message):
    r=[f"j'ai découvert ton mot de passe changes en rapidement"]
    if message.content.lower() in r:
        await client.get_channel(912872453901017191).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(912872402793414747).set_permissions(message.author, overwrite=None)  
        role = discord.utils.get(message.guild.roles, name="Advanced Player")
        await message.author.add_roles(role)
        role = discord.utils.get(message.guild.roles, name="New Player")
        await message.author.cdremove_roles(role)

async def room08(message):
    r=['a tout bout de champ']
    if message.content.lower() in r:
        await client.get_channel(912872501187592212).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(912872453901017191).set_permissions(message.author, overwrite=None) 

async def room09(message):
    r=datetime.now().strftime('%H:%M')
    if message.content == r:
        await client.get_channel(912872552542658620).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(912872501187592212).set_permissions(message.author, overwrite=None) 

async def room10(message):
    if message.content == "30":
        await client.get_channel(919004281888202782).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(912872552542658620).set_permissions(message.author, overwrite=None) 

async def room11(message):
    if message.content == "720":
        await client.get_channel(919264379155939338).set_permissions(message.author,read_messages=True,send_messages=True)
        await client.get_channel(919004281888202782).set_permissions(message.author, overwrite=None) 


client.run(os.getenv("TOKEN"))

