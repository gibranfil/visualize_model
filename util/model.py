import tensorflow as tf
import os



class ModelLoad:
    def __init__(self, path='model.hdf5', savesummary='model.png'):
        self.path = path
        self.save_path = savesummary

    def model (self) :
        model = tf.keras.models.load_model(self.path, compile=False)

        return model

    def plot_model (self) :
        if os.path.exists (self.save_path) :
            pass
        else :
            tf.keras.utils.plot_model(self.model(), to_file="model.png",
                show_shapes=True)