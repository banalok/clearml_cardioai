import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Load the NIfTI file
img = nib.load(r'F:\icardio\data\test_slice.nii')

# Get the data array
data = img.get_fdata()
#data_array = np.array(data)
print(data.shape)
plt.imshow(data[:,:,0])
plt.show()
# Save the slice as a new NIfTI file
#slice_data = data[:, :, 44]
#new_img = nib.Nifti1Image(slice_data, affine=img.affine)
#nib.save(new_img, 'test_slice.nii')

# Display a slice of the data
#slice_0 = data[:, :, data.shape[2] // 2]

#plt.imshow(slice_0.T, cmap='gray', origin='lower')
#plt.title('Middle Slice of NIfTI Image')
#plt.show()
