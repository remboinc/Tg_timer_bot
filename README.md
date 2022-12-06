# Telegram timer bot
A simple telegram bot that counts time and displays a progressbar.
Bot will inform you if the time is up and offer to start a new timer.
    
   
    Запускаю таймер
    
    Осталось 0 секунд из 5
     |░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0.0%
    
    Время вышло
    
    На сколько поставить таймер?

## How to install
Clone the project:

    git clone https://github.com/remboinc/Tg_timer_bot

Create a virtual environment on directory project:

    python3.10 -m venv env
    
Start virtual environment:
    
    . env/bin/activate
    
Create an `.env` file and declare two global environment variables:

    TG_CHAT_ID=392681111
    TG_TOKEN=3403981261:AAGfL5Nyv3WPmEs1hhwe87ehewienkjk

Get a token from the [Bot Father](https://t.me/BotFather) and write it to a variable `TG_TOKEN`. 
Find out your telegram-id, for example, using [IDBot](https://t.me/username_to_id_bot) and enter it into a variable `TG_CHAT_ID`.
