import tensorflow as tf
from keras.models import Model
import numpy as np

class LayerExtract:
    def __init__(self, model, input):
        self.model = model
        self.input = np.expand_dims (input, axis =0)

    def layer_count (self):
        layer_names = [layer.name for layer in self.model.layers]
        return layer_names

    def save_output (self):
        output=[]
        layer_names = self.layer_count()
        for i in layer_names :
            intermediate_layer_model = Model(inputs=self.model.input,
                                        outputs=self.model.get_layer(i).output)
            intermediate_output = intermediate_layer_model.predict(self.input)
            output.append (intermediate_output)
        return output