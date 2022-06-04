
def plot_residuals(actual, predicted):
    residuals = actual - predicted
    plt.hlines(0, actual.min(), actual.max(), ls=':', colors = 'r')
    plt.scatter(actual, residuals)
    plt.ylabel('Residual ($y - \hat{y}$)')
    plt.xlabel('Actual Value ($y$)')
    plt.title('Actual vs Residual')
    plt.show()

#def residuals for manual calc
def residuals(actual, predicted):
    return actual - predicted

# manually define: sse, mse, rmse, ess, tss, r2_score 

def sse(actual, predicted):
    return (residuals(actual, predicted) ** 2).sum()

def mse(actual, predicted):
    n = actual.shape[0]
    return sse(actual, predicted) / n

def rmse(actual, predicted):
    #import math module to ensure function runs
    import math
    return math.sqrt(mse(actual, predicted))

def ess(actual, predicted):
    return ((predicted - actual.mean()) ** 2).sum()

def tss(actual):
    return ((actual - actual.mean()) ** 2).sum()

def r2_score(actual, predicted):
    return ess(actual, predicted) / tss(actual)


#return  a series with sse, ess, tss, mse, and rmse
def regression_errors(actual, predicted):
    return pd.Series({
        'sse': sse(actual, predicted),
        'ess': ess(actual, predicted),
        'tss': tss(actual),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    })

#return sse, mse, rmse
def baseline_mean_errors(actual):
    predicted = actual.mean()
    return {
        'sse': sse(actual, predicted),
        'mse': mse(actual, predicted),
        'rmse': rmse(actual, predicted),
    }


def better_than_baseline(actual, predicted):
    rmse_baseline = rmse(actual, actual.mean())
    rmse_model = rmse(actual, predicted)
    if rmse_model < rmse_baseline:
        print('OLS Regression Model performs better than the baseline model.')
    
    else:
        print('OLS Regression Model performs worse than the baseline model.')
    return rmse_model < rmse_baseline