#!/usr/bin/env python3.7

#imports
import boto3
import string


#variables
choice = 0
list_of_vpcs = []

#functions

#how to create vpc
client = boto3.client("ec2")

def create_VPC():
    client.create_vpc(CidrBlock = '10.0.0.0/16')
    

#how to describe vpc
def describe_VPCs():
    response = client.describe_vpcs()
    num_vpcs = response["Vpcs"]
    ctr = 1
    global list_of_vpcs
    #reset list for each call of the function
    list_of_vpcs = []
    
    for vpc in num_vpcs:
        print("#"+str(ctr)+" ",vpc["VpcId"])
        ctr += 1
        list_of_vpcs.append(vpc["VpcId"])
        
    #print(list_of_vpcs)
    #print(response["Vpcs"])
    print()
    
def describe_VPC(vpc_id):
    response = client.describe_vpcs(VpcIds=[vpc_id])
    print(response["Vpcs"])

#how to delete vpc
def remove_VPC(vpc_str):
    print("IN UR BAES DELETIN UR FIELS")
    response = client.delete_vpc(
        VpcId = vpc_str)
    return response


def main():
    choice = 0
    while choice != 4:
        print()
        print("Welcome to VPCwerx!")
        print("________________________________________")
        print("Create  |  Describe  |  Delete  |  Exit")
        print("  1     |     2      |     3    |   4")
        print("________________________________________")
        
        try:
            choice = int(input("Please select an option: "))
            
        except ValueError:
            print()
            print("Sorry, I didn't understand that.")
            print()
            continue
            
        if choice < 1 or choice > 4:
            print()
            print("Sorry, please choose a valid option.")
            print()
            continue
        elif choice == 1:
            print()
            print("Creating your VPC....")
            print()
            create_VPC()
        elif choice == 2:
            print()
            print("Describing VPCs....")
            print()
            #describe() function here.. lists ALL VPCs
            describe_VPCs()
            
            more_info = "y"
            while more_info == 'y':
                more_info = input("Would you like to learn more? (y/n) ")
                more_info = more_info.lower()
                
                if more_info == 'y':
                    vpc_id = input("Please enter VPC ID: ")
                    print()
                    describe_VPC(vpc_id)
                    
                else: #user has either enter 'n' or invalid input, either way, break out
                    break
        
        elif choice == 3:
            print()
            print("Current VPCs....")
            print()
            describe_VPCs()
            #delete() function here
            first_run = True
            destruction = "n"
            which = 0
            vpc_str = ""
            if len(list_of_vpcs) > 1:
                destruction = "y"
            else:
                print("Sorry, can't delete the last VPC. Exiting...")
                print()
            
            while destruction == "y":
                #update the list of VPCs
                if first_run == False:
                    print("Updated VPC list:")
                    print()
                    describe_VPCs()
                    
                which = int(input("Choose a VPC to delete: (1/2/etc) "))
                
                print("Deleting #"+str(which))
                #print("list_of_vpcs:")
                #print(list_of_vpcs)
                vpc_str = list_of_vpcs[which-1]
                #print(vpc_str)
                
                #doublecheck we're deleting the right one
                #print(which)
                print("Confirm deletion of "+vpc_str+"? ENTER TO CONFIRM ",end="")
                confirm = input()
                    
                remove_VPC(vpc_str)    #delete that shit
                
                #always leave one VPC remaining
                #print(len(list_of_vpcs))
                if (len(list_of_vpcs)-1) > 1:
                    destruction = input("Would you like to delete another? ")
                    first_run = False
                else:
                    print()
                    print("Sorry, unable to delete the last VPC. Exiting...")
                    print()
                    destruction = "n"
            
            #pass
        
        else: #user has entered 4 and wishes to exit.
            print("Goodbye!")
            break
    
if __name__ == "__main__":
    main()