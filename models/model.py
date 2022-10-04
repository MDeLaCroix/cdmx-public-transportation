from turtle import filling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import app
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from cdmx_public_transportation.models.regress_model import Regress_model
from cdmx_public_transportation.models.get_vif import Get_VIF
from cdmx_public_transportation.features.build_features import build_features

class Model:
    def __init__(self, km: float, px: float):
        metro, metrobus = build_features()

        metro = metro.iloc[:,2:7]
        X_mt = metro.drop(columns=metro.columns[4])
        y_mt = metro[metro.columns[4]]

        vif = Get_VIF(X_mt)
        print(vif)

        X_mt1 = X_mt.drop(columns=metro.columns[2])
        vif1 = Get_VIF(X_mt1)
        print(vif1)

        X_mt2 = X_mt1.drop(columns=X_mt1.columns[1])
        vif2 = Get_VIF(X_mt2)
        print(vif2)

        X_train_mt, X_test_mt, y_train_mt, y_test_mt = train_test_split(X_mt2, y_mt, random_state=19)

        scaler = StandardScaler().fit(X_train_mt)
        X_train_mt = scaler.transform(X_train_mt)
        X_test_mt = scaler.transform(X_test_mt)

        selection = Regress_model(X_train_mt, y_train_mt)
        print('\nSelected model: ', selection)

        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit(X_train_mt,y_train_mt)
        y_pred = model.predict(X_test_mt)

        ## Fase 2

        #km = input('Longitud del servicio en kilómetros: ')
        #km = float(km)
        #px = input('Pasajeros transportados (en millones): ')
        #px = float(px)
        #km = 200
        #px = 120
        new_data = pd.DataFrame(np.array([[km, px]]))


        X_new = scaler.transform(new_data)
        y_hat = model.predict(X_new)
        print(y_hat)

       ## Visualize
        fig = plt.figure()
        x_line = np.linspace(np.min(metro.iloc[:,3]),
            np.max(metro.iloc[:,3]),
            200)
        new_group = scaler.transform(np.column_stack((np.full(200, km),x_line)))
        y_line = model.predict(new_group)

        plt.plot(x_line,
            y_line,
            c='red')

        plt.vlines(x= px,
            ymin= np.min(metro.iloc[:,-1]),
            ymax= y_hat,
            color= 'red',
            linestyles= 'dashed')

        plt.scatter(metro.iloc[:,3],
            metro.iloc[:,4],
            c= metro.iloc[:,0],
            cmap='Blues')
        plt.colorbar().ax.set_ylabel(metro.columns[0])
        plt.xlabel(metro.columns[3])
        plt.ylabel(metro.columns[4])
        self.figure = fig
        self.y_hat = str(y_hat)

