## 문제

[문제 링크](https://www.codetree.ai/missions/2/problems/move-to-max-k-times?&utm_source=clipboard&utm_medium=text)

## 풀이

이 문제는 BFS 탐색과 시뮬레이션으로 풀었다.
이 문제는 문제를 잘 읽고 이해해서 구현하라는 대로 코드를 작성하면 돼서 풀이 방법보다는 문제를 풀면서 했던 실수들을 복기하는 게 더 좋을 것 같다.

- 문제 풀면서 했던 실수들

1. 44번 줄 can_go() 함수에서 `not visited[x][y]` 조건 추가하지 않아 발생한 메모리 초과 에러
   BFS 탐색의 가장 중요한 규칙 중 <b>하나는 한 번 방문한 곳은 다시 방문하지 않아야 한다</b>는 것이다.
   그래서 문제를 풀 때 한 번 방문한 곳에 대해 2차원 배열 visited 이용해 방문했음을 표시해주고, 방문한 곳이면 이동하지 못하게 막아줘야 한다.
   왜냐하면 만약 한 번 방문했던 곳에 또 방문할 수 있게 한다면, 방문했던 곳에서 다른 곳으로 이동했다가, 이동한 그 곳에서 다시 이전의 위치로 되돌아왔다가, 다시 다른 곳으로 이동했다가, 또 다시 되돌아오는 등 같은 위치들을 왔다갔다 무한 반복하게 되기 때문이다.

2. 83번 줄의 if문 `visited[x][y] and x != r and y != c`으로 설정하여 발생한 오류
   기본적인 것이지만 제한된 시간 내에 코드를 작성해야 한다는 조급함 때문에 `visited[x][y] and (x != r or y != c)`와 `visited[x][y] and x != r and y != c` 가 동일하다고 잘못 생각했다.

## 시간/공간 복잡도

- 시간 복잡도 : O(K\*N^2)
- 공간 복잡도 : O(N^2)

## 출처

코드트리 > intermediate-low > BFS > BFS 탐색 > K번 최댓값으로 이동하기
