# XAI

---

Explainable AI is artificial intelligence in which the results of the solution can be understood by humans. It contrasts with the concept of the "black box" in machine learning where even its designers cannot explain why an AI arrived at a specific decision

# AI vs XAI

---

Artificial intelligence (AI) is just an black box model to predict outcomes based on its previous learnings but we can’t figure out the reason for the outcome . Its fully abstracted so that the user don’t know its internal workings and this makes it not completely trustable model

Explainable Artificial Intelligence (XAI) is just the white box version of AI where the user knows the exact reason for an outcome to happen or not. It helps us to create an efficient AI model.

![AI-vs-XAI](https://miro.medium.com/max/1400/1*NFxDcMGD8ctFFsJauACHyA.png)

# Aim of XAI

---

- The Explainable AI (XAI) program aims to create a suite of machine learning techniques that:

  - To develop more explainable models, while maintaining a high level of learning performance with improved prediction results
  - Human users should be able to trust, understand, and effectively manage the new generation of artificially intelligent partners.

# Why - XAI?

---

It is crucial for an organization to have a full understanding of the AI decision-making processes with model monitoring and accountability of AI and not to trust them blindly. Explainable AI can help humans understand and explain machine learning (ML) algorithms, deep learning and neural networks

Explainable AI is one of the key requirements for implementing responsible AI, a methodology for the large-scale implementation of AI methods in real organizations with fairness, model explainability and accountability.³ To help adopt AI responsibly, organizations need to embed ethical principles into AI applications and processes by building AI systems based on trust and transparency.

## Used for Continuos Model Evaluation :

With explainable AI, a business can troubleshoot and improve model performance while helping stakeholders understand the behaviors of AI models. Investigating model behaviors through tracking model insights on deployment status, fairness, quality and drift is essential to scaling AI. Continuous model evaluation empowers a business to compare model predictions, quantify model risk and optimize model performance. Displaying positive and negative values in model behaviors with data used to generate explanation speeds model evaluations.

# Some pre-built Models for XAI

---

## FACET :

FACET is an open source library for human-explainable AI. It combines sophisticated model inspection and model-based simulation to enable better explanations of your supervised machine learning models.

It has 3 main features :

- ### Model Inspection

  **FACET** introduces a new algorithm to quantify dependencies and
  interactions between features in ML models.
  This new tool for **human-explainable** AI adds a new, global
  perspective to the observation-level explanations
  provided by the popular **SHAP** approach.

- ### Model Simulation

  FACET’s model simulation algorithms use ML models for virtual experiments to help identify scenarios that optimise predicted outcomes. To quantify the uncertainty in simulations, FACET utilises a range of bootstrapping algorithms including **_stationary and stratified bootstraps_**.

- ### Enhanced Machine Learning Workflow

  FACET offers an efficient and transparent machine learning workflow, enhancing scikit-learn's tried and tested pipelining paradigm with new capabilities for model selection, inspection, and simulation. FACET also introduces **_"sklearndf"_** [documentation](https://bcg-gamma.github.io/sklearndf/index.html) an augmented version of scikit-learn with enhanced support for pandas data frames that ensures end-to-end traceability of features.

Github-Repo -> [FACET](https://github.com/BCG-Gamma/facet)

---

## explainX: Explainable AI Framework for Data Scientists

**xplainX** is a model explainability/interpretability framework for data scientists and business users.

Github-Repo -> [explainX](https://github.com/explainX/explainx)

![xplainxai](https://camo.githubusercontent.com/03f9e0729544717710427ed393dae32b8d055159/68747470733a2f2f692e6962622e636f2f7734534631474a2f47726f75702d322d312e706e67)

---

## XAI - An eXplainability toolbox for machine learning

**XAI** is a Machine Learning library that is designed with AI explainability in its core. XAI contains various tools that enable for analysis and evaluation of data and models. The XAI library is maintained by **The Institute for Ethical AI & ML**, and it was developed based on the 8 principles for Responsible Machine Learning.

You can find the [documentation](https://ethicalml.github.io/xai/index.html).

---

## ELI5

ELI5 is a Python package which helps to debug machine learning classifiers and explain their predictions. It has support for many ML frameworks like scikit-learn, Keras, XGBoost, LightGBM, and CatBoost.

There are two main ways to look at a classification or a regression model:

1. inspect model parameters and try to figure out how the model works globally;
2. inspect an individual prediction of a model, try to figure out why the model makes the decision it makes.

![ELI5](https://miro.medium.com/max/1400/1*mIooDw4zZhvJx1o632FgIw.png)

---

## What-If Tool

Whatif Tool (WIT) is developed by Google to understand the working of ML trained models. Using WIT, you can test performance in hypothetical situations, analyze the importance of different data features, and visualize model behavior across multiple models and subsets of input data, and for different ML fairness metrics.

The What-If Tool is available as an extension in Jupyter, Colaboratory, and Cloud AI Platform notebooks. It can be used for different tasks like binary classification, multi-class classification and regression. It can be used with various types of data like Tabular, Image and Text data.

![WIT](https://miro.medium.com/max/1400/1*H7S9oSQgPP7H56NSFXg_hg.png)
