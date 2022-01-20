import telebot

from telebot import types

bot = telebot.TeleBot('1939461215:AAFcgouq1aUfvtHi6PZ0jUKsj67raIby9_M')


def keyboard(where_call):  # функция вызова всех типов клавиатур
    keyboards = types.InlineKeyboardMarkup(row_width=1)
    if where_call == 'start':
        button_1 = types.InlineKeyboardButton(text='Меню', callback_data='menu')
        keyboards.add(button_1)
        return keyboards
    elif where_call == 'choice':
        button_2_1 = types.InlineKeyboardButton(text='Методические рекомендации', callback_data='MetRek')
        button_2_2 = types.InlineKeyboardButton(text='Что-то, чего нет)', callback_data='reference')
        keyboards.add(button_2_1, button_2_2)  # для кнопки "Справка добавить в список button_2_2
        return keyboards

    elif where_call == 'Subs':  # Субсидии
        button_3_1 = types.InlineKeyboardButton(text='Е1 Дети с ОВЗ', callback_data='3_1_inline')
        button_3_2 = types.InlineKeyboardButton(text='Е1 Точка роста', callback_data='3_2_inline')
        button_3_3 = types.InlineKeyboardButton(text='Е1 Кванториум', callback_data='3_3_inline')
        button_3_4 = types.InlineKeyboardButton(text='Е2 ЦОД', callback_data='3_4_inline')
        button_3_5 = types.InlineKeyboardButton(text='Е2 РМЦ', callback_data='3_5_inline')
        button_3_6 = types.InlineKeyboardButton(text='Е2 Физкультура и спорт', callback_data='3_6_inline')
        button_3_7 = types.InlineKeyboardButton(text='Е2 Новые места ДОД', callback_data='3_7_inline')
        button_3_8 = types.InlineKeyboardButton(text='Е4 ЦОС', callback_data='3_8_inline')
        button_3_9 = types.InlineKeyboardButton(text='Е4 Эксперимент по ЦОС', callback_data='3_9_inline')
        button_3_10 = types.InlineKeyboardButton(text='Е4 ИТ-куб', callback_data='3_10_inline')
        button_3_11 = types.InlineKeyboardButton(text='Е6 ЦОПП', callback_data='3_11_inline')
        button_3_12 = types.InlineKeyboardButton(text='Е6 Мастерские', callback_data='3_12_inline')
        button_3_back = types.InlineKeyboardButton(text='Назад', callback_data='3_back_inline')
        keyboards.add(button_3_1, button_3_2, button_3_3, button_3_4, button_3_5, button_3_6, button_3_7, button_3_8,
                      button_3_9, button_3_10, button_3_11, button_3_12, button_3_back)
        return keyboards


@bot.message_handler(commands=['start', 'help'], content_types=['text'])
def category(message):
    bot.reply_to(message,
                 'Добрый день. \n  Я электронный ассистент и помогу Вам найти необходимые данные. \n'
                 'Нажмите "Меню" для начала работы',
                 reply_markup=keyboard('start'))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'menu':  # основное меню
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пока доступно только получение методических рекомендаций',
                              reply_markup=keyboard('choice'))
    elif call.data == 'MetRek':  # выбор федерального округа
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Выберете субсидию', reply_markup=keyboard('Subs'))

    elif call.data == 'reference':  # ниче нет
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='сказали же, ничего нет, давай сначала',
                              reply_markup=keyboard('menu'))

    elif call.data == '3_1_inline':  # Е1 Дети с ОВЗ
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'МР Дети с ОВЗ ДГ-2337_07 от 07.12.2021.pdf', 'rb'))
    elif call.data == '3_2_inline':  # Е1 Точка роста
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1913_02_20211101_ТР.pdf', 'rb'))
    elif call.data == '3_3_inline':  # Е1 Кванториум
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1914_02_20211101_ШК.pdf', 'rb'))
    elif call.data == '3_4_inline':  # Е2 ЦОД
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ДГ-2054_06 от 19.11.2021_ЦОД.pdf', 'rb'))
    elif call.data == '3_5_inline':  # Е2 РМЦ
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'КД_РМЦ 1.pdf', 'rb'))
    elif call.data == '3_6_inline':  # Е2 Физкультура и спорт
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1920_06 от 02.11.2021 Физкультура и спорт.pdf', 'rb'))
    elif call.data == '3_7_inline':  # Е2 Новые места ДОД
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'Методрекомендации по НМ (октябрь 2021 года).pdf', 'rb'))
    elif call.data == '3_8_inline':  # Е4 ЦОС
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1968_04_20211109_ЦОС МР.pdf', 'rb'))
    elif call.data == '3_9_inline':  # Е4 Эксперимент по ЦОС
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1983_04_20211110_ЦОС эксп МР.pdf', 'rb'))
    elif call.data == '3_10_inline':  # Е4 ИТ-куб
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'ТВ-1984_04_20211110_ИТ-Куб МР.pdf', 'rb'))
    elif call.data == '3_11_inline':  # Е6 ЦОПП
        bot.send_document(chat_id=call.message.chat.id, document=open(
            'C:/Users/savchuk.ys/YandexDisk-yussavchuk/_ФНФРО/Методические рекомендации/2022/'
            'Метод. рекомендации_ЦОПП_2021.pdf', 'rb'))
    elif call.data == '3_12_inline':  # Е6 Мастерские
        document_12 = '../guidelines/Методические_рекомендации_2022_2024_Е6_мастерские.pdf'
        bot.send_document(chat_id=call.message.chat.id, document=open(document_12, 'rb'))
        if call.data == '3_back_inline':  # Назад
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Пока доступно только получение методических рекомендаций',
                                  reply_markup=keyboard('choice'))

        if __name__ == "__main__":
            bot.polling(none_stop=True, interval=0)
            # while True:
            #     try:
            #         bot.polling(none_stop=True, interval=0, timeout=0)
            #     except:
            #         time.sleep(10)  как вариант такой модуль использовать, только я пока не понял в чем разница
