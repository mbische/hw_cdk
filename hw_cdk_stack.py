
import os.path

from aws_cdk.aws_s3_assets import Asset as S3asset


import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_rds as rds
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import aws_s3 as s3

dirname = os.path.dirname(__file__)

class HwCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, hw_cdk_vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        

        # The code that defines your stack goes here
                # The code that defines your stack goes here

        # Instance Role and SSM Managed Policy
        InstanceRole = iam.Role(self, "InstanceSSM", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        InstanceRole.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"))
        
        # Create an EC2 instance
        # hw_cdk_east_web_instance = ec2.Instance(self, "hw_cdk_east_web_instance", vpc=hw_cdk_vpc,
        #                                         instance_type=ec2.InstanceType("t2.micro"),
        #                                         machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
        #                                         role=InstanceRole, vpc_subnets='priv01')
        # hw_cdk_west_web_instance = ec2.Instance(self, "hw_cdk_west_web_instance", vpc=hw_cdk_vpc,
        #                                         instance_type=ec2.InstanceType("t2.micro"),
        #                                         machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
        #                                         role=InstanceRole, vpc_subnets='priv02')
        ## Create an EC2 instance w/o vpc_subnets
        hw_cdk_east_web_instance = ec2.Instance(self, "hw_cdk_east_web_instance", vpc=hw_cdk_vpc,
                                                instance_type=ec2.InstanceType("t2.micro"),
                                                machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                                role=InstanceRole)
        hw_cdk_west_web_instance = ec2.Instance(self, "hw_cdk_west_web_instance", vpc=hw_cdk_vpc,
                                                instance_type=ec2.InstanceType("t2.micro"),
                                                machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
                                                role=InstanceRole)
        #vpc_subnets = ec2.SubnetSelection(subnets = [priv01, priv02])

        
        # Script in S3 as Asset
        webinitscriptasset = S3asset(self, "Asset", path=os.path.join(dirname, "web_server.sh"))
        asset_path = hw_cdk_east_web_instance.user_data.add_s3_download_command(
            bucket=webinitscriptasset.bucket,
            bucket_key=webinitscriptasset.s3_object_key
        )
        asset_path = hw_cdk_west_web_instance.user_data.add_s3_download_command(
            bucket=webinitscriptasset.bucket,
            bucket_key=webinitscriptasset.s3_object_key
        )
        # Userdata executes script from S3
        hw_cdk_east_web_instance.user_data.add_execute_file_command(
            file_path=asset_path
            )
        hw_cdk_west_web_instance.user_data.add_execute_file_command(
            file_path=asset_path
            )
        webinitscriptasset.grant_read(hw_cdk_east_web_instance.role)
        webinitscriptasset.grant_read(hw_cdk_west_web_instance.role)
        
        
        
        # Allow inbound HTTP traffic in security groups
        hw_cdk_east_web_instance.connections.allow_from_any_ipv4(ec2.Port.tcp(80))
        hw_cdk_west_web_instance.connections.allow_from_any_ipv4(ec2.Port.tcp(80))
        
        
        
        
        #         #
        # ## MySQL Instance
        # ##
        # rds.DatabaseInstance(self, "hw_cdk_mysql",
        #     database_name=hw_cdk_mysql,
        #     engine=rds.DatabaseInstanceEngine.mysql(version=engine_version),
        #     instance_type=ec2.InstanceType.of,
        #     vpc_subnets=vpc_subnets,
        #     vpc=hw_cdk_vpc,
        #     port=3306,
        #     removal_policy=RemovalPolicy.DESTROY,
        #     deletion_protection=False
        # )


# app = App()
# MySql(app, "hw_cdk_mysql", env={"region":"us-east-1"}, description="MySQL Instance Stack",
#     vpc_id    = "hw_cdk_vpc",
#     subnet_ids=["subnet-PRIVATE01", "subnet-PRIVATE02"],
#     db_name="db1")
        
        
        
                                            
                                            



    
