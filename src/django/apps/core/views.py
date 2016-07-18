import os

from django.shortcuts import render_to_response
from django.conf import settings
from react.render import render_component

components_path = os.path.join(settings.BASE_DIR, 'src', 'react')


def democracy_app(request):
    rendered = None
    rendered = render_component(
        os.path.join(components_path, 'DemocracyApp.jsx'),
        {'counters': 2}
    )
    return render_to_response('democracy_app.html', {'rendered': rendered})
