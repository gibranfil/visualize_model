import nibabel as nib
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import glob

class LoadImage :
    def __init__ (self, path='/home/daewogibran/project/3dsegmentation/BraTS20_Training_158/'):
        self.path = path


    def load_path (self) :
        t2_list = glob.glob(self.path + "*t2.nii")
        t1ce_list = glob.glob(self.path + "*t1ce.nii")
        flair_list = glob.glob(self.path + "*flair.nii")
        mask_list = glob.glob(self.path + "*seg.nii")
        list_path = t2_list + t1ce_list + flair_list + mask_list
        return list_path

    def load_image (self) :
        scaler = MinMaxScaler()
        list_path = self.load_path()

        combined = {}
        for idx, i in enumerate(list_path) :
            temp=nib.load(i).get_fdata()
            if idx != 3 :
                temp = scaler.fit_transform(temp.reshape(-1, temp.shape[-1])).reshape(temp.shape)
            else :
                temp = temp.astype(np.uint8)
                temp [temp==4] = 3
            name = idx
            combined[name] = temp

        temp_combined_images = np.stack([combined[0],combined[1],combined[2]], axis=3)
        temp_combined_images = temp_combined_images[56:184, 56:184, 13:141]

        mask = combined[3][56:184, 56:184, 13:141]



        #x = image
        #x_norm = (x-np.min(x))/(np.max(x)-np.min(x))
        ##image = x_norm
        #image = np.stack ((image,image,image),axis=-1)
        #image = np.expand_dims (image, axis=0)
        return temp_combined_images, mask
    

if __name__ == "__main__" :
    test =LoadImage()
    print (test.load_path())