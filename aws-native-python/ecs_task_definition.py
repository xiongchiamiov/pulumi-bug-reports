import pulumi
from pulumi_aws_native import ecs

def not_optional_arguments():
    ecs.TaskDefinition('this is required')

def unused_resource_name():
    task_definition = ecs.TaskDefinition(
        resource_name='a-cool-unique-name',
        container_definitions=[
            ecs.TaskDefinitionContainerDefinitionArgs(
                name="my-app",
                image="amazon/amazon-ecs-sample",
                memory=128,
            )
        ],
    )
    pulumi.export('name', task_definition.task_definition_arn)

def cannot_change_arn():
    ecs.TaskDefinition(
        resource_name='cannot-change-arn',
        container_definitions=[
            ecs.TaskDefinitionContainerDefinitionArgs(
                name="my-app",
                image="amazon/amazon-ecs-sample",
                memory=128,
            )
        ],
        # After the first run to create the resource, uncomment this line to
        # try to update the object and reproduce the error.
        #task_role_arn='arn:aws:iam::1234567890:role/example',
    )
