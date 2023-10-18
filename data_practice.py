# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
read_in_array = np.loadtxt("lab2_clyde_data.txt")
time_millis = read_in_array[:, 0]
dist_cm = read_in_array[:, 1]

# Time from ms to s
time_s = time_millis / 1000

# Distance from cm to m
dist_m = dist_cm / 100

lower_index = 2
lower_time_limit = time_millis[lower_index]
print("The lower time cutoff is " + str(lower_time_limit))


upper_index = 49
upper_time_limit = time_millis[upper_index]
print("The upper time cutoff is " + str(upper_time_limit))

# Create new arrays for the time window and distance window that we care about
time_window = time_s[lower_index:upper_index]
dist_window = dist_m[lower_index:upper_index]

plt.plot(time_window, dist_window)

coeff_quad = np.polyfit(time_window, dist_window, 2)
y_fit = coeff_quad[0] * time_window**2 + coeff_quad[1] * time_window + coeff_quad[2]
# f(x) = ax^2 + bx + c


# x(t) = X0 + Vo(t) + (1/2) Ao(t)^2
plt.scatter(time_window, dist_window, label="Data")
plt.plot(time_window, y_fit, label="Model")
plt.legend()
# Add axes labels
plt.title("Time Vs. Position")
plt.xlabel("Time (s)")
plt.ylabel("Position (cm)")
# %%
