#!/bin/bash

# Variables
resourceGroup="acdnd-c4-project"
location="eastus2"
appName="ApplicationInsightsRp$RANDOM"
logAnalyticsWorkspaceName="LogAnalyticsRp29518"

# Create Application Insights
echo "Creating Application Insights: $appName..."

az monitor app-insights component create \
--app $appName \
--location $location \
--resource-group $resourceGroup \
--application-type web \
--kind web \
--workspace $logAnalyticsWorkspaceName \
--verbose

echo "Log Application Insights created: $appName"

echo "Script completed!"
