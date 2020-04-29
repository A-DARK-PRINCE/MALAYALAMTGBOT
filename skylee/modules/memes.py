import random, re
import requests as r

from time import sleep
from typing import Optional, List
from requests import get
from random import randint

from telegram import Message, Update, Bot, User, ParseMode, MessageEntity
from telegram.ext import Filters, CommandHandler, MessageHandler, run_async
from telegram import TelegramError, Chat, Message
from telegram.error import BadRequest
from telegram.utils.helpers import mention_html, escape_markdown

from skylee.modules.helper_funcs.extraction import extract_user
from skylee.modules.helper_funcs.filters import CustomFilters
from skylee import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WALL_API, TOKEN
from skylee.modules.disable import DisableAbleCommandHandler

import skylee.modules.helper_funcs.fun_strings as fun

@run_async
def runs(update, context):
    update.effective_message.reply_text(random.choice(fun.RUN_STRINGS))


@run_async
def slap(update, context):
    args = context.args
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        slapped_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if slapped_user.username:
            user2 = "@" + escape_markdown(slapped_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(slapped_user.first_name,
                                                   slapped_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(context.bot.first_name, context.bot.id)
        user2 = curr_user

    temp = random.choice(fun.SLAP_TEMPLATES)
    item = random.choice(fun.ITEMS)
    hit = random.choice(fun.HIT)
    throw = random.choice(fun.THROW)

    repl = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)

@run_async
def punch(update, context):
    args = context.args
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        punched_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if punched_user.username:
            user2 = "@" + escape_markdown(punched_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(punched_user.first_name,
                                                   punched_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(context.bot.first_name, context.bot.id)
        user2 = curr_user

    temp = random.choice(fun.PUNCH_TEMPLATES)
    item = random.choice(fun.ITEMS)
    punch = random.choice(fun.PUNCH)

    repl = temp.format(user1=user1, user2=user2, item=item, punches=punch)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)



@run_async
def hug(update, context):
    args = context.args
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        hugged_user = context.bot.get_chat(user_id)
        user1 = curr_user
        if hugged_user.username:
            user2 = "@" + escape_markdown(hugged_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(hugged_user.first_name,
                                                   hugged_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "Awwh! [{}](tg://user?id={})".format(context.bot.first_name, context.bot.id)
        user2 = curr_user

    temp = random.choice(fun.HUG_TEMPLATES)
    hug = random.choice(fun.HUG)

    repl = temp.format(user1=user1, user2=user2, hug=hug)

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)


@run_async
def abuse(update, context):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun.ABUSE_STRINGS))

@run_async
def shrug(update, context):
    # reply to correct message
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun.SHGS))

@run_async
def decide(update, context):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun.DECIDE))

@run_async
def table(update, context):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun.TABLE))

@run_async
def cri(update, context):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun.CRI))

@run_async
def dice(update, context):
    context.bot.sendDice(update.effective_chat.id)

# untill library add api 4.8 support
@run_async
def dart(update, context):
    chat = update.effective_chat
    try:
       r.post(f"https://api.telegram.org/bot{TOKEN}/sendDice?chat_id={chat.id}&emoji='🎯'")
    except BadRequest:
        return

@run_async
def gbun(update, context):
    user = update.effective_user
    chat = update.effective_chat

    if update.effective_message.chat.type == "private":
       return
    if int(user.id) in SUDO_USERS or int(user.id) in SUPPORT_USERS:
       context.bot.sendMessage(chat.id, (random.choice(fun.GBUN)))

@run_async
def snipe(update, context):
    args = context.args
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError as excp:
        update.effective_message.reply_text("Please give me a chat to echo to!")     
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            context.bot.sendMessage(int(chat_id), str(to_send))        
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))             
            update.effective_message.reply_text("Couldn't send the message. Perhaps I'm not part of that group?")


# Bug reporting module for X00TD PORTS!

@run_async
def ports_bug(update, context):
    message = update.effective_message
    user = update.effective_user
    bug = message.text[len('/bug '):]
    chat = update.effective_chat

    PORT_GRP = [-1001297379754, -1001469684768]

    if not int(chat.id) in PORT_GRP:
        return

    if not bug:
        message.reply_text("Submitting empty bug report won't do anything!")
        return

    if bug:
        context.bot.sendMessage(-1001495581911, "<b>NEW BUG REPORT!</b>\n\n<b>Submitted by</b>: {}.\n\nDescription: <code>{}</code>.".format(mention_html(user.id, user.first_name), bug), parse_mode=ParseMode.HTML)
        message.reply_text("Successfully submitted bug report!")


__help__ = """
Some dank memes for ya all!

 × /shrug | /cri: Get shrug or (ToT)!
 × /decide: Randomly answers yes/no/maybe
 × /abuse: Abuses the retard!
 × /table: Flips a table...
 × /runs: Reply a random string from an array of replies.
 × /slap: Slap a user, or get slapped if not a reply.
 × /dice: Sends a dice which returns randomly from 1 to 6!
 × /dart: Send a dart and see if you hit bullseye.
 × /warm: Hug a user warmly, or get hugged if not a reply.
 × /punch: Punch a user, or get punched if not a reply.
"""

__mod_name__ = "Memes"

SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
SNIPE_HANDLER = CommandHandler("snipe", snipe, pass_args=True, filters=CustomFilters.sudo_filter)
ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
PORT_BUG_HANDLER = CommandHandler("bug", ports_bug)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True)
PUNCH_HANDLER = DisableAbleCommandHandler("punch", punch, pass_args=True)
HUG_HANDLER = DisableAbleCommandHandler("warm", hug, pass_args=True)
GBUN_HANDLER = CommandHandler("gbun", gbun)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
DICE_HANDLER = DisableAbleCommandHandler("dice", dice)
DART_HANDLER = DisableAbleCommandHandler("dart", dart)
CRI_HANDLER = DisableAbleCommandHandler("cri", cri)

dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SNIPE_HANDLER)
dispatcher.add_handler(PORT_BUG_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PUNCH_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(GBUN_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(DICE_HANDLER)
dispatcher.add_handler(DART_HANDLER)
dispatcher.add_handler(CRI_HANDLER)
