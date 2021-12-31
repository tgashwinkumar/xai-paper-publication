# Time Series

## Time horizons

Reference : [Tableau - Time Series forecasting](https://www.tableau.com/learn/articles/time-series-forecasting)

The time frame of your forecast also matters. This is known as a **time horizon**—a fixed point in time where a process (like the forecast) ends. It’s much easier to forecast a shorter time horizon with fewer variables than it is a longer time horizon. The further out you go, the more unpredictable the variables will be. Alternatively, having **less data can sometimes still work** with forecasting if you adjust your time horizons. If you’re lacking long-term recorded data but you have an extensive amount of short-term data, you can create short-term forecasts.

## Data quality

Reference : [Tableau - Time Series forecasting](https://www.tableau.com/learn/articles/time-series-forecasting)

- Make sure data is complete,
- is not duplicated or redundant,
- was collected in a timely and consistent manner,
- is in a standard and valid format,
- is accurate for what it is measuring,
- and is uniform across sets.

## Types of data

Reference: [Tableau - Time Series Analysis](https://www.tableau.com/learn/articles/time-series-analysis)

### Time series data

Time series data is data that is recorded over consistent intervals of time.

- **Stock time series data** means measuring attributes at a certain point in time, like a static snapshot of the information as it was.
- **Flow time series data** means measuring the activity of the attributes over a certain period, which is generally part of the total whole and makes up a portion of the results.

### Cross-sectional data

Cross-sectional data consists of several variables recorded at the same time.

### Pooled data

Pooled data is a combination of both time series data and cross-sectional data.

## Time Series Variations

In time series data, variations can occur sporadically throughout the data:

- **Functional analysis** can pick out the patterns and relationships within the data to identify notable events.
- **Trend analysis** means determining consistent movement in a certain direction. There are two types of trends: deterministic, where we can find the underlying cause, and stochastic, which is random and unexplainable.
- **Seasonal variation** describes events that occur at specific and regular intervals during the course of a year. Serial dependence occurs when data points close together in time tend to be related.

## Types of time series analysis

- **Classification**: Identifies and assigns categories to the data.
- **Curve fitting**: Plots the data along a curve to study the relationships of variables within the data.
- **Descriptive analysis**: Identifies patterns in time series data, like trends, cycles, or seasonal variation.
- **Explanative analysis**: Attempts to understand the data and the relationships within it, as well as cause and effect.
- **Exploratory analysis**: Highlights the main characteristics of the time series data, usually in a visual format.
- **Forecasting** Predicts future data. This type is based on historical trends. It uses the historical data as a model - for future data, predicting scenarios that could happen along future plot points.
- **Intervention analysis**: Studies how an event can change the data.
- **Segmentation**: Splits the data into segments to show the - underlying properties of the source information.

## Time Series Models

- **Box-Jenkins ARIMA models:** These univariate models are used to better understand a single time-dependent variable, such as temperature over time, and to predict future data points of variables. These models work on the assumption that the data is stationary. Analysts have to account for and remove as many differences and seasonality in past data points as they can. Thankfully, the ARIMA model includes terms to account for moving averages, seasonal difference operators, and autoregressive terms within the model.
- **Box-Jenkins Multivariate Models:** Multivariate models are used to analyze more than one time-dependent variable, such as temperature and humidity, over time.
- **Holt-Winters Method:** The Holt-Winters method is an exponential smoothing technique. It is designed to predict outcomes, provided that the data points include seasonality.
