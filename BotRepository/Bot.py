from vkbottle.bot import Bot, Message
from Config import Config
from States import States
from Validations import Validations
from Keyboards import Keyboards
from MachineLearningRepository.MLCreatingPostScript import GeneratePost

bot = Bot(token=Config.token)

storage = {}

@bot.on.message(text="Начать")
@bot.on.message(payload={"button":"subscribed"})
async def start(message: Message):
    is_member = await bot.api.groups.is_member(group_id = 228616233, user_id = message.from_id)

    hello_text = Config.hello_text
    if is_member:
        keyboard = Keyboards.get_start_keyboard()
        await bot.state_dispenser.set(message.peer_id, States.START_INPUT)
        await message.answer(message = hello_text, keyboard = keyboard)
    else:
        keyboard = Keyboards.subscribe_keyboard()
        await message.answer("Для создания поста подпишитесь на группу", keyboard = keyboard)
    
@bot.on.message(state=States.START_INPUT)
async def start(message: Message):
    await bot.state_dispenser.set(message.peer_id, States.POST_TYPE_INPUT)
    await message.answer(message = "Напишите, про что должен быть пост. Описания обязано быть осмысленным и четким. Чем подробнее описание, тем лучше")

@bot.on.message(state=States.POST_TYPE_INPUT)
async def post_type_handler(message: Message):
    keyboard = Keyboards.get_language_keyboard()
    storage["post_description"] = message.text
    await bot.state_dispenser.set(message.peer_id, States.LANGUAGE_INPUT)
    await message.answer(message = "Введите язык поста", keyboard = keyboard)

@bot.on.message(state=States.LANGUAGE_INPUT)
async def language_handler(message: Message):
    keyboard = Keyboards.get_language_keyboard()
    if Validations.language_is_valid(message.text):
        storage["language"] = message.text
        await bot.state_dispenser.set(message.peer_id, States.COUNT_OF_SYMBOLS_INPUT)
        await message.answer(message = "Введите количество слов в посте")
    else:
        await message.answer(message = "Некорректный ввод, введите язык еще раз", keyboard = keyboard)

@bot.on.message(state=States.COUNT_OF_SYMBOLS_INPUT)
async def count_of_symbols_handler(message: Message):
    if Validations.count_of_symbols_is_valid(message.text):
        storage["max_length"] = message.text
        await bot.state_dispenser.delete(message.peer_id)
        await message.answer("Текст генерируется...")
        post = GeneratePost(storage["post_description"], storage["language"], storage["max_length"]).create_post()
        await message.answer(post)
        storage.clear()
        keyboard = Keyboards.get_start_keyboard()
        await message.answer("Спасибо за то, что используете нас!", keybaord = keyboard)
    else:
        await message.answer(message = "Некорректный ввод, введите количество символов еще раз")

@bot.on.message()
async def nothing_handler(message: Message):
    is_member = await bot.api.groups.is_member(group_id = 228616233, user_id = message.from_id)

    if is_member:
        keyboard = Keyboards.get_start_keyboard()
        await bot.state_dispenser.set(message.peer_id, States.START_INPUT)
        await message.answer(message = "Для создания поста нажмите на кнопку 'Создать пост'!", keyboard = keyboard)
    else:
        keyboard = Keyboards.subscribe_keyboard()
        await message.answer("Для создания поста подпишитесь на группу", keyboard = keyboard)

bot.run_forever()