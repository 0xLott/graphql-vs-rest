import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

parser = argparse.ArgumentParser(description='Benchmark REST vs GraphQL performance')
parser.add_argument('--mode', choices=['java', 'javascript'], required=True, help="Language mode")
args = parser.parse_args()


def load_results():
    rest_results = pd.read_csv(f"results/{args.mode}/rest_results.csv")
    graphql_results = pd.read_csv(f"results/{args.mode}/graphql_results.csv")
    return rest_results, graphql_results


# Generate comparative plots
def plot_comparative_performance():
    # Load the results
    rest_results, graphql_results = load_results()

    # Set up the seaborn style
    sns.set(style="whitegrid")

    # Combine REST and GraphQL results into a single DataFrame for comparison
    rest_results['type'] = 'REST'
    graphql_results['type'] = 'GraphQL'
    combined_results = pd.concat([rest_results, graphql_results], ignore_index=True)

    # Bar plot of average response time for each query type
    plt.figure(figsize=(12, 6))
    avg_response_time = combined_results.groupby(['query', 'type'])['response_time_ms'].mean().unstack()
    avg_response_time.plot(kind='bar', stacked=False, width=0.8)
    plt.title(f'Average Response Time for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Query')
    plt.ylabel('Average Response Time (ms)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Boxplot for response time distribution comparison
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='query', y='response_time_ms', hue='type', data=combined_results)
    plt.title(f'Response Time Distribution for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Query')
    plt.ylabel('Response Time (ms)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Histogram of response times for both REST and GraphQL
    plt.figure(figsize=(12, 6))
    sns.histplot(data=combined_results, x='response_time_ms', hue='type', multiple="stack", bins=30)
    plt.title(f'Response Time Distribution for {args.mode.capitalize()} - REST vs GraphQL')
    plt.xlabel('Response Time (ms)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_comparative_performance()
