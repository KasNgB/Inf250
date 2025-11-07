from sklearn import datasets
from sklearn import decomposition
import pandas as pd
import matplotlib.pyplot as plt

data = datasets.load_iris()

dataframe = pd.DataFrame(data.data, columns=data.feature_names)
dataframe['species'] = pd.Categorical.from_codes(data.target, data.target_names)
pca = decomposition.PCA(n_components=3)
data_reduced = pca.fit_transform(data.data)
print(dataframe)


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

dataframe.plot.scatter(ax=axes[0], x="sepal width (cm)", y="sepal length (cm)")
print("Variance explained by each component:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"PC{i+1}: {var:.2f}")

# dataframe['sepal length (cm)'].hist(ax=axes[1])

# plt.scatter(data_reduced[:,1],data_reduced[:,2], c=data.target)
# plt.xlabel('PCA Component 1')
# plt.ylabel('PCA Component 2')
# plt.title('PCA (3 Components, Showing 1st and 2nd)')


# plt.show()



