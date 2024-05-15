import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar la base de datos desde un archivo CSV
data = pd.read_csv("Mall_Customers.csv")

# Mostrar las primeras filas del DataFrame para comprender la estructura de los datos
print(data.head())

# Obtener estadísticas descriptivas de las variables numéricas
print(data.describe())

# Gráfico de distribución de variables
sns.pairplot(data)
plt.show()

# Boxplot para identificar valores atípicos
sns.boxplot(data=data)
plt.show()
