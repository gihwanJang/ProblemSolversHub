# 풀이

해당 문제는 주어진 값 x보다 작은 거리의 간선을 택하여 출발지에서 목적지 까지 도달 할 수 있는 지에 대한 여부를 확인 하는 문제입니다.  

우선 해당 문제는 BFS, DFS, 플로이드 워샬과 같은 방식으로 해결을 할 수 있으나 문제의 주어진 제약 조건 때문에 시간 초과 및 메모리 초과가 발생하게 됩니다.  

그러므로 위의 알고리즘 보다 작은 시간 복잡도와 공간 복잡도의 알고리즘을 사용하여 해결해야합니다. 

우선 해당 문제에서는 부스터를 아낄 필요가 없기 때문에 부스터를 먼저 사용하여 원하는 체크포인트의 x 또는 y좌표를 일치 시킨 후 거리를 생각하면 됩니다.  
즉 체크 포인트 a에서 b까지로 가려면 |a.x - b.x|의 거리로 가거나 |a.y - b.y|의 거리로 갈 수 있습니다.  
하지만 위의 방식으로 현 위치에서 갈 수 있는 곳을 모두 표기하게 되면 O(n^2)의 공간 복잡도를 사용하게 됩니다.  
그러므로 해당 문제에서는 간선이 이어져만 있으면 모든 곳으로 갈 수 있기 때문에 최소한의 간선으로 만 먼저 이어놓습니다.  
그러기 위해 x값을 기준으로 정렬하여 x축의 인접한 체크포인트들을 연결하고 y값을 기준으로 정렬하여 y축의 인접한 체크 포인트들을 연결합니다.  

위에서 연결한 간선들을 모두 우선순위큐에 넣어줍니다.  
이제 간선을 하나씩 빼며 최소신장트리를 만들어야합니다.  
이때 최소신장트리를 만들때 간선은 질의에 주어진 x값보다 작은 값들만을 선택하며 만들 수 있습니다.  
그러므로 입력 받은 질의들을 x값을 기준으로 정렬해줍니다.  

이후 질의들을 하나씩 뽑아 해당 x값보다 작은 간선을 선택하며 최소신장트리를 만들고 이때 해당 질의의 시작점에서 도착점으로 갈 수 있다면 즉 두점이 하나의 집합이라면 yes를 아니면 no를 저장합니다.  
위의 과정을 모든 질의 들에 대하여 수행합니다.  

이제 질의의 입력 순서대로 다시 정렬후 수행 결과를 출력해 주시면 됩니다.