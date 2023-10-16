#include <iostream>
#include <cstdio>
#include <vector>

int main() {
    int n;
    int size = 1000001;
    std::cin >> n;

    std::vector<int> numList(n);
    std::vector<int> res(size, 0);
    std::vector<bool> isCard(size, false);

    for (int i = 0; i < n; i++) {
        std::cin >> numList[i];
        isCard[numList[i]] = true;

    }

    for (int i : numList) {
        for (int j = i * 2; j < size; j += i) {
            if (isCard[j]) {
                ++res[i];
                --res[j];

            }
        }
    }

    for (int i : numList) {
        std::cout << res[i] << " ";

    }
    return 0;

}