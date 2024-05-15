from sklearn.cluster import KMeans

# Entrenar el modelo K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_scaled)

from scipy.cluster.hierarchy import linkage, dendrogram

# Calcular enlace
Z = linkage(data_scaled, method='ward')

# Dendrograma
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.show()
