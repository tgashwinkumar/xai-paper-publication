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

---

## Backshift Operator

- $Bx_t = x_{t-1}$
- forward-shift operator $B⁻¹$, which satisfies $B⁻¹B = 1$.
- **First Order:** using the operator $(1-B)$ on xₜ gets us the difference $x_t - x_{t-1}$
- **Second Order:** $(1-B)²$ on xₜ, which gives us $(1–2B+B²)xₜ = xₜ-2x_{t-1}+ x_{t-2} = (x_t - x_{t-1}) - (x_{t-1} - x_{t-2})$

---

## Autoregressive Model

Reference: [OTexts - Forecasting: Principles and Practice](https://otexts.com/fpp2/AR.html)

An autoregressive model of order p, abbreviated AP(p), models the current value as a linear combination of the **previous p values.**

<center>

$y_t = c + \phi_1 y_{t-1} + \phi_2 y{t-2} + . . .  + \phi_py{t-p} + \epsilon_t$

</center>

where $ε_t$ is white noise.

| ![](https://otexts.com/fpp2/fpp_files/figure-html/arp-1.png)                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Two examples of data from autoregressive models with different parameters. Left: AR(1) with $y_t = 18 - 0.8y_{t-1} + \epsilon*t$ Right: AR(2) with $y_t = 8 + 1.3y*{t-1} - 0.7y*{t-2} + \epsilon_t$ In both cases, $\epsilon_t$ is normally distributed white noise with mean zero and variance one. |

For an AR(1) model:

- when $\phi_1 = 0$ is equivalent to white noise;
- when $\phi_1 = 1$ and $c=0$ is equivalent to a random walk;
- when $\phi_1$ and $c\ne0$ is equivalent to a random walk with drift;
- when $\phi_1 < 0$ tends to oscillate around the mean.

We normally restrict autoregressive models to stationary data, in which case some constraints on the values of the parameters are required.

- For an AR(1) model: $-1 < \phi_1 < 1$
- For an AR(2) model: $-1 < \phi_2 < 1, \phi_1 + \phi_2 < 1, \phi_2 - \phi_1 < 1$
- When $p \geq 3$, the restrictions are much more complicated.

In terms of backshift operator, the AR model is defined as

<center>

![](https://miro.medium.com/max/488/1*_SsRoHvEzt4RrC-oHx7h8A.png)

</center>

---

## Moving Average Model

Reference: [OTexts - Forecasting: Principles and Practice](https://otexts.com/fpp2/MA.html)

Rather than using past values of the forecast variable in a regression, a moving average model uses past forecast errors in a regression-like model.

$y_{t} = c + \varepsilon_t + \theta_{1}\varepsilon_{t-1} + \theta_{2}\varepsilon_{t-2} + \dots + \theta_{q}\varepsilon_{t-q}$

where $\varepsilon_t$ is white noise. We refer to this as an MA(q) model, a moving average model of order q. f course, we do not observe the values of $\varepsilon_t$, so it is not really a regression in the usual sense.

| ![](https://otexts.com/fpp2/fpp_files/figure-html/maq-1.png)                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Figure 8.6: Two examples of data from moving average models with different parameters. Left: MA(1) with $y_t = 20 + \varepsilon_t + 0.8\varepsilon_{t-1}$ ; Right: MA(2) with $y_t = \epsilon_t - \varepsilon_{t-1}+0.8\varepsilon_{t-2}$ In both cases, $\epsilon_t$ is normally distributed white noise with mean zero and variance one. |

It is possible to write any stationary AR(p) model as an MA($\infty$) model

$y_t = \phi_1y_{t-1} + \varepsilon_t$
$= \phi_1(\phi_1y_{t-2} + \varepsilon_{t-1}) + \varepsilon_t$
$= \phi_1^2y_{t-2} + \phi_1 \varepsilon_{t-1} + \varepsilon_t$
$= \phi_1^3y_{t-3} + \phi_1^2\varepsilon_{t-2} + \phi_1 \varepsilon_{t-1} + \varepsilon_t; \text{etc.}$

In terms of the back-shift operator, the moving average model can be defined as

<center>

![](https://miro.medium.com/max/485/1*Is8pESaD3qoLPOvi68_bCg.png)

</center>

---

## ARMA model

<center>

![](https://miro.medium.com/max/745/1*Jz3Eu9lzv5WqGikbLv9Tkw.png)

</center>

where $ϕ_p ≠ 0, θ_q ≠ 0, w_t$ ~ $w_n(0, σᵥᵥ²)$, and $σᵥᵥ² > 0.$ The parameters p and q are the autoregressive and the moving average orders respectively, as mentioned before. In terms of the back-shift operator, the ARIMA model can be written as

<center>

![](https://miro.medium.com/max/201/1*2Nz1SL74FZpvRHW8xC4ChQ.png)

</center>

### Definition of Seasonal ARMA

<center>

![](https://miro.medium.com/max/588/1*hzHLqZduedPJLDrp7g69sw.png)

</center>

### The value of h

This depends on the frequency of the seasonality, for example, if the seasonal variation appears once in a year in some specific months, then $h = 12$, if it appears once in each quarter of the year, then $h = 4$.

