import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# CONFIGURACIÓN DEL MODELO (ChatOpenAI de LangChain)
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# CHATPROMPTTEMPLATE CON ROLES SYSTEM/HUMAN Y VARIABLE {pregunta}
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente útil que responde preguntas de forma clara y concisa."),
    ("human", "{pregunta}")
])

# IMPLEMENTACIÓN DE SINTAXIS LCEL: composicion con operador pipe (|)
chain = prompt | model | StrOutputParser()

# GESTIÓN DE ASINCRONÍA: función async principal con await chain.ainvoke()
async def main():
    pregunta = "¿Qué es la refactorización a LCEL asíncrono y cuáles son sus beneficios?"
    resultado = await chain.ainvoke({"pregunta": pregunta})
    print(resultado)

if __name__ == "__main__":
    asyncio.run(main())