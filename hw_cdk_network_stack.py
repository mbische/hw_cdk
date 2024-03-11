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
                            subnet_configuration=[
                            ec2.SubnetConfiguration(name="PublicSubnet01", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                            ec2.SubnetConfiguration(name ="PrivateSubnet01", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE),
                            ec2.Subnetconfiguration(name="PublicSubnet02",cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                            ec2.SubnetConfiguration(name ="PrivateSubnet02", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)]
        )