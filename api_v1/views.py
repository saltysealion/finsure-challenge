from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer
from finsure.models import Lender
from .serializers import LenderSerializer


class LenderViewSet(ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    filterset_fields = {
        'active': ('exact', ),
    }
    search_fields = (
        'id',
        'code',
    )


class LenderImportAPIView(APIView):
    def post(self, request, format=None):
        pass


class LenderExportAPIView(APIView):
    '''
    A custom endpoint allowing to export lenders into a CSV file.
    Made with extendibility in mind.
    '''

    # Keep JSON renderer for errors and add CSV renderer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES + [CSVRenderer]

    # Custom constants
    CSV_FORMAT = 'text/csv'  # CSV media type
    EXCLUDE_FIELDS = ['id']  # Fields to exclude from Lender model

    def get(self, request, format=None):
        # Logic for CSV export
        if request.accepted_media_type == self.CSV_FORMAT:
            # CSV renderer expects a list of dicts, which it converts into
            # a CSV. We'll use Django's shortcut for model to dict conversion
            from django.forms.models import model_to_dict

            # Prepare lenders for export
            result = []
            for lender in Lender.objects.all():
                result.append(
                    model_to_dict(lender, exclude=self.EXCLUDE_FIELDS)
                )

            return Response(
                result,
                headers={
                    # Suggest a filename for the CSV
                    'Content-Disposition': 'attachment; filename=lenders.csv'
                }
            )

        # If we reached this code it means the request was made with
        # `application/vnd.api+json` in Accept header, because all other
        # media types are rejected during content negotiation. For the
        # purpose of the challenge, we deny this media type too
        else:
            raise NotAcceptable

    def get_renderer_context(self):
        '''
        Overrides the headers in the renderer context to
        enforce custom order of the CSV columns.
        '''
        context = super().get_renderer_context()
        context['header'] = [
            # Order fields as per the model excluding the ID
            x.name for x in Lender._meta.fields
            if x.name not in self.EXCLUDE_FIELDS
        ]
        return context
