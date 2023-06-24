#dictionary (forest of 3 trees)
families={
    'charley':
            {'sam':{'boxy','rosy'},
             'nila':{'pepsi'}},
    'devi' :
            {'tommy':{'tony'},
             'timmy':{'hamster'},
             'tammy':{'hamster'}}
        }
for parent,children in families.items():
    print(f"{parent} has {len(children)} kids:")
    print(f"{' ,and '.join([str(child) for child in [*children]])}") 