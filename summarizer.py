from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence

# Set up Groq model
GROQ_API_KEY = "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"
model = ChatGroq(temperature=0.7, model_name="llama3-8b-8192", groq_api_key=GROQ_API_KEY)

# Define summarization prompts
brief_summary_prompt = PromptTemplate(
    input_variables=["content"],
    template="Summarize the following article in 1-2 sentences: {content}"
)

detailed_summary_prompt = PromptTemplate(
    input_variables=["content"],
    template="Summarize the following article in a paragraph: {content}"
)

# Define summarization chains
brief_summary_chain = RunnableSequence(brief_summary_prompt | model)
detailed_summary_chain = RunnableSequence(detailed_summary_prompt | model)

def summarize_article(content, summary_type="brief"):
    """
    Summarize an article based on the specified type (brief or detailed).
    """
    if summary_type == "brief":
        result = brief_summary_chain.invoke({"content": content})
    else:
        result = detailed_summary_chain.invoke({"content": content})
    
    # Extract the content from the AIMessage object
    return result.content