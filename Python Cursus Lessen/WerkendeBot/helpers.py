from upsidedown import ud_letters

USERNAME = ""
TOKEN = ""


def reply_to_self(client, user):
  id = user

  def reply_to_self_impl(func):

    @client.event
    async def on_message(message):
      if str(
          message.author.id) != str(id) or message.channel.name != 'bot-spam':
        return
      reply = func(message)
      if reply != None and reply != "":
        await message.channel.send(reply)

    return on_message

  return reply_to_self_impl


def reply_to_all(client):

  def reply_to_all_impl(func):

    @client.event
    async def on_message(message):
      if message.author == client.user:
        return
      if message.author.bot:
        return
      if message.channel.name != 'bot-spam':
        return
      reply = func(message)
      if reply != None and reply != "":
        await message.channel.send(reply)

    return on_message

  return reply_to_all_impl


# Source: https://github.com/Druyv/AussieBot/blob/master/src/upsidedown.py
def upside_down(message):
  result = ''
  for letter in message:
    if letter in ud_letters:
      result += ud_letters[letter]
    else:
      result += letter
  return result[::-1]
