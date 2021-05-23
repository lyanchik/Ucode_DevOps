def search_cookbook(cookbook, recipe, section):
    if recipe not in cookbook:
        return f'There is no "{recipe}" recipe in the cookbook.'
    recp = cookbook.get(recipe)
    if section not in recp:
        return f'There is no section "{section}" in the "{recipe}" recipe.'
    item = recp.get(section)
    return item
