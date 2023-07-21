import yaml

with open("pmm_config_vars.yml") as f:
    data = yaml.safe_load(f)
    promptables = {k: v for k, v in data.items() if v["required"] and v["promptable"]}
    the_rest = {k: v for k, v in data.items() if v["required"] and not v["promptable"]}


# print("promptables")
# print(promptables)
print("the_rest")
print(the_rest)

# with open("promptables.yml", "w") as f:
#     reqs = {k: v["default"] for k, v in promptables.items()} | {
#         k: v["default"] for k, v in the_rest.items()
#     }
#     yaml.dump(reqs, f)
