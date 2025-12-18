from typing import Optional, TypedDict

import pulumi


class Args(TypedDict):
    str_input: pulumi.Input[str]


class MyComponent(pulumi.ComponentResource):
    str_output: pulumi.Output[str]

    def __init__(self, name: str, args: Args, opts: Optional[pulumi.ResourceOptions]=None):
        super().__init__("provider:index:MyComponent", name, {}, opts)
        self.str_output = pulumi.Output.from_input(args["str_input"])
