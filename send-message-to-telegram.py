import telegram
import asyncio
import mysql.connector
import datetime

async def send_message_to_telegram_group(group_id, bot_token, message):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=group_id, text=message)

def query_database(query, data=None):
    # Connect to the database
    conn = mysql.connector.connect(
        host="xxx",
        user="xxx",
        password="xxx",
        database="xxx"
    )
    
    # Create a cursor and execute the query
    cursor = conn.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    
    # Fetch the results of the query
    results = cursor.fetchall()
    
    # Clean up and close the connection
    cursor.close()
    conn.close()
    
    return results

def send_birthday_greeting():
    # Get the current date
    now = datetime.datetime.now()
    today = now.date()
    
    # Query the database for users with a birthday that matches the current month and day
    query = "SELECT name FROM users WHERE MONTH(birthday) = %s AND DAY(birthday) = %s;"
    data = (now.month, now.day)
    results = query_database(query, data)
    
    # Build the message to send to the group
    if len(results) == 0:
        message = "🎂🤖 Good morning. Today is " + str(today) + " and no birthdays today."
    else:
        message = "🎂🤖🥳 \n Happy birthday to: \n"
        for result in results:
            message += "🌟 {}\n".format(result[0])
        message += "\n 😇  We wish you a happy birthday. \n 📅  Today is " + str(today)

    # Send the message to the Telegram group
    group_id = -11223344  # replace this with your group id
    bot_token = "bot_token_id"  # replace this with your bot token
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_to_telegram_group(group_id, bot_token, message))

# Call the send_birthday_greeting function
send_birthday_greeting()
