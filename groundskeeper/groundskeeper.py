from datetime import datetime

import discord
from discord.ext import commands
from constants import CLIENT_KEY, INTRO_ID, GENERAL_CHANNEL_ID, MEMBER_ROLE_ID, SERVER_ID, ROLES_CHANNEL_ID

intents = discord.Intents.default()
intents.members = True
BOT_PREFIX = '>'

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
# bot = interactions.Client(CLIENT_KEY)

server = None

# Roles of interest
member_role = None

# channels of interest
general_channel = None
intros_channel = None
roles_channel = None


@bot.event
async def on_member_remove(member):
    if member_role in member.roles:
        await general_channel.send(f"{member.name} left the castle")

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return

    print(f'Message received: {message.content}')
    if message.channel.id == INTRO_ID and not message.author.bot and member_role not in message.author.roles:
        await message.author.add_roles(member_role)
        return

@bot.listen()
async def on_message_delete(message):
    print(f'Message deleted: {message}')
    if message.channel.id == INTRO_ID and not message.author.bot:
        await message.author.remove_roles(member_role)
        return

@bot.event
async def on_member_update(before, after):
    print(f'GUILD MEMBER UPDATE: {before}')
    if member_role not in before.roles and member_role in after.roles:
        await general_channel.send(f"Welcome to the Castle, {after.mention}!\n"
                                 f"Don't forget to pick your {roles_channel.mention}!")


@bot.event
async def on_ready():
    print("logged in")
    global server
    global member_role
    global intros_channel
    global general_channel
    global roles_channel

    server = bot.get_guild(SERVER_ID)

    general_channel = server.get_channel(GENERAL_CHANNEL_ID)
    intros_channel = server.get_channel(INTRO_ID)
    roles_channel = server.get_channel(ROLES_CHANNEL_ID)

    member_role = server.get_role(MEMBER_ROLE_ID)

bot.run(CLIENT_KEY)
