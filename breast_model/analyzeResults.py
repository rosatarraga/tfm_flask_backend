import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

from src.modeling.run_model_single import (
    load_model, load_inputs, process_augment_inputs, batch_to_tensor
)
import src.utilities.pickling as pickling

shared_parameters = {
    "device_type": "gpu",
    "gpu_number": 1,
    "max_crop_noise": (100, 100),
    "max_crop_size_noise": 100,
    "batch_size": 1,
    "seed": 0,
    "augmentation": True,
    "use_hdf5": True,
}

random_number_generator = np.random.RandomState(shared_parameters["seed"])

image_only_parameters = shared_parameters.copy()
image_only_parameters["view"] = "R-CC"
image_only_parameters["use_heatmaps"] = False
image_only_parameters["model_path"] = "models/ImageOnly__ModeImage_weights.p"
model, device = load_model(image_only_parameters)

model_input = load_inputs(
    image_path="sample_single_output/cropped.png",
    metadata_path="sample_single_output/cropped_metadata.pkl",
    use_heatmaps=False,
)

batch = [
    process_augment_inputs(
        model_input=model_input,
        random_number_generator=random_number_generator,
        parameters=image_only_parameters,
    ),
]
tensor_batch = batch_to_tensor(batch, device)
y_hat = model(tensor_batch)

predictions = np.exp(y_hat.cpu().detach().numpy())[:, :2, 1]
predictions_dict = {
    "benign": float(predictions[0][0]),
    "malignant": float(predictions[0][1]),
}
print(predictions_dict)