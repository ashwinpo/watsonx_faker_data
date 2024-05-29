import streamlit as st
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
# Utils
import os, glob, sys
import json
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import re
from faker import Faker

st.set_page_config(layout="wide")
NUM_TOP_RETRIEVED_EXAMPLES=15
load_dotenv()

# Load WML Key
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": os.getenv("IAM_KEY")
}
project_id = os.getenv("PROJECT_ID")
parameters = {
    GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
    GenParams.MAX_NEW_TOKENS: 8000,
    GenParams.MIN_NEW_TOKENS: 25,
    GenParams.REPETITION_PENALTY: 1.1,
}

if "model" not in st.session_state:
    st.session_state["model"] = Model(
        model_id='ibm/granite-34b-code-instruct',
        params=parameters,
        credentials=credentials,
        project_id=project_id
    )

def extract_code(text):
    regex = ".*```([^`]*)```.*"
    sub_regex = "```[^`]*```"
    m = re.search(regex, text)
    if m:
        code = m.group(1).strip()
        rest = re.sub(sub_regex, '', text)
        rest = rest.strip()
        #print(rest)
        return code, rest
    else:
        print("Error - code not found in output")
        return None, None
    
# Prompt template
template = """
You are an AI assistant that generates Python code to create synthetic datasets using the Faker library based on natural language descriptions.

Description: {dataset_description}

Generate the Python code to create the dataset described above using Faker. The code should include the necessary Faker providers and generate a pandas DataFrame named df with the synthetic data.
Put your code within a code block, for example:
```
import pandas as pd
# rest of the code
```
"""

# Create prompt
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(template),
    HumanMessagePromptTemplate.from_template("{dataset_description}")
])


# Streamlit app
st.title("Synthetic Data Generator")

# User input
dataset_description = st.text_input("Describe the dataset you want to generate:")



# Generate code using LLM
if st.button("Generate Dataset"):
    

    # Generate code
    response = st.session_state["model"].generate_text(params=parameters, prompt=prompt.format(dataset_description=dataset_description))
    print(response)
    code, message = extract_code(response)
    code = re.sub(r"^python", "", code, flags=re.IGNORECASE).strip() # remove word python at beginning of code block
    # Display generated code
    st.write(message)
    st.code(code, language="python")
    df = pd.DataFrame()
    # Execute the generated code
    exec(code)

    # Display the generated dataset
    st.dataframe(df)
