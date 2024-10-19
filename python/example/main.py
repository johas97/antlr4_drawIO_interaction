import os
import discord
import requests 
import json
from pprint import pprint 
import meme
import reactions

client = discord.Client()
  
  
@client.event 
async def on_redy(): 
  print('We have logged in as {0.user}'.format(client))


@client.event 
async def on_message(message): 
  if message.author == client.user: 
    return
  messg = message.content
 
  
  #Meme actions
  if messg.startswith('summon' or 'Summon'):
    json_data = meme.get_meme()
    await message.channel.send(json_data['title'])
    await message.channel.send(json_data['preview'][-1])
  
    
    #Tagging actions
  if  messg.startswith('tag' or 'Tag'): 
    messg_arr = messg.split(' ', 3) 
    emoji_id = messg_arr[3]
    user_id = messg_arr[1]
    reactions.add_to_taglist(user_id, emoji_id)

  if  messg.startswith('untag' or 'Untag'): 
    messg_arr = messg.split(' ', 3) 
    emoji_id = messg_arr[3]
    user_id = messg_arr[1]
    reactions.remove_from_taglist(user_id, emoji_id)

  if reactions.is_tagged(message.author):
   await reactions.execute_reactions(message.author, message)
    

    
    
    

    
    

    

    

#  if (message.author in sus_list) 
    
    

client.run(os.environ['bot_token'])

