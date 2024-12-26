import os
import streamlit as st
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
load_dotenv()

# Set up environment variables for API keys
os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = ""  # Replace with your actual Serper API key

# Initialize search tool (SerperDevTool)
search_tool = SerperDevTool()

# Define the research agents
research_agent_usa = Agent(
    role='USA Places Researcher',
    goal='Find and best places in the USA States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the USA States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_india = Agent(
    role='India Places Researcher',
    goal='Find and best places in the India States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the India States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_japan = Agent(
    role='Japan Places Researcher',
    goal='Find and best places in the Japan Prefectures.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the Japan Prefectures. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_uk = Agent(
    role='UK Places Researcher',
    goal='Find and best places in the UK States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the UK States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_italy = Agent(
    role='Italy Places Researcher',
    goal='Find and best places in the Italy States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the Italy States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_mexico = Agent(
    role='Mexico Places Researcher',
    goal='Find and best places in the Mexico States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the Mexico States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

research_agent_thailand = Agent(
    role='Thailand Places Researcher',
    goal='Find and best places in the Thailand States.',
    backstory="""You're a researcher tasked with analyzing both the historical and current locations of the Thailand States. 
    You will gather information on cities, tourist spots, and regional insights, providing a complete picture from past to present.""",
    verbose=True,
    allow_delegation=True,
    max_execution_time=300
)

# Define the tasks for each agent
task_usa = Task(
    description='Find and summarize both historical and current information about notable places in the USA, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_usa,
    tools=[search_tool]
)

task_india = Task(
    description='Find and summarize both historical and current information about notable places in India, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_india,
    tools=[search_tool]
)

task_japan = Task(
    description='Find and summarize both historical and current information about notable places in Japan, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_japan,
    tools=[search_tool]
)

task_uk = Task(
    description='Find and summarize both historical and current information about notable places in the UK, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_uk,
    tools=[search_tool]
)

task_italy = Task(
    description='Find and summarize both historical and current information about notable places in Italy, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_italy,
    tools=[search_tool]
)

task_mexico = Task(
    description='Find and summarize both historical and current information about notable places in Mexico, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_mexico,
    tools=[search_tool]
)

task_thailand = Task(
    description='Find and summarize both historical and current information about notable places in Thailand, including tourist destinations and cities.',
    expected_output='A bullet list of the oldest and newest attraction places, including details and context for each.',
    agent=research_agent_thailand,
    tools=[search_tool]
)

# Set up the crew to carry out the research task
crew = Crew(
    agents=[research_agent_usa, research_agent_india, research_agent_japan, research_agent_uk, research_agent_italy, research_agent_mexico, research_agent_thailand],
    verbose=True
)

# Function to summarize text sentence by sentence
def summarize_text(text):
    # Split the text into sentences
    sentences = text.split('.')
    summarized_result = ""
    
    # Add each sentence to the summary, removing extra spaces and ensuring a clean format
    for sentence in sentences:
        if sentence.strip():  # Skip empty sentences
            summarized_result += f"{sentence.strip()}.\n"
    
    return summarized_result

# Streamlit app layout
st.markdown("### **Crew AI Global Explorer**")  # Heading in bold using markdown
st.subheader("Find information on popular tourist destinations and cities around the world.")

# Add checkboxes to select countries
usa_selected = st.checkbox("USA")
india_selected = st.checkbox("India")
japan_selected = st.checkbox("Japan")
italy_selected = st.checkbox("Italy")
uk_selected = st.checkbox("UK")
mexico_selected = st.checkbox("Mexico")
thailand_selected = st.checkbox("Thailand")

# Text input for the user to specify the query
query = st.text_input("Enter a place or region (e.g., 'top tourist spots in USA, India' or 'famous places in USA, India'): ")

# Button to trigger the research
if st.button("Get Results"):
    if query:
        selected_tasks = []
        if usa_selected:
            selected_tasks.append(task_usa)
        if india_selected:
            selected_tasks.append(task_india)
        if japan_selected:
            selected_tasks.append(task_japan)
        if italy_selected:
            selected_tasks.append(task_italy)
        if uk_selected:
            selected_tasks.append(task_uk)
        if mexico_selected:
            selected_tasks.append(task_mexico)
        if thailand_selected:
            selected_tasks.append(task_thailand)

        if selected_tasks:
            # Run the selected tasks and retrieve results
            results = []
            for task in selected_tasks:
                crew.tasks = [task]
                result = crew.kickoff()
                results.append(result)

            # Summarize the results sentence by sentence
            try:
                summarized_result = ""
                for result in results:
                    if hasattr(result, 'text'):  # This checks if the result has a 'text' attribute
                        result_text = result.text
                    else:
                        result_text = str(result)  # If it's not a CrewOutput with a 'text' attribute, convert it to a string

                    # Get the summarized result
                    summarized_result += summarize_text(result_text)

                # Display the summarized results
                st.success("Summarized Results:")
                st.write(summarized_result)
            except Exception as e:
                st.error(f"An error occurred while processing the result: {e}")
        else:
            st.error("Please select at least one country.")
    else:
        st.error("Please enter a valid query.")