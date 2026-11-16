from langchain_classic.text_splitter import RecursiveCharacterTextSplitter, Language

code = """
def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total

def calculate_average(prices):
    total = calculate_total(prices)
    average = total / len(prices)
    return average

def main():
    prices = [100, 200, 300, 400, 500]

    total = calculate_total(prices)
    average = calculate_average(prices)

    print("Total:", total)
    print("Average:", average)

if __name__ == "__main__":
    main()
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 230,
    chunk_overlap = 0
)

chunks = splitter.split_text(code)

print(len(chunks))
print(chunks[1])