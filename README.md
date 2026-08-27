# Financial-Time-Series-Analytics
# Bank Stock Closing Price Forecasting: A Comparative Study of ARIMA, Random Forest and LSTM

## MSc Data Science Project

This project investigates the prediction of daily closing prices for three major bank stocks using historical stock-market data and three different forecasting approaches:

- ARIMA – classical statistical time-series forecasting
- Random Forest – machine-learning regression
- LSTM – deep-learning sequence forecasting

The banks analysed are:

- Lloyds Banking Group (LLOY.L)
- Barclays (BARC.L)
- Goldman Sachs (GS)

The project focuses not only on model accuracy, but also on whether apparently strong forecasting results represent genuine predictive performance. Particular attention is given to data leakage, scaling, currency differences, model assumptions, numerical stability and comparison with a persistence baseline.

---

## 1. Project Overview

Stock-price forecasting is a challenging problem because financial markets are affected by changing economic conditions, market sentiment, company-specific events and information that may not be contained in historical price data.

This project compares three different modelling approaches using the same general financial forecasting problem.

The analysis covers daily observations from:

**2 January 2015 to 24 August 2026**

The final dataset contains approximately **8,810 observations** across the three banks.

The project evaluates whether more complex machine-learning and deep-learning models provide meaningful improvements over classical statistical forecasting and a simple persistence baseline.



## 2. Research Question

 **How accurately can the daily closing prices of major bank stocks such as Lloyds, Barclays, and Goldman Sachs be predicted using their historical price and volume information, and which forecasting method is most effective for this task?**


## 3. Research Objectives

The project has five main objectives:

1. **Create a consistent daily OHLCV dataset** for Lloyds, Barclays and Goldman Sachs.

2. **Explore the financial data** by examining trends, trading volume, price distributions, volatility and correlations.

3. **Develop three forecasting models** representing different modelling approaches:
   - ARIMA
   - Random Forest
   - LSTM

4. **Tune and evaluate the models** using appropriate time-series procedures and performance metrics.

5. **Critically evaluate the forecasting results**, including data leakage, extrapolation problems, numerical instability, scaling issues and comparison with a persistence baseline.

## 4. Data

The stock-market data was obtained using the `yfinance` Python library from Yahoo Finance.

The dataset contains daily:

- Date
- Open price
- High price
- Low price
- Closing price
- Trading volume
- Bank identifier

### Stocks analysed

| Bank | Ticker | Exchange | Currency |
|---|---|---|---|
| Lloyds Banking Group | LLOY.L | London Stock Exchange | GBX |
| Barclays | BARC.L | London Stock Exchange | GBX |
| Goldman Sachs | GS | New York Stock Exchange | USD |

Lloyds and Barclays are quoted in GBX, while Goldman Sachs is quoted in USD.

For pooled modelling and direct cross-bank comparisons, Goldman Sachs prices are converted from USD to GBX.

ARIMA is fitted separately for each bank using its native price series.


## 5. Exploratory Data Analysis

The exploratory analysis examines the main characteristics of the three financial time series.

### Price trends

The three banks show different long-term price behaviour over the study period.

Goldman Sachs experienced substantially stronger price growth than the two UK banks. This difference in price level is important when comparing absolute forecasting errors.

### Trading volume

Trading volume is examined separately from price behaviour to identify differences in market activity and potential relationships between volume and price movements.

### Return volatility

Daily returns are used to compare volatility between the three banks.

The standard deviation of daily returns shows that:

- Barclays has the highest return volatility.
- Lloyds has intermediate volatility.
- Goldman Sachs has the lowest return volatility.

### Correlation

Pearson correlation is used to examine relationships between the financial variables.

The correlation analysis shows strong relationships between Open, High, Low and Close prices because these variables describe different aspects of the same daily trading session.

Volume has a weaker relationship with the price variables.


# 6. ARIMA Model

## Why ARIMA?

ARIMA was selected because it is a well-established statistical approach for forecasting time-series data.

It provides a useful baseline against which more complex machine-learning and deep-learning models can be compared.

ARIMA is particularly appropriate when the temporal structure of the series is important.

## ARIMA methodology

The ARIMA modelling process includes:

- Augmented Dickey-Fuller testing
- Differencing
- ACF analysis
- PACF analysis
- Parameter selection
- AIC-based model selection
- Walk-forward forecasting
- Residual diagnostics

The model is represented as:

**ARIMA(p,d,q)**

where:

- `p` = autoregressive order
- `d` = differencing order
- `q` = moving-average order

The selected configurations were:

| Bank | ARIMA Model |
|---|---|
| Lloyds | ARIMA(3,1,4) |
| Barclays | ARIMA(0,1,0) |
| Goldman Sachs | ARIMA(2,1,2) |

The Barclays result is particularly important because ARIMA(0,1,0) corresponds to a random-walk/persistence-type forecasting structure.


# 7. Random Forest Model

## Why Random Forest?

Random Forest was selected because it can model nonlinear relationships and interactions between multiple engineered features.

Unlike ARIMA, it does not require the data to be represented explicitly as an autoregressive statistical process.

## Features

The Random Forest model uses historical and lagged information, including:

- Previous-day Open
- Previous-day High
- Previous-day Low
- Previous-day Volume
- Lag 1
- Lag 2
- Lag 3
- 5-day moving average
- 10-day moving average
- Bank identifier

The model predicts the **next-day price change** rather than directly predicting the future price level.
