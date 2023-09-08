from bs4 import BeautifulSoup
import pandas as pd
import chardet
import requests
import os
def get_htm(url):
    
    d = requests.get(url)
    # print(d.content)
    return d.content


def htm_(if_file: bool,data: str,zamena:bool|None=True,):
    def nane(value):
        if type(value)!=list:
            value = value if value!='nan' else ''
            return value
        else:
            for i in range(len(value)):
                value[i] = value[i] if value[i]!='nan' else ''
            return value
        
    if if_file == True:
        if os.path.exists(data):
            with open(data, 'rb') as file:
                result = chardet.detect(file.read())
                file.close()
            print(result)
                
            encoding = result['encoding']

            with open(data, 'r', encoding=encoding) as file:
                html_content = file.read()
            file.close()
    else:
        html_content = data
    # # Загрузите HTML-файл
    # with open('1.htm', 'r', encoding='utf-8') as file:
    #     html_content = file.read()

    # Создайте объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлечение текста
    # text = soup.get_text()

    # Используйте метод find_all, чтобы найти все таблицы на странице
    tables = soup.find_all('table')

    # Преобразуйте каждую таблицу в DataFrame и сохраните их в список
    # dataframes = []
    for table in tables:
        df = pd.read_html(str(table))[0]  # Преобразование таблицы в DataFrame
        # dataframes.append(df)
    # print(dataframes)
