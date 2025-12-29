class HTMLNode:
    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            f"child class {type(self)} must override to_html method"
        )

    def props_to_html(self):
        res = ""
        for key, val in self.props.items():
            res += f' {key}="{val}"'
        return res

    def __repr__(self):
        return (
            "HTMLNode "
            f'tag: "{self.tag}" '
            f'value: "{self.value}" '
            f'children: "{self.children}" '
            f'props: "{self.props}"'
        )
