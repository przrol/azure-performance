"""
Azure Automation documentation : https://aka.ms/azure-automation-python-documentation
Azure Python SDK documentation : https://aka.ms/azure-python-sdk
"""
#!/usr/bin/env python3
import os
from azure.mgmt.compute import ComputeManagementClient
import azure.mgmt.resource 
import automationassets 
from OpenSSL import crypto 
import binascii 
from msrestazure import azure_active_directory 
import adal 

def get_automation_runas_credential(runas_connection): 
    # Get the Azure Automation RunAs service principal certificate 
    cert = automationassets.get_automation_certificate("AzureRunAsCertificate") 
    pks12_cert = crypto.load_pkcs12(cert) 
    pem_pkey = crypto.dump_privatekey(crypto.FILETYPE_PEM,pks12_cert.get_privatekey()) 

    # Get run as connection information for the Azure Automation service principal 
    application_id = runas_connection["ApplicationId"] 
    thumbprint = runas_connection["CertificateThumbprint"] 
    tenant_id = runas_connection["TenantId"] 

    # Authenticate with service principal certificate 
    resource ="https://management.core.windows.net/" 
    authority_url = ("https://login.microsoftonline.com/"+tenant_id) 
    context = adal.AuthenticationContext(authority_url) 
    return azure_active_directory.AdalAuthentication( 
    lambda: context.acquire_token_with_client_certificate( 
            resource, 
            application_id, 
            pem_pkey, 
            thumbprint) 
    ) 

# Authenticate to Azure using the Azure Automation RunAs service principal 
runas_connection = automationassets.get_automation_connection("AzureRunAsConnection") 
azure_credential = get_automation_runas_credential(runas_connection)

# Initialize the compute management client with the RunAs credential and specify the subscription to work against.# Initialize the compute management client with the RunAs credential and specify the subscription to work against.
compute_client = ComputeManagementClient(
    azure_credential,
    str(runas_connection["SubscriptionId"])
)

print('\nStarting VM 0')
async_vm_0_start = compute_client.virtual_machine_scale_set_vms.start(
    "udacity-c4-project", "rp2021-vmss", 0)
async_vm_0_start.wait()

print('\nStarting VM 1')
async_vm_1_start = compute_client.virtual_machine_scale_set_vms.start(
    "udacity-c4-project", "rp2021-vmss", 1)
async_vm_1_start.wait()

