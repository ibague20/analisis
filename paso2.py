from sklearn.preprocessing import StandardScaler

# Verificar valores faltantes
print(data.isnull().sum())

# Normalizar variables numéricas
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
