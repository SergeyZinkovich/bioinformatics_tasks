#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int LevenshteinDistance(const string &source, const string &target) {
    if (source.size() > target.size()) {
        return LevenshteinDistance(target, source);
    }

    const int min_size = source.size(), max_size = target.size();
    std::vector<int> lev_dist(min_size + 1);

    for (int i = 0; i <= min_size; ++i) {
        lev_dist[i] = i;
    }

    for (int j = 1; j <= max_size; ++j) {
        int previous_diagonal = lev_dist[0], previous_diagonal_save;
        ++lev_dist[0];

        for (int i = 1; i <= min_size; ++i) {
            previous_diagonal_save = lev_dist[i];
            if (source[i - 1] == target[j - 1]) {
                lev_dist[i] = previous_diagonal;
            } else {
                lev_dist[i] = std::min(std::min(lev_dist[i - 1] + 1, lev_dist[i]) + 1, previous_diagonal + 2);
            }
            previous_diagonal = previous_diagonal_save;
        }
    }

    return lev_dist[min_size];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    vector<string> data;
    std::string line;
    while (std::getline(std::cin, line))
    {
        data.push_back(line);
    }

    int i_1 = 0, i_2 = 0, dist = INT_MAX;

    for (int i = 0; i < data.size(); i++)
        for (int j = i; j < data.size(); j++) {
            if (i == j) continue;
            int d = LevenshteinDistance(data[i], data[j]);
            if (d < dist) {
                i_1 = i;
                i_2 = j;
                dist = d;
            }
        }
    cout << i_1 + 1 << ' ' << i_2 + 1 << ' ' << dist;

    return 0;
}
