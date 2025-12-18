# Component as a Python Package

This Python Pulumi component uses "boostrap-less" mode, that is it does not have a `__main__.py` file that calls [component_provider_host](https://github.com/pulumi/pulumi/blob/master/sdk/python/lib/pulumi/provider/experimental/host.py#L27-L58). Instead it is buildable a Python package with a [`pyproject.toml`](./pyproject.toml), and a [`PulumiPlugin.yaml`](./PulumiPlugin.yaml) to mark it as a Pulumi plugin. When run as a plguin, Pulumi automatically discovers any components that are exported from the project's [module](./src/compo/__init__.py).

```
% pulumi package get-schema .
{
  "name": "compo",
...
}
```

## Example

The [`./example`](./example) folder contains a Pulumi program that has the package linked in editable mode, via `uv add --editable ../`.

```
% cd example
% pulumi up
Previewing update (dev)

     Type                           Name          Plan
 +   pulumi:pulumi:Stack            example-dev3  create
 +   └─ provider:index:MyComponent  hey           create

Outputs:
    str_output: "abc"

Resources:
    + 2 to create
```

The [`./example-provider`](./example-provider) folder contains a Pulumi program that uses the plugin as a [component provider](https://www.pulumi.com/docs/iac/guides/building-extending/components/build-a-component/). The package was added via `pulumi package add ..`.
