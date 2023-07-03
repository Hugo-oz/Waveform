from main import*

# Test waveform
T = np.array([0, 1, 2,  3, 4, 5, 6,  7, 8, 9, 10])
Y = np.array([0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0])

# Delta time for waveform sampling
delta_t = 0.5

# Get value at time t
t = 3.53
value = get_value_at_time(T, Y, t)
print(f"The waveform value at time {t} is: {value}\n")

# Sample the waveform
sampled_T, sampled_Y = sample_waveform(T, Y, delta_t)
print("Sampled waveform:")
for t, y in zip(sampled_T, sampled_Y):
    print(f"Time: {t}, Value: {y}")