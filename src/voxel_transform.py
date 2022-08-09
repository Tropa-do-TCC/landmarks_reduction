import os

from dicom_numpy import DicomImportException, combine_slices
from pydicom import dcmread


def get_slices(dcm_dir_name: str = "CT"):
    """
    Get all CT slices from dicom files directory 
    """
    dcm_dir_path = dcm_dir_name
    dcm_files = os.listdir(dcm_dir_name)
    dcm_files_paths = [os.path.join(dcm_dir_path, file) for file in dcm_files]

    slices = [dcmread(file) for file in dcm_files_paths]

    return slices


def extract_voxel_data():
    """
    Extract voxel data and transformation affine matrix from CT slices
    """
    try:
        voxel_ndarray, affine_matrix = combine_slices(get_slices())
    except DicomImportException as ex:
        # invalid DICOM data
        raise

    return voxel_ndarray, affine_matrix
