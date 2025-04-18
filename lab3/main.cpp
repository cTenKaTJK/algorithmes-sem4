#include <iostream>
#include <string>


int straight_algorithm(std::string text, std::string to_find) {
	for (size_t i = 0; i < text.length(); i++) {
		if (text[i] == to_find[0]) {
			for (size_t j = 0; j < to_find.length(); j++) {
				if (text[i + j] != to_find[j]) break;
				if (j == to_find.length() - 1) return i;
			}
		}
	}
	return -1;
}


int main() {
	std::string test = "cacc abaaa cb";

	int result = straight_algorithm(test, "a cb");
	if (result == -1)
		std::cout << "substr not found\n";
	else
		std::cout << result << '\n';

	return 0;
}