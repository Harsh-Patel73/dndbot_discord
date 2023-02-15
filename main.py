import bot
import db

if __name__ == '__main__':
    db.createConnection()
    bot.run_discord_bot()
