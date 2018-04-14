import discord
import requests
import math


client = discord.Client()

# Constant
DISCORD_TOKEN = "NDMyNTg0NTI0NjE5MzE3MjQ4.DbLp5w.bIt7-bSr6KVlT_boQLnfTF_RWjc"
FORTNITE_API_KEY = 'ea5ffa46-76a0-426c-a2e8-8b9c6084ee96' 

LISTE = ['Silver', 'Gold', 'Master', 'Distinguished', 'Legendary', 'Supreme', 'Expert', 'SemiPro', 'Pro', 'Professional', 'God']
SILVER_B = 0.00
SILVER_E = 0.99
GOLD_B = 1.00
GOLD_E = 1.49
MASTER_B = 1.50
MASTER_E = 1.99
DISTINGUISHED_B = 2.00
DISTINGUISHED_E = 2.49
LEGENDARY_B = 2.50
LEGENDARY_E = 2.99
SUPREME_B = 3.00
SUPREME_E = 3.49
EXPERT_B = 3.50
EXPERT_E = 3.99
SEMIPRO_B = 4.00
SEMIPRO_E = 4.99
PRO_B = 5.00
PRO_E = 5.99
PROFESSIONAL_B = 6.00
PROFESSIONAL_E = 7.99
GOD_B = 8.00
GOD_E = 100




# Return the overall K/D of the fortnite player pass in parameter
def get_ratio(username):
    print(username)
    link = 'https://api.fortnitetracker.com/v1/profile/pc/' + username
    response = requests.get(link, headers={'TRN-Api-Key': FORTNITE_API_KEY})
    if response.status_code == 200:
        collection = response.json()
        if 'error' in collection:
            return "-1"
        else:
            for data_item in collection['lifeTimeStats']:
                if data_item['key'] == 'K/d':
                    ratio = data_item['value']
                    return ratio
        print("Invalid username")
        return "-1"
    else:
        print("Error recovering fortnite data")
        return "-2"

def get_role(server_roles, target_name):
   for each in server_roles:
      if each.name == target_name:
         return each
   return None

def print_nextLvl(begin, end, ratio):
    rang = end - begin 
    if ratio >= rang * 0.00 + begin and ratio <= rang * 0.05 + begin:
        return '[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.06 + begin and ratio <= rang * 0.10 + begin:
        return '[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.11 + begin and ratio <= rang * 0.15 + begin:
        return '[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.16 + begin and ratio <= rang * 0.20 + begin:
        return '[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.21 + begin and ratio <= rang * 0.25 + begin:
        return '[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.26 + begin and ratio <= rang * 0.30 + begin:
        return '[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.31 + begin and ratio <= rang * 0.35 + begin:
        return '[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.36 + begin and ratio <= rang * 0.40 + begin:
        return '[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.41 + begin and ratio <= rang * 0.45 + begin:
        return '[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.46 + begin and ratio <= rang * 0.50 + begin:
        return '[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.51 + begin and ratio <= rang * 0.55 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.56 + begin and ratio <= rang * 0.60 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.61 + begin and ratio <= rang * 0.65 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.66 + begin and ratio <= rang * 0.70 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]'
    elif ratio >= rang * 0.71 + begin and ratio <= rang * 0.75 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]'
    elif ratio >= rang * 0.76 + begin and ratio <= rang * 0.80 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]'
    elif ratio >= rang * 0.81 + begin and ratio <= rang * 0.85 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]'
    elif ratio >= rang * 0.86 + begin and ratio <= rang * 0.90 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□]'
    elif ratio >= rang * 0.91 + begin and ratio <= rang * 0.95 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]'
    elif ratio >= rang * 0.96 + begin and ratio <= rang * 1.00 + begin:
        return '[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # The command /patch return a link withvthe lastest patch note
    if message.content.startswith('/patch'):
        await client.send_message(message.channel, 'Last patchnotes: https://www.epicgames.com/fortnite/en/news')
    # The command /rank return attribute a rank according to the K/D of the user
    if message.content.startswith("/rank"):
        username = '{0.author.display_name}'.format(message)
        ratio = float(get_ratio(username))
        print(ratio)
        if ratio >= SILVER_B and ratio <= SILVER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[0])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(GOLD_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(SILVER_B, SILVER_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= GOLD_B and ratio <= GOLD_E:
            role = discord.utils.get(message.server.roles, name=LISTE[1])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(MASTER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(GOLD_B, GOLD_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= MASTER_B and ratio <= MASTER_E:
            role = discord.utils.get(message.server.roles, name=LISTE[2])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(SILVER_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(MASTER_B, MASTER_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= DISTINGUISHED_B and ratio <= DISTINGUISHED_E:
            role = discord.utils.get(message.server.roles, name=LISTE[3])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(LEGENDARY_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(DISTINGUISHED_B, DISTINGUISHED_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= LEGENDARY_B and ratio <= LEGENDARY_E:
            role = discord.utils.get(message.server.roles, name=LISTE[4])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(SUPREME_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(LEGENDARY_B, LEGENDARY_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role)  
        elif ratio >= SUPREME_B and ratio <= SUPREME_E:
            role = discord.utils.get(message.server.roles, name=LISTE[5])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(EXPERT_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(SUPREME_B, SUPREME_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= EXPERT_B and ratio <= EXPERT_E:
            role = discord.utils.get(message.server.roles, name=LISTE[6])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(SEMIPRO_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(EXPERT_B, EXPERT_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= SEMIPRO_B and ratio <= SEMIPRO_E:
            role = discord.utils.get(message.server.roles, name=LISTE[7])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(PRO_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(SEMIPRO_B, SEMIPRO_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= PRO_B and ratio <= PRO_E:
            role = discord.utils.get(message.server.roles, name=LISTE[8])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(PROFESSIONAL_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(PRO_B, PRO_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= PROFESSIONAL_B and ratio <= PROFESSIONAL_E:
            role = discord.utils.get(message.server.roles, name=LISTE[9])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Next level: " + str(ratio) + "k/d  **→**  " + str(GOD_B) + "k/d"
            await client.send_message(message.channel, msgRatio)
            await client.send_message(message.channel, print_nextLvl(PROFESSIONAL_B, PROFESSIONAL_E, ratio))
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio >= GOD_B:
            role = discord.utils.get(message.server.roles, name=LISTE[10])
            msg = ("{0.author.mention} Your have been ranked " + role.name).format(message)
            await client.send_message(message.channel, msg)
            msgRatio = "Your ratio: " + str(ratio) + " K/D \n Niveau Max! ¯\_(ツ)_/¯ "
            await client.send_message(message.channel, msgRatio)
            for list in LISTE:
                roles = discord.utils.get(message.server.roles, name=list)
                await client.remove_roles(message.author, roles)
            await client.add_roles(message.author, role) 
        elif ratio == -1:
            msg = "Your discord name is not a fortnite username! Use the command ```/nick YOUR_FORTNITE_USERNAME``` first!".format(message)
            await client.send_message(message.channel, msg)
        elif ratio == -2:
            msg = "The fortnite servers are offline. Try again later!".format(message)
            await client.send_message(message.channel, msg)
 

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(DISCORD_TOKEN)

