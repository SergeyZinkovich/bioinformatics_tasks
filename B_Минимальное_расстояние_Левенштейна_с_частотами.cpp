#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

int all_count = 0;
vector<float> countt((int)'Z');


float LevenshteinDistance(const string &source, const string &target) {
    if (source.size() > target.size()) {
        return LevenshteinDistance(target, source);
    }

    const int min_size = source.size(), max_size = target.size();
    std::vector<float> lev_dist(min_size + 1);

    lev_dist[0] = 0;
    for (int i = 1; i <= min_size; ++i) {
        lev_dist[i] += countt[(int) source[i-1]];
    }

    for (int j = 1; j <= max_size; ++j) {
        float previous_diagonal = lev_dist[0], previous_diagonal_save;
        lev_dist[0] += countt[(int) target[j-1]];

        for (int i = 1; i <= min_size; ++i) {
            previous_diagonal_save = lev_dist[i];
            if (source[i - 1] == target[j - 1]) {
                lev_dist[i] = previous_diagonal;
            } else {
                lev_dist[i] = std::min(std::min(lev_dist[i - 1] + countt[(int) source[i-1]], lev_dist[i] + countt[(int) target[j-1]]), previous_diagonal + countt[(int) source[i-1]]+ countt[(int) target[j-1]]);
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
        all_count += line.size();
        for(int i = 0; i < line.size(); i++) {
            countt[(int) line[i]]++;
        }
    }

    for (float & i : countt) {
        i /= all_count;
    }

    int i_1 = 0, i_2 = 0;
    float dist = FLT_MAX;

    for (int i = 0; i < data.size(); i++)
        for (int j = i; j < data.size(); j++) {
            if (i == j) continue;
            float d = LevenshteinDistance(data[i], data[j]);
//            cout << data[i] << ' ' << data[j] << ' ' << d << endl;
            if (d < dist) {
                i_1 = i;
                i_2 = j;
                dist = d;
            }
        }
    cout << fixed << std::setprecision(2) << i_1 + 1 << ' ' << i_2 + 1 << ' ' << dist;

    return 0;
}
