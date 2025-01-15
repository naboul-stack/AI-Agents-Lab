@lab.Title

Hello, and welcome to your lab environment for Agent Service! 🤖

In this environment you have all you need to follow this lab.

First, we need to log in to the virtual machine. Use the following password **+++@lab.VirtualMachine(Win11-Pro-Base).Password+++** for that.

After you logged in use the following steps to log in to **Azure Portal**:

1. Open **Edge Browser** and navigate to **+++portal.azure.com+++**

2. When prompted, log in using the following credentials:

    Username: **+++@lab.CloudPortalCredential(User1).Username+++**

    Password: **+++@lab.CloudPortalCredential(User1).Password+++**

===

# Azure CLI Authentication

Azure AI Agent Service needs authentication to work.
In order to authenticate and execute the notebooks follow the steps below.

1. **Open Windows Terminal**:
   - You should have it pinned in your taskbar.

2. **Log In to Azure**:
   - Run the following command to log in to your Azure account:

     ```
     az login
     ```

   - This command will open a web browser window where you can enter your Azure credentials. If the browser does not open automatically, follow the instructions in the terminal to open the URL manually and enter the provided code.
   - If prompted, log in using the following credentials:

    Username: **+++@lab.CloudPortalCredential(User1).Username+++**

    Password: **+++@lab.CloudPortalCredential(User1).Password+++**

===

# Open Notebooks

👉 All notebooks are located  in the **C:\lab** directory.

Open this directory in **Visual Studio Code**, and select from the table below the labs which you want to follow.
The labs were created to be executed independently of each other.

| Lab                     | Description                                   |
|-------------------------|-----------------------------------------------|
| lab01-basics.ipynb      | Basics on how to create agents.               |
| lab02-models.ipynb      | Using other models than OpenAI for agents.    |
| lab03-grounding.ipynb   | How to ground agents.                         |
| lab04-actions.ipynb     | Giving arms and legs for agents.              |
| lab05-monitoring.ipynb  | Monitoring agents.                            |
| lab06-multiagents.ipynb | How to implement a multi-agent architecture.  |
| lab07-bonus.ipynb       | Bonus lab.                                    |

**Enjoy your lab!** ❤️
