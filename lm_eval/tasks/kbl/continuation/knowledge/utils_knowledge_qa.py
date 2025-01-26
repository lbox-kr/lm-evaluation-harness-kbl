def doc_to_choice_label(doc):
    choices = []
    pools = ["A", "B", "C", "D", "E"]
    for key in pools:
        if key in doc:
            choices.append(key)
    return choices

def doc_to_target(doc):
    choices = ["A", "B", "C", "D", "E"]
    try:
        return choices.index(doc["label"])
    except:
        print(f"{doc}")
        print(f"No choices possible due to GT error")
        print(f"Force return 0")
        return 0