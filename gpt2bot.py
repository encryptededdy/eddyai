from telegram.ext import ApplicationBuilder, CommandHandler
import subprocess
from telegram import Update
from tiktokbot import TikTokVoice

gpt2tcThreads = 1
allowedChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!+-?,.' "

tik_tok_runner = TikTokVoice()


def filtertext(text):
    return ''.join(filter(lambda x: x in allowedChars, text.replace('\n', ' ').strip()))


def gpt2tc(text, modelSize, modelName):
    cleanInput = filtertext(text)
    output = subprocess.run(["gpt2tc", "-m", modelSize, "-f", modelName, "-T", str(
        gpt2tcThreads), "g", cleanInput], text=True, capture_output=True)
    if output.returncode == 0:
        gptoutput = output.stdout
        cutoutput = gptoutput[:gptoutput.find("<|endoftext|>")]
        return cutoutput
    else:
        return "Error"


async def hello(update, context):
    await update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


async def parse_to_query(update):
    split = update.message.text.split(' ', 1)
    return split[1] if len(split) > 1 else ''


async def austin(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_austinmedium.bin"),
        quote=True)


async def terran(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_terranmedium.bin"),
        quote=True)


async def sid(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_sidmedium.bin"),
        quote=True)


async def jono(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_jonomedium.bin"),
        quote=True)


async def lauren(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_laurensmall.bin"),
        quote=True)


async def thomas(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_thomassmall.bin"),
        quote=True)


async def yige(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_yigesmall.bin"),
        quote=True)


async def mohan(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_mohanmedium.bin"),
        quote=True)


async def edward(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_edwardmedium.bin"),
        quote=True)


async def generic(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_genericmedium.bin"),
        quote=True)


async def henry(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_henrysmall.bin"),
        quote=True)


async def logan(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "117M", "gpt2_logansmall.bin"),
        quote=True)

async def hive(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "774M", "gpt2_hive_2024Jan.bin"),
        quote=True)


async def hivelegacy(update, context):
    await update.message.reply_text(
        gpt2tc(parse_to_query(update), "345M", "gpt2_hive2medium.bin"),
        quote=True)


async def tiktok(update: Update, context):
    try:
        query = " ".join(update.message.text.split(" ")[1:])
        if (len(query) == 0):
            await update.message.reply_text("Please provide a query", quote=True)
            return

        if (len(query) > 400):
            await update.message.reply_text(
                "Query too long. Max 400 chars", quote=True)
            return

        tik_tok_runner.generate(query)
        # update.message.reply_voice sends as a file not a voice message for some reason so using the long format command
        await context.bot.send_voice(update.effective_chat.id, open('tiktok.webm', 'rb'), reply_to_message_id=update.message.message_id)
    except Exception as e:
        print(e)
        await update.message.reply_text("Something went wrong, sorry :(", quote=True)

key = ''
with open("telegramkey.txt", "r") as config:
    key = config.readlines()[0]


def main():

    application = ApplicationBuilder().token(key).build()

    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(CommandHandler('mohan', mohan))
    application.add_handler(CommandHandler('edward', edward))
    application.add_handler(CommandHandler('terran', terran))
    application.add_handler(CommandHandler('sid', sid))
    application.add_handler(CommandHandler('lauren', lauren))
    application.add_handler(CommandHandler('yige', yige))
    application.add_handler(CommandHandler('jono', jono))
    application.add_handler(CommandHandler('thomas', thomas))
    application.add_handler(CommandHandler('austin', austin))
    application.add_handler(CommandHandler('generic', generic))
    application.add_handler(CommandHandler('henry', henry))
    application.add_handler(CommandHandler('logan', logan))
    application.add_handler(CommandHandler('hive', hive))
    application.add_handler(CommandHandler('hivelegacy', hivelegacy))
    application.add_handler(CommandHandler('tiktok', tiktok))

    application.run_polling()


if __name__ == '__main__':
    main()
