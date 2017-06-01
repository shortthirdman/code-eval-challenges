/*
Reverse and Add  Share on LinkedIn

Description:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure. eg.

195 (initial number) + 591 (reverse of initial number) = 786

786 + 687 = 1473

1473 + 3741 = 5214

5214 + 4125 = 9339 (palindrome)
In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.
Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 4,294,967,295. Assume each test case will always have an answer and that it is computable with less than 1000 iterations (additions)

Output sample:

For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character)
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

long reverse(long x) {
	long res = 0;

	while (x > 0) {
		res *= 10;
		res += x % 10;
		x /= 10;
	}

	return res;
}

bool isPalin(long x) {
	vector<int> v;
	v.clear();

	while (x > 0) {
		v.push_back(x%10);
		x /= 10;
	}

	for (int i = 0; i < v.size()/2; ++i) {
		if (v[i] != v[v.size()-1-i]) return false;
	}

	return true;
}

int main(int argc, char *argv[]) {
    ifstream ifs(argv[1]);
    long x;

    while (ifs >> x) {
    	long cur = x;
    	int count = 0;
    	while (!isPalin(cur)) {
    		++count;
    		long tmp = reverse(cur);
    		cur += tmp;
    	}

    	cout << count << " " << cur << endl;
    }

    return 0;
}