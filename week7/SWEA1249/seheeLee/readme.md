## 풀이
다익스트라 알고리즘은 여러가지 노드와 간선이 연결되어 있을 때
노드를 이동할 때 마다 최적인 거리값으로 업데이트하며 목적지까지 최소거리를 찾는 알고리즘입니다. 

이 문제를 잘 보면,  상하좌우 각각 노드와 연결되어 있는 비용이 있는 그래프로 볼 수 있습니다. 그렇다면 다익스트라 알고리즘을 적용할 수 있습니다. 


이 문제는 모든 경우를 탐색하지 않으면 알 수 없기 때문에 완전탐색해야합니다. 

다익스트라 알고리즘은 우선 순위 큐를 정의하여 비용이 낮은 경로를 택합니다.

상하좌우 모두 방문하면서 

이전 노드 값 + 이전 노드에서 지금 노드까지 오는 값  < 현재 노드 값

조건이라면 이전 노드를 거쳐서 오는 것이 더 비용이 적다는 의미이므로 업데이트합니다. 계속해서 반복하여 최단 경로를 선택하여 이동합니다.

