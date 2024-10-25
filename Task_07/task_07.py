import random

num_simulations = 1000000

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Підрахунок к-ті випадків для кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sum_counts[dice_sum] += 1

# Обчислення ймовірностей для симуляції:
simulated_probablilies = {s: (count / num_simulations) * 100 for s, count in sum_counts.items()}

print("Див. readme.md для висновків щодо порівняння результатів.")

# Виводимо результат симуляції та порівняння з аналітичними результатами
print("Сума\tІмовіорність (Монте- Карло)\tІмовірність (аналітична)\tРізниця")
for s in range(2, 13):
    simulated = simulated_probablilies[s]
    analytical = analytical_probabilities [s]
    difference = simulated - analytical
    print(f"{s}\t{simulated:.2f}%\t\t{analytical:.2f}%\t\t{difference:.2f}%")
    
