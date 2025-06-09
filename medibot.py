import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


@st.cache_resource
def get_vector_store():

    return Chroma(
        collection_name='my_collection',
        persist_directory='chroma_db',
        embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    )


def format_docs(retrieved_docs):

    return '\n\n'.join(doc.page_content for doc in retrieved_docs)


def build_chain(vector_store):

    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})

    prompt_template = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided context in detail.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
    )

    model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.5, max_output_tokens=512)

    chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    }) | prompt_template | model | StrOutputParser()

    return chain


def main():
    st.title("Ask MediBot!")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    user_input = st.chat_input("Enter your prompt here")
    if user_input:
        
        st.chat_message('user').markdown(user_input)
        st.session_state.messages.append({'role': 'user', 'content': user_input})

        vector_store = get_vector_store()
        chain = build_chain(vector_store)

        response = chain.invoke(user_input)

        st.chat_message('assistant').markdown(response)
        st.session_state.messages.append({'role': 'assistant', 'content': response})

if __name__ == "__main__":
    main()
