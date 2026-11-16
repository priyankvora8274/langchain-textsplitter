from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings   import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = """
Artificial Intelligence is transforming the technology industry.
Machine learning allows computers to learn from data and make predictions.
Deep learning uses neural networks to solve complex problems.
Companies are using AI to automate tasks and improve business decisions.
Eating healthy food is important for maintaining a healthy lifestyle.
Fruits and vegetables provide essential vitamins and minerals.
Regular exercise helps improve physical fitness and mental well-being.

The Super Bowl is the annual championship game of the National Football League (NFL) in the United States.
It is one of the most popular sporting events, attracting millions of viewers worldwide.
The game features the champions of the AFC and NFC competing for the Vince Lombardi Trophy.
The Super Bowl is also famous for its exciting halftime performances, creative commercials, and celebrations.
"""


splitter = SemanticChunker(
    embeddings=OpenAIEmbeddings(),
    breakpoint_threshold_type = "standard_deviation",
    breakpoint_threshold_amount=0.8
)

chunks = splitter.create_documents([text])
print(len(chunks))
print(chunks[2])