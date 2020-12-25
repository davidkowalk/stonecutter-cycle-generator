def gen_contents(ids: list):

    recipes = list()
    json = """
    {{
        "type": "minecraft:stonecutting",
        "ingredient": {{
            "item": "{src}"
        }},
        "result": "{dest}",
        "count": 1
    }}
    """

    for source_item in ids:

        for dest_item in ids:

            if source_item == dest_item:
                continue

            recipes.append(json.format(src = source_item, dest = dest_item))

    return recipes
