
def limpiezaBtcVsc(df):
    df[["Price","Open","High","Low","Vol.","Change %"]].replace(to_replace=(",","%"),value="",regex=True).replace(to_replace="M",value="0000",regex=True).replace(to_replace="K",value="0",regex=True).replace(to_replace="B",value="0000000",regex=True).astype(float)
    return df
