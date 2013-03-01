from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library('wysihtml5', 'resources')

wysihtml5 = Resource(
    library,
    'js/wysihtml5-0.3.0.js',
    minified='js/wysihtml5-0.3.0.min.js'
    )

advanced_parser = Resource(
    library,
    'parser_rules/advanced.js'
    )

simple_parser = Resource(
    library,
    'parser_rules/simple.js'
    )

simple_wysihtml5 = Group([simple_parser, wysihtml5])

advanced_wysihtml5 = Group([advanced_parser, wysihtml5])
