import math
import matplotlib.pyplot as plt

a = 24693  # multiplier
c = 3517  # increment
K = 2 ** 17  # modulus
probabilities = []
times = []


# a numerical algorithm which outputs a sequence of real
# numbers from the interval (0, 1), termed pseudo-random numbers, which the observer unfamiliar
# with the algorithm, as well as the standard statistical tests, cannot distinguish from a sample of
# independent realizations (observations) of a uniform random variable.
def random_num(n):  # generates random probabilities
    x_i = 1000  # starts at 1000
    # 𝑥𝑖 = (𝑎 𝑥𝑖−1 + 𝑐)(𝑚𝑜𝑑𝑢𝑙𝑜 K)
    # 𝑢𝑖 = 𝑑𝑒𝑐𝑖𝑚𝑎𝑙 𝑟𝑒𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛 𝑜𝑓 𝑥𝑖/𝐾
    for i in range(1, n):
        x_i = (a * x_i + c) % K
        u_i = x_i / K
        probabilities.append(u_i)
        if 50 < i < 54:
            print("u_" + str(i) + ": " + str(round(u_i,4)))
    return probabilities


def customer_status(prob):
    if prob < 0.2:
        return "busy"
    elif prob < 0.5:
        return "unavailable"
    else:
        return "available"


# computes the time it takes
def answer_time(prob):
    # lambda = 1/12
    # u = 1 - e^-(lambda)(x)
    # inverse: x = 12ln(1 - u)
    x = -12 * math.log(1 - prob)
    return x  # time it takes in seconds for customer to answer phone
   

def sim_W(random_numbers, index):
    time_W = 0
    calls = 0
    while calls < 4:
        calls += 1
        time_W += 6  # 6 seconds to dial
        prob_avail = random_numbers[index] # probability that customer is busy, available, or unavailable
        status = customer_status(prob_avail)
        index += 1
        if status == "busy":
            time_W += 3  # detect busy
        elif status == "unavailable":
            time_W += 25  # 5 rings no answer
        else:  # available
            prob_ans = random_numbers[index]  # probability that customer answers if they're available
            index += 1
            time = answer_time(prob_ans)
            if time <= 25:
                time_W += time
                time_W += 1  # end call
                break  # customer answered
            else:
                time_W += 25  # 5 rings no answer
        time_W += 1  # end call
    return time_W, index


prob_list = random_num(20000)
W_values = []
ind = 0

for i in range(500):
    W, ind = sim_W(prob_list, ind)
    W_values.append(W)

# Sort values for report
W_values_sorted = sorted(W_values)

W_mean = sum(W_values_sorted) / len(W_values_sorted)

# Thresholds for probability checks
w5 = W_values_sorted[int(0.80 * len(W_values_sorted))]  # 80th percentile
w6 = W_values_sorted[int(0.90 * len(W_values_sorted))]  # 90th percentile
w7 = W_values_sorted[int(0.95 * len(W_values_sorted))]  # 95th percentile

# Compute probabilities
p_le_15 = sum(w <= 15 for w in W_values_sorted) / len(W_values_sorted)
p_le_20 = sum(w <= 20 for w in W_values_sorted) / len(W_values_sorted)
p_le_30 = sum(w <= 30 for w in W_values_sorted) / len(W_values_sorted)
p_g_40 = sum(w > 40 for w in W_values_sorted) / len(W_values_sorted)
p_g_w5 = sum(w > w5 for w in W_values_sorted) / len(W_values_sorted)
p_g_w6 = sum(w > w6 for w in W_values_sorted) / len(W_values_sorted)
p_g_w7 = sum(w > w7 for w in W_values_sorted) / len(W_values_sorted)

n = len(W_values_sorted)
if n % 2 == 1:
    # If odd, take the middle value
    median = W_values_sorted[n // 2]
else:
    # If even, take the average of the two middle values
    median = (W_values_sorted[n // 2 - 1] + W_values_sorted[n // 2]) / 2

def quartile(sorted_data, percentile):
    n = len(sorted_data)
    pos = percentile * (n - 1)
    lower = int(pos)
    upper = lower + 1
    if upper >= n:
        return sorted_data[lower]
    weight = pos - lower
    return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight

Q1 = quartile(W_values_sorted, 0.25)
Q3 = quartile(W_values_sorted, 0.75)

# Print results
print(W_values_sorted)
print(len(W_values_sorted))
print(W_mean)
print("Median:", median)
print("First Quartile (Q1):", Q1)
print("Third Quartile (Q3):", Q3)
print(f"P(W ≤ 15) = {round(p_le_15, 4)}")
print(f"P(W ≤ 20) = {round(p_le_20, 4)}")
print(f"P(W ≤ 30) = {round(p_le_30, 4)}")
print(f"P(W > 40) = {round(p_g_40, 4)}")
print(f"P(W > (w_5 = {w5})) = {round(p_g_w5, 4)}")
print(f"P(W > (w_6 = {w6})) = {round(p_g_w6, 4)}")
print(f"P(W > (w_7 = {w7})) = {round(p_g_w7, 4)}")


# Given data points for W and their corresponding cumulative probabilities
W_values = [15, 20, 30, 40, 72.93, 84.99, 106]
probabilities = [0.256, 0.362, 0.486, 0.552, 0.802, 0.902, 0.96]

# Plot the CDF using the provided values
plt.plot(W_values, probabilities, marker='.', linestyle='-', color='b')

# Adding title and labels
plt.title('Cumulative Distribution Function (CDF) of W')
plt.xlabel('W (Total Time Spent by Representative)')
plt.ylabel('Cumulative Probability')

# Adding grid for better visualization
plt.grid(True)

# Display the plot
plt.show()

