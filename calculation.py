import matplotlib.pyplot as plt


class contract_grid():
    def __init__(self, High_value, Low_value, Grid_number, Multiple, Initial_value):
        self.high_value = High_value
        self.low_value = Low_value
        self.grid_number = Grid_number
        self.multiple = Multiple
        self.initial_value = Initial_value
        self.one_position_value = (
            Initial_value * self.multiple * 2) / ((High_value + Low_value) * Grid_number)
        self.one_position_gap = (High_value - Low_value) / (Grid_number)

    def liquidate_calculation(self, Now_price):
        A = int((Now_price - self.low_value) / self.one_position_gap)

        if A < 0:
            A = 0
        elif A > self.grid_number:
            A = self.grid_number

        P_A = self.low_value + A * self.one_position_gap
        P_L = -0.5 * ((2 * self.initial_value) / (A * self.one_position_value)
                      - P_A - self.low_value)
        P_H = 0.5 * ((2 * self.initial_value) / ((self.grid_number - A) * self.one_position_value)
                     + P_A + self.high_value)
        return P_L, P_H


# ------------Parameter------------
now_price_list = [i for i in range(50, 4000, 1)]
grid_range = 400
grid_numbers = 149
multiple = 5
initial_captial = 300
# ---------------End---------------
x = []
y_L = []
y_L_g = []
y_H = []
y_H_g = []
for now_price in now_price_list:
    ETHBUSD = contract_grid(High_value=now_price + grid_range, Low_value=now_price - grid_range,
                            Grid_number=grid_numbers, Multiple=multiple, Initial_value=initial_captial)
    try:
        re = ETHBUSD.liquidate_calculation(now_price)
    except:
        pass
    x.append(now_price)
    y_L.append(re[0])
    y_L_g.append(abs(now_price - re[0]))
    y_H.append(re[1])
    y_H_g.append(abs(now_price - re[1]))

print(f"x_first: {x[0]}, y_H_first: {y_H[0]}, y_L_first: {y_L[0]}")
print(f"x_last: {x[-1]}, y_H_last: {y_H[-1]}, y_L_last: {y_L[-1]}")
print(
    f"ratio_y_H: {(y_H[-1] - y_H[0]) / 3950}, ratio_y_L: {(y_L[-1] - y_L[0]) / 3950}")

fig, axs = plt.subplots(3)
fig.tight_layout(pad=2.0)
axs[0].set_title("Price and Liquidate")
axs[0].plot(x, y_L, label="Low Liquidate")
axs[0].plot(x, y_H, label="High Liquidate")
axs[0].plot([50, 4000], [50, 4000], label="Now Price")
axs[0].legend()
axs[1].set_title("Low Liquidate Gap")
axs[1].plot(x, y_L_g)
axs[2].set_title("High Liquidate Gap")
axs[2].plot(x, y_H_g)
plt.show()
