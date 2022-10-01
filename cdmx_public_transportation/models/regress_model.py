import numpy as np
import matplotlib.pyplot as plt

def Regress_model(x_train,y_train,x_test=None,y_test=None,degree=2,test_size=0.1):
    """_summary_

    Args:
        x_train (_type_): _description_
        y_train (_type_): _description_
        x_test (_type_, optional): _description_. Defaults to None.
        y_test (_type_, optional): _description_. Defaults to None.
        degree (int, optional): _description_. Defaults to 2.
        test_size (float, optional): _description_. Defaults to 0.1.

    Returns:
        _type_: _description_
    """
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