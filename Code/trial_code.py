import numpy as np

def predict_class(input_data):
    data_df = np.genfromtxt('color_data_test3.csv', delimiter=',', skip_header=1)
    data = data_df[:, 3:-1]
    pred = data_df[:, -1]

    def manual_standard_scaler(data):
        mean = np.mean(data, axis=0)
        std_dev = np.std(data, axis=0)
        scaled_data = (data - mean) / std_dev
        return scaled_data, mean, std_dev

    scaled_data, mean, std_dev = manual_standard_scaler(data)

    def euclidean_distance(point1, point2):
        return np.sqrt(np.sum((np.array(point2) - np.array(point1)) ** 2))

    scaled_input = (input_data - mean) / std_dev
    distances_and_labels = []

    for i in range(data.shape[0]):
        distance = euclidean_distance(scaled_input, scaled_data[i])
        distances_and_labels.append((distance, pred[i]))

    distances_and_labels.sort()
    k = 3
    nearest_neighbors = distances_and_labels[:k]

    class_counts = {}
    for _, label in nearest_neighbors:
        if label in class_counts:
            class_counts[label] += 1
        else:
            class_counts[label] = 1

    pred_val = max(class_counts, key=class_counts.get)
    return pred_val
