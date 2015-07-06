from diagnostic_msgs.msg import KeyValue


def keyval_to_dict(keyval_list):
    if keyval_list is None:
        return {}
    out = {}
    for item in keyval_list:
        out[item.key] = item.value
    return out


def dict_to_keyval(in_dict):
    if in_dict is None:
        return []
    out = []
    for item in in_dict.iteritems():
        out.append(KeyValue(*item))
    return out
