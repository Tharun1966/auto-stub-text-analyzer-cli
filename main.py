import re
from collections import Counter

def analyze_text(text):
    words = re.findall(r'\w+', text)
    return Counter(words)
def main():
    text = input('Enter some text: ')
    result = analyze_text(text)
    print(f'Word count: {len(result)}
{result}')
if __name__ == '__main__':
    main()