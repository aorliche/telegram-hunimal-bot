import telebot

token = open('HunimalNumbersWizard.token', 'r').readline().strip()
bot = telebot.TeleBot(token)

dec = []
hun = []
digits = []

with open('decimal.txt', 'r') as f:
    for line in f:
        dec.append(line.strip().lower())

with open('hun.txt', 'r') as f:
    for line in f:
        hun.append(line.strip().lower())

for i in range(101):
    digits.append(f" {i} ")

def get_numbers(message):
    txt = message.text
    txt = txt.replace('-', '').replace('\n',' ').lower()
    nums = []
    for i in range(len(dec)):
        if txt.find(dec[i].replace('-', '')) != -1:
            nums.append(i)
    for i in range(len(digits)):
        if txt.find(digits[i]) != -1:
            nums.append(101 + i)
    return nums

def has_numbers(message):
    return len(get_numbers(message)) > 0

def translate_numbers(message):
    nums = get_numbers(message)
    res = ""
    for n in nums:
        if n < 101:
            res += dec[n] + " is " + hun[n] + "\n"
        else:
            res += digits[n - 101].strip() + " is " + hun[n - 101] + "\n"
    return res

@bot.message_handler(func=has_numbers)
def echo_numbers(message):
    bot.reply_to(message, translate_numbers(message))

bot.infinity_polling()

'''
class Message:
    def __init__(self, text):
        self.text = text

print(translate_numbers(Message('one')))
print(translate_numbers(Message(' 1 ')))
print(translate_numbers(Message('ninety-nine one hundred')))
print(translate_numbers(Message('one hundred two hundered')))
print(translate_numbers(Message('ninety nine')))
print(translate_numbers(Message(' 75 ')))
print(has_numbers(Message('a random message')))
print(has_numbers(Message('a random message 5\n')))
print(translate_numbers(Message('a random message 5\n')))
'''
