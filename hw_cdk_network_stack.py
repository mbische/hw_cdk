import os.path

from aws_cdk.aws_s3_assets import Asset as S3asset

from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
    # aws_sqs as sqs,
)

from constructs import Construct

class HwCdkNetworkStack(Stack):

    @property
    def vpc(self):
        return self.hw_cdk_vpc
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC. CDK by default creates and attaches internet gateway for VPC
    
        self.hw_cdk_vpc = ec2.Vpc(self, "hw_cdk_vpc", 
                            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
                           
                         
                            ##availability_zone is not part of Subnetconfiguration...
                            # pub01_subnet=[ec2.SubnetConfiguration(name="PublicSubnet01", subnet_type=ec2.SubnetType.PUBLIC)],
                            # pub02_subnet=[ec2.SubnetConfiguration(name="PublicSubnet02", availability_zone="us-west-1", subnet_type=ec2.SubnetType.PUBLIC)],
                            # priv01_subnet=[ec2.SubnetConfiguration(name="PrivSubnet01", availability_zone="us-east-1", subnet_type=ec2.SubnetType.PRIVATE)],
                            # priv02_subnet=[ec2.SubnetConfiguration(name="PrivSubnet02", availability_zone="us-west-1", subnet_type=ec2.SubnetType.PRIVATE)]
                            
                            
                            # pub01_subnet=[ec2.SubnetConfiguration(name="PublicSubnet01", subnet_type=ec2.SubnetType.PUBLIC)],
                            # pub02_subnet=[ec2.SubnetConfiguration(name="PublicSubnet02", subnet_type=ec2.SubnetType.PUBLIC)],
                            # priv01_subnet=[ec2.SubnetConfiguration(name="PrivSubnet01", subnet_type=ec2.SubnetType.PRIVATE)],
                            # priv02_subnet=[ec2.SubnetConfiguration(name="PrivSubnet02", subnet_type=ec2.SubnetType.PRIVATE)]
                            
                            # max_azs=2,
                            # subnet_configuration =[
                            # pub01=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                            # priv01=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
                            # pub02=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                            # priv02=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
                            # ]
                           
                           
                            
                            ##March 29th Attempt
                            max_azs=2,
                            subnet_configuration=[
                                ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PUBLIC, name= 'pub01',cidr_mask=24),
                                ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, name='priv01', cidr_mask=24),
                                ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PUBLIC, name='pub02',cidr_mask=24),
                                ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, name='priv02',cidr_mask=24)
                                ]
        
        
        )