import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

taxi = pd.read_csv('https://stepik.org/media/attachments/lesson/359240/taxi_peru.csv', sep=';' \
                 , parse_dates=['start_at', 'end_at', 'arrived_at'])


driver_score_counts = (taxi
                        .driver_score
                        .value_counts(normalize=True)
                        .mul(100)
                        .round(2)
                        .reset_index()
                        .rename(columns={'index':'driver_score','driver_score':'percentage'})
                        .sort_values(by=['driver_score']))

rider_score_counts = (taxi
                        .rider_score
                        .value_counts(normalize=True)
                        .mul(100)
                        .round(2)
                        .reset_index()
                        .rename(columns={'index':'rider_score','rider_score':'percentage'})
                        .sort_values(by=['rider_score']))


fig, axes = plt.subplots(1,2)
axes[0] = sns.barplot(x='driver_score', y='percentage', data=driver_score_counts, color='blue', alpha=0.5, ax=axes[0])
axes[1] = sns.barplot(x='rider_score', y='percentage', data=rider_score_counts, color='blue', alpha=0.5, ax=axes[1])
axes[0].set(xlabel='Driver score', ylabel='Percentage')
axes[1].set(xlabel='Rider score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()


# percent = taxi \
#             .source \
#             .value_counts(normalize=True) \
#             .mul(100) \
#             .max() \
#             .round()
# print(percent)