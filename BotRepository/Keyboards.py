from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink

class Keyboards:

    def get_post_type_keyboard():
        keyboard = (Keyboard(one_time=True, inline=False)
                    .add(Text("Реклама"))
                    .add(Text("Новость"))
                    .add(Text("Анекдот"))).get_json()
        return keyboard
    
    def get_language_keyboard():
        keyboard = (Keyboard(one_time=True, inline=False)
                    .add(Text("Английский"))
                    .add(Text("Русский"))).get_json()
        return keyboard
    
    def get_start_keyboard():
        keyboard = (Keyboard(one_time=True, inline=False)
                    .add(Text("Создать пост"))).get_json()
        return keyboard

    def error_keyboard():
        keyboard = (Keyboard(one_time=True, inline=False)
                    .add(Text("Начать"))).get_json()
        return keyboard 
    
    def subscribe_keyboard():
        keyboard = (Keyboard(inline=True)
                    .add(OpenLink("https://vk.com/club228616233", "Перейти на страницу сообщества"))
                    .add(Text("Я подписался", payload={"button":"subscribed"}))).get_json()
        
        return keyboard