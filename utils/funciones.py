
import matplotlib.pyplot as plt
import seaborn as sns

def limpiezaBtcVsc(df):
    df[["Price","Open","High","Low","Vol.","Change %"]].replace(to_replace=(",","%"),value="",regex=True).replace(to_replace="M",value="0000",regex=True).replace(to_replace="K",value="0",regex=True).replace(to_replace="B",value="0000000",regex=True).astype(float)
    return df

def graficaCorrelacion(df):
    plt.figure(figsize=(7,7))
    sns.heatmap(df.corr(),
            vmin=-1,
            vmax=1,
            cmap='jet',
            linecolor="black",
            square=True,
            linewidths=.3,
            annot=True)
    plt.title("Correlacion Precio Bitcoin Volumen Busquedas");