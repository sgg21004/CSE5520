import pygal

# Correct Fibonacci sequence generator
def fibonacci_sequence(n):
    sequence = []
    n1, n2 = 0, 1
    for _ in range(n):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return sequence

# Generates and returns a pygal Bar chart object
def generate_plot_items(num):
    fib_items = fibonacci_sequence(num)

    bar_chart = pygal.Bar()
    bar_chart.title = f'Fibonacci Sequence ({num} terms)'
    bar_chart.x_labels = list(range(1, num + 1))
    bar_chart.add('Fibonacci', fib_items)

    return bar_chart

# Main code: generate and save two plots
if __name__ == "__main__":
    generate_plot_items(10).render_to_file('fibonacci_10_terms.svg')
    generate_plot_items(50).render_to_file('fibonacci_50_terms.svg')
    print("SVG files saved: fibonacci_10_terms.svg and fibonacci_50_terms.svg")