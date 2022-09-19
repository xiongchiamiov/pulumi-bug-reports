from pulumi_aws_native import ecs

def not_optional_arguments():
    ecs.TaskDefinition('this is required')
