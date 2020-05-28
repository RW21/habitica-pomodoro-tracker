from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def create_bar_plot(result, day: datetime):
    """
    Takes last day of range as input.
    :param result:
    :param day: last day in range
    :return:
    """
    days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    plt.xticks(range(len(result)), days)
    plt.ylabel('Pomodoros')
    day_range = (day - timedelta(days=6), day)
    plt.title(str(day_range[0].date()) + ' - ' + str(day_range[1].date()))
    plt.bar(days, result, align='center', alpha=0.5)
    plt.savefig(str(day_range[1].date())+'.svg')