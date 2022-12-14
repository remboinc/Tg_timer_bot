import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse


def wait(chat_id, time):
    secs_left = parse(time)
    start_timer = "Запускаю таймер"
    bot.send_message(chat_id, start_timer)
    message_id = bot.send_message(chat_id, secs_left)
    bot.create_countdown(parse(time), notify_progress, message_id=message_id, time=time)
    bot.create_timer(parse(time), choose, chat_id=chat_id)


def notify_progress(secs_left, message_id, time):
    time = parse(time)
    progressbar = f'Осталось {secs_left} секунд из {time}\n' \
                  f'{render_progressbar(time, secs_left)}'
    bot.update_message(tg_chat_id, message_id, progressbar)


def render_progressbar(total, iteration, prefix='', suffix='', length=13, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def choose(chat_id):
    time_is_over = "Время вышло"
    bot.send_message(chat_id, time_is_over)
    message = 'На сколько поставить таймер?'
    bot.send_message(chat_id, message)



if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")
    bot = ptbot.Bot(tg_token)

    bot.reply_on_message(wait)
    bot.run_bot()
