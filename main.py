from src.landmarks_reduction import apply_PCA
from src.voxel_transform import extract_voxel_data


def main():
    _, affine_matrix = extract_voxel_data()

    apply_PCA(components_number=2)

    print(f"affine_matrix: {affine_matrix}")


if __name__ == '__main__':
    main()
