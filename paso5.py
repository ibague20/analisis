from sklearn.metrics import silhouette_score, calinski_harabasz_score

# Coeficiente de Silhouette
silhouette_score(data_scaled, kmeans.labels_)

# Índice de Calinski-Harabasz
calinski_harabasz_score(data_scaled, kmeans.labels_)
