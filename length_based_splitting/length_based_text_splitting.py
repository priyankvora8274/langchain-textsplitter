from langchain_classic.text_splitter import CharacterTextSplitter

text = """
Texas is one of the largest and most popular states in the United States. 
It is located in the southern part of the country and is known for its rich history, diverse culture, and strong economy. The capital of Texas 
is Austin, while Houston is its largest city. Other major cities include Dallas, San Antonio, and Fort Worth. Texas is famous for 
its delicious barbecue, cowboy traditions, and beautiful landscapes. The state has many opportunities in industries such as technology, healthcare, energy, 
and education. Texas also attracts people from different backgrounds because of its job opportunities, universities, and relatively affordable living options.

California is a beautiful and economically important state located on the western coast of the United States. 
Its capital is Sacramento, and its largest city is Los Angeles. California is famous for its beaches, mountains, national parks, 
and pleasant weather in many areas. It is home to Hollywood, which is known worldwide for movies and entertainment. Silicon Valley is 
another important region, where many major technology companies are located. Popular tourist attractions include Disneyland, 
the Golden Gate Bridge, and Yosemite National Park. California has a diverse population and offers many opportunities in technology,
education, entertainment, agriculture, and tourism, making it an exciting place to live.

New York is one of the most famous states in the United States, located in the northeastern part of the country. 
Its capital is Albany, while New York City is its largest and most well-known city. New York City is famous for 
landmarks such as the Statue of Liberty, Times Square, Central Park, and the Empire State Building. The state is an important 
center for business, finance, education, fashion, and entertainment. Many people from different countries live in New York, 
creating a diverse culture. The state also has beautiful natural attractions, including Niagara Falls and the Adirondack Mountains. 
New York offers many opportunities for students, professionals, and tourists.
"""

# Chunk overlap: It will define how many chars will overlap in between chunks, let say if it is 5, then last 5 chars of first chunk & first 5 of next chunk will be same.
#       Usecase of chunk overlap: In length based text splitting, we lose the context, because sometimes sentences split from between, also sometimes word is also splits from 
#       in between. So, with overlap, we can retain that context. So, it helps to not lose the context when splitting occurs abruptly. 
# What is good number for overlap? : We cannot choose very large because it will increase the num of chunks. So, 10 to 20% of  total chunk size is good number.
text_splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=""    
)

text_chunks = text_splitter.split_text(text=text)

print(len(text_chunks))

# print(text_chunks[0])