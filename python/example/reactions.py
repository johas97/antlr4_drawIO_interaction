import os
import discord
import requests 
import json
from pprint import pprint 

taglist = []

class PersonTag: 
  def __init__(self, user_id, emoji_id):
    self.user_id = user_id
    self.emoji_id = emoji_id
    
def add_to_taglist(user_id, emoji_id):
  
  user = PersonTag(user_id, emoji_id)
  taglist.append(user)

def remove_from_taglist(user_id, emoji_id): 
  for user in taglist: 
    if str(user.user_id) == str(user_id) and str(user.emoji_id) == str(emoji_id):
      taglist.remove(user)


def is_tagged(user_id):
  for user in taglist:
    if str(user.user_id) == str(user_id):
       return True
       
  return False
 
async def execute_reactions(user_id, message):
  actions_to_execute = []
  for user in taglist: 
    if str(user.user_id) == str(user_id): 
      actions_to_execute.append(user.emoji_id)

  for reaction in actions_to_execute: 
   await message.add_reaction(reaction)
  

  

  

  
      
    
  
  
       
    
  


  
  
  