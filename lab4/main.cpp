#include <iostream>
#include <string>


static size_t max_prefix(std::string str, size_t index) {
	for (size_t i = index - 1; i > 0; i--) {
		if (str.substr(0, i) == str.substr(index - i, i))
			return i;
	}
	return 0;
}

int KnuttMorrisPratt(std::string text, std::string to_find) {
	std::string str = to_find + "%" + text;
	size_t find_len = to_find.length();
	size_t text_len = text.length();

	size_t prev_prefix = max_prefix(str, find_len + 2);
	size_t curr_prefix;
	std::cout << "!!!->" << prev_prefix << '\n';
	for (size_t i = 1; i < text_len; i++) {
		if (str[i + find_len] == str[prev_prefix])
			curr_prefix = prev_prefix + 1;
		else
			curr_prefix = max_prefix(str, find_len + i + 2);
		std::cout << "!!!->" << curr_prefix << '\n';
		if (curr_prefix == find_len)
			return i;
		prev_prefix = curr_prefix;
	}
	return -1;
}


int main() {
	std::string test = "aaa bbc cabbca ac";
	
	int result = KnuttMorrisPratt(test, "c ca");
	if (result == -1)
		std::cout << "substr not found\n";
	else
		std::cout << result << '\n';

	return 0;
}
