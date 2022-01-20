import telebot
from telebot import types
from settings import TG_BOT_TOKEN

bot = telebot.TeleBot(TG_BOT_TOKEN)


def keyboard(where_call):  # функция вызова всех типов клавиатур
    keyboards = types.InlineKeyboardMarkup(row_width=1)
    if where_call == 'start':
        button_1 = types.InlineKeyboardButton(text='Меню', callback_data='menu')
        keyboards.add(button_1)
        return keyboards
    elif where_call == 'choice':
        button_2_1 = types.InlineKeyboardButton(text='Информация', callback_data='info')
        # button_2_2 = types.InlineKeyboardButton(text='Справка', callback_data='reference')
        keyboards.add(button_2_1)  # для кнопки "Справка добавить в список button_2_2
        return keyboards
    elif where_call == 'federal_district':  # Федеральные округа
        button_3_1 = types.InlineKeyboardButton(text='Центральный федеральный округ', callback_data='3_1_inline')
        button_3_2 = types.InlineKeyboardButton(text='Северо-Западный федеральный округ', callback_data='3_2_inline')
        button_3_3 = types.InlineKeyboardButton(text='Южный федеральный округ', callback_data='3_3_inline')
        button_3_4 = types.InlineKeyboardButton(text='Северо-Кавказский Федеральный округ', callback_data='3_4_inline')
        button_3_5 = types.InlineKeyboardButton(text='Приволжский федеральный округ', callback_data='3_5_inline')
        button_3_6 = types.InlineKeyboardButton(text='Уральский федеральный округ', callback_data='3_6_inline')
        button_3_7 = types.InlineKeyboardButton(text='Сибирский федеральный округ', callback_data='3_7_inline')
        button_3_8 = types.InlineKeyboardButton(text='Дальневосточный федеральный округ', callback_data='3_8_inline')
        button_3_back = types.InlineKeyboardButton(text='Назад', callback_data='3_back_inline')
        keyboards.add(button_3_1, button_3_2, button_3_3, button_3_4, button_3_5, button_3_6, button_3_7, button_3_8,
                      button_3_back)
        return keyboards
    elif where_call == 'central_federal_district':  # Центральный федеральный округ
        button_3_1_1 = types.InlineKeyboardButton(text='Белгородская область', callback_data='3_1_1_inline')
        button_3_1_2 = types.InlineKeyboardButton(text='Брянская область', callback_data='3_1_2_inline')
        button_3_1_3 = types.InlineKeyboardButton(text='Владимирская область', callback_data='3_1_3_inline')
        button_3_1_4 = types.InlineKeyboardButton(text='Воронежская область', callback_data='3_1_4_inline')
        button_3_1_5 = types.InlineKeyboardButton(text='Ивановская область', callback_data='3_1_5_inline')
        button_3_1_6 = types.InlineKeyboardButton(text='Калужская область', callback_data='3_1_6_inline')
        button_3_1_7 = types.InlineKeyboardButton(text='Костромская область', callback_data='3_1_7_inline')
        button_3_1_8 = types.InlineKeyboardButton(text='Курская область', callback_data='3_1_8_inline')
        button_3_1_9 = types.InlineKeyboardButton(text='Липецкая область', callback_data='3_1_9_inline')
        button_3_1_10 = types.InlineKeyboardButton(text='Орловская область', callback_data='3_1_10_inline')
        button_3_1_11 = types.InlineKeyboardButton(text='Рязанская область', callback_data='3_1_11_inline')
        button_3_1_12 = types.InlineKeyboardButton(text='Смоленская область', callback_data='3_1_12_inline')
        button_3_1_13 = types.InlineKeyboardButton(text='Тамбовская область', callback_data='3_1_13_inline')
        button_3_1_14 = types.InlineKeyboardButton(text='Тверская область', callback_data='3_1_14_inline')
        button_3_1_15 = types.InlineKeyboardButton(text='Тульская область', callback_data='3_1_15_inline')
        button_3_1_16 = types.InlineKeyboardButton(text='Ярославская область', callback_data='3_1_16_inline')
        button_3_1_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_1_1, button_3_1_2, button_3_1_3, button_3_1_4, button_3_1_5, button_3_1_6,
                      button_3_1_7, button_3_1_8, button_3_1_9, button_3_1_10, button_3_1_11, button_3_1_12,
                      button_3_1_13, button_3_1_14, button_3_1_15, button_3_1_16, button_3_1_back)
        return keyboards
    elif where_call == 'northwestern_federal_district':  # Северо-Западный федеральный округ
        button_3_2_1 = types.InlineKeyboardButton(text='Архангельская область', callback_data='3_2_1_inline')
        button_3_2_2 = types.InlineKeyboardButton(text='Вологодская область', callback_data='3_2_2_inline')
        button_3_2_3 = types.InlineKeyboardButton(text='Калининградская область', callback_data='3_2_3_inline')
        button_3_2_4 = types.InlineKeyboardButton(text='Ленинградская область', callback_data='3_2_4_inline')
        button_3_2_5 = types.InlineKeyboardButton(text='Мурманская область', callback_data='3_2_5_inline')
        button_3_2_6 = types.InlineKeyboardButton(text='Ненецкий автономный округ', callback_data='3_2_6_inline')
        button_3_2_7 = types.InlineKeyboardButton(text='Новгородская область', callback_data='3_2_7_inline')
        button_3_2_8 = types.InlineKeyboardButton(text='Псковская область', callback_data='3_2_8_inline')
        button_3_2_9 = types.InlineKeyboardButton(text='Республика Карелия', callback_data='3_2_9_inline')
        button_3_2_10 = types.InlineKeyboardButton(text='Республика Коми', callback_data='3_2_10_inline')
        button_3_2_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_2_1, button_3_2_2, button_3_2_3, button_3_2_4, button_3_2_5, button_3_2_6,
                      button_3_2_7, button_3_2_8, button_3_2_9, button_3_2_10, button_3_2_back)
        return keyboards
    elif where_call == 'southern_federal_district':  # Южный федеральный округ
        button_3_3_1 = types.InlineKeyboardButton(text='Астраханская область', callback_data='3_3_1_inline')
        button_3_3_2 = types.InlineKeyboardButton(text='Волгоградская область', callback_data='3_3_2_inline')
        button_3_3_3 = types.InlineKeyboardButton(text='Краснодарский край', callback_data='3_3_3_inline')
        button_3_3_4 = types.InlineKeyboardButton(text='Республика Адыгея', callback_data='3_3_4_inline')
        button_3_3_5 = types.InlineKeyboardButton(text='Республика Калмыкия', callback_data='3_3_5_inline')
        button_3_3_6 = types.InlineKeyboardButton(text='Ростовская область', callback_data='3_3_6_inline')
        button_3_3_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_3_1, button_3_3_2, button_3_3_3, button_3_3_4, button_3_3_5, button_3_3_6,
                      button_3_3_back)
        return keyboards
    elif where_call == 'north_caucasian_federal_district':  # Северо-Кавказский Федеральный округ
        button_3_4_1 = types.InlineKeyboardButton(text='Кабардино-Балкарская Республика', callback_data='3_4_1_inline')
        button_3_4_2 = types.InlineKeyboardButton(text='Карачаево-Черкесская Республика', callback_data='3_4_2_inline')
        button_3_4_3 = types.InlineKeyboardButton(text='Республика Дагестан', callback_data='3_4_3_inline')
        button_3_4_4 = types.InlineKeyboardButton(text='Республика Ингушетия', callback_data='3_4_4_inline')
        button_3_4_5 = types.InlineKeyboardButton(text='Республика Северная Осетия – Алания',
                                                  callback_data='3_4_5_inline')
        button_3_4_6 = types.InlineKeyboardButton(text='Ставропольский край', callback_data='3_4_6_inline')
        button_3_4_7 = types.InlineKeyboardButton(text='Чеченская Республика', callback_data='3_4_7_inline')
        button_3_4_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_4_1, button_3_4_2, button_3_4_3, button_3_4_4, button_3_4_5, button_3_4_6, button_3_4_7,
                      button_3_4_back)
        return keyboards
    elif where_call == 'volga_federal_district':  # Приволжский федеральный округ
        button_3_5_1 = types.InlineKeyboardButton(text='Кабардино-Балкарская Республика', callback_data='3_5_1_inline')
        button_3_5_2 = types.InlineKeyboardButton(text='Карачаево-Черкесская Республика', callback_data='3_5_2_inline')
        button_3_5_3 = types.InlineKeyboardButton(text='Республика Дагестан', callback_data='3_5_3_inline')
        button_3_5_4 = types.InlineKeyboardButton(text='Республика Ингушетия', callback_data='3_5_4_inline')
        button_3_5_5 = types.InlineKeyboardButton(text='Республика Северная Осетия – Алания',
                                                  callback_data='3_4_5_inline')
        button_3_5_6 = types.InlineKeyboardButton(text='Ставропольский край', callback_data='3_5_6_inline')
        button_3_5_7 = types.InlineKeyboardButton(text='Чеченская Республика', callback_data='3_5_7_inline')
        button_3_5_8 = types.InlineKeyboardButton(text='Кабардино-Балкарская Республика', callback_data='3_5_8_inline')
        button_3_5_9 = types.InlineKeyboardButton(text='Карачаево-Черкесская Республика', callback_data='3_5_9_inline')
        button_3_5_10 = types.InlineKeyboardButton(text='Республика Дагестан', callback_data='3_5_10_inline')
        button_3_5_11 = types.InlineKeyboardButton(text='Республика Ингушетия', callback_data='3_5_11_inline')
        button_3_5_12 = types.InlineKeyboardButton(text='Республика Северная Осетия – Алания',
                                                   callback_data='3_5_12_inline')
        button_3_5_13 = types.InlineKeyboardButton(text='Ставропольский край', callback_data='3_5_13_inline')
        button_3_5_14 = types.InlineKeyboardButton(text='Чеченская Республика', callback_data='3_5_14_inline')
        button_3_5_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_5_1, button_3_5_2, button_3_5_3, button_3_5_4, button_3_5_5, button_3_5_6, button_3_5_7,
                      button_3_5_8, button_3_5_9, button_3_5_10, button_3_5_11, button_3_5_12, button_3_5_13,
                      button_3_5_14, button_3_5_back)
        return keyboards
    elif where_call == 'ural_federal_district':  # Уральский федеральный округ
        button_3_6_1 = types.InlineKeyboardButton(text='Свердловская область', callback_data='3_6_1_inline')
        button_3_6_2 = types.InlineKeyboardButton(text='Курганская область', callback_data='3_6_2_inline')
        button_3_6_3 = types.InlineKeyboardButton(text='Тюменская область', callback_data='3_6_3_inline')
        button_3_6_4 = types.InlineKeyboardButton(text='Ханты-Мансийский автономный округ - Югра',
                                                  callback_data='3_6_4_inline')
        button_3_6_5 = types.InlineKeyboardButton(text='Челябинская область', callback_data='3_6_5_inline')
        button_3_6_6 = types.InlineKeyboardButton(text='Ямало-Ненецкий АО', callback_data='3_6_6_inline')
        button_3_6_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_6_1, button_3_6_2, button_3_6_3, button_3_6_4, button_3_6_5, button_3_6_6,
                      button_3_6_back)
        return keyboards
    elif where_call == 'siberian_federal_district':  # Сибирский федеральный округ
        button_3_7_1 = types.InlineKeyboardButton(text='Свердловская область', callback_data='3_7_1_inline')
        button_3_7_2 = types.InlineKeyboardButton(text='Курганская область', callback_data='3_7_2_inline')
        button_3_7_3 = types.InlineKeyboardButton(text='Тюменская область', callback_data='3_7_3_inline')
        button_3_7_4 = types.InlineKeyboardButton(text='Ханты-Мансийский автономный округ - Югра',
                                                  callback_data='3_7_4_inline')
        button_3_7_5 = types.InlineKeyboardButton(text='Челябинская область', callback_data='3_7_5_inline')
        button_3_7_6 = types.InlineKeyboardButton(text='Ямало-Ненецкий АО', callback_data='3_7_6_inline')
        button_3_7_7 = types.InlineKeyboardButton(text='Тюменская область', callback_data='3_7_7_inline')
        button_3_7_8 = types.InlineKeyboardButton(text='Ханты-Мансийский автономный округ - Югра',
                                                  callback_data='3_7_8_inline')
        button_3_7_9 = types.InlineKeyboardButton(text='Челябинская область', callback_data='3_7_9_inline')
        button_3_7_10 = types.InlineKeyboardButton(text='Ямало-Ненецкий АО', callback_data='3_7_10_inline')
        button_3_7_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_7_1, button_3_7_2, button_3_7_3, button_3_7_4, button_3_7_5, button_3_7_6, button_3_7_7,
                      button_3_7_8, button_3_7_9, button_3_7_10, button_3_7_back)
        return keyboards
    elif where_call == 'far_eastern_federal_district':  # Дальневосточный федеральный округ
        button_3_8_1 = types.InlineKeyboardButton(text='Амурская область', callback_data='3_8_1_inline')
        button_3_8_2 = types.InlineKeyboardButton(text='Еврейская автономная область', callback_data='3_8_2_inline')
        button_3_8_3 = types.InlineKeyboardButton(text='Забайкальский край', callback_data='3_8_3_inline')
        button_3_8_4 = types.InlineKeyboardButton(text='Камчатский край', callback_data='3_8_4_inline')
        button_3_8_5 = types.InlineKeyboardButton(text='Магаданская область', callback_data='3_8_5_inline')
        button_3_8_6 = types.InlineKeyboardButton(text='Приморский край', callback_data='3_8_6_inline')
        button_3_8_7 = types.InlineKeyboardButton(text='Республика Бурятия', callback_data='3_8_7_inline')
        button_3_8_8 = types.InlineKeyboardButton(text='Республика Саха (Якутия)', callback_data='3_8_8_inline')
        button_3_8_9 = types.InlineKeyboardButton(text='Сахалинская область', callback_data='3_8_9_inline')
        button_3_8_10 = types.InlineKeyboardButton(text='Хабаровский край', callback_data='3_8_10_inline')
        button_3_8_11 = types.InlineKeyboardButton(text='Чукотский автономный округ', callback_data='3_8_11_inline')
        button_3_8_back = types.InlineKeyboardButton(text='Назад', callback_data='3_1_back_inline')
        keyboards.add(button_3_8_1, button_3_8_2, button_3_8_3, button_3_8_4, button_3_8_5, button_3_8_6, button_3_8_7,
                      button_3_8_8, button_3_8_9, button_3_8_10, button_3_8_11, button_3_8_back)
        return keyboards


