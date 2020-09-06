import pandas as pd

# №1. Считываем датасет, приводим названия колонок к рабочему виду
bookings = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', sep=';')
bookings_head = bookings[:7]
bookings.columns = bookings.columns.str.lower().str.replace(' ', '_')

# №2. Оцениваем размеры таблицы
print('Table size:', bookings.shape, '\n')

# №3. Определяем количество типов переменных
print('The most frequent type of variable:', '\n', bookings.dtypes.value_counts(), '\n')

# №4. Топ 5 стран по кол-ву успешных бронирований
country_top = bookings.query('is_canceled == 0').value_counts('country').head()
print(country_top, '\n')

# №5. Узнаём среднее кол-во ночей, на которое бронируют отель. (по типу отеля)
count_of_nights = bookings.groupby('hotel', as_index=False) \
                            .agg({'stays_total_nights': 'mean'}) \
                            .round(2)
print(count_of_nights, '\n')

# №6. Считаем кол-во случаев овербукинга (когда полученный клиентом номер отличается от брони)
overbooking = bookings.query('assigned_room_type != reserved_room_type').shape[0]
print('Total count of overbooking is', overbooking, '\n')

# №7. Анализируем даты планируемых прибытий. Определяем месяцы с наибольшим кол-м
# бронирований в 2016-м и 2017-м годах.
arrival_date = bookings.query('arrival_date_year == 2016 or arrival_date_year == 2017') \
                        .groupby(['arrival_date_month', 'arrival_date_year'], as_index=False) \
                        .agg({'customer_type': 'count'}) \
                        .sort_values('customer_type', ascending = False).head()
print(arrival_date, '\n')

# №8. Узнаём в каких месяцах чаще всего отменяли бронь City Hotel по годам.
cancellations = bookings.query("hotel == 'City Hotel' and is_canceled == 1") \
                            .groupby('arrival_date_year') \
                            .arrival_date_month.value_counts()
print(cancellations, '\n')

# №9. Наибольшее среднее значение посетителей среди взрослых, детей, младенцев.
age_type = bookings[['adults','children','babies']].mean().idxmax()
print('Max mean number is for', age_type, '\n')

# №10.
bookings['total_kids'] = bookings['children'] + bookings['babies']
total_kids_hotels = bookings.groupby('hotel').agg({'total_kids':'mean'}).round(2).max()
print(total_kids_hotels, '\n')

# №11. Отток клиентов с детьми/без в процентах. Наибольшее значение
bookings['has_kids'] = bookings['total_kids'] > 0
res1 = bookings.query('has_kids == False and is_canceled == 1').shape[0] \
                / bookings.query('has_kids == False ').shape[0]
res1 = round(res1*100, 2)
res2 = bookings.query('has_kids == True and is_canceled == 1').shape[0] \
                / bookings.query('has_kids == False ').shape[0]
res2 = round(res2*100, 2)
ans = max(res1, res2)
print(ans)
