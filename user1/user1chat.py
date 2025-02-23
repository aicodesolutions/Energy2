import os
import requests
import streamlit as st

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
def IBM_token():
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


#################################
##
##   Streamlit App UI
##
#################################
# Get user specific details for the context
msg1={"role": "system", "content": 'Answer to user John Miller'}
msg2={"role": "system", "content": 'John miller gets energy from APS'}
msg2={"role": "system", "content": 'Consider the current date as Feb 23 and time as 11 AM. '}
msg3={"role": "system", "content" :
    "John Miller use the Time-of-Use 4pm-7pm Weekdays plan. This plan has \
  the following benefits: Potential to save money by shifting energy use to off-peak hours, \
  Ability to manage energy costs by using less energy during on-peak hours. \
  The plan details are as follows: rateStructure: Time-of-use, onPeakHours: 4pm-7pm weekdays, \
  offPeakHours: all other hours, superOffPeakHours: 10am-3pm weekdays (winter months), \
  The rates are as follows: summer: onPeak: higher rate, offPeak: lower rate, winter: onPeak: higher rate,\
      offPeak: lower rate, superOffPeak: lowest rate.  The ways to save energy are: Shift use of major \
        appliances to off-peak hours, Use less energy during on-peak hours, Use delay settings on appliances, Adjust pool pump timer.\
        Potential to save money by shifting energy use to off-peak hours \
    Ability to manage energy costs by using less energy during on-peak hours"
  }
energyplan= {"Available energy plans" : 
             [
    {
  "planName": "Fixed Energy Charge Plan",
  "description": "Energy rate stays the same regardless of time of day or day of week",
  "whyChoose": [
    "Don't use a lot of energy",
    "Have a small to average sized home",
    "Prefer not to worry about time or day of energy use"
  ],
  "benefits": [
    "Flexibility to use energy at any time",
    "Potential to save money by reducing energy use or improving efficiency"
  ],
  "waysToSave": [
    "Decrease overall energy use",
    "Improve energy efficiency",
    "Switch to LED light bulbs",
    "Adjust thermostat settings"
  ],
  "planDetails": {
    "rateStructure": "Same rate year-round based on assigned usage tier",
    "usageTiers": [
      {
        "tier": 1,
        "usageRange": "600 kWh or less",
        "rate": "12.925¢/kWh"
      },
      {
        "tier": 2,
        "usageRange": "601-999 kWh",
        "rate": "14.052¢/kWh"
      },
      {
        "tier": 3,
        "usageRange": "1,000 kWh or more",
        "rate": "15.418¢/kWh"
      }
    ]
  }
},
{
  "planName": "Time-of-Use 4pm-7pm Weekdays with Demand Charge",
  "description": "Energy rate based on time of day and day of week, with monthly demand charge for highest hour of usage during on-peak hours",
  "whyChoose": [
    "Use a lot of energy and can benefit from lower energy rate",
    "Have average to larger sized home",
    "Willing to adjust energy use and manage demand during on-peak hours"
  ],
  "benefits": [
    "Potential to save money by shifting energy use to off-peak hours",
    "Ability to manage energy demand during on-peak hours"
  ],
  "waysToSave": [
    "Shift energy use to off-peak hours",
    "Stagger use of major appliances during on-peak hours",
    "Use delay settings on appliances",
    "Pre-cool or pre-heat home during off-peak hours"
  ],
  "planDetails": {
    "rateStructure": "Time-of-use with demand charge",
    "onPeakHours": "4pm-7pm weekdays",
    "offPeakHours": "all other hours",
    "superOffPeakHours": "10am-3pm weekdays (winter months)",
    "demandCharge": "monthly demand charge for highest hour of usage during on-peak hours",
    "demandLimiter": "automatically lowers demand charge for rare, unusual spikes in usage during on-peak hours"
  },
  "rates": {
    "summer": {
      "onPeak": "higher rate",
      "offPeak": "lower rate"
    },
    "winter": {
      "onPeak": "higher rate",
      "offPeak": "lower rate",
      "superOffPeak": "lowest rate"
    }
  },
  "demandChargeCredit": {
    "available": "once during any 12-month period",
    "calculation": "based on difference between current kW and kW from same billing period last year"
  }
},
{
  "planName": "Time-of-Use 4pm-7pm Weekdays",
  "description": "Energy rate based on time of day and day of week, with higher rates during on-peak hours",
  "whyChoose": [
    "Can use less energy during higher-cost on-peak hours",
    "Have average to larger sized home",
    "Willing to adjust energy use to save"
  ],
  "benefits": [
    "Potential to save money by shifting energy use to off-peak hours",
    "Ability to manage energy costs by using less energy during on-peak hours"
  ],
  "waysToSave": [
    "Shift use of major appliances to off-peak hours",
    "Use less energy during on-peak hours",
    "Use delay settings on appliances",
    "Adjust pool pump timer"
  ],
  "planDetails": {
    "rateStructure": "Time-of-use",
    "onPeakHours": "4pm-7pm weekdays",
    "offPeakHours": "all other hours",
    "superOffPeakHours": "10am-3pm weekdays (winter months)",
    "holidays": "lower off-peak energy rates on weekends and holidays"
  },
  "rates": {
    "summer": {
      "onPeak": "higher rate",
      "offPeak": "lower rate"
    },
    "winter": {
      "onPeak": "higher rate",
      "offPeak": "lower rate",
      "superOffPeak": "lowest rate"
    }
  }
}
]
}
msg30={"role": "system", "content" :[energyplan]}
msg40={"role": "system", "content":{
  "planName": "Time-of-Use 4pm-7pm Weekdays with Demand Charge",
  "description": "Energy rate based on time of day and day of week, with monthly demand charge for highest hour of usage during on-peak hours",
  "whyChoose": [
    "Use a lot of energy and can benefit from lower energy rate",
    "Have average to larger sized home",
    "Willing to adjust energy use and manage demand during on-peak hours"
  ],
  "benefits": [
    "Potential to save money by shifting energy use to off-peak hours",
    "Ability to manage energy demand during on-peak hours"
  ],
  "waysToSave": [
    "Shift energy use to off-peak hours",
    "Stagger use of major appliances during on-peak hours",
    "Use delay settings on appliances",
    "Pre-cool or pre-heat home during off-peak hours"
  ],
  "planDetails": {
    "rateStructure": "Time-of-use with demand charge",
    "onPeakHours": "4pm-7pm weekdays",
    "offPeakHours": "all other hours",
    "superOffPeakHours": "10am-3pm weekdays (winter months)",
    "demandCharge": "monthly demand charge for highest hour of usage during on-peak hours",
    "demandLimiter": "automatically lowers demand charge for rare, unusual spikes in usage during on-peak hours"
  },
  "rates": {
    "summer": {
      "onPeak": "higher rate",
      "offPeak": "lower rate"
    },
    "winter": {
      "onPeak": "higher rate",
      "offPeak": "lower rate",
      "superOffPeak": "lowest rate"
    }
  },
  "demandChargeCredit": {
    "available": "once during any 12-month period",
    "calculation": "based on difference between current kW and kW from same billing period last year"
  }
}}
# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(msg1)
    st.session_state.messages.append(msg2)
    st.session_state.messages.append(msg3)
IBM_token();

# UI
st.title("💬 Your Energy AI Chatbot")
st.write("Ask me anything!")

# Display chat history
for message in st.session_state.messages:
    if (message["role"]!='system'):
     with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from IBM
    with st.spinner("Thinking..."):
        assistant_reply = IBM_chat(st.session_state.messages)
    
    # Display assistant message
    st.chat_message("assistant").markdown(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})