@bot.message_handler(commands=['start', 'help'], content_types=['text'])
def category(message):
    bot.reply_to(message,
                 'Добрый день. \n   Я электронный ассистент и помогу Вам найти необходимые данные. \n'
                 'Нажмите "Меню" для начала работы',
                 reply_markup=keyboard('start'))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'menu':  # основное меню
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пока доступно только получение методических рекомендаций',
                              reply_markup=keyboard('choice'))
    elif call.data == 'info':  # выбор федерального округа
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ', reply_markup=keyboard('federal_district'))
    elif call.data == '3_1_inline':  # ЦФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект', reply_markup=keyboard('central_federal_district'))
    elif call.data == '3_2_inline':  # СЗФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект',
                              reply_markup=keyboard('northwestern_federal_district'))
    elif call.data == '3_3_inline':  # ЮФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект', reply_markup=keyboard('southern_federal_district'))
    elif call.data == '3_4_inline':  # СКФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект',
                              reply_markup=keyboard('north_caucasian_federal_district'))
    elif call.data == '3_5_inline':  # ПФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект', reply_markup=keyboard('volga_federal_district'))
    elif call.data == '3_6_inline':  # УФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект', reply_markup=keyboard('ural_federal_district'))
    elif call.data == '3_7_inline':  # СФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект', reply_markup=keyboard('siberian_federal_district'))
    elif call.data == '3_8_inline':  # ДВФО
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный субъект',
                              reply_markup=keyboard('far_eastern_federal_district'))
    # обработчик кнопок "назад" пока реализован в таком виде, если найду более элегантный способ, то заменю.
    elif call.data == '3_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пока доступно только получение инфомрации об учебном заведении',
                              reply_markup=keyboard('choice'))
    elif call.data == '3_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пока доступно только получение инфомрации об учебном заведении',
                              reply_markup=keyboard('choice'))
    elif call.data == '3_1_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_2_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_3_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_4_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_5_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_6_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_7_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))
    elif call.data == '3_8_back_inline':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете федеральный округ',
                              reply_markup=keyboard('federal_district'))


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
# while True:
#     try:
#         bot.polling(none_stop=True, interval=0, timeout=0)
#     except:
#         time.sleep(10)  как вариант такой модуль использовать, только я пока не понял в чем разница
