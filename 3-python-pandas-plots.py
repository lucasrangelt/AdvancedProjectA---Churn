import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv", decimal=".")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

tenurebins = [0, 6, 12, 24, 36, 48, 60, np.inf]
tenurelabels = ["Menos de 6 meses", "6 meses a 1 ano", "1 a 2 anos", "2 a 3 anos",
                "3 a 4 anos", "4 a 5 anos", "Mais de 5 anos"]
df["TenureGroup"] = pd.cut(df["tenure"], bins=tenurebins, labels=tenurelabels, right=True, include_lowest=True)
monthlymean = df["MonthlyCharges"].mean()
df["MonthlyGroup"] = np.where(df["MonthlyCharges"] >= monthlymean, "Acima da Média", "Abaixo da Média")
totalmean = df["TotalCharges"].mean()
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].mean())
df["TotalGroup"] = np.where(df["TotalCharges"] >= totalmean, "Acima da Média", "Abaixo da Média")

def read_data():
  a = df[df["Churn"] == "Yes"]
  print(df["TenureGroup"].value_counts())
  # gchurn = a["gender"].value_counts() / df["gender"].value_counts()
  scchurn = a["SeniorCitizen"].value_counts() / df["SeniorCitizen"].value_counts()
  pchurn = a["Partner"].value_counts() / df["Partner"].value_counts()
  dchurn = a["Dependents"].value_counts() / df["Dependents"].value_counts()
  tgchurn = a["TenureGroup"].value_counts() / df["TenureGroup"].value_counts()
  # pschurn = a["PhoneService"].value_counts() / df["PhoneService"].value_counts()
  # mlchurn = a["MultipleLines"].value_counts() / df["MultipleLines"].value_counts()
  ischurn = a["InternetService"].value_counts() / df["InternetService"].value_counts()
  oschurn = a["OnlineSecurity"].value_counts() / df["OnlineSecurity"].value_counts()
  obchurn = a["OnlineBackup"].value_counts() / df["OnlineBackup"].value_counts()
  dpchurn = a["DeviceProtection"].value_counts() / df["DeviceProtection"].value_counts()
  tschurn = a["TechSupport"].value_counts() / df["TechSupport"].value_counts()
  # stvchurn = a["StreamingTV"].value_counts() / df["StreamingTV"].value_counts()
  # smchurn = a["StreamingMovies"].value_counts() / df["StreamingMovies"].value_counts()
  cchurn = a["Contract"].value_counts() / df["Contract"].value_counts()
  pbchurn = a["PaperlessBilling"].value_counts() / df["PaperlessBilling"].value_counts()
  pmchurn = a["PaymentMethod"].value_counts() / df["PaymentMethod"].value_counts()
  mgchurn = a["MonthlyGroup"].value_counts() / df["MonthlyGroup"].value_counts()
  totalgchurn = a["TotalGroup"].value_counts() / df["TotalGroup"].value_counts()

  print("",
      #   gchurn,
        scchurn,
        pchurn,
        dchurn,
        tgchurn,
      #   pschurn,
      #   mlchurn,
        ischurn,
        oschurn,
        obchurn,
        dpchurn,
        tschurn,
      #   stvchurn,
      #   smchurn,
        cchurn,
        pbchurn,
        pmchurn,
        mgchurn,
        totalgchurn,
        "")

  def plots_part_one():
    fig, axes = plt.subplots(1, 4, figsize=(12, 7))
    scchurn.plot(kind="bar", ax=axes[0])
    axes[0].set_title("Senioridade")
    axes[0].set_ylabel("Taxa de Churn")
    axes[0].set_xticks(ticks=[0, 1], labels=["Não-Idoso", "Idoso"])
    pchurn.plot(kind="bar", ax=axes[1])
    axes[1].set_title("Parceiro")
    axes[1].set_xticks(ticks=[0, 1], labels=["Sem parceiro", "Com parceiro"])
    dchurn.plot(kind="bar", ax=axes[2])
    axes[2].set_title("Dependentes")
    axes[2].set_xticks(ticks=[0, 1], labels=["Sem dependentes", "Com dependentes"])
    tgchurn.plot(kind="bar", ax=axes[3])
    axes[3].set_title("Tempo de Permanência")
    axes[3].set_xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=["<6m", "6m-1a", "1a-2a", "2a-3a", "3a-4a",
                                                              "4a-5a", "5a>"])
    for ax in axes:
      ax.set_xlabel("")
      ax.set_ylim(0.0, 0.55)
      ax.tick_params(axis="x", rotation=30)
      if ax == axes[3]:
        ax.tick_params(axis="x", rotation=45)
      ax.set_xticklabels(labels=ax.get_xticklabels(), ha="right")
    plt.show()

  def plots_part_two():
    fig, axes = plt.subplots(1, 5, figsize=(12, 7))
    ischurn.plot(kind="bar", ax=axes[0])
    axes[0].set_title("Serviço de Internet")
    axes[0].set_xticks(ticks=[0, 1, 2], labels=["Fibra Ótica", "DSL", "Sem Internet"])
    oschurn.plot(kind="bar", ax=axes[1])
    axes[1].set_title("Segurança Online")
    axes[1].set_xticks(ticks=[0, 1, 2], labels=["Não", "Sim", "Sem Internet"])
    obchurn.plot(kind="bar", ax=axes[2])
    axes[2].set_title("Backup Online")
    axes[2].set_xticks(ticks=[0, 1, 2], labels=["Não", "Sim", "Sem Internet"])
    dpchurn.plot(kind="bar", ax=axes[3])
    axes[3].set_title("Proteção de Dispositivo")
    axes[3].set_xticks(ticks=[0, 1, 2], labels=["Não", "Sim", "Sem Internet"])
    tschurn.plot(kind="bar", ax=axes[4])
    axes[4].set_title("Suporte Técnico")
    axes[4].set_xticks(ticks=[0, 1, 2], labels=["Não", "Sim", "Sem Internet"])
    for ax in axes:
      ax.set_xlabel("")
      ax.set_ylim(0.0, 0.55)
      ax.tick_params(axis="x", rotation=30)
      ax.set_xticklabels(labels=ax.get_xticklabels(), ha="right")
    plt.show()
  
  def plots_part_three():
    fig, axes = plt.subplots(1, 5, figsize=(12, 7))
    cchurn.plot(kind="bar", ax=axes[0])
    axes[0].set_title("Contrato")
    axes[0].set_xticks(ticks=[0, 1, 2], labels=["Mensal", "Um ano", "Dois anos"])
    pbchurn.plot(kind="bar", ax=axes[1])
    axes[1].set_title("Faturação Eletrônica")
    axes[1].set_xticks(ticks=[0, 1], labels=["Sim", "Não"])
    pmchurn.plot(kind="bar", ax=axes[2])
    axes[2].set_title("Método de Pagamento")
    axes[2].set_xticks(ticks=[0, 1, 2, 3], labels=["Cheque eletrônico", "Cheque enviado por correio", "Transferência bancária", "Cartão de crédito"])
    mgchurn.plot(kind="bar", ax=axes[3])
    axes[3].set_title("Cobranças Mensais")
    axes[3].set_xticks(ticks=[0, 1], labels=["Acima da média", "Abaixo da média"])
    totalgchurn.plot(kind="bar", ax=axes[4])
    axes[4].set_title("Cobranças Totais")
    axes[4].set_xticks(ticks=[0, 1], labels=["Abaixo da média", "Acima da média"])
    for ax in axes:
      ax.set_xlabel("")
      ax.set_ylim(0.0, 0.55)
      ax.tick_params(axis="x", rotation=30)
      ax.set_xticklabels(labels=ax.get_xticklabels(), ha="right")
      if ax == axes[2] or ax == axes[3] or ax == axes[4]:
        ax.tick_params(axis="x", rotation=20)
    plt.show()

  # plots_part_one()
  # plots_part_two()
  plots_part_three()

