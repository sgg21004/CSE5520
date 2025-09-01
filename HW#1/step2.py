import plotly.graph_objects as go

# Same correct Fibonacci logic
def fibonacci_sequence(n):
    sequence = []
    n1, n2 = 0, 1
    for _ in range(n):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return sequence

# Generate and save a bar chart using Plotly
def generate_plotly_chart(num_terms):
    sequence = fibonacci_sequence(num_terms)
    x_labels = list(range(1, num_terms + 1))

    fig = go.Figure(data=[
        go.Bar(x=x_labels, y=sequence, name='Fibonacci')
    ])

    fig.update_layout(
        title=f'Fibonacci Sequence ({num_terms} terms)',
        xaxis_title='Term Index',
        yaxis_title='Fibonacci Number'
    )

    filename = f'fibonacci_{num_terms}_terms.html'
    fig.write_html(filename)
    print(f"HTML file saved: {filename}")

# Main
if __name__ == "__main__":
    generate_plotly_chart(10)
    generate_plotly_chart(50)