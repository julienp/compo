import compo
import pulumi

c = compo.MyComponent("hey", args={"str_input": "abc"})

pulumi.export("str_output", c.str_output)
