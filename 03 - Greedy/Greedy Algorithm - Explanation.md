- Greedy 알고리즘 -

Greedy 알고리즘(탐욕적 알고리즘)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미한다. [매 순간 가장 좋아보이는걸 고르지만 현재의 선택이 "나중에 미칠 영향"에 대해서는 고려하지 않는다]


그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.


3-1 거스름돈
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.


문제 해설
'가장 큰 화페 단위부터' 돈을 거슬러 주겠다. N원을 거슬러 줄때, 먼저 500원으로 거슬러 줄 수 있는 만큼 거슬러 주고, 그 다음 100원, 50원, 10원짜리 동전을 차례대로 거슬러 준다. => 최소의 동전 개수로 모두 거슬러준다.

N = 1260원

500 2개
100 2개
50  1개
10  1개

=> 문제 풀이
=>=> 3-1.py 참조


* 그리디 알고리즘을 언제 적용할 수 있을까 *
위의 3-1 거스름돈 같은 경우 정확히 어떤 해(500/100/50/10)를 사용해서 문제를 해결할 수 있을지 정해져 있다.

코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 아래의 절차로 해결할 수 있는지 확인한다.
1. 그리디 알고리즘
2. 다이나믹 프로그래밍
3. 그래프 알고리즘

----------------------------------------------------------------

큰 수의 법칙

큰 수의 법식은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이법칙의 특징이다.

예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3,4,3,4,3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4+4+4+4+4+4+4인 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

-입력 조건-
    * 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    * 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000 이하의 수로 주어진다.
    * 입력으로 주어지는 K는 항상 M보다 작거나 같다.

-출력 조건-
    * 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

-입력 예시-
5 8 3
2 4 5 4 6

-출력 예시-
46

=> Big_Num.py 참조

(기존의 코드와 Big_Num.py의 차이)
Big_Num.py는 기존의 코드와 달리 6번줄의 맨 끝에 [:n]을 추가하여 지정한 n개를 넘어서 입력되면 맨처음부터 n번째까지 입력되도록 수정했습니다.

----------------------------------------------------------------

큰 수의 법칙 2
수학적으로 생각해보면 결국 가장 큰 수는 아래와 같이 구할 수 있다.
int(M/(k+1))*K+M%(K+1)
또한 이를 토대로 두번째로 큰 수까지 구할 수 있다.

=> 3-2.py 참조

----------------------------------------------------------------

숫자 카드 게임

여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

입력 조건

* 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1<=N, M<=100)
* 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10000 이하의 자연수이다.

출력 조건

* 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

입력 예시 1
3 3
3 1 2
4 1 4
2 2 2

출력 예시 1
2

입력 예시 2
2 4
7 3 1 8
3 3 3 4

출력 예시 2
3

=> 3-3.py, 3-3-1.py (min 함수를 이용하는 답안)
=> 3-4.py (2중 for문)
각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾자!

----------------------------------------------------------------

1이 될 때까지

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예를 들어 N이 17, K가 4라고 가정한다. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다. 이후에 2번의 과정을 두 번 수행하면 N은 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다. 이는 N을 1로 만드는 최소 횟수이다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

입력조건

* 첫째 줄에 N(2<=N<=100000)과 K(2<=K<=100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

출력조건

* 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

입력 예시
25 5

출력 예시
2

----------------------------------------------------------------