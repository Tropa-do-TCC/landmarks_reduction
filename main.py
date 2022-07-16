#!/usr/bin/env python
import os

import dicom
import dicomtools
import pydicom
from dicomtools.series import DicomSeries


def main():
    dcm_path = f"CT/CT000015.dcm"

    print(os.path.abspath(dcm_path))

    file = pydicom.read_file(dcm_path)

    print(file)

    series = DicomSeries([file])
    print(series)

    volume = dicomtools.volume.DicomVolume(series)

    dicomtools.visualization.plot_slice(volume, 2, 0)


if __name__ == '__main__':
    main()
