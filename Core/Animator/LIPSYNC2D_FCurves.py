"""
Helpers to read F-Curves from an Action in Blender 5.x.

In Blender 5.x, ``Action.fcurves`` no longer exists. F-Curves live in a channelbag,
which is reached through ``action.layers[].strips[].channelbag(slot)``.
"""


def iter_fcurves(action, slot=None):
    """
    Yield every F-Curve of an action.

    :param action: The action to read.
    :param slot: The action slot to read. If None, all slots are read.
    """
    slots = [slot] if slot is not None else list(action.slots)
    for layer in action.layers:
        for strip in layer.strips:
            for current_slot in slots:
                channelbag = strip.channelbag(current_slot)
                if channelbag is not None:
                    yield from channelbag.fcurves


def find_fcurve(action, slot, data_path, index):
    """
    Return the F-Curve matching data_path and array index in the given slot, or None.
    """
    for fcurve in iter_fcurves(action, slot):
        if fcurve.data_path == data_path and fcurve.array_index == index:
            return fcurve
    return None
