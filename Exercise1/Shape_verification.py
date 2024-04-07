## Self written verification code assisted by ChatGPT

import numpy as np
import tifffile as tiff


def verify_z_step(acquisition_script_path, expected_z_step):
    """
    Verify that the z-step defined in the acquisition script matches the expected z-step.

    :param acquisition_script_path: The path to the acquisition script.
    :param expected_z_step: The expected z-step in micrometers.
    :return: None
    """
    # This is a simplified example and assumes you have a way to extract the z_step from the script.
    # In reality, you may need to parse the script or otherwise determine the z_step.
    z_step_defined_in_script = 0.1  # Example value

    if np.isclose(z_step_defined_in_script, expected_z_step):
        print("Z-step check passed.")
    else:
        print(f"Z-step mismatch: Expected {expected_z_step} um, got {z_step_defined_in_script} um")

# Load the dataset
path_to_dataset = r'C:\Users\chang\Desktop\2024_AssocRDEng_TakeHome\Exercise1\my_acquisition_6\my_acquisition_NDTiffStack.tif'
images = tiff.imread(path_to_dataset)
print(images.shape)

# Example usage:
expected_dims = (9, 12, 512, 512)  # Adjust based on actual expected dimensions
expected_channels = ['DAPI', 'FITC']
expected_z_step = 0.1  # in micrometers

# Verify dimensions
if images.shape[:] != expected_dims[:]:
    print(f"Dimension mismatch: Expected {expected_dims[:]}, got {images.shape[:]}")
else:
    print(images.shape[1:])
    print("Dimension check passed.")

