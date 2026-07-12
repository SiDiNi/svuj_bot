from urllib.parse import quote

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


seller_username = "SVUJYK_11"

mix_master = "Здарова! Я выбрал это:\n• Mix/Master - 1,5к ₽"
presets = "Здарова! Я выбрал это:\n• Пресеты/Presets - 500 ₽"
lern = "Здарова! Я выбрал это:\n• Уроки сведения - 3к ₽"
gost = "Здарова! Я выбрал это:\n• Гострайт - 700 ₽"

encoded_text1 = quote(mix_master)
encoded_text2 = quote(presets)
encoded_text3 = quote(lern)
encoded_text4 = quote(gost)

url1 = f"https://t.me/{seller_username}?text={encoded_text1}"
url2 = f"https://t.me/{seller_username}?text={encoded_text2}"
url3 = f"https://t.me/{seller_username}?text={encoded_text3}"
url4 = f"https://t.me/{seller_username}?text={encoded_text4}"


class InlineKeyboard:
    @staticmethod
    def inline_menu():
        builder = InlineKeyboardBuilder()
        our_services_button = InlineKeyboardButton(
            text="наши услуги", callback_data="services"
        )
        about_me_button = InlineKeyboardButton(text="обо мне", callback_data="about_me")
        builder.add(our_services_button, about_me_button)
        builder.adjust(1, 1, 1)
        return builder.as_markup()

    @staticmethod
    def our_services():
        builder = InlineKeyboardBuilder()
        mix_master_button = InlineKeyboardButton(
            text="• Mix/Master - 1,5к ₽", url=url1, callback_data="mix_master"
        )
        builder.add(mix_master_button)
        return builder.as_markup()

    @staticmethod
    def other_services():
        builder = InlineKeyboardBuilder()
        presets_button = InlineKeyboardButton(
            text="• Пресеты/Presets - 500 ₽", url=url2, callback_data="presets"
        )
        training_button = InlineKeyboardButton(
            text="• Уроки сведения - 3к ₽", url=url3, callback_data="training"
        )
        state_website_button = InlineKeyboardButton(
            text="• Гострайт - 700 ₽", url=url4, callback_data="state_website"
        )
        back_button = InlineKeyboardButton(text="назад", callback_data="back_other")
        builder.add(presets_button, training_button, state_website_button, back_button)
        builder.adjust(1, 1, 1)
        return builder.as_markup()

    @staticmethod
    def back():
        builder = InlineKeyboardBuilder()
        back_button = InlineKeyboardButton(text="назад", callback_data="back")
        builder.add(back_button)
        return builder.as_markup()

    @staticmethod
    def buy():
        builder = InlineKeyboardBuilder()
        buy = InlineKeyboardButton(text="купить!", callback_data="buy")
        builder.add(buy)
        return builder.as_markup()
