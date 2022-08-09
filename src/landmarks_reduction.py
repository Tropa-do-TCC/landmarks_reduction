import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def scale_data(landmarks_data: pd.DataFrame):
    """
    Normalize data to apply PCA
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(landmarks_data.astype(float))

    return scaled_data


def load_data():
    """
    Load 3D cephalometric landmarks coordinates from text file
    """
    data = pd.read_csv('landmarks_coords.txt', sep=",", header=None)
    data.columns = ["x", "y", "z"]

    return data


def plot_accounted_variance_by_component(components_number: int, explained_variance: list):
    """
    Investigate the variance accounted for by each principal component.
    """
    components = np.arange(components_number)
    plt.figure(figsize=(15, 6))
    plt.bar(components, explained_variance)
    plt.xlabel("Principal Component")
    plt.ylabel("Variance Explained (%)")
    plt.title("Explained Variance Per Principal Component")

    plt.plot()
    plt.show()


def apply_PCA(components_number: int):
    """
    Reduce specified cephalometric landmarks dimension
    """
    landmarks_data = load_data()
    scaled_landmarks_data = scale_data(landmarks_data)

    pca = PCA(n_components=components_number).fit(scaled_landmarks_data)

    explained_variance: list[float] = pca.explained_variance_ratio_
    print(f"explained_variance: {sum(explained_variance)}")

    plot_accounted_variance_by_component(components_number, explained_variance)
