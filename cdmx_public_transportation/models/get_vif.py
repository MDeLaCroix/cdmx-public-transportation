import pandas as pd

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