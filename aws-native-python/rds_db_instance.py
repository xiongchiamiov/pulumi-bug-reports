import pulumi_aws as aws_classic
from pulumi_aws_native import rds

def password_must_be_provided():
    # Security groups aren't yet supported in aws-native.
    sg = aws_classic.ec2.SecurityGroup(
        resource_name='pulumi-bug-report-password-must-be-provided',
        name_prefix='pulumi-bug-report-password-must-be-provided',
    )

    rds.DBInstance(
        resource_name='pulumi-bug-report-password-must-be-provided',

        master_username='root',
        manage_master_user_password=False,
        master_user_password='super-secret',

        d_b_instance_class='db.t4g.micro',
        engine='postgres',
        allocated_storage='5',

        # Adding this line causes provisioning to fail.
        #v_pc_security_groups=[sg],
    )
