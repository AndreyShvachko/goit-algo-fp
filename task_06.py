items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorythm(items, budget):
    #створення списку зі страв, відсортованих за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return chosen_items, total_calories, total_cost 

def dynamic_programming(items, budget):

    # ініціалізуємо таблицю для зберігання максимальних калорій
    dp =[[0 for _ in range(budget + 1)] for _ in range(len(items) +1)]
    item_names = list(items.keys())

    # заповнення таблиці dp
    for i in range(1, len(items) + 1):
        item_name = item_names[i -1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]

        for b in range(budget + 1):
            if item_cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - item_cost] + item_calories)
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[len(items)][budget]
    total_cost = 0
    chosen_items = []
    b = budget

    for i in range(len(items), 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(item_names[i - 1])
            total_cost += items[item_names[i - 1]]["cost"]
            b -= items [item_names[i - 1]]["cost"]

    return chosen_items, total_calories, total_cost

if __name__ == "__main__":
    budget = 100

    # Використання жадібного алгоритму
    chosen_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorythm(items, budget)
    print(f"Жадібний алгоритм:")
    print(f"Обрані страви: {chosen_items_greedy}, Загальні калорії: {total_calories_greedy}, Загальна вартість: {total_cost_greedy}")
    
    # Використання алгоритму динамічного програмування
    chosen_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
    print(f"\nДинамічне програмування:")
    print(f"Обрані страви: {chosen_items_dp}, Загальні калорії: {total_calories_dp}, Загальна вартість: {total_cost_dp}")

