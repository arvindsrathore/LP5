#include <stdio.h>
#include <omp.h>

const int N = 100;
const int NP = 4;

int main() {
    int arr[N];
    for (int i = 0; i < N; i++) {
        arr[i] = i + 1;
    }

    int sm = 0;
    int prsm[NP] = {0};

    #pragma omp parallel num_threads(NP)
    {
        int thread_id = omp_get_thread_num();
        int st = thread_id * (N / NP);
        int ed = (thread_id + 1) * (N / NP);
        prsm[thread_id] = 0;

        for (int i = st; i < ed; i++) {
            prsm[thread_id] += arr[i];
        }
    }

    for (int i = 0; i < NP; i++) {
        sm += prsm[i];
        std::cout << "Partial sum of thread " << i << ": " << prsm[i] << std::endl;
    }

    std::cout << "Sum: " << sm << std::endl;
    return 0;
}

// g++-13 -fopenmp main.cpp -o output
// ./output
