import numpy as np

def get_value_at_time(T, Y, t):
    # This function returns the interpolation of the function (T, Y) at the time t.
    return np.interp(t, T, Y)

def sample_waveform(T, Y, delta_t):
    # Make a sample array in time from the first sample to the last sample in delta_t steps.
    sampled_T = np.arange(T[0], T[-1]+delta_t, delta_t)
    # Interpolates the waveform T, Y at the sampled time (sampled_T).
    sampled_Y = np.interp(sampled_T, T, Y)
    # Return the sampled waveform 
    return sampled_T, sampled_Y