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

     ```console
     az login
     ```

   - This command will open a web browser window where you can enter your Azure credentials. If the browser does not open automatically, follow the instructions in the terminal to open the URL manually and enter the provided code.
   - If prompted, log in using the following credentials:

    Username: **+++@lab.CloudPortalCredential(User1).Username+++**

    Password: **+++@lab.CloudPortalCredential(User1).Password+++**

===

# Azure AI Foundry Provisioning

🔴 **This step should be executed only if the instructors told you to do, because there is know bug that might affect the automatic provisioning process.** 🔴

Open **Windows Terminal** and navigate to folder **C:\Users\LabUser\Lab Files\Azure**.

If you don't have this folder, clone the repository with the following command:

```console
git clone --single-branch --depth 1 "https://github.com/gxjorge/AI-Agents-Lab.git" "C:\Users\LabUser\Lab Files"
```

Execute the command below to provision the required Azure AI Foundry resources. The process takes around 10-15 minutes.

```console
az deployment group create --resource-group agents-lab --template-file main.bicep --only-show-errors
```

You should see no error, but if there is any error, then delete the resources and try again.


===

# Open Notebooks

👉 All notebooks are located in the **C:\Users\LabUser\Lab Files** directory.

Before anything let's make sure we have the latest version of the notebooks. Execute the commands below on **Windows Terminal**. 

```console
git config --global --add safe.directory 'C:/Users/LabUser/Lab Files'
cd "C:\Users\LabUser\Lab Files"
git pull
```

Now open this directory in **Visual Studio Code**, and select the notebook **lab00-intro+setup.ipynb**.

You need to select a **Python kernel** to execute the notebooks. There is already Python installed, with all the required libraries installed.
Select this kernel, before executing any code.

After you followed the instructions in the setup notebook, then you can select from the table below the labs which you want to follow.
The labs were created to be executed independently of each other.

| Lab                             | Description                                   |
|---------------------------------------------------------------------------------|
| lab00-intro+setup.ipynb         | Introduction and setup to notebooks.          |
| lab01-basics.ipynb              | Basics on how to create agents.               |
| lab02-models.ipynb              | Using other models than OpenAI for agents.    |
| lab03-grounding.ipynb           | How to ground agents.                         |
| lab04-actions.ipynb             | Giving arms and legs for agents.              |
| lab05-monitoring.ipynb          | Monitoring agents.                            |
| lab06-multiagents.ipynb         | How to implement a multi-agent architecture.  |
| lab07-bonus.ipynb               | Bonus lab.                                    |

**Enjoy your lab!** ❤️
