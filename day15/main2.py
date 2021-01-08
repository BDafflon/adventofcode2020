history = {value: i + 1 for i, value in enumerate([14,8,16,0,1,17])}
previous = list(history)[-1]
for turn in range(len(history), 30_000_000):
    history[previous], previous = turn, turn - history.get(previous, turn)
print(previous)