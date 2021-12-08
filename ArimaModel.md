# ARIMA Model

Reference: [TowardsDataScience - Understanding ARIMA Model](https://towardsdatascience.com/deep-understanding-of-the-arima-model-d3f0751fc709)

## Definition

<center>

$y_{t+h} = g(X_t, \theta) + \epsilon_{t+h}$

</center>

- It is worth noting that the observed data is uniquely orderly according to the time of observation, but it doesn’t have to be dependent on time, i.e. time (index of the observations) doesn’t have to be one of the independent variables.

## Properties

### Stationarity

When using ARIMA to model a time series, one of the assumptions is that the data is stationary.

<center>

| ![](https://miro.medium.com/max/431/1*hA65GONtR9Sj4ryH0hxceA.png)   | ![](https://miro.medium.com/max/588/1*MjI0g2l1hRqBTMep2QawdA.png) |
| :------------------------------------------------------------------ | ----------------------------------------------------------------- |
| _Shows the simplest example of a stationary process — white noise._ | _Example of non-stationarity time series._                        |

|         ![](https://miro.medium.com/max/875/1*3cg9COProxB1wa0Zna70Sw.jpeg)         |
| :--------------------------------------------------------------------------------: |
| _(left) Fit a line to the original data, (right) Result after removing the trend._ |

</center>

### Seasonality

<center>

| ![](https://miro.medium.com/max/761/1*sjBHk8NUguBS1MxmKTprQA.png) | ![](https://miro.medium.com/max/668/1*T2Lm0q-vibpB1keWZ1sLrA.png) |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| there is a peak of electricity usage in July and August           | electricity usage throughout the whole period                     |

</center>

## Backshift Operator

- $Bx_t = x_{t-1}$
- forward-shift operator $B⁻¹$, which satisfies $B⁻¹B = 1$.
- **First Order:** using the operator $(1-B)$ on xₜ gets us the difference $x_t - x_{t-1}$
- **Second Order:** $(1-B)²$ on xₜ, which gives us $(1–2B+B²)xₜ = xₜ-2x_{t-1}+ x_{t-2} = (x_t - x_{t-1}) - (x_{t-1} - x_{t-2})$

## Autoregressive Model
