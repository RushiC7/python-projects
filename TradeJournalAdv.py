import numpy as np

trades = np.array([
    [100, 110],[95, 90],[105, 120]])
profit=trades[:, 1] - trades[:, 0]
profitArray=np.array(profit)
Avg=np.mean(profitArray)
MaxP=np.max(profitArray)
print(f"Win: {len(profitArray[profitArray > 0])}")
print(f"Loss: {len(profitArray[profitArray < 0])}")
print(f"Win Rate: {len(profitArray[profitArray > 0]) / len(profitArray) * 100:.2f}%")
print(f"Profit: {profitArray}")
print(f"Average Profit: {Avg}")
print(f"Maximum Profit: {MaxP}")