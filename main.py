def main():
	book_text = get_book_text()
	character_counts = count_characters(book_text)
	number_of_words = count_words_in_string(book_text)
	print(generate_character_count_report(number_of_words, character_counts))

def generate_character_count_report(number_of_words, character_counts):
	def sort_on(dict):
		return dict["count"]

	sorted_character_counts = []
	for char in character_counts:
		sorted_character_counts.append({ "char": char, "count": character_counts[char] })

	sorted_character_counts.sort(reverse=True, key=sort_on)

	report = ""
	report += line("--- Begin report of books/frankenstein.txt ---")
	report += line(f"{number_of_words} words found in the document")
	report += line("")

	for dict in sorted_character_counts:
		report += line(f"the {dict['char']} character was found {dict['count']} times")

	report += line("--end report")
	return report

def line(line):
	return f"{line}\n"

def count_characters(text):
	chars = {}
	chars_to_count = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	for char in text:
		lowercase_char = char.lower()
		if lowercase_char not in chars_to_count:
			continue
		if lowercase_char not in chars:
			chars[lowercase_char] = 0
		chars[lowercase_char] += 1
	return chars

def count_words_in_string(string):
	return len(string.split())

def get_book_text():
	with open('./books/frankenstein.txt') as f:
		return f.read()

main()
