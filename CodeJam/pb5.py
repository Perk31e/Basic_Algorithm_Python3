'''
5. Untie

문제
한 그룹의 사람들이 원형으로 앉아 있습니다. 그들은 특별한 버전의 가위바위보 게임을 하고 있습니다. 이 게임에서 각각의 사람은 가위, 바위, 보 중에서 하나를 선택하고, 그것을 다른 사람들에게 공개합니다. 각 사람은 자신의 좌우 이웃의 선택과 비교하여 그들 중 하나와 이길 수 있습니다. 각각의 이웃에 대해서, 이길 수도, 질 수도, 비길 수도 있습니다. 두 사람이 같은 선택을 한 경우에만 비길 수 있습니다.

이 게임에서 어떤 두 사람도 비길 수 없도록 하려고 합니다. 각각의 사람들에 대해서, 그들이 처음에 선택한 것을 유지할 수도 있고, 또는 다른 두 선택 중 하나로 바꿀 수 있습니다(어떤 선택으로 바꿀지는 당신이 결정합니다). 이들 중 최소 몇 명에게 바꾸라는 요청을 해야 두 이웃이 같은 선택을 하지 않도록 할 수 있을까요?

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어집니다. 이어지는 T개의 줄에는 각각 하나의 테스트 케이스가 주어집니다.

각 테스트 케이스는 문자열 C로 주어집니다. C의 i번째 문자는 시계방향으로 i번째 사람의 원래 선택을 나타냅니다. C는 대문자 R을 이용해 바위를, 대문자 P를 이용해 보를, 대문자 S를 이용해 가위를 나타냅니다.

출력
각각의 테스트 케이스에 대해, 출력은 "Case #x: y" 형태로 구성됩니다. 여기서 x는 테스트 케이스의 번호(1부터 시작), y는 인접한 두 사람이 같은 선택을 하지 않도록 하기 위해 최소 몇 명에게 선택을 바꾸라는 요청을 해야 하는지입니다.

제한
시간 제한: 10초

메모리 제한: 2 GB

1 ≤ T ≤ 100

C의 각 문자는 대문자 R, P, S 중 하나입니다.

테스트 세트 1 (해결 가능)
3 ≤ C의 길이 ≤ 10

테스트 세트 2 (해결 가능)
3 ≤ C의 길이 ≤ 1000

샘플

샘플 입력

3
PRSSP
RRRRRRR
RSPRPSPRS

샘플 출력

Case #1: 2
Case #2: 4
Case #3: 0

샘플 Case #1에 대해서, 입력에서 첫 번째와 마지막 글자가 모두 "P"이고, 두 번째와 세 번째 글자가 모두 "S"입니다. 따라서 적어도 두 번은 선택을 바꿔야 합니다. 두 번의 선택 바꾸기로 가능한 한 방법은 왼쪽 끝의 "P"를 "S"로, 오른쪽 끝의 "S"를 "R"로 바꾸는 것입니다. 그러면 "SRSRP"가 되어 이웃 사이에 같은 선택이 없습니다.

샘플 Case #2에 대해서는, 모든 사람이 바위를 선택했습니다. 선택을 최대 세 번 바꾸면 적어도 네 개의 바위가 남아 있고, 그 중 적어도 두 개는 이웃한 사람입니다. 따라서 최소한 네 번 이상의 선택을 바꾸어야 합니다. 바꾸는 방법 중 하나로 "PRSRPRS"가 있습니다.

샘플 Case #3에 대해서는, 인접한 두 사람이 모두 같은 선택을 하지 않으므로, 선택을 바꿀 필요가 없습니다.
'''