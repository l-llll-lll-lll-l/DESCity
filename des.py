import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

def plot_results(yearvalue, loadvalue, t, predicted_values, fitted_values, name):
    plt.figure(figsize=(10, 6))
    plt.plot(yearvalue, loadvalue, marker='o', label='Actual')
    plt.plot(np.arange(yearvalue[-1]+1, yearvalue[-1] + t + 1), predicted_values, marker='x', label='Predicted')
    plt.plot(yearvalue, fitted_values, marker='s', label='Fitted', linestyle='dashed')
    plt.xlabel('Year')
    plt.ylabel('Load Value')
    plt.title('Actual, Predicted, and Fitted Load Values')
    plt.legend()
    plt.grid(True)
    plt.savefig('./result/' + name + '.png')
    plt.show()

def des(data, yearvalue, fcstnum, name):
    fit1 = sm.tsa.ExponentialSmoothing(data, trend='add', damped_trend=True).fit()
    print(fit1.summary())
    fcst = fit1.forecast(fcstnum)
    fitted_values = fit1.fittedvalues
    print('forecast:', fcst)
    fp = open('./result/' + name + '.txt', 'w')
    fp.write('-' * 35 + name + '-' * 37 + '\n')
    fp.write(str(fit1.summary()))
    fp.write('\nforecast:' + str(fcst))
    fp.close()
    plot_results(yearvalue, data, fcstnum, fcst.tolist(), fitted_values.tolist(), name)

if __name__ == '__main__':
    des([4, 4, 6, 0, 0, 0, 0, 6, 11, 9, 13, 8, 8, 28, 26, 49, 118, 232, 393, 99, 136, 89, 85],
        np.arange(2000, 2023), 3, 'test')
