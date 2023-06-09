from django.urls import path
from devduck.apps.core.views.DocsView import (
    AboutView, ContactView, EditorGuideView,
    TermsView
)

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('editor-guide/', EditorGuideView.as_view(), name='editor_guide'),
    path('terms/', TermsView.as_view(), name='terms'),
]