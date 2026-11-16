from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

text = """
Texas is one of the largest and most popular states in the United States. 
It is located in the southern part of the country and is known for its rich history, diverse culture, and strong economy. The capital of Texas 
is Austin, while Houston is its largest city. Other major cities include Dallas, San Antonio, and Fort Worth. Texas is famous for 
its delicious barbecue, cowboy traditions, and beautiful landscapes. 

California is a beautiful and economically important state located on the western coast of the United States. 
Its capital is Sacramento, and its largest city is Los Angeles. California is famous for its beaches, mountains, national parks, 
and pleasant weather in many areas. It is home to Hollywood, which is known worldwide for movies and entertainment. Silicon Valley is 
another important region, where many major technology companies are located. 

New York is one of the most famous states in the United States, located in the northeastern part of the country. 
Its capital is Albany, while New York City is its largest and most well-known city. New York City is famous for 
landmarks such as the Statue of Liberty, Times Square, Central Park, and the Empire State Building. The state is an important 
center for business, finance, education, fashion, and entertainment. 
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0:5])