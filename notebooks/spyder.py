import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def Regress_model(x_train,y_train,x_test=None,y_test=None,degree=2,test_size=0.1):
    print('Regression Model Selection...')

    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.svm import SVR
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score
    from sklearn.model_selection import train_test_split
    
    if x_test is None or y_test is None:
        x_train,x_test,y_train,y_test = train_test_split(x_train,y_train,random_state=0,test_size=test_size)

    print('\nLinear Regression ...')
    
    lr=LinearRegression()
    lr.fit(x_train,y_train)
    y_pred_lir = lr.predict(x_test)
    lr_pred=r2_score(y_test, y_pred_lir)
    print('Rsq :',lr_pred )

    print('\nPolinomial Regression ...')
    
    polr=PolynomialFeatures(degree)
    x_polr=polr.fit_transform(x_train)
    polr.fit(x_polr,y_train)
    lr.fit(x_polr,y_train)
    y_pred_poly=lr.predict(polr.fit_transform(x_test))
    poly_pred=r2_score(y_pred_poly,y_test)
    print('Rsq :',poly_pred )

    print('\nSVM Model ...')

    regressor = SVR(kernel = 'rbf')
    regressor.fit(x_train, y_train)
    y_pred=regressor.predict(x_test)
    svr_pred=r2_score(y_test,y_pred)
    print('Rsq :',svr_pred)

    print('\nDesision Tree ...')
    
    d_tree=DecisionTreeRegressor(random_state=1)
    d_tree.fit(x_train,y_train)
    y_pred=d_tree.predict(x_test)
    d_tree_acc=r2_score(y_test,y_pred)
    print('Rsq : ',d_tree_acc)

    print('\nRandom Forest ...')
    
    rand = RandomForestRegressor(n_estimators = 100, random_state = 1)
    rand.fit(x_train,y_train)
    y_pred=rand.predict(x_test)
    ran_for_acc=r2_score(y_test,y_pred)
    print('Rsq :',ran_for_acc)

    l=[lr_pred,poly_pred,svr_pred,d_tree_acc,ran_for_acc]
    x_label=['Lin_Reg','Poly_Reg','Svm','Des_Tr','Rand_For']
    ma=l.index(max(l))

    if ma==0:
        model=lr
    elif(ma==1):
        model=polr
    elif(ma==2):
        model=regressor
    elif(ma==3):
        model=d_tree
    else:
        model=rand
        
    xx=np.arange(0,5)
    plt.plot(xx,l)
    plt.ylabel('Rsq')
    plt.title('Regression Models')
    plt. xticks(xx,x_label)
    plt.show()

    return model

def Get_VIF(X):

    """[summary]
        PARAMETERS :-        
            X = Pandas DataFrame 
        
        Return :-
            Pandas DataFrame of Features and there VIF values
        
    """
    
    def A(X):

        vif_data = pd.DataFrame()
        vif_data["feature"] = X.columns
        vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                           for i in range(len(X.columns))]

        return vif_data

    try:
        return A(X)

    except:
        from statsmodels.stats.outliers_influence import variance_inflation_factor
        return A(X)

metro = pd.read_csv('../data/raw/Metro.csv')
metrobus = pd.read_csv('../data/raw/Metrobus.csv')

metro = metro.iloc[:,2:7]
X_mt = metro.drop(columns=metro.columns[4])
y_mt = metro[metro.columns[4]]
#metrobus = metrobus.iloc[:,2:-1]
#X_mb = metrobus.drop(columns=metro.columns[4])
#y_mb = metrobus[metrobus.columns[4]]

vif = Get_VIF(X_mt)

print(vif)

X_mt1 = X_mt.drop(columns=metro.columns[2])

vif1 = Get_VIF(X_mt1)

print(vif1)

X_mt2 = X_mt1.drop(columns=X_mt1.columns[1])

vif2 = Get_VIF(X_mt2)

print(vif2)


X_train_mt, X_test_mt, y_train_mt, y_test_mt = train_test_split(X_mt2, y_mt, 
                                                                random_state=19)

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
km = 200
px = 120
new_data = pd.DataFrame(np.array([[km, px]]))


X_new = scaler.transform(new_data)
y_hat = model.predict(X_new)
print(y_hat)

## Visualize

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

plt.show()