# 
    # # Извлечение таблицы (если она есть)
    # table = soup.find('table')  # Предполагается, что в HTML есть только одна таблица
    # table = dataframes[num_of_dat]

    if zamena:
        # Преобразование таблицы в объект DataFrame с помощью pandas
        df = pd.read_html(str(table))[0]
        # df.fillna('', inplace=True)
        # dfdict = dict(df)
        k_table = 0
        df1day,df2day = '',''
        spl=22
        spl2=18
        df1 = df.iloc[1:spl2].copy()
        df2 = df.iloc[spl:].copy()
        df1dict = dict(df1)
        df2dict = dict(df2)
        for i in df1dict.get(0):
            df1day+=nane(str(i))
        df1day = df1day.split('ДНИ')[1]
        # print()
        for i in df2dict.get(0):
            df2day+=nane(str(i))
        df2day = df2day.split('ДНИ')[1]
        # print(f"Первая часть: {df1day}")
        # print(df1)
        # print(f"\nВторая часть: {df2day}")
        # print(df2)
        k_table = 2

            # Выводим новые DataFrame
            
            # print(dict(df2))
        # Теперь df содержит данные из таблицы

        # Вывод текста и таблицы (если есть)
        # print(text)

        # if table:
        #     print(df)
            # new_df = df.copy()

        # print(df.info())
        
        # print(x,y)
        # y -= 1
        # x -= 1
        # print(x,y)
        # for i in range(x):
        #     for j in range(y):
        #         temp = df[i][j]
        #         # print(temp,type(temp),str(temp),type(str(temp)))
        #         df.at[j,str(i)] = temp if str(temp)!= 'nan' or temp!= pd.Float64Dtype else ''

        # for i in new_df:
        #     for j in new_df[i]:
        #         new_df.at[i, j] = j
                # df[i][j] = j if str(j)!= 'nan' else ''
                # print(j if str(j)!= 'nan' else '')
        # pd.concat(df,axis=1)
        # print('IFMIWEFJI(WFJNIUHFIWUHFIFHW*IFUWG*G*FW)')

        # new_df['Курс'] = [float(i[:-2])for i in list(new_df["Курс"]) ]

        

        
        def f(df_):
            zero_index = df_.index[0]
            last_index = df_.index[-1]
            dfdict_ = dict(df_)
            def start_with():
                for i in range(zero_index, last_index):
                    # print(dfdict_[0][i])
                    if dfdict_[0][i] == 'ДНИ':
                        start = i-zero_index+1
                # print('star with:',start)
                return start
            spliti = start_with()
            df_ = df_[spliti-1:]
            # print(df_)
            # dfdict_ = dict(df_)
            all = {}
            group_list = []
            zero_index = df_.index[0]
            last_index = df_.index[-1]
            start_ = start_with()
            # print(start_)
            y,x = df_.shape
            # print(x,y)
            # print(zero_index, last_index)
            # dfdict_ = dict(df_)
            # print(dfdict_)
            # print(len(dfdict_))
            # return 0
            bans = ['курс','Расписание']
            for i in range(0,x,2):
                # print(dfdict_[i],dfdict_[i+1])
                num = 0
                group_ = [[] for _ in range(y//2)]
                group = ''
                for j in range(zero_index,last_index+2):
                    # try:
                    num+=1
                    # print(nane(str(dfdict_[i][j])),nane(str(dfdict_[i+1][j])))
                    if num == start_:
                        # print(dfdict_[i])
                        group = nane(str(dfdict_[i][j]))
                        # print(f'group{j}=',group)
                        if group == 'ДНИ':
                            break
                        # print(group)
                        group_list.append(group)
                        # print('group_list.append(group)')
                        # group_.append(group)

                    elif num % 2 == 0:
                        lesson,cab = nane(str(dfdict_[i][j])),nane(str(dfdict_[i+1][j]))
                        # print(num//2, lesson, cab)
                        # for ban in bans:
                        if 'Расписание' in lesson or 'Расписание' in cab or 'курс' in lesson or 'курс' in cab:
                            continue
                        # print(lesson, cab)
                        group_[num//2-1].append(lesson)
                        group_[num//2-1].append(cab)
                        # print('group_list.append(lesson,cab)')

                    else:
                        teacher,adres =  nane(str(dfdict_[i][j])),nane(str(dfdict_[i+1][j]))
                        # print(' ', teacher, adres)
                        if 'Расписание' in teacher or 'Расписание' in adres or 'курс' in teacher or 'курс' in adres:
                            continue
                        group_[num//2-1].append(teacher)
                        group_[num//2-1].append(adres)
                        # print('group_list.append(teacher,adres)')
                    #     # print()
                    # print(num,x,j)
                    if num == last_index-zero_index+1:
                        # print(group)
                        all[group] = group_
                        break
                        # print('all[group] = group_')
                    # # except Exception as e:
                    # #     print(e)
                    #     # print("EWKOFKJIOWFJIWFJI")
            # print(all)
            # print(all,group_list,sep='\n\n')
            return all
        # print(df1dict)
        # print(df2dict)
        if k_table == 2:
            all_df = {}
            all_df[df1day]=f(df1)
            all_df[df2day]=f(df2)
            # print(df1day,df2day)
            return all_df
        elif k_table == 1:
            return f(df)

        
import datetime
from telebot import *
first_kurs = 'https://kasict.ru/students/schedule/files/Raspisanie_1kurs_2020_21.htm'
other_kurs = 'https://kasict.ru/students/schedule/files/Raspisanie_2_3_4kurs_2020_21.htm'
zamena = 'https://kasict.ru/students/schedule/files/zamena.htm'
bot = TeleBot('6467766586:AAGkS1RA3oF8ero9EZGfbfRc1rLnHwENhHg')
# Получаем текущую дату
today = datetime.now()
# Преобразуем день недели в текст
day_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
for i in range(len(day_of_week)):
    day_of_week[i] = day_of_week[i].upper()
today_ru = day_of_week[today.weekday()]
print(f"Сегодня {today.day} {today.strftime('%B %Y года')}, {today_ru}")
zvonki = '''
1: <code>8:00 - 8:45</code>
    <code>8:50 - 9:35</code>
===================
2: <code>9:45 - 10:30</code>
    <code>10:35 - 11:20</code>
===================
3: <code>11:50 - 12:35</code>
    <code>12:40 - 13:25</code>
===================
4: <code>13:35 - 14:20</code>
    <code>14:25 - 15:10</code>
===================
5: <code>15:20 - 16:05</code>
    <code>16:10 - 16:55</code>
===================
6: <code>17:05 - 17:50</code>
    <code>17:55 - 18:40</code>
    '''

# data = get_htm(zamena)
# itog = htm_(False, data,zamena=True)
# print(itog[today_ru])
def addp(o1,o2,o3,o4,o5,result):
    return f'{result}\n{o1}<code>||</code> <code>{o2} {o3}</code>\n<code> ||</code><code>{o4} {o5}</code>\n==========--------------'
# def addp2(o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,result):
#     [
#         [f'{result}'],
#         []
#     ]
#     return f'{result}\n{o1} {o2} | {o3}||{o6} | {o7}\n  {o4} | {o5}|||{o8} | {o9}\n=========='

def center_text(text, width):
    return text.center(width)

@bot.message_handler(commands=['start'])
def start(message):
    chatik = message.chat.id
    start = 'Здравствуйте! Этот Telegram-бот предоставляет вам актуальное расписание вашей учебной группы на текущий и следующий учебные дни.\nПросто отправьте мне название вашей группы, например, <code>ИБ 23-1</code> (регистр букв не важен).\nКроме того, вы можете узнать расписание звонков, отправив команду /zvonok.'
    bot.send_message(chatik, text=start,parse_mode='html')

@bot.message_handler(commands=['звонки','zvonok','звонок','zvonki'])
def zvonk(message):
    chatik = message.chat.id
    bot.send_message(chatik, text=zvonki,parse_mode='html')

@bot.message_handler(func=lambda m: True)
def botik(message):
    try:
        chatik = message.chat.id
        global day_of_week,today
        today_ru_ = day_of_week[today.weekday()]
        data = get_htm(zamena)
        itog = htm_(False, data,zamena=True)
        tomorow_ru_ = ''
        for i in range(6):
            if itog.get(day_of_week[i])!=None and day_of_week[i]!=today_ru_:
                tomorow_ru_ = day_of_week[i]
                # print(tomorow_ru_)
        if tomorow_ru_!='':
            result = f'<code>{today_ru_}, </code><code>{message.text.upper()}</code>\n===================='
            result2 = f'<code>{tomorow_ru_}, </code><code>{message.text.upper()}</code>\n===================='
            for i in range(len(itog[today_ru_][message.text.upper()])):
                # print(len(itog[today_ru_][message.text.upper()]))
                j = itog[today_ru_][message.text.upper()]
                j2 = itog[tomorow_ru_][message.text.upper()]
                result = addp(i+1,j[i][0],j[i][1],j[i][2],j[i][3],result)
                result2 = addp(i+1,j2[i][0],j2[i][1],j2[i][2],j2[i][3],result2)
                # print(result_list)
                # print(i,j[i][0],j[i][2],'\n ',j[i][1],j[i][3],'\n==========')
                # center_text(result,20)
            bot.send_message(chatik, text=result,parse_mode='html')
            bot.send_message(chatik, text=result2,parse_mode='html')
            
            # print(result)
        else:
            result = f'<code>{today_ru_}, </code><code>{message.text.upper()}</code>\n===================='
            for i in range(len(itog[today_ru_][message.text.upper()])):
                j = itog[today_ru_][message.text.upper()]
                result = addp(i+1,j[i][0],j[i][1],j[i][2],j[i][3],result)
            bot.send_message(chatik, text=result,parse_mode='html')
    except Exception as e:
        bot.send_message(chatik, text=f'Error!\n{e}',parse_mode='html')



# one, two, thre = htm_(False, data,spli=True)
# one, two, thre = htm_(False, data)
# print(len(thre))
# print(all_info)

# print(two)
# print(one)

# for i in one:
#     print(i)
# print(one.get('ИБ 23-1'))

# print(one)
# if 'ИБ 23-1_' in one:
#     print(one['ИБ 23-1_'])
# print()
# if 'ИБ 23-1' in one:
#     print(one['ИБ 23-1'])
bot.infinity_polling()