const citiesData = {
            A: {
                BFS: { duration: 18.949, expandedNodes: 21, visitedNodes: 16, cost: 450 },
                DFS: { duration: 12.965, expandedNodes: 18, visitedNodes: 10, cost: 733 },
                Branch_and_bound_Without: { duration: 36.904, expandedNodes: 31, visitedNodes: 24, cost: 418 },
                Branch_and_bound_With: { duration: 25.456, expandedNodes: 16, visitedNodes: 6, cost: 418 }
            },
            O: {
                BFS: { duration: 79.784, expandedNodes: 45, visitedNodes: 43, cost: 730 },
                DFS: { duration: 40.411, expandedNodes: 41, visitedNodes: 31, cost: 698 },
                Branch_and_bound_Without: { duration: 47.872, expandedNodes: 43, visitedNodes: 40, cost: 698 },
                Branch_and_bound_With: { duration: 60.837, expandedNodes: 32, visitedNodes: 15, cost: 698 }
            },
            B: {
                BFS: { duration: 14.96, expandedNodes: 21, visitedNodes: 16, cost: 450 },
                DFS: { duration: 11.967, expandedNodes: 18, visitedNodes: 10, cost: 733 },
                Branch_and_bound_Without: { duration: 23.972, expandedNodes: 31, visitedNodes: 24, cost: 418 },
                Branch_and_bound_With: { duration: 15.957, expandedNodes: 16, visitedNodes: 6, cost: 418 }
            },
            E: {
                BFS: { duration: 59.838, expandedNodes: 45, visitedNodes: 43, cost: 730 },
                DFS: { duration: 32.948, expandedNodes: 41, visitedNodes: 31, cost: 698 },
                Branch_and_bound_Without: { duration: 40.891, expandedNodes: 43, visitedNodes: 40, cost: 698 },
                Branch_and_bound_With: { duration: 45.907, expandedNodes: 32, visitedNodes: 15, cost: 698 }
            },
            G: {
                BFS: { duration: 66.339, expandedNodes: 41, visitedNodes: 34, cost: 615 },
                DFS: { duration: 27.924, expandedNodes: 32, visitedNodes: 21, cost: 1284 },
                Branch_and_bound_Without: { duration: 40.894, expandedNodes: 41, visitedNodes: 35, cost: 583 },
                Branch_and_bound_With: { duration: 32.912, expandedNodes: 26, visitedNodes: 12, cost: 583 }
            },
            N: {
                BFS: { duration: 47.869, expandedNodes: 32, visitedNodes: 26, cost: 765 },
                DFS: { duration: 24.933, expandedNodes: 31, visitedNodes: 19, cost: 1151 },
                Branch_and_bound_Without: { duration: 33.908, expandedNodes: 32, visitedNodes: 26, cost: 765 },
                Branch_and_bound_With: { duration: 28.922, expandedNodes: 23, visitedNodes: 12, cost: 765 }
            },
            M: {
                BFS: { duration: 33.909, expandedNodes: 31, visitedNodes: 23, cost: 520 },
                DFS: { duration: 27.933, expandedNodes: 29, visitedNodes: 18, cost: 928 },
                Branch_and_bound_Without: { duration: 35.046, expandedNodes: 36, visitedNodes: 27, cost: 520 },
                Branch_and_bound_With: { duration: 83.776, expandedNodes: 25, visitedNodes: 16, cost: 520 }
            },
        };

        function createChart(city, metric, label, data) {
            const canvasId = `${city}_${metric}Chart`;
            const chartConfig = {
                type: 'bar',
                data: {
                    labels: Object.keys(data),
                    datasets: [
                        {
                            label: `Expanded Nodes`,
                            data: Object.values(data).map(item => item.expandedNodes),
                            backgroundColor: 'rgba(75, 192, 192, 0.6)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        },
                        {
                            label: `Visited Nodes`,
                            data: Object.values(data).map(item => item.visitedNodes),
                            backgroundColor: 'rgba(255, 99, 132, 0.6)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                color: "#ffffff"
                            }
                        },
                        x: {
                            ticks: {
                                color: '#ffffff'
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: '#ffffff'
                            }
                        }
                    }
                }
            };
            new Chart(document.getElementById(canvasId).getContext('2d'), chartConfig);
        }

        createChart('A', 'duration', 'Duration', citiesData.A);
        createChart('O', 'duration', 'Duration', citiesData.O);
        createChart('G', 'duration', 'Duration', citiesData.G);
        createChart('N', 'duration', 'Duration', citiesData.N);