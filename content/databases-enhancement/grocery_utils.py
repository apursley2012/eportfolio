####################################################################
#  grocery_utils.py                                                                                                                                               #
#  Name: Alysha Pursley                                                                                                                                     #
#  Date: July 2025                                                                                                                                                #
#  Description:                                                                                                                                                       #
#    Helper functions for sorting and searching. These utilities accept either a  dict[str,int]      #
#     or an iterable of (item, count)  pairs so they work for both in-memory and DB-backed     #
#    versions.                                                                                                                                                            #
####################################################################

from typing import Dict, Iterable, Tuple, Union, List

FreqLike = Union[Dict[str, int], Iterable[Tuple[str, int]]]


####################################################################
#  _as_pairs                                                                                                                                                             #
#  Normalizes input to a list of (item, count) pairs.                                                                                     #
####################################################################
def _as_pairs(freq_data: FreqLike) -> List[Tuple[str, int]]:
    if isinstance(freq_data, dict):
        return [(k, int(v)) for k, v in freq_data.items()]
    # assume iterable of pairs
    return [(str(k), int(v)) for k, v in freq_data]

####################################################################
#  sort_alpha                                                                                                                                                          #
#  Prints items in A–Z order with their frequency counts.                                                                        #
####################################################################
def sort_alpha(freq_data: FreqLike) -> None:
    pairs = _as_pairs(freq_data)
    for item, count in sorted(pairs, key=lambda kv: kv[0]):
        print(f"{item}: {count}")


####################################################################
#  sort_by_freq                                                                                                                                                      #
#  Prints items by highest frequency first (ties broken A–Z).                                                                 #
####################################################################
def sort_by_freq(freq_data: FreqLike) -> None:
    pairs = _as_pairs(freq_data)
    for item, count in sorted(pairs, key=lambda kv: (-kv[1], kv[0])):
        print(f"{item}: {count}")


####################################################################
#  search_item                                                                                                                                                         #
#  Prints frequency for a specific item or "Item not found."                                                                      #
####################################################################
def search_item(freq_data: FreqLike, item_name: str) -> None:
    target = item_name.strip().lower()
    if not target:
        print("Item not found.")
        return

    pairs = _as_pairs(freq_data)
    lookup = {k.lower(): v for k, v in pairs}
    if target in lookup:
        print(f"{target}: {lookup[target]}")
    else:
        print("Item not found.") 