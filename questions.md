# Questions

* Where are the agents from Agent service suppose to run?
* What functionalities do you recommend to show during the Tech connect Lab
* What regions are supported by the Agent Service? (France central and Sweeden central are not supported)
https://learn.microsoft.com/en-gb/azure/ai-services/agents/concepts/model-region-support?tabs=python#azure-openai-models
* Do you have any bicep files with bing, Azure Monitor, application insights, etc.
https://github.com/Azure/azure-ai-agents
* How can i add the bing grounding to the bicep files?

# Content examples:
* Showcasing with the OpenAI SDK
* Show model choice (llama3/cohere)
* Grounding support:
    * Bring your own blob storage 
    * Bring your AI index
    * Bring your file to assistant API
    * Fabric/Sharepoint

* Bing grounding: 
    * https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/agents/sample_agents_bing_grounding.py
    * https://github.com/Azure/azure-ai-agents/blob/main/standard-agent-bing.bicep
* On-behalf of workflow
* Actions:
    * Code Interpreter: Advance data analytics
    * OpenAPI action : https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/agents/sample_agents_openapi.py
    * Logicapps connectors (not ready)
    * Azure functions
* Tracing/ Monitoring 
* Multiagent with SK or Autogen


