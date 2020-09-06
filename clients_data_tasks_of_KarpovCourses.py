import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# №1. Считываем датасеты
user_data = pd.read_csv('https://stepik.org/media/attachments/lesson/360348/user_data.csv')
logs = pd.read_csv('https://stepik.org/media/attachments/lesson/360348/logs.csv')

# # №1.1. Проверяем размеры таблиц
# print('Size of user_data df:', user_data.shape)
# print('Size of logs df:',logs.shape, "\n")
#
# # №1.2. Оцениваем типы переменных
# print('Types of user_data df variables:', "\n" ,user_data.dtypes, "\n")
# print('Types of logs df variables:', "\n" ,logs.dtypes, "\n")
#
# # №1.3. Смотрим описательную статистику
# print('Describe stats of user_data df:', "\n" ,user_data.describe(), "\n")
# print('Describe stats of logs df:', "\n" ,logs.describe(), "\n")
#
# # №1.4. Проверяем наличие пропущенных значений
# print(user_data.isna().sum(), "\n")
# print(logs.isna().sum(), "\n")
#
# # №1.5. Узнаём кол-во уникальных значений переменной platform
# print('Count of unique values platform variable is', logs.platform.nunique())

# # №2. Находим клиента (список клиентов) с наибольшим кол-ом успешных операций
# # DF 'Client_id'-'Кол-во успешных'
# success_client_number = (logs
#                   .query("success == True")
#                   .groupby('client', as_index=False)
#                   .agg({'time':'count'})
#                   .sort_values('time', ascending = False))
#
# max_success = success_client_number.time.max()
# # DF Client_id с max кол-м успешных
# success_client = (success_client_number
#                     .query('time == @max_success') #ссылаемся на переменную с помощью @
#                     .client
#                     .sort_values()
#                   )
# print(', '.join([str(client) for client in success_client])) # Переводим DF в строку

# # №3. Узнаем платформу с наибольшим кол-м успешных операций
# max_platform_success_count = logs.query('success == True').platform.value_counts().idxmax()
# print(max_platform_success_count)

# # №4. Узнаём какую платформу предпочитают премиумные клиенты?
# premium_platform = (user_data.merge(logs)
#                     .groupby('platform')
#                     .agg({'premium':'sum'})
#                     .idxmax()
#                     )
# print(premium_platform)

# №5. Визуализируем распределение возраста клиентов в зависимости от типа клиента
# merge_df = user_data.merge(logs)

# sns.distplot(merge_df.query('premium == False').age)
# sns.distplot(merge_df.query('premium == True').age)
# plt.show()

# # или так
# fig, axes = plt.subplots(2,1)
# axes[0] = sns.distplot(merge_df.query('premium == False').age, ax=axes[0], color='green')
# axes[1] = sns.distplot(merge_df.query('premium == True').age, ax=axes[1])
# axes[0].set(xlabel='Age', ylabel='Percentage')
# axes[1].set(xlabel='Age_premium', ylabel='Percentage')
# sns.despine()  # убрать часть рамки графика
# plt.show()


# №6. Строим график распределения числа успешных операций
# clients_success_number = (user_data.merge(logs)
#             .groupby('client')
#             .agg({'success':'sum'})
#             )
# print(clients_success_number, "\n")
# print(clients_success_number.value_counts())
#
# sns.distplot(clients_success_number, kde=False)
# plt.show()

# # №7. Визуализируем число успешных операций, сделанных на платформе computer, в зависимости от возраста
# merged_df = (user_data.merge(logs)
#                         .query('success == True and platform == "computer"')
#              )
# plt.figure(figsize=(12, 8))
# sns.countplot(merged_df.age)
# plt.show()


