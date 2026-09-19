from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from project.schemas.problem import ProblemUnderstanding

def get_problem_understanding_chain(model_name: str = "openai/gpt-oss-20b"):
    """
    Returns a LangChain runnable that extracts structured JSON
    from a natural language environmental problem.
    """
    # Initialize the Groq Chat Model. Ensure GROQ_API_KEY is in the environment.
    llm = ChatGroq(model=model_name, temperature=0.0)

    # Define the strict extraction prompt.
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an expert environmental science analyst. Your task is to extract structured information "
         "from natural-language environmental problems.\n\n"
         "RULES:\n"
         "- DO NOT diagnose the cause.\n"
         "- DO NOT recommend solutions.\n"
         "- DO NOT invent missing measurements.\n"
         "- ONLY extract information explicitly supported by the user's query.\n"
         "- ALWAYS provide a clear string summary for problem_statement.\n"
         "- ALWAYS preserve numeric values, units, and quantitative measurements in observed_values (e.g., 'species richness: 18', 'house sparrow: 24 per ha').\n"
         "Keep the output strict and factual."
        ),
        ("human", "{problem}")
    ])

    # Enforce structured output via Pydantic
    chain = prompt | llm.with_structured_output(ProblemUnderstanding)
    return chain

def analyze_problem(problem_text: str) -> dict:
    """
    Analyzes the text and returns a dictionary matching the structured schema.
    """
    chain = get_problem_understanding_chain()
    result = chain.invoke({"problem": problem_text})
    return result.model_dump()
