import os

import discord
import asyncio
from profanity import profanity

client = discord.Client()
client._strict = False

@client.event
async def on_ready():
    print('Pooh is ready to enforce family values!')


def get_pooh(server):
    for emoji in server.emojis:
        if emoji.name == 'pooh':
            return emoji

    print('No :pooh: emoji found!')
    return '💩'


def is_admin(member):
    for role in member.roles:
        if role.name == 'admin':
            return True
    return False


async def handle_message(message):
    if client._strict:
        await client.delete_message(message)
        reply =  f'Sorry sir, this is a Christian server, so no swearing <@{message.author.id}>.'
        await client.send_message(message.channel, reply)
    else:
        await client.add_reaction(message, get_pooh(message.server))


@client.event
async def on_message(message):
    if message.channel.is_private:
        return

    if is_admin(message.author):
        if message.content.startswith('!strict'):
            client._strict = not client._strict
            strict = "on" if client._strict else "off"
            reply = f'Watch your language kids! Strict mode: {strict}'
            await client.send_message(message.channel, reply)
            return

    if profanity.contains_profanity(message.content):
        await handle_message(message)

@client.event
async def on_message_edit(before, after):
    if after.channel.is_private:
        return

    if profanity.contains_profanity(after.content):
        await handle_message(message)
    elif not profanity.contains_profanity(after.content):
        await client.remove_reaction(after, get_pooh(after.server), after.server.me)

client.run(os.environ.get('DISCORD_TOKEN'))
