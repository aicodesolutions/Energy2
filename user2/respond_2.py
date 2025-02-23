""" import streamlit as st

st.header("resp2")
st.write(f"You are logged in as {st.session_state.role}.")
import os
import requests
import streamlit as st
 """
# Get API key from https://cloud.ibm.com/iam/apikeys
#IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_API_KEY='jNhdhHbmJmiphJ_HnyI3gDK-_SJEmmeTpw8cWkF_yBP_'

# Get Project ID from https://dataplatform.cloud.ibm.com/projects/?context=wx   (it is in your project url)
IBM_PROJECT_ID = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"
IBM_PROJECT_ID = "68518b55-09d0-4a6c-b75d-6f69507d84eb"

IBM_URL_TOKEN = "https://iam.cloud.ibm.com/identity/token"
IBM_URL_CHAT = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-10-25"

##############################################
##
##   IBM API
##
##############################################
""" def IBM_token():
    # Define the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Define the data payload
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": IBM_API_KEY
    }
    
    # Make the POST request
    response = requests.post(IBM_URL_TOKEN, headers=headers, data=data)
    st.session_state.IBM_ACCESS_TOKEN = response.json().get("access_token", "")


def IBM_chat (messages):
    body = {
        "model_id": "ibm/granite-3-8b-instruct",
        "project_id": IBM_PROJECT_ID,
        "messages": messages,
        "max_tokens": 100,
        "temperature": 0.7,
        "time_limit": 5000
    }
    headers = {
    	"Accept": "application/json",
    	"Content-Type": "application/json",
    	"Authorization": "Bearer " + st.session_state.IBM_ACCESS_TOKEN
    }    
    response = requests.post(
    	IBM_URL_CHAT,
    	headers=headers,
    	json=body
    )
    
    if response.status_code != 200:
    	raise Exception("Non-200 response: " + str(response.text))
    
    response = response.json()
    return response["choices"][0]["message"]["content"]

# """

article_01 = \
"Tomatoes are one of the most popular plants for vegetable gardens.  Tip for success: If you select " \
"varieties that are resistant to disease and pests, growing tomatoes can be quite easy.  For "        \
"experienced gardeners looking for a challenge, there are endless heirloom and specialty varieties "  \
"to cultivate.  Tomato plants come in a range of sizes.  There are varieties that stay very small, "  \
"less than 12 inches, and grow well in a pot or hanging basket on a balcony or patio.  Some grow "    \
"into bushes that are a few feet high and wide, and can be grown is larger containers.  Other "       \
"varieties grow into huge bushes that are several feet wide and high in a planter or garden bed.  "   \
"Still other varieties grow as long vines, six feet or more, and love to climb trellises.  Tomato "   \
"plants do best in full sun.  You need to water tomatoes deeply and often.  Using mulch prevents "    \
"soil-borne disease from splashing up onto the fruit when you water.  Pruning suckers and even "      \
"pinching the tips will encourage the plant to put all its energy into producing fruit."

article_02 = \
"Cucumbers are fun to grow for beginning gardeners and advanced gardeners alike.  There are two "     \
"types of cucumbers: slicing and pickling.  Pickling cucumbers are smaller than slicing cucumbers.  " \
"Cucumber plants come in two types: vining cucumbers, which are more common, and bush cucumbers.  "   \
"Vining cucumbers, which can grow to more than 5 feet tall, grow fast, yield lots of fruit, and you " \
"can train them up a trellis.  Growing cucumbers up a trellis or fence can maximize garden space, "   \
"keep fruit clean, and make it easier to harvest the fruit.  Tropical plants, cucumbers are very "    \
"sensitive to frost or cold weather. Cucumbers prefer full sun for 6 to 8 hours per day.  Cucumbers " \
"need constant watering.  Cucumbers can grow quickly and ripen in just 6 weeks.  Harvest cucumbers "  \
"every day or two because the more you harvest, the more the plant will produce.  If any cucumber "   \
"is left on the vine to fully mature, the plant will stop producing more cucumbers.  You can extend " \
"the harvest season by planting cucumbers in batches, 2 weeks apart."
 
knowledge_base = [ 
    { 
        "title"     : "Growing tomatoes", 
        "Author"    : "A. Rossi",
        "Published" : "2010",
        "txt"       : article_01 
    }, 
    {
        "title"     : "Cucumbers for beginners",
        "Author"    : "B. Melnyk",
        "Published" : "2018",
        "txt"       : article_02 
    }
]
 
def search( query_in, knowledge_base_in ):
    if re.match( r".*tomato.*", query_in, re.IGNORECASE ):
        return 0
    elif re.match( r".*cucumber.*", query_in, re.IGNORECASE ):
        return 1
    return -1
import re
index = search( "How tall do tomatoes grow?", knowledge_base )

if index >= 0:
    print( "Index: " + str( index ) + "\nArticle: \"" + knowledge_base[index]["title"] + "\"" )
else:
    print( "No matching content was found" )



index = search( "How tall do tomatoes grow?", knowledge_base )

if index >= 0:
    print( "Index: " + str( index ) + "\nArticle: \"" + knowledge_base[index]["title"] + "\"" )
else:
    print( "No matching content was found" )

prompt_template = """
Article:
###
%s
###

Answer the following question using only information from the article. 
Answer in a complete sentence, with proper capitalization and punctuation. 
If there is no good answer in the article, say "I don't know".

Question: %s
Answer: 
"""

def augment( template_in, context_in, query_in ):
    return template_in % ( context_in,  query_in )

query = "How tall do cucumber plants grow?"

article_txt = knowledge_base[1]["txt"]

augmented_prompt = augment( prompt_template, article_txt, query )

print( augmented_prompt )

import os
from ibm_watson_machine_learning.foundation_models import Model

model_id = "google/flan-t5-xxl"

gen_parms = { 
    "DECODING_METHOD" : "greedy", 
    "MIN_NEW_TOKENS" : 1, 
    "MAX_NEW_TOKENS" : 50 
}

project_id = IBM_PROJECT_ID
credentials = { 
    "url"    : "https://us-south.ml.cloud.ibm.com", 
    "apikey" : IBM_API_KEY
}

model = Model( model_id, credentials, gen_parms, project_id )

import json

def generate( model_in, augmented_prompt_in ):
    
    generated_response = model_in.generate( augmented_prompt_in )

    if ( "results" in generated_response ) \
       and ( len( generated_response["results"] ) > 0 ) \
       and ( "generated_text" in generated_response["results"][0] ):
        return generated_response["results"][0]["generated_text"]
    else:
        print( "The model failed to generate an answer" )
        print( "\nDebug info:\n" + json.dumps( generated_response, indent=3 ) )
        return ""
output = generate( model, augmented_prompt )
print( output )

def searchAndAnswer( knowledge_base_in, model ):
    
    question = input( "Type your question:\n")
    if not re.match( r"\S+", question ):
        print( "No question")
        return
        
    # Retrieve the relevant content
    top_matching_index = search( question, knowledge_base_in )
    if top_matching_index < 0:
        print( "No good answer was found in the knowledge base" )
        return;
    asset = knowledge_base_in[top_matching_index]
    asset_txt = asset["txt"]
    
    # Augment a prompt with context
    augmented_prompt = augment( prompt_template, asset_txt, question )
    
    # Generate output
    output = generate( model, augmented_prompt )
    if not re.match( r"\S+", output ):
        print( "The model failed to generate an answer")
    print( "\nAnswer:\n" + output )
    print( "\nSource: \"" + asset["title"] + "\", " + asset["Author"] + " (" + asset["Published"] + ")"  )

searchAndAnswer( knowledge_base, model )