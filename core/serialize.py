import json


def traverse_postorder(
    node,
    visited,
    ordered
):

    if id(node) in visited:
        return

    visited.add(id(node))

    for child in node.inputs:

        traverse_postorder(
            child,
            visited,
            ordered
        )

    ordered.append(node)


def to_dict(root):

    visited = set()

    ordered = []

    traverse_postorder(
        root,
        visited,
        ordered
    )

    node_to_id = {}

    for idx, node in enumerate(ordered):

        node_to_id[id(node)] = idx

    nodes = []

    for node in ordered:

        nodes.append({

            "id": node_to_id[id(node)],

            "kind": node.kind,

            "inputs": [
                node_to_id[id(child)]
                for child in node.inputs
            ],

            "attrs": node.attrs,

            "metadata": node.metadata
        })

    return {

        "root": node_to_id[id(root)],

        "nodes": nodes
    }


def to_json(root):

    return json.dumps(
        to_dict(root),
        indent=2
    )