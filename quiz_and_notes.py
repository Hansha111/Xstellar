from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain.schema.runnable import RunnableParallel

load_dotenv()


prompt1 = ChatPromptTemplate.from_template("Generate short and concise notes from {text}")

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=256,
    temperature=0.6,
    timeout=30
)
model1 = ChatHuggingFace(llm=llm1)

prompt2 = ChatPromptTemplate.from_template("Generate 5 questions from {text}")

llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=256,
    temperature=0.6,
    timeout=30
)

model2 = ChatHuggingFace(llm=llm2)

prompt3 = ChatPromptTemplate.from_template("Merge the provided notes and quiz into a single document\n notes -> {notes} and quiz -> {quiz}")

llm3 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    max_new_tokens=256,
    temperature=0.6,
    timeout=30
)

model3 = ChatHuggingFace(llm=llm3)


parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser,
})

merged_chain = prompt3 | model3 | parser

chain = parallel_chain | merged_chain

text = "The LangChain framework is designed to simplify the development of applications that use large language models (LLMs). It provides a set of tools and abstractions that make it easier to build complex workflows involving LLMs, such as chatbots, question-answering systems, and more."


res = chain.invoke({'text':text})

print(res)


# to see the workflow of the model (optional)
chain.get_graph().print_ascii()


