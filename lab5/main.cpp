#include <iostream>
#include <string>


bool not_in(char sym, std::string str) {
	for (size_t i = 0; i < str.length(); i++) {
		if (str[i] == sym)
			return false;
	}
	return true;
}


int BoierMuire(std::string text, std::string pattern) {
	unsigned start = 0;
	unsigned pattern_len = pattern.length();
	unsigned pattern_curr = pattern_len - 1;
	while (start + pattern_len <= text.length()) {
		unsigned curr_pos = start + pattern_curr;
		//std::cout << start << ' ' << curr_pos << ' ' << text.substr(start, pattern_len) << '\n';
		if (text[curr_pos] == pattern[pattern_curr]) {
			//std::cout << curr_pos << ' ' << pattern_curr << '\n';
			if (pattern_curr == 0 && curr_pos == start)
				return start;
			else {
				pattern_curr--;
				curr_pos--;
			}
		}
		else if (not_in(text[curr_pos], pattern))
			start += pattern_len;
		else
			start += (pattern_len - pattern.rfind(text[curr_pos]) - 1);

	}
	return -1;
}


int main() {
	std::string test = "aaa bbc cabbca ac";

	int result = BoierMuire(test, "c ca");

	if (result == -1)
		std::cout << "substr not found\n";
	else
		std::cout << result << '\n';

	return 0;
}
