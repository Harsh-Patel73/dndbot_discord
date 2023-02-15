import discord
import responses


async def send_message(message, user_message, is_private, server_id):

    try: 
        response = responses.handle_response(user_message, server_id)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTA2NDcyMTIzNTg4OTYzMTI1NA.GyJRKn.QuqG_KfQ6wExz8V6jMfSiq6eflh8cuVU_u9lgI'
    discord.Permissions = 1634235578432
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        server_id = str(message.guild.id)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False, server_id = server_id)
        else:
            await send_message(message, user_message,is_private=False, server_id = server_id)


    client.run(TOKEN)


