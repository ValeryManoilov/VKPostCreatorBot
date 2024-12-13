import vk_api

class Validations:

    def post_type_is_valid(post_type):
        post_types = ["Новость", "Реклама"]
        if post_type in post_types:
            return True
        return False
    
    def count_of_symbols_is_valid(count):
        result = False
        try:
            int(count)
            result = True
        except:
            result = False
        finally:
            return result
    
    def language_is_valid(language):
        languages = ["Русский", "Английский"]
        if language in languages:
            return True
        return False