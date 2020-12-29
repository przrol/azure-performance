#!/bin/bash

# Variables
resourceGroup="acdnd-c4-project"
location="eastus2"
logAnalyticsWorkspaceName="LogAnalyticsRp$RANDOM"

# Create Log Analytics workspace
echo "Creating Log Analytics workspace: $logAnalyticsWorkspaceName..."

az monitor log-analytics workspace create \
--resource-group $resourceGroup \
--workspace-name $logAnalyticsWorkspaceName \
--location $location \
--sku pergb2018 \
--verbose

echo "Log Analytics workspace created: $logAnalyticsWorkspaceName"

echo "Script completed!"
