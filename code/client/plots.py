import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

parser = argparse.ArgumentParser(description='Benchmark REST vs GraphQL performance')
parser.add_argument('--mode', choices=['java', 'javascript'], required=True, help="Language mode")
args = parser.parse_args()


def load_time_results():
    rest_results = pd.read_csv(f"results/{args.mode}/response_time/rest_results.csv")
    graphql_results = pd.read_csv(f"results/{args.mode}/response_time/graphql_results.csv")
    return rest_results, graphql_results


def load_size_results():
    rest_results = pd.read_csv(f"results/{args.mode}/response_size/rest_results.csv")
    graphql_results = pd.read_csv(f"results/{args.mode}/response_size/graphql_results.csv")
    return rest_results, graphql_results


def plot_comparative_performance():
    rest_results, graphql_results = load_time_results()

    sns.set(style="whitegrid")

    output_dir = f"results/plots/{args.mode}"
    os.makedirs(output_dir, exist_ok=True)

    # Combine REST and GraphQL results into a single DataFrame for comparison
    rest_results['type'] = 'REST'
    graphql_results['type'] = 'GraphQL'
    combined_results = pd.concat([rest_results, graphql_results], ignore_index=True)

    # Bar plot of average response time for each query type
    plt.figure(figsize=(12, 12))
    avg_response_time = combined_results.groupby(['query', 'type'])['response_time_ms'].mean().unstack()
    avg_response_time.plot(kind='bar', stacked=False, width=0.8)
    plt.title(f'Average Response Time for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Query')
    plt.ylabel('Average Response Time (ms)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/average_response_time.png")
    plt.show()

    # Boxplot for response time distribution comparison
    plt.figure(figsize=(20, 10))
    sns.boxplot(x='response_time_ms', y='query', hue='type', data=combined_results)
    plt.title(f'Response Time Distribution for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Query')
    plt.ylabel('Response Time (ms)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/response_time_distribution.png")
    plt.show()


def plot_comparative_size():
    rest_results, graphql_results = load_size_results()

    sns.set(style="whitegrid")

    output_dir = f"results/plots/{args.mode}"
    os.makedirs(output_dir, exist_ok=True)

    rest_results['type'] = 'REST'
    graphql_results['type'] = 'GraphQL'

    combined_results = pd.concat([rest_results, graphql_results], ignore_index=True)

    # Convert response_size_chars to numeric
    combined_results['response_size_chars'] = pd.to_numeric(combined_results['response_size_chars'], errors='coerce')

    # Bar plot of average response size for each query type
    plt.figure(figsize=(12, 8))
    avg_response_size = combined_results.groupby(['query', 'type'])['response_size_chars'].mean().unstack()
    avg_response_size.plot(kind='bar', stacked=False, width=0.8)
    plt.title(f'Average Response Size for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Query')
    plt.ylabel('Average Response Size (chars)')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Type')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/response_size_comparison.png")
    plt.show()


def plot_total_response_size():
    # Load REST and GraphQL size data
    rest_results = pd.read_csv(f"results/{args.mode}/response_size/rest_results.csv")
    graphql_results = pd.read_csv(f"results/{args.mode}/response_size/graphql_results.csv")

    # Combine data into a single DataFrame
    combined_results = pd.DataFrame({
        'Protocol': ['REST', 'GraphQL'],
        'Total Response Size (chars)': [
            rest_results['total_response_size'].sum(),
            graphql_results['total_response_size'].sum()
        ]
    })

    # Plot the data
    sns.set(style="whitegrid")
    output_dir = f"results/plots/{args.mode}"
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(8, 6))
    sns.barplot(x='Protocol', y='Total Response Size (chars)', data=combined_results, palette='viridis')

    plt.title(f'Total Response Size Comparison - {args.mode.capitalize()}')
    plt.xlabel('Protocol')
    plt.ylabel('Total Response Size (characters)')
    plt.tight_layout()

    # Save the plot
    plt.savefig(f"{output_dir}/total_response_size_comparison.png")
    plt.show()


if __name__ == "__main__":
    plot_comparative_performance()
    plot_total_response_size()
