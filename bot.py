import discord
import asyncio
from profanity import profanity

client = discord.Client()

@client.event
async def on_ready():
    print('Pooh is ready to enforce family values!')


def get_pooh(server):
    for emoji in server.emojis:
        if emoji.name == 'pooh':
            return emoji

    print('No :pooh: emoji found!')
    return '💩'


@client.event
async def on_message(message):
    if message.channel.is_private:
        return

    if profanity.contains_profanity(message.content):
        await client.add_reaction(message, get_pooh(message.server))

@client.event
async def on_message_edit(before, after):
    if after.channel.is_private:
        return

    if profanity.contains_profanity(after.content):
        await client.add_reaction(after, get_pooh(after.server))
    elif not profanity.contains_profanity(after.content):
        await client.remove_reaction(after, get_pooh(after.server), after.server.me)

client.run(os.environ.get('DISCORD_TOKEN'))
