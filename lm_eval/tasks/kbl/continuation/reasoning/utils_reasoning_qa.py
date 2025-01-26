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
        raise NotImplementedError
        return 0

def doc_to_choice_consistency(doc):
    choices = [
        "일관되지 않음",
        "일관됨",
    ]
    return choices

def doc_to_target_consistency(doc):

    if doc[doc["label"]] == "일관되지 않음":
        return 0
    elif doc[doc["label"]] == "일관됨":
        return 1
    else:
        raise NotImplementedError


def doc_to_choice_causal(doc):
    choices = [
        "인과관계없음",
        "인과관계있음",
    ]
    return choices


def doc_to_target_causal(doc):
    if doc[doc["label"]] == "인과관계없음":
        return 0
    elif doc[doc["label"]] == "인과관계있음":
        return 1
    else:
        raise NotImplementedError
