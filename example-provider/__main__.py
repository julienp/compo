import pulumi
import pulumi_compo as compo

c = compo.MyComponent("hey", str_input="abc")

pulumi.export("str_output", c.str_output)
