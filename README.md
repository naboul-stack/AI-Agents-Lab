# Agents in Action: Transforming through Automation and Intelligence

## Table of Contents

1. [📘 Introduction to Agentic Systems](#introduction-to-agentic-systems)
2. [🤖 What is an Agent?](#what-is-an-agent)
   - [Characteristics of Agents](#characteristics-of-agents)
3. [🚀 Applications of Agentic Systems](#applications-of-agentic-systems)
   - [Automotive & Transportation](#automotive--transportation)
   - [Retail & Consumer Packaged Goods](#retail--consumer-packaged-goods)
   - [Finance](#finance)
   - [Manufacturing](#manufacturing)
4. [☁️ Azure AI Agent Service](#azure-ai-agent-service)
   - [Key Features of Azure AI Agent Service](#key-features-of-azure-ai-agent-service)
   - [How Azure AI Agent Service Works](#how-azure-ai-agent-service-works)
   - [Setup](#setup)
   - [Getting started with the Azure Agent Service with the OpenAI SDK](#getting-started-with-the-azure-agent-service-with-the-openai-sdk)
   - [Getting started with the Azure AI Foundry SDK](#getting-started-with-the-azure-ai-foundry-sdk)
   - [Use other models with the Azure AI Agent Service](#use-other-models-with-the-azure-ai-agent-service)
   - [Grounding with Bing](#grounding-with-bing)
   - [Actions with Code Interpreter](#actions-with-code-interpreter)
   - [OpenAPI Actions](#openapi-actions)
   - [Actions with Azure functions](#actions-with-azure-functions)
   - [Tracing and monitoring](#tracing-and-monitoring)
   - [Multi-agent with SK/Autogen](#multi-agent-with-skautogen)
5. [💼 Bonus exercise: Personal Financial Assistant](#bonus-exercise-personal-financial-assistant)
6. [📊 Bonus exercise: Sales Analyst Agent](#bonus-exercise-sales-analyst-agent)

## Introduction to Agentic Systems

In the rapidly evolving field of Artificial Intelligence, agentic systems represent a significant step forward in designing intelligent applications. These systems are composed of autonomous entities, known as *agents*, that can perceive their environment, make decisions, and act upon their environment to achieve specific goals.

### What is an Agent?

An *agent* can be defined as a software entity designed to autonomously or semi-autonomously:

- **Perceive**: Gather data from its environment through sensors or data inputs.
- **Reason**: Process perceived information to make informed decisions based on its goals.
- **Act**: Execute decisions by performing actions that influence their environment.
- **Remember**: Store past experiences and information to inform future decisions, enabling learning and adaptation.

#### Characteristics of Agents:

1. **Autonomy**: Operates without direct human intervention.
2. **Proactiveness**: Takes initiative to achieve goals.
3. **Reactivity**: Responds to changes in its environment in real-time.
4. **Event-Driven Behavior**: Reacts to specific events or changes in its environment, enabling real-time adaptability.
5. **Social Ability**: Communicates with other agents or systems to collaborate.

### Applications of Agentic Systems

Here are some use cases for agentic Systems in different sectors:
* Automotive & Transportation
    * Autonomous Vehicles
        * Self-Driving Capabilities: AI agents use a combination of sensors, cameras, and machine learning algorithms to perceive the environment, make decisions, and control the vehicle. This includes tasks like lane keeping, obstacle detection, and adaptive cruise control.
        * Improved Navigation: AI agents can analyze real-time traffic data, road conditions, and map information to optimize routes, reduce travel time, and improve fuel efficiency.
        * Enhanced Safety Features: AI agents can monitor driver behavior, detect potential hazards, and take preventive actions such as automatic braking, lane departure warnings, and collision avoidance systems.
    * Predictive Maintenance
        * Vehicle Health Monitoring: AI agents continuously collect data from various sensors in the vehicle to monitor the condition of critical components like the engine, brakes, and transmission.
        * Predicting Maintenance Needs: By analyzing historical data and current performance metrics, AI agents can predict when a component is likely to fail and schedule maintenance before a breakdown occurs.
        * Scheduling Services: AI agents can automatically book service appointments, order necessary parts, and notify the owner, ensuring timely maintenance and reducing downtime.
    * Customer Experience
        * Personalized Recommendations: AI agents can analyze user preferences and driving habits to recommend features, services, and even new vehicles that match the customer’s needs.
        * Vehicle Configuration Assistance: AI agents can guide customers through the process of configuring their vehicle, suggesting options and packages based on their preferences and budget.
        * Enhanced Customer Service: AI agents can provide 24/7 support through chatbots and virtual assistants, answering questions, scheduling test drives, and providing updates on service status.
    * Transportation
    * Fleet Management
        * Route Optimization: AI agents can analyze traffic conditions, delivery schedules, and vehicle locations to determine the most efficient routes, reducing fuel consumption and travel time.
        * Schedule Management: AI agents can manage driver schedules, ensuring compliance with regulations and optimizing shift patterns to maximize productivity.
        * Vehicle Health Monitoring: Similar to predictive maintenance in automotive, AI agents can monitor the health of fleet vehicles, predict maintenance needs, and schedule services to minimize downtime.
    * Traffic Management
        * Traffic Pattern Analysis: AI agents can analyze real-time traffic data from various sources to identify congestion patterns and predict traffic flow.
        * Signal Timing Optimization: By adjusting traffic signal timings based on current traffic conditions, AI agents can reduce congestion and improve traffic flow.
        * Congestion Management: AI agents can implement dynamic traffic management strategies, such as rerouting traffic, adjusting speed limits, and providing real-time traffic updates to drivers.
    * Logistics Optimization
        * Inventory Management: AI agents can forecast demand, manage stock levels, and automate reordering processes, ensuring that inventory is always at optimal levels.
        * Demand Forecasting: By analyzing historical sales data and market trends, AI agents can predict future demand, helping businesses plan their logistics operations more effectively.
        * Optimized Logistics: AI agents can plan and coordinate the movement of goods, optimizing routes, schedules, and load distribution to ensure timely delivery and reduce cost

* Retail & Consumer Packaged Goods
    * Personalized Marketing
        * Customer Data Analysis: AI agents can analyze vast amounts of customer data, including purchase history, browsing behavior, and demographic information, to understand individual preferences and behaviors.
        * Targeted Campaigns: Using this data, AI agents can create highly targeted marketing campaigns that resonate with specific customer segments, increasing engagement and conversion rates.
        * Product Recommendations: AI agents can recommend products to customers based on their past purchases and browsing history, enhancing the shopping experience and boosting sales.
        * Dynamic Pricing: AI agents can optimize pricing strategies by analyzing market trends, competitor pricing, and customer demand, ensuring competitive pricing while maximizing profits.
    * Inventory Management
        * Demand Forecasting: AI agents can predict future demand by analyzing historical sales data, market trends, and seasonal patterns, helping retailers maintain optimal inventory levels.
        * Stock Level Management: AI agents can monitor stock levels in real-time, ensuring that popular items are always available and reducing the risk of overstocking or stockouts.
        * Automated Reordering: When stock levels fall below a certain threshold, AI agents can automatically place reorders, streamlining the supply chain and reducing manual intervention.
        * Waste Reduction: By accurately predicting demand and managing stock levels, AI agents can help reduce waste, particularly for perishable goods.
    * Customer Experience
        * Virtual Assistants: AI-powered virtual assistants can assist customers with their queries, provide product information, and guide them through the shopping process, enhancing customer satisfaction.
        * Personalized Recommendations: AI agents can offer personalized product recommendations based on individual customer preferences and past behavior, making the shopping experience more enjoyable and relevant.
        * Efficient Customer Service: AI agents can handle routine customer service tasks, such as answering FAQs, processing returns, and tracking orders, freeing up human agents to handle more complex issues.
    * Consumer Packaged Goods (CPG)
    * Supply Chain Optimization
        * Demand Forecasting: AI agents can analyze sales data, market trends, and external factors (like weather or economic conditions) to accurately forecast demand, ensuring that supply meets demand.
        * Inventory Management: AI agents can manage inventory levels across the supply chain, ensuring that products are available where and when they are needed, reducing stockouts and excess inventory.
        * Logistics Optimization: AI agents can optimize logistics by planning efficient routes, consolidating shipments, and managing transportation schedules, reducing costs and improving delivery times.
    * Product Development
        * Market Trend Analysis: AI agents can analyze market trends, consumer feedback, and social media data to identify emerging trends and consumer preferences, guiding product development.
        * Consumer Feedback Analysis: By analyzing customer reviews, surveys, and feedback, AI agents can identify areas for improvement in existing products and suggest new product ideas.
        * Rapid Prototyping: AI agents can assist in the rapid prototyping and testing of new products, using data-driven insights to refine and improve product designs before full-scale production.
    * Quality Control
        * Production Monitoring: AI agents can monitor production processes in real-time, detecting any deviations from quality standards and alerting operators to potential issues.
        * Defect Detection: Using advanced image recognition and machine learning algorithms, AI agents can detect defects in products during the manufacturing process, ensuring high-quality output.
        * Process Optimization: AI agents can analyze production data to identify inefficiencies and suggest improvements, optimizing processes and reducing waste.

* Finance
    * Fraud Detection
        * Transaction Data Analysis: AI agents can process vast amounts of transactional data to identify patterns and detect anomalies in real time.
        * Detect Unusual Patterns: By using advanced machine learning algorithms, AI agents can flag transactions that deviate from normal behavior, signaling potential fraud.
        * Prevent Fraud: Proactive monitoring and analysis by AI agents help prevent fraudulent activities before they escalate, ensuring financial security for customers.
        * Customer Security: AI agents enhance customer trust by safeguarding sensitive financial data and ensuring secure transactions.
    * Risk Management
        * Analyze Market Data: AI agents can analyze diverse datasets, including market trends, economic indicators, and geopolitical events, to assess risks.
        * Predict Trends: By leveraging predictive analytics, AI agents can forecast market movements and potential risks, enabling proactive decision-making.
        * Insights and Recommendations: AI agents provide actionable insights and tailored recommendations for minimizing financial risks and maximizing returns.
    * Customer Service
        * Virtual Assistants: AI-powered virtual assistants can handle customer inquiries, provide account information, and resolve common issues efficiently.
        * Process Transactions: AI agents can automate routine transactions, such as fund transfers and bill payments, reducing wait times and improving convenience.
        * Provide Financial Advice: AI agents can offer personalized financial advice based on a customer’s financial history, goals, and risk appetite.
    * Algorithmic Trading
        * Analyze Market Conditions: AI agents analyze real-time market data to identify trading opportunities and potential risks.
        * Execute Trades: AI agents can execute trades automatically, ensuring timely and accurate execution in fast-moving markets.
        * Optimize Trading Strategies: By analyzing historical data and market trends, AI agents can refine and optimize trading algorithms for better outcomes.
        * Reduce Human Error: Automation by AI agents minimizes the risk of human error, ensuring precise and consistent trading operations.
    * Regulatory Compliance
        * Monitor Transactions and Communications: AI agents ensure compliance by continuously monitoring financial transactions and communications for irregularities.
        * Flag Suspicious Activities: AI agents can identify and flag potential compliance breaches or suspicious activities for further investigation.
        * Automatically Report to Regulatory Authorities: AI agents streamline compliance processes by generating and submitting regulatory reports automatically, reducing manual effort.

* Manufacturing 
    * Predictive Maintenance
        * Machine Sensor Data Analysis: AI agents analyze real-time sensor data from machinery to identify patterns and anomalies that may indicate potential issues.
        * Failure Prediction: By leveraging advanced machine learning models, AI agents can predict equipment failures before they occur, minimizing downtime.
        * Preemptive Maintenance Scheduling: AI agents enable manufacturers to schedule maintenance proactively, reducing the risk of unexpected breakdowns and increasing operational efficiency.
    * Energy Management
        * Monitor Energy Usage: AI agents continuously monitor energy consumption across production facilities to identify inefficiencies.
        * Optimize Usage: AI agents provide actionable insights to optimize energy use, reducing costs while maintaining operational requirements.
        * Adjust Energy-Intensive Processes: By analyzing energy-intensive operations, AI agents can recommend adjustments to improve energy efficiency and   * sustainability.
    * Process Automation
        * Material Handling: AI agents automate material handling processes, ensuring precise and efficient movement of goods within facilities.
        * Assembly Line Operations: AI agents enhance assembly line efficiency by automating repetitive tasks and monitoring workflows for bottlenecks or issues.
    * Supply Chain Optimization
        * Demand Forecasting: AI agents predict demand by analyzing historical sales data, market trends, and external factors, ensuring an optimized supply chain.
        * Logistics Optimization: AI agents plan efficient logistics routes and schedules, reducing transportation costs and delivery times.
        * Inventory Optimization: By analyzing stock levels and demand patterns, AI agents ensure the right products are available at the right time, minimizing overstock and stockouts.
    * Product Development
        * Market Trend Analysis: AI agents analyze market trends and consumer preferences to guide the development of new products.
        * Consumer Feedback Analysis: By processing customer reviews and feedback, AI agents identify areas for product improvement and innovation.
        * Rapid Prototyping: AI agents assist in designing and testing prototypes quickly, using data-driven insights to refine product designs.
    * Quality Control
        * Production Monitoring: AI agents monitor production processes in real-time to ensure adherence to quality standards.
        * Defect Detection: Using advanced image recognition, AI agents detect defects in products during manufacturing, improving overall quality.
        * Process Optimization: AI agents analyze production data to identify inefficiencies, streamline workflows, and reduce waste.
    
## Azure AI Agent Service

The Azure AI Agent Service is a fully managed platform designed to enable developers to build, deploy, and manage intelligent agents efficiently. By leveraging Azure's ecosystem, developers can focus on the logic and behaviors of their agents without worrying about infrastructure and scalability challenges.

### Key Features of Azure AI Agent Service

1. **Agent Lifecycle Management**: Provides tools to simplify the development, deployment, and monitoring of agents across various environments.
2. **Event-Driven Architecture**: Agents respond to triggers and events, enabling real-time decision-making and interactions.
3. **Skill Integration and Orchestration**: Enables agents to connect and orchestrate multiple external tools, APIs, and services to extend their functionality.
4. **State Management**: Supports memory and state retention to ensure agents can maintain context and continuity during interactions.
5. **Multi-Modal Interactions**: Allows agents to interact through multiple channels, such as chat, voice, and APIs.
6. **Security and Compliance**: Leverages Azure’s security features to ensure secure and compliant deployment.
7. **Interoperability**: Seamlessly integrates with Azure OpenAI, Cognitive Services, and other Azure tools to create comprehensive solutions.
8. **Low-Code/No-Code Options**: Empowers users with varying technical expertise to design and deploy agents using intuitive interfaces and pre-built templates.

### How Azure AI Agent Service Works

Within Azure AI Foundry, an AI Agent acts as a "smart" microservice that can be used to answer questions (RAG), perform actions, or completely automate workflows. It achieves this by combining the power of generative AI models with tools that allow it to access and interact with real-world data sources.

Because Azure AI Agent Service uses the same wire protocol as Azure OpenAI Assistants, you can use either OpenAI SDKs or Azure AI Foundry SDKs to create and run an agent in just a few lines of code. 

Let's do a quick recap of the concepts we will need to understand to use the Azure AI Agent Service with the OpenAI SDK or the AI Foundry SDK:

* **Agent / Assistant***: An AI entity that uses AI models in conjunction with tools. It can be instructed and controlled to perform various tasks.
* **Tool**:	Tools help extend an agent’s ability to reliably and accurately respond during conversation. Such as connecting to user-defined knowledge bases to ground the model, or enabling web search to provide current information.
* **Thread**: Represents a conversation session between an AI entity (or Agent) and another agent or user. It stores messages and handles truncation to fit content into a model’s context.	
* **Message**:  A message created by an agent or a user. Messages can include text, images, and other files. Messages are stored as a list on the Thread.
* **Run**: Activation of an agent to begin running based on the contents of Thread. The agent uses its configuration and Thread’s Messages to perform tasks by calling models and tools. As part of a Run, the agent appends Messages to the Thread.
* **Run Step**: A detailed list of steps the agent took as part of a Run. An agent can call tools or create Messages during its run. Examining Run Steps allows you to understand how the agent is getting to its results.

Azure AI Agent Service provides a more streamlined and secure way to build and deploy AI agents. This includes:
* Automatic tool calling – no need to parse a tool call, invoke the tool, and handle the response; all of this is now done server-side
* Securely managed data – instead of managing your own conversation state, you can rely on threads to store all the information you need
* Out-of-the-box tools – In addition to the file retrieval and code interpreter tools provided by Azure OpenAI Assistants, Azure AI Agent Service also comes with a set of tools that you can use to interact with your data sources, such as Bing, Azure AI Search, and Azure Functions.

### Setup: 

The machines that you will be using, have a predeployed version of the Standard agent setup resource architecture:
![Standard Agent Setup Resource Architecture](./assets/img/standard-agent-setup-resources.png "Standard Agent Setup Resource Architecture")
Resources for the AI hub, AI project, key vault, storage account, AI Services, and AI Search are created for you. The AI Services, AI Search, key vault, and storage account are connected to your project and hub. A gpt-4o-mini model is deployed in eastus region using the Azure OpenAI endpoint for your resource.

Before creating and running any agents we need to you will need to create a connection string using information from the project that has been created for you. This string is in the format: 
```
<HostName>;<AzureSubscriptionId>;<ResourceGroup>;<ProjectName>
```
 You can also find your connection string in the overview for your project in the Azure AI Foundry portal, under Project details > Project connection string.
![Connection String](./assets/img/portal-connection-string.png "Connection String")

Now set this connection string as an environment variable named *PROJECT_CONNECTION_STRING*

   - [🧾 Notebook Lab00 - Intro and Set Up of Azure AI Agents](lab00-intro+setup.ipynb)  

### Getting started with the Azure Agent Service with the OpenAI SDK 
Finally we are able to start executing code.

In this first example we will be using the OpenAI SDK to create an Agent. 

First we will start by importing the necessary libraries:
``` python
import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI
```

Next we will :
```python
with AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
) as project_client:

    # Explicit type hinting for IntelliSense
    client: AzureOpenAI = project_client.inference.get_azure_openai_client(
        # The latest API version is 2024-10-01-preview
        api_version = os.environ.get("AZURE_OPENAI_API_VERSION"),
    )

    with client:
        agent = client.beta.assistants.create(
            model="gpt-4o-mini", name="my-agent", instructions="You are a helpful agent"
        )
        print(f"Created agent, agent ID: {agent.id}")

        thread = client.beta.threads.create()
        print(f"Created thread, thread ID: {thread.id}")

        message = client.beta.threads.messages.create(thread_id=thread.id, role="user", content="Hello, tell me a joke")
        print(f"Created message, message ID: {message.id}")

        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=agent.id)

        # Poll the run while run status is queued or in progress
        while run.status in ["queued", "in_progress", "requires_action"]:
            time.sleep(1)  # Wait for a second
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            print(f"Run status: {run.status}")

        client.beta.assistants.delete(agent.id)
        print("Deleted agent")

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        print(f"Messages: {messages}")
```

   - [🧾 Notebook Lab01 - Basics of Azure AI Agents](lab01-basics.ipynb)  

### Getting started with the Azure AI Foundry SDK

Now that we have seen how to create an agent with the OpenAI SDK, let's try to do the same with the Azure AI Foundry SDK: 
```python
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import CodeInterpreterTool
from azure.identity import DefaultAzureCredential
from typing import Any
from pathlib import Path

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(), conn_str=os.environ["PROJECT_CONNECTION_STRING"]
)

with project_client:
    # Create an instance of the CodeInterpreterTool
    code_interpreter = CodeInterpreterTool()

    # The CodeInterpreterTool needs to be included in creation of the agent
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    print(f"Created agent, agent ID: {agent.id}")

    # Create a thread
    thread = project_client.agents.create_thread()
    print(f"Created thread, thread ID: {thread.id}")

    # Create a message
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    print(f"Created message, message ID: {message.id}")

    # Run the agent
    run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        # Check if you got "Rate limit is exceeded.", then you want to get more quota
        print(f"Run failed: {run.last_error}")

    # Get messages from the thread
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")

    # Get the last message from the sender
    last_msg = messages.get_last_text_message_by_sender("assistant")
    if last_msg:
        print(f"Last Message: {last_msg.text.value}")

    # Generate an image file for the bar chart
    for image_content in messages.image_contents:
        print(f"Image File ID: {image_content.image_file.file_id}")
        file_name = f"{image_content.image_file.file_id}_image_file.png"
        project_client.agents.save_file(file_id=image_content.image_file.file_id, file_name=file_name)
        print(f"Saved image file to: {Path.cwd() / file_name}")

    # Print the file path(s) from the messages
    for file_path_annotation in messages.file_path_annotations:
        print(f"File Paths:")
        print(f"Type: {file_path_annotation.type}")
        print(f"Text: {file_path_annotation.text}")
        print(f"File ID: {file_path_annotation.file_path.file_id}")
        print(f"Start Index: {file_path_annotation.start_index}")
        print(f"End Index: {file_path_annotation.end_index}")
        project_client.agents.save_file(file_id=file_path_annotation.file_path.file_id, file_name=Path(file_path_annotation.text).name)

    # Delete the agent once done
    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")
```

### Use other models with the Azure AI Agent Service

The Azure AI Agent Service also supports the following models from the Azure AI Foundry model catalog:
* Llama 3.1-70B-instruct
* Mistral-large-2407
* Cohere command R+

Now let's create agents using Llama 3 in Azure AI Agents Service. To get started: 
1. Go to ai.azure.com and select **Model catalog** in the left navigation menu, and scroll down to **Meta-Llama-3-70B-Instruct**. You can also use  this link.  

2. Select **Deploy**. 

3. In the Deployment options screen that appears, select Serverless API with Azure AI Content Safety. 

    ![An image of the llama model project selection  screen](./assets/img/llama-deployment.png)
 
4. Select your project and click **Subscribe and deploy**. 

     ![An image of the llama model deployment screen](./assets/img/llama-deployment-2.png)

5. Add the Serverless connection to your hub / project. The deployment name you choose will be the one you reference in your code.  

6. When calling agent creation API, set the `models` parameter to your deployment name. For example:

    
    ```python
    agent = project_client.agents.create_agent( model="llama-3", name="my-agent", instructions="You are a helpful agent" ) 
    ```

Feel free to test with other models

   - [🧾 Notebook Lab02 - How to use other models in Azure AI Agent Service](lab02-models.ipynb)  


### Grounding with Bing
**Grounding with Bing Search** allows your Azure AI Agents to incorporate real-time public web data when generating responses. You need to create a Grounding with Bing Search resource, and then connect this resource to your Azure AI Agents. When a user sends a query, Azure AI Agents decide if Grounding with Bing Search should be leveraged or not. If so, it will leverage Bing to search over public web data and return relevant chunks. Lastly, Azure AI Agents will use returned chunks to generate a response.  

You can ask questions such as "*what is the top news today*" or "*what is the recent update in the retail industry in the US?*", which require real-time public data.

Developers and end users don't have access to raw content returned from Grounding with Bing Search. The response, however, includes citations with links to the websites used to generate the response, and a link to the Bing query used for the search. These two *References* must be retained and displayed in the exact form provided by Microsoft, as per Grounding with Bing Search's [Use and Display Requirements](https://www.microsoft.com/en-us/bing/apis/grounding-legal#use-and-display-requirements). See the [how to display Grounding with Bing Search results](#how-to-display-grounding-with-bing-search-results) section for details.

>[!IMPORTANT]
> 1. Your usage of Grounding with Bing Search may incur costs. See the [pricing page](https://www.microsoft.com/bing/apis/grounding-pricing) for details.
> 1. By creating and using a Grounding with Bing Search resource through code-first experience, such as Azure CLI, or deploying through deployment template, you agree to be bound by and comply with the terms available at https://www.microsoft.com/en-us/bing/apis/grounding-legal, which may be updated from time to time.


#### **Setup:**  

> [!NOTE]
> 1. Grounding with Bing Search only works with the following Azure OpenAI models: `gpt-3.5-turbo-0125`, `gpt-4-0125-preview`, `gpt-4-turbo-2024-04-09`, `gpt-4o-0513`

1. Register the Bing Search provider.

   ```console
       az provider register --namespace 'Microsoft.Bing'
   ```

1. Create a new Grounding with Bing Search resource in the [Azure portal](https://portal.azure.com/#create/Microsoft.BingGroundingSearch), and select the different fields in the creation form. Make sure you create this Grounding with Bing Search resource in the same resource group as your Azure AI Agent, AI Project, and other resources.

1. After you have created a Grounding with Bing Search resource, you can find it in [Azure portal](https://portal.azure.com/#home). Navigate to the resource group you've created the resource in, search for the Grounding with Bing Search resource you have created.

   ![alt text](assets/img/resource-azure-portal.png)

1. Select the Grounding with Bing Search resource you have created and copy any of the API keys.

    ![alt text](assets/img/key-resource-azure-portal.png)

1. Go to the [Azure AI Foundry portal](https://ai.azure.com/) and select the AI Project (make sure it's in the same resource group of your Grounding with Bing Search resource). Click **management center**.

    ![alt text](assets/img/project-settings-button.png)

1. Select **+ new connection** in the settings page. 

    >[!NOTE]
    > If you re-generate the API key at a later date, you need to update the connection with the new key.

    ![alt text](assets/img/project-connections.png)

1. Select **API key** in **other resource types**.

    ![alt text](assets/img/api-key-connection.png)

1. Enter the following information and then create a new connection to your Grounding with Bing Search resource.

    - Endpoint: `https://api.bing.microsoft.com/`
    - Key: `YOUR_API_KEY`
    - Connection name: `YOUR_CONNECTION_NAME` (You will use this connection name in the sample code below.)
    - Access: you can choose either *this project only* or *shared to all projects*. Just make sure in the sample code below, the project you entered connection string for has access to this connection.

Now that we have configured everything, let's create a client object, which will contain the connection string for connecting to your AI project and other resources. To make the Grounding with Bing search tool available to your agent, use a connection to initialize the tool and attach it to the agent. You can find your connection in the **connected resources** section of your project in the Azure AI Foundry portal.


```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import BingGroundingTool


project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

bing_connection = project_client.connections.get(
    connection_name=os.environ["BING_CONNECTION_NAME"]
)
conn_id = bing_connection.id

print(conn_id)

# Initialize agent bing tool and add the connection id
bing = BingGroundingTool(connection_id=conn_id)

# Create agent with the bing tool and process assistant run
with project_client:
    agent = project_client.agents.create_agent(
        model="gpt-4o",
        name="my-assistant",
        instructions="You are a helpful assistant",
        tools=bing.definitions,
        headers={"x-ms-enable-preview": "true"}
    )
    print(f"Created agent, ID: {agent.id}")

# Create thread for communication
thread = project_client.agents.create_thread()
print(f"Created thread, ID: {thread.id}")

# Create message to thread
message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="What is the top news today",
)
print(f"Created message, ID: {message.id}")

# Create and process agent run in thread with tools
run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
print(f"Run finished with status: {run.status}")

# Retrieve run step details to get Bing Search query link
# To render the webpage, we recommend you replace the endpoint of Bing search query URLs with `www.bing.com` and your Bing search query URL would look like "https://www.bing.com/search?q={search query}"
run_steps = project_client.agents.list_run_steps(run_id=run.id, thread_id=thread.id)
run_steps_data = run_steps['data']
print(f"Last run step detail: {run_steps_data}")

if run.status == "failed":
    print(f"Run failed: {run.last_error}")

# Delete the assistant when done
project_client.agents.delete_agent(agent.id)
print("Deleted agent")

# Fetch and log all messages
messages = project_client.agents.list_messages(thread_id=thread.id)
print(f"Messages: {messages}")
```
> **Important Considerations:** 
>    * According to Grounding with Bing's [terms of use and use and display requirements](https://www.microsoft.com/en-us/bing/apis/grounding-legal#use-and-display-requirements), you need to display both website URLs and Bing search query URLs in your custom interface. You can find website URLs through `annotations` parameter in API response and Bing search query URLs through `runstep` details. To render the webpage, we recommend you replace the endpoint of Bing search query URLs with `www.bing.com` and your Bing search query URL would look like "https://www.bing.com/search?q={search query}"
>    * Microsoft will use data you send to Grounding with Bing to improve Microsoft products and services. Where you send personal data to this service, you are responsible for obtaining sufficient consent from the data subjects. The Data Protection Terms in the Online Services Terms do not apply to Grounding with Bing. 

   - [🧾 Notebook Lab03 - How to add real-time knowledge to your Azure AI Agent via Bing (tool)](lab02-models.ipynb)  

### Actions with Code Interpreter

Code Interpreter allows the agents to write and run Python code in a sandboxed execution environment. With Code Interpreter enabled, your agent can run code iteratively to solve more challenging code, math, and data analysis problems. When your Agent writes code that fails to run, it can iterate on this code by modifying and running different code until the code execution succeeds.

> [!IMPORTANT]
> Code Interpreter has [additional charges](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) beyond the token based fees for Azure OpenAI usage. If your Agent calls Code Interpreter simultaneously in two different threads, two code interpreter sessions are created. Each session is active by default for one hour.

To use code interpreter, first add the `import` statements shown in the example, and create a project client, which will contain a connection string to your AI project, and will be used to authenticate API calls. 

The [models page](https://learn.microsoft.com/en-us/azure/ai-services/agents/quotas-limits) contains the most up-to-date information on regions/models where agents and code interpreter are supported.

We recommend using Agents with the latest models to take advantage of the new features, larger context windows, and more up-to-date training data.


```python
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import CodeInterpreterTool
from azure.ai.projects.models import FilePurpose
from azure.identity import DefaultAzureCredential
from pathlib import Path

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(), conn_str=os.environ["PROJECT_CONNECTION_STRING"]
)

file = project_client.agents.upload_file_and_poll(
    file_path="nifty_500_quarterly_results.csv", purpose=FilePurpose.AGENTS
)
print(f"Uploaded file, file ID: {file.id}")

code_interpreter = CodeInterpreterTool(file_ids=[file.id])

# create agent with code interpreter tool and tools_resources
agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="my-agent",
    instructions="You are helpful agent",
    tools=code_interpreter.definitions,
    tool_resources=code_interpreter.resources,
)
# create a thread
thread = project_client.agents.create_thread()
print(f"Created thread, thread ID: {thread.id}")

# create a message
message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="Could you please create bar chart in the TRANSPORTATION sector for the operating profit from the uploaded csv file and provide file to me?",
)
print(f"Created message, message ID: {message.id}")

# create and execute a run
run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
print(f"Run finished with status: {run.status}")

if run.status == "failed":
    # Check if you got "Rate limit is exceeded.", then you want to get more quota
    print(f"Run failed: {run.last_error}")

# delete the original file from the agent to free up space (note: this does not delete your version of the file)
project_client.agents.delete_file(file.id)
print("Deleted file")

# print the messages from the agent
messages = project_client.agents.list_messages(thread_id=thread.id)
print(f"Messages: {messages}")

# get the most recent message from the assistant
last_msg = messages.get_last_text_message_by_sender("assistant")
if last_msg:
    print(f"Last Message: {last_msg.text.value}")
```

Files generated by Code Interpreter can be found in the Agent message responses. You can download image file generated by code interpreter, by iterating through the response's `image_contents` and calling `save_file()` with a name and the file ID.  

```python
# save the newly created file
for image_content in messages.image_contents:
  print(f"Image File ID: {image_content.image_file.file_id}")
  file_name = f"{image_content.image_file.file_id}_image_file.png"
  project_client.agents.save_file(file_id=image_content.image_file.file_id, file_name=file_name)
  print(f"Saved image file to: {Path.cwd() / file_name}") 
```

In the following exercise 
#### **Solution:** 
```python

```

### OpenAPI Actions

You can now connect your Azure AI Agent to an external API using an OpenAPI 3.0 specified tool, 
allowing for scalable interoperability with various applications. Enable your custom tools 
to authenticate access and connections with managed identities (Microsoft Entra ID) for 
added security, making it ideal for integrating with existing infrastructure or web services.

OpenAPI Specified tool improves your function calling experience by providing standardized, 
automated, and scalable API integrations that enhance the capabilities and efficiency of your agent. 
[OpenAPI specifications](https://spec.openapis.org/oas/latest.html) provide a formal standard for 
describing HTTP APIs. This allows people to understand how an API works, how a sequence of APIs 
work together, generate client code, create tests, apply design standards, and more. Currently, we support 3 authentication types with the OpenAPI 3.0 specified tools: `anonymous`, `API key`, `managed identity`.



1. Check the OpenAPI spec for the following requirements:
    1. `operationId` should only contain letters, `-` and `_`. You can modify it to meet the requirement. We recommend using descriptive name to help models efficiently decide which function to use.


1. Verify that the OpenAPI spec supports API keys: it has `securitySchemes` section and has one scheme of type `apiKey". An example would be:
   ```json
       "securitySchemes": {
          "apiKeyHeader": {
                    "type": "apiKey",
                    "name": "x-api-key",
                    "in": "header"
                }
        }
   ```
   If the security schemes include multiple schemes, we recommend keeping only one of them.

1. Remove any parameter in the OpenAPI spec that needs API key, because API key will be stored and passed through a connection, as described here bellow.

1. Create a `custom keys` connection to store your API key.

    1. Go to the [Azure AI Foundry portal](https://ai.azure.com/) and select the AI Project. Click **connected resources**.
    ![alt text](assets/img/project-settings-button.png)

    1. Select **+ new connection** in the settings page. 
        >[!NOTE]
        > If you re-generate the API key at a later date, you need to update the connection with the new key.
        
       ![alt text](assets/img/project-connections.png)

   1. Select **custom keys** in **other resource types**.
    
        ![alt text](assets/img/api-key-connection.png)
    
   1. Enter the following information
      - key: `name` of your security scheme. In this example, it should be `x-api-key`
        ```json
               "securitySchemes": {
                  "apiKeyHeader": {
                            "type": "apiKey",
                            "name": "x-api-key",
                            "in": "header"
                        }
                }
        ```
      - value: YOUR_API_KEY
      - Connection name: YOUR_CONNECTION_NAME (You will use this connection name in the sample code below.)
      - Access: you can choose either *this project only* or *shared to all projects*. Just make sure in the sample code below, the project you entered connection string for has access to this connection.

Let's now try this out with the following code:
```python
import os
import jsonref
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import OpenApiTool, OpenApiAnonymousAuthDetails

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# You might want to store the OpenAPI specification in another file and import the content to initialize the tool. Please note the sample code is using `anonymous` as authentication type.
with open('./weather_openapi.json', 'r') as f:
    openapi_spec = jsonref.loads(f.read())

# Create Auth object for the OpenApiTool (note that connection or managed identity auth setup requires additional setup in Azure)
auth = OpenApiAnonymousAuthDetails()

# Initialize agent OpenApi tool using the read in OpenAPI spec
openapi = OpenApiTool(name="get_weather", spec=openapi_spec, description="Retrieve weather information for a location", auth=auth)
```
If you want to use connection, which stores API key, for authentication, replace the line with
```python
auth = OpenApiConnectionAuthDetails(security_scheme=OpenApiConnectionSecurityScheme(connection_id="your_connection_id"))
```
Your connection ID looks like `/subscriptions/{subscription ID}/resourceGroups/{resource group name}/providers/Microsoft.MachineLearningServices/workspaces/{project name}/connections/{connection name}`.

If you want to use managed identity for authentication, replace the line with
```python
auth = OpenApiManagedAuthDetails(security_scheme=OpenApiManagedSecurityScheme(audience="https://your_identity_scope.com"))
```
An example of the audience would be ```https://cognitiveservices.azure.com/```.

Then create the thread
```python
# Create agent with OpenApi tool and process assistant run
with project_client:
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-assistant",
        instructions="You are a helpful assistant",
        tools=openapi.definitions
    )
    print(f"Created agent, ID: {agent.id}")

    # Create thread for communication
    thread = project_client.agents.create_thread()
    print(f"Created thread, ID: {thread.id}")

# Create a run and observe that the model uses the OpenAPI Spec tool to provide a response to the user's question.
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="What's the weather in Seattle?",
    )
    print(f"Created message, ID: {message.id}")

    # Create and process agent run in thread with tools
    run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # Delete the assistant when done
    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")

    # Fetch and log all messages
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
```

### Actions with Azure functions

The Azure AI Agent Service integrates with Azure Functions, enabling you to create intelligent, event-driven applications with minimal overhead. This combination allows AI-driven workflows to leverage the scalability and flexibility of serverless computing, making it easier to build and deploy solutions that respond to real-time events or complex workflows.

Azure Functions provide support for triggers and bindings, which simplify how your AI Agents interact with external systems and services. Triggers determine when a function executes—such as an HTTP request, message from a queue, or a file upload to Azure Blob Storage and allows agents to act dynamically based on incoming events.

Meanwhile, bindings facilitate streamlined connections to input or output data sources, such as databases or APIs, without requiring extensive boilerplate code. For instance, you can configure a trigger to execute an Azure Function whenever a customer message is received in a chatbot and use output bindings to send a response via the Azure AI Agent.

   - [🧾 Notebook Lab04 - How to make your Azure AI Agent act](lab04-actions.ipynb)  

### Tracing and monitoring

   - [🧾 Notebook Lab05 - Intro to Tracing and Monitoring in Azure AI foundry](lab05-monitoring.ipynb)  

### Multi-agent with SK/Autogen

   + [🧾 Notebook Lab06 - Building MaS with Azure AI Agents & [Autogen v0.4 (New Autogen Architecture) or SK Agentic Framework)]](lab06-multiagents.ipynb)

   > If you need an in-depth hands-on learning lab about AutoGen and Semantic Kernel agentic frameworks, please visit this GitHub repo: https://github.com/pablosalvador10/gbbai-agent-architecture-lab 

#### **Formula (and Mental Model) for building MaS**

```
Multi-Agent Architecture = Σ (Production-Ready Single Agents (with tools, memory, traceability, and isolated execution)) + Preferred Framework (Semantic Kernel, AutoGen, etc.)
```

Always start by breaking down the problem into its fundamental components. Identify the decoupled, modular functions that need to be developed, and then design and build the system from a high-level perspective down to the low-level details. In other words:

**First, build single agents:** Ensure that individual agents are scalable and work reliably for the identified specialized task. Leverage Azure AI Agent Service.

**Then, establish connections between agents, if needed:** Begin constructing inter-agent connections as add-on capabilities. This enables agents to collaborate on tasks—either by directly negotiating or by being indirectly guided toward a common goal. This approach will define your overall architecture and design pattern.

#### **Why Start with Single Agents?**

The `Azure AI Agent Service` makes it straightforward to design agents that are robust, context-aware, and capable of achieving specific goals autonomously. Once these agents successfully handle their tasks as singletons, you can gradually expand them into more complex multi-agent architectures.

**But how do we enable our agents to talk to each other?** In the human world, we might simply put people in the same room to converse naturally. Similarly, agents can be set up to interact and collaborate in virtual rooms, exchanging messages and forming the foundation for advanced, event-driven agent architectures. To achieve this, you can either build your code from scratch or leverage an existing framework. There are many options available, but at Microsoft, we are focusing on two open-source SDKs.

#### **Enable Agent Communication with the Power Duo: Semantic Kernel or AutoGen**

- **AutoGen:**  
Ideal for creativity and experimentation, AutoGen serves as a state-of-the-art research SDK. It allows you to test new ideas, experiment with collaboration patterns, and push the boundaries of agent capabilities.

- **Semantic Kernel:**  
Provides an enterprise-grade orchestration framework that supports seamless, non-breaking changes once your ideas are validated. It's designed for production-scale reliability, enabling teams to move quickly without sacrificing stability.

### Bonus exercise: Personal Financial Assistant

In this exercise the goal is to demonstrates a practical use case where an AI Agent will be leveraged to gain actionable insights and address key analytical questions related to managing an investment portfolio. For this use case we will ask you to combine Function Calling and Code Interpreter. These tools work together to retrieve stock prices and calculate portfolio metrics, replicating real-world workflows in investment management.

#### **Key Steps:**
1. Upload Investment Data: Import a CSV file containing the user’s investment portfolio into the OpenAI Project.
1. Fetch Real-Time Stock Prices: Use the Yahoo! Finance API via Function Calling to retrieve up-to-date closing stock data.
1. Perform Portfolio Analysis: Leverage Code Interpreter to compute key portfolio metrics and insights.
1. Create Data Visualations: Leverage Code Interpreter to generate portfolio visualization, and leverage Python libraries to render image.

#### **Hints:**
Here bellow you can find a potential yahoo Finance API function:
```py
import yfinance as yf

def fetch_stock_price(ticker_symbol: str) -> str:
    """
    Fetch the latest stock price for a given ticker symbol.

    Parameters:
    - ticker_symbol (str): The ticker symbol of the stock to retrieve data for.

    Returns:
    - str: The closing price of the stock for the latest trading day, or an error message if data is unavailable.

    Example:
    >>> fetch_stock_price("AAPL")
    "148.9"
    """
    
    try:
        # Fetch the stock's trading history for the last day
        stock = yf.Ticker(ticker_symbol)
        stock_data = stock.history(period="1d")

        # Check if the data is empty, indicating an invalid ticker or no data available
        if stock_data.empty:
            return f"Error: No data found for ticker symbol: {ticker_symbol}"

        # Retrieve and return the latest closing price
        latest_close_price = stock_data['Close'].iloc[-1]
        return str(round(latest_close_price, 3))

    except KeyError as e:
        return f"Error: Data missing for key: {e}. Verify the ticker symbol."

    except Exception as e:
        return f"Error: Unexpected issue occurred - {type(e).__name__}: {e}"
    
print("Function defined successfully.")
```
And its correspondant json to add to the tool list:
```json
{
    "type": "function",
    "function": {
        "name": "fetch_stock_price",
        "description": "Retrieve the latest closing price of a stock using its ticker symbol.",
        "parameters": {
            "type": "object",
            "properties": {"ticker_symbol": {"type": "string", "description": "The ticker symbol of the stock"}},
            "required": ["ticker_symbol"],
        },
    },
}
```

### Bonus exercise: Sales Analyst Agent

In this bonus exercise you will have to use of Azure Agent Service to analyze sales data for AdventureWorks. The AI agent will need to performs key tasks, including retrieving files, conducting sales calculations, and generating actionable insights. The key objective here is to upload, and analyze sales data to generate actionable insights like regional revenue metrics.