

# Provisioning Resources

There is a know issue where the deployment of Azure AI Foundry resources doesn't happen successfully.
In order to mi

Open a Windows Terminal and navigate to the folder **C:\Users\LabUser\Lab Files\Azure**.

If you don't have this folder, clone the repository with the following command:

```console
git clone --single-branch --depth 1 "https://github.com/gxjorge/AI-Agents-Lab.git" "C:\Users\LabUser\Lab Files"
```

```console
az deployment group create --resource-group agents-lab --template-file main.bicep --only-show-errors
```
