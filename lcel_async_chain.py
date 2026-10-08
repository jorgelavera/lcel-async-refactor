import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente útil que responde preguntas de forma clara y concisa."),
    ("human", "{pregunta}")
])

chain = prompt | model | StrOutputParser()

async def main():
    pregunta = "¿Qué es la refactorización a LCEL asíncrono y cuáles son sus beneficios?"
    resultado = await chain.ainvoke({"pregunta": pregunta})
    print(resultado)

if __name__ == "__main__":
    asyncio.run(main())