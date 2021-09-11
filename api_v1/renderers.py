import rest_framework_json_api.renderers
from rest_framework.exceptions import ValidationError


class BrowsableAPIRenderer(
    rest_framework_json_api.renderers.BrowsableAPIRenderer
):
    def get_filter_form(self, *args, **kwargs):
        '''
        Override `get_filter_form` so that if a user uses
        uses a filter backend that throws a `ValidationError`
        such as `QueryParameterValidationFilter` the server
        will return the proper 4XX error with incorrect query
        parameters, rather than a 500 error.
        '''
        try:
            return super().get_filter_form(*args, **kwargs)
        except ValidationError:
            return
