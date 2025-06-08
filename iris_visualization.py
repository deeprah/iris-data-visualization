# iris_visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
df = sns.load_dataset("iris")

# Display first 5 rows
print(df.head())

# Pairplot to show relationships
sns.pairplot(df, hue="species", palette="bright")
plt.savefig("pairplot.png")

# Boxplot to compare petal length by species
plt.figure(figsize=(8, 6))
sns.boxplot(x="species", y="petal_length", data=df)
plt.title("Petal Length by Species")
plt.savefig("boxplot_petal_length.png")

# Heatmap of correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop("species", axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
