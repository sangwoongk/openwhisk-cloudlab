import six
from time import time
import random
from chameleon import PageTemplate
import resource

BIGTABLE_ZPT = """\
<table xmlns="http://www.w3.org/1999/xhtml"
xmlns:tal="http://xml.zope.org/namespaces/tal">
<tr tal:repeat="row python: options['table']">
<td tal:repeat="c python: row.values()">
<span tal:define="d python: c + 1"
tal:attributes="class python: 'column-' + %s(d)"
tal:content="python: d" />
</td>
</tr>
</table>""" % six.text_type.__name__

tmpl = PageTemplate(BIGTABLE_ZPT)
data = {}

def render(num_of_rows, num_of_cols):
    global data
    for i in range(num_of_cols):
        data[str(i)] = i

    table = [data for x in range(num_of_rows)]
    options = {"table": table}
    out = tmpl.render(options=options)
    return out

def main(params):
    num_of_rows = params['N']
    num_of_cols = params['N']

    start = time()

    data = render(num_of_rows, num_of_cols)
    latency = time() - start
    ret_val = {}
    ret_val["delay"] = latency

    return ret_val

if __name__ == '__main__':
    params = {'N': 1000}
    main(params)
