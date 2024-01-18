def mcculloch_pitts_neuron(inputs, weights, threshold):
    total_input = sum(i * w for i, w in zip(inputs, weights))
    if total_input >= threshold:
        return 1
    else:
        return 0

inputs = [1, 0, 1]
weights = [1, 0, 1]
threshold = 2

output = mcculloch_pitts_neuron(inputs, weights, threshold)
print(f"Output of the neuron: {output}")
