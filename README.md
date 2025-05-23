# 📞 Monte Carlo Simulation of Customer Call Duration

This project uses a Monte Carlo simulation to model the total time a customer service representative spends trying to contact a customer. It was developed as part of a probability course at the University of Virginia.

## 🧠 Problem Description

Each customer call attempt includes:
- 6 seconds to dial
- 1 second to end the call
- A random outcome:
  - **20% chance**: Line is busy → +3 seconds
  - **30% chance**: No answer (5 rings) → +25 seconds
  - **50% chance**: Customer may answer → Exponential wait time (λ = 1/12), max 25 seconds

The representative retries up to **4 times** or until the customer picks up.

## 🎯 Project Goals

- Simulate 500 independent customer interactions
- Calculate and analyze:
  - Mean and quartiles of total time (W)
  - Probability distributions (e.g., P[W ≤ 15], P[W > 106])
- Visualize the cumulative distribution function (CDF) of W
- Provide insights for staffing and call time expectations

## 🛠️ Implementation

- **Language:** Python
- **Randomness:** Custom Linear Congruential Generator (LCG)
- **Distributions:** Uniform and Exponential
- **Visualization:** `matplotlib`

## 📈 Key Findings

- The average call time was **~41.6 seconds**
- Distribution is **right-skewed**, with most calls taking less time
- Rare but significant tail cases can take up to **128 seconds**

These insights can help businesses estimate call handling times and optimize call center operations.

## 📚 Skills Used

- Monte Carlo Simulation
- Probability Modeling
- Python Programming
- Data Visualization
- Statistical Analysis

## 📄 License

This project is part of a course assignment and is shared for educational purposes only.

---