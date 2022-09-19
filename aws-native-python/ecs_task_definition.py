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
