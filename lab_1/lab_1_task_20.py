def unique_elements(lists: list):
    result = []
    seen = set()

    def traverse(item):
        if isinstance(item, list):
            for sub_item in item:
                traverse(sub_item)
        else:
            if item not in seen:
                seen.add(item)
                result.append(item)

    traverse(lists)
    return result

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
