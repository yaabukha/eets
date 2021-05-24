provider "azurerm" {
    subscription_id = "e1186581-0123-4618-8511-92dd708ec7d3"
    client_id       = "12dcd9df-547a-4690-8339-477c3c155c8f"
    client_secret   = "0MV-OBaYoyvMlwoA_La4L0PBuX.YrQjs6V"
    tenant_id       = "72f988bf-86f1-41af-91ab-2d7cd011db47"
    features {}
}

variable "resourceGroupName" {
  type = string
  default = "webAppRGYAZsdadsdadas"
}



 variable "location" {
  type = string
 default = "eastus"
}    


# Create a resource group if it doesn’t exist
resource "azurerm_resource_group" "myterraformgroup" {
    name     = var.resourceGroupName
  #name = "FrontDoorTestVMs"
    location = var.location

    tags = {
        environment = "dev"
    }
}

