variable "my_name" {
    type = string
    description = "First name of the student"
}

variable "location" {
    type = string
    default = "westeurope"
    description = "The location where all resources will be placed"
}