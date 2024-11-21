import requests
import time
import csv
import argparse
import json

parser = argparse.ArgumentParser(description='Benchmark REST vs GraphQL performance')
parser.add_argument('--mode', choices=['java', 'javascript'], required=True, help="Language mode")
args = parser.parse_args()

if args.mode == 'java':
    REST_BASE_URL = "http://localhost:8080/rest/comments"
    GRAPHQL_URL = "http://localhost:8080/graphql"
elif args.mode == 'javascript':
    REST_BASE_URL = "http://localhost:3000/comments"
    GRAPHQL_URL = "http://localhost:3001/"

REST_ENDPOINTS = [
    {"name": "allComments", "url": REST_BASE_URL},
    {"name": "commentById", "url": f"{REST_BASE_URL}/4"},
    {"name": "commentsByUserId", "url": f"{REST_BASE_URL}/user/13"},
    {"name": "commentsByMinScore", "url": f"{REST_BASE_URL}/min-score/5"},
]

GRAPHQL_QUERIES = [
    {"name": "allComments", "query": "{ allComments { id } }"},
    {"name": "commentById", "query": "query($id: ID!) { commentById(id: $id) { id } }", "variables": {"id": 4}},
    {"name": "commentsByUserId", "query": "query($id: ID!) { commentsByUserId(id: $id) { id } }",
     "variables": {"id": 13}},
    {"name": "commentsByMinScore", "query": "query($score: Int!) { commentsByMinScore(score: $score) { id } }",
     "variables": {"score": 5}},
]

graphql_responses = []
rest_responses = []


def count_chars_in_json_array(json_array):
    combined_json_str = json.dumps(json_array)
    return sum(1 for char in combined_json_str if not char.isspace())

def benchmark_rest():
    results = []
    for endpoint in REST_ENDPOINTS:
        for _ in range(100):
            start_time = time.time()
            response = requests.get(endpoint["url"])
            end_time = time.time()
            rest_responses.append(response.json())
            results.append({
                "query": endpoint["name"],
                "status_code": response.status_code,
                "response_time_ms": (end_time - start_time) * 1000,
            })
    return results


def benchmark_graphql():
    results = []
    for query in GRAPHQL_QUERIES:
        for _ in range(100):
            start_time = time.time()
            response = requests.post(GRAPHQL_URL, json={
                "query": query["query"],
                "variables": query.get("variables", {}),
            })
            graphql_responses.append(response.json())
            end_time = time.time()
            results.append({
                "query": query["name"],
                "status_code": response.status_code,
                "response_time_ms": (end_time - start_time) * 1000,
            })
    return results



def save_to_csv(filename, data, fieldnames):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# if __name__ == "__main__":
#     response = requests.post(GRAPHQL_URL, json={
#         "query": "{ allComments { id } }",
#         "variables": {},
#     })
#
#     print(response.content)

#
if __name__ == "__main__":
    # Benchmark REST
    print(f"Benchmarking REST endpoints in {args.mode} mode...")
    rest_results = benchmark_rest()
    save_to_csv(f"results/{args.mode}/response_time/rest_results.csv", rest_results, ["query", "status_code", "response_time_ms"])
    print("REST results saved to rest_results.csv")

    save_to_csv(f"results/{args.mode}/response_size/rest_results.csv",
    [
            {
                "protocol": "rest",
                "total_response_size": count_chars_in_json_array(rest_responses)
            }
        ],
        ["protocol", "total_response_size"]
    )

    # Benchmark GraphQL
    print(f"Benchmarking GraphQL queries in {args.mode} mode...")
    graphql_results = benchmark_graphql()
    save_to_csv(f"results/{args.mode}/response_time/graphql_results.csv", graphql_results,
                ["query", "status_code", "response_time_ms"])

    save_to_csv(f"results/{args.mode}/response_size/graphql_results.csv",
    [
            {
                "protocol": "graphql",
                "total_response_size": count_chars_in_json_array(graphql_responses)
            }
        ],
        ["protocol", "total_response_size"]
    )

    print("GraphQL results saved to graphql_results.csv")