def logistic_regression_model():
  # limpar dados de colunas com "sub serviços"
  sub_services = ["MultipleLines", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                           "TechSupport", "StreamingTV", "StreamingMovies"]
  for i in sub_services:
    df[i] = df[i].replace("No internet service", "No")
    df[i] = df[i].replace("No phone service", "No")

# transformar colunas em binárias e converter valores contínuos para desvio padrão
  df_encoded = pd.get_dummies(df, columns=["gender", "SeniorCitizen", "Partner", "Dependents",
                                           "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
                                           "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
                                           "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod"],
                                           drop_first=True, dtype=int)
  continuous_numbers = ["tenure", "MonthlyCharges"]
  scaler = StandardScaler() # para colunas com vários números como tenure (permanência)
  df_encoded[continuous_numbers] = scaler.fit_transform(df_encoded[continuous_numbers]) # aplicar desvio padrão

# criando o modelo e verificando redundâncias
  y = df_encoded["Churn"] # o alvo para treinar o modelo
  X = df_encoded.drop(["Churn", "TenureGroup", "MonthlyGroup", "TotalGroup",
                       "TotalCharges", "customerID"], axis=1) # elementos para treinar o modelo, menos exceções
  # x_vif = X
  # vif_data = pd.DataFrame()
  # vif_data["feature"] = x_vif.columns
  # vif_data["VIF"] = [variance_inflation_factor(x_vif.values, i)
  #                           for i in range(len(x_vif.columns))] 
  # print(vif_data.sort_values(ascending=False, by="VIF"))

# treinando e testando o modelo, printando coeficientes, dados de precisão e matriz
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # testar 20% dos dados
  model = LogisticRegression(class_weight="balanced", solver="liblinear", random_state=42) # selecionar tipo
  model.fit(X_train, y_train) # treinar o modelo
  #
  coefficients = pd.Series(model.coef_[0], index=X.columns)
  print(np.exp(coefficients.sort_values(ascending=False)))
  #
  y_pred = model.predict(X_test)
  print(classification_report(y_test, y_pred))
  print(confusion_matrix(y_test, y_pred))

# read_data()
logistic_regression_model()