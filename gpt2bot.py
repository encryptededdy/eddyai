from telegram.ext import Updater, CommandHandler
import subprocess

gpt2tcThreads = 1
allowedChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!+-?,.' "

def filtertext(text):
    return ''.join(filter(lambda x: x in allowedChars, text.replace('\n', ' ').strip()))

def gpt2tc(text, modelSize, modelName):
    cleanInput = filtertext(text)
    output = subprocess.run(["gpt2tc", "-m", modelSize, "-f", modelName, "-T", str(gpt2tcThreads), "g", cleanInput], text=True, capture_output=True)
    if output.returncode == 0:
        gptoutput = output.stdout
        cutoutput = gptoutput[:gptoutput.find("<|endoftext|>")]
        return cutoutput
    else:
        return "Error"

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def parse_to_query(update):
    split = update.message.text.split(' ', 1)
    return split[1] if len(split) > 1 else ''

def austin(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_austinmedium.bin"),
        quote = True)

def terran(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_terranmedium.bin"),
        quote = True)

def sid(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_sidmedium.bin"),
        quote = True)

def jono(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_jonomedium.bin"),
        quote = True)

def lauren(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_laurensmall.bin"),
        quote = True)

def thomas(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_thomassmall.bin"),
        quote = True)

def yige(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_yigesmall.bin"),
        quote = True)

def mohan(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_mohanmedium.bin"),
        quote = True)

def edward(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_edwardmedium.bin"),
        quote = True)

def generic(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_genericmedium.bin"),
        quote = True)

def henry(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_henrysmall.bin"),
        quote = True)

def logan(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_logansmall.bin"),
        quote = True)

def hive(update, context):
    update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_hivemedium.bin"),
        quote = True)

key = ''
with open ("telegramkey.txt", "r") as config:
    key = config.readlines()[0]

updater = Updater(key, use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('mohan', mohan))
updater.dispatcher.add_handler(CommandHandler('edward', edward))
updater.dispatcher.add_handler(CommandHandler('terran', terran))
updater.dispatcher.add_handler(CommandHandler('sid', sid))
updater.dispatcher.add_handler(CommandHandler('lauren', lauren))
updater.dispatcher.add_handler(CommandHandler('yige', yige))
updater.dispatcher.add_handler(CommandHandler('jono', jono))
updater.dispatcher.add_handler(CommandHandler('thomas', thomas))
updater.dispatcher.add_handler(CommandHandler('austin', austin))
updater.dispatcher.add_handler(CommandHandler('generic', generic))
updater.dispatcher.add_handler(CommandHandler('henry', henry))
updater.dispatcher.add_handler(CommandHandler('logan', logan))
updater.dispatcher.add_handler(CommandHandler('hive', hive))

updater.start_polling()
updater.idle()
