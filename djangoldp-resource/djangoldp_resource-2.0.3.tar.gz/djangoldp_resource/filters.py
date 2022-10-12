from django.db.models import Q
from djangoldp.filters import LDPPermissionsFilterBackend

class ResourceFilterBackend(LDPPermissionsFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        # Test if this not an anonymous user
        if request.user.is_authenticated:
            # Exclude all resources with privates circles not believe to this user
            return queryset.exclude(
                Q(circle__status__iexact='private') &
                ~Q(circle__members__user=request.user)
            )
        else :
            # Exclude all resources with privates circles
            return queryset.exclude( Q( circle__status__iexact='private' ) )

