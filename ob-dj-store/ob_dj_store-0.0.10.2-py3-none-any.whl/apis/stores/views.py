import logging
import typing

from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_gis.filters import DistanceToPointOrderingFilter

from ob_dj_store.apis.stores.filters import (
    CategoryFilter,
    InventoryFilter,
    OrderFilter,
    ProductFilter,
    StoreFilter,
    VariantFilter,
)
from ob_dj_store.apis.stores.rest.serializers.serializers import (
    CartItemSerializer,
    CartSerializer,
    CategorySerializer,
    CreateOrderResponseSerializer,
    FeedbackSerializer,
    InventorySerializer,
    OrderSerializer,
    PaymentMethodSerializer,
    PaymentSerializer,
    ProductListSerializer,
    ProductSerializer,
    ProductVariantSerializer,
    ShippingMethodSerializer,
    StoreSerializer,
    TaxSerializer,
)
from ob_dj_store.core.stores.models import (
    Cart,
    CartItem,
    Category,
    Favorite,
    FeedbackConfig,
    Order,
    Payment,
    PaymentMethod,
    Product,
    ProductVariant,
    ShippingMethod,
    Store,
    Tax,
)
from ob_dj_store.core.stores.models._inventory import Inventory

logger = logging.getLogger(__name__)


class StoreView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = StoreSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    filterset_class = StoreFilter
    queryset = Store.objects.active()
    distance_ordering_filter_field = "location"
    filter_backends = [DistanceToPointOrderingFilter, DjangoFilterBackend]

    def get_permissions(self):
        if self.action in ["favorites", "favorite", "recently_ordered_from"]:
            return [
                permissions.IsAuthenticated(),
            ]
        return super(StoreView, self).get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "favorites":
            favorite_store_ids = Favorite.objects.favorites_for_model(
                Store, self.request.user
            ).values_list("object_id", flat=True)
            queryset = self.queryset.filter(pk__in=favorite_store_ids)
        # stores that the user has recently ordered from
        if self.action == "recently_ordered_from":
            queryset = (
                queryset.prefetch_related(
                    Prefetch(
                        "orders",
                        queryset=Order.objects.filter(
                            customer=self.request.user, status__in=["PAID", "DELIVERED"]
                        ),
                    )
                )
                .filter(
                    orders__customer=self.request.user,
                    orders__status__in=[
                        "PAID",
                        "DELIVERED",
                    ],
                )
                .order_by("-orders__created_at")
            )
        return queryset

    @swagger_auto_schema(
        operation_summary="List Stores",
        operation_description="""
            List Stores
        """,
        tags=[
            "Store",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List Stores",
        operation_description="""
            List Stores
        """,
        tags=[
            "Store",
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Favorites",
        operation_description="""
            Retrieve user favorite stores
        """,
        tags=[
            "Store",
        ],
    )
    @action(
        detail=False,
        methods=["GET"],
        url_path="favorites",
        serializer_class=StoreSerializer,
    )
    def favorites(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Recently Ordered From",
        operation_description="""
            Stores that the user has recently ordered from
        """,
        tags=[
            "Store",
        ],
    )
    @action(
        detail=False,
        methods=["GET"],
        url_path="recently_ordered_from",
        serializer_class=StoreSerializer,
    )
    def recently_ordered_from(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Add or Remove Store from Favorites",
        operation_description="""
            Add or Remove Store from Favorites
        """,
        tags=[
            "Store",
        ],
    )
    @action(
        detail=True,
        methods=["GET"],
        url_path="favorite",
    )
    def favorite(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            Favorite.objects.favorite_for_user(instance, request.user).delete()
        except Favorite.DoesNotExist:
            Favorite.add_favorite(instance, request.user)
        serializer = StoreSerializer(instance=instance, context={"request": request})
        return Response(serializer.data)


class CartView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Cart.objects.all()

    def get_object(self):
        return self.request.user.cart

    @swagger_auto_schema(
        operation_summary="Retrieve Customer Cart",
        operation_description="""
            Retrieve the current customer's cart /store/cart/me
        """,
        tags=[
            "Cart",
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Customer Cart",
        operation_description="""
            Updates the current customer's cart /store/cart/me
        """,
        tags=[
            "Cart",
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class CartItemView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CartItemSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = CartItem.objects.all()

    @swagger_auto_schema(
        operation_summary="Retrieve Cart Item",
        operation_description="""
            Retrieve the current cart's cart item
        """,
        tags=[
            "CartItem",
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update Customer Cart Item",
        operation_description="""
            Updates the current customer's cart item
        """,
        tags=[
            "CartItem",
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete Customer Cart Item",
        operation_description="""
            Deletes the current customer's cart item
        """,
        tags=[
            "CartItem",
        ],
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OrderView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filterset_class = OrderFilter
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderResponseSerializer
        return self.serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    @swagger_auto_schema(
        operation_summary="Retrieve An Order",
        operation_description="""
            Retrieve an order by id
        """,
        tags=[
            "Order",
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List Orders",
        operation_description="""
            List Orders
        """,
        tags=[
            "Order",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a Customer Order",
        operation_description="""
            Create a customer order
        """,
        tags=[
            "Order",
        ],
    )
    def create(self, request, *args, **kwargs):
        context = self.get_serializer_context()
        serializer = OrderSerializer(data=request.data, context=context)
        orders = []
        if serializer.is_valid(raise_exception=True):
            orders, payment_url = serializer.save().values()
        orders_data = OrderSerializer(orders, many=True).data
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "payment_url": payment_url,
                "orders": orders_data,
            },
        )

    @action(
        methods=["POST"],
        detail=True,
        url_path=r"feedback",
        permission_classes=[
            permissions.IsAuthenticated,
        ],
    )
    def feedback(
        self, request: Request, pk=None, *args: typing.Any, **kwargs: typing.Any
    ):
        """Action for users to submit a feedback on successful order;"""
        serializer = FeedbackSerializer(
            data=request.data,
            instance=self.get_object(),
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except FeedbackConfig.DoesNotExist:
            return Response(
                _(
                    "No FeedbackAttribute instance found for the related feedbackconfig attribute."
                ),
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.data, status=status.HTTP_200_OK)


class VariantView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductVariantSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    filterset_class = VariantFilter
    queryset = ProductVariant.objects.all()

    @swagger_auto_schema(
        operation_summary="List Variants",
        operation_description="""
            List Variants
        """,
        tags=[
            "Variant",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductView(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    filterset_class = ProductFilter
    queryset = Product.objects.active()

    def get_permissions(self):
        if self.action in ["favorites", "favorite"]:
            return [
                permissions.IsAuthenticated(),
            ]
        return super(ProductView, self).get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "favorites":
            favorite_product_ids = Favorite.objects.favorites_for_model(
                Product, self.request.user
            ).values_list("object_id", flat=True)
            queryset = self.queryset.filter(pk__in=favorite_product_ids)
        return queryset

    def get_serializer_class(self):
        # # TODO: Replace If logic with dict lookup
        # Listing Serializer
        return ProductListSerializer if self.action == "list" else ProductSerializer

    @swagger_auto_schema(
        operation_summary="Retrieve A Product",
        operation_description="""
            Retrieve a Product by id
        """,
        tags=[
            "Product",
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List Products",
        operation_description="""
            List Products
        """,
        tags=[
            "Product",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Favorites",
        operation_description="""
            Retrieve user favorite products
        """,
        tags=[
            "Product",
        ],
    )
    @action(
        detail=False,
        methods=["GET"],
        url_path="favorites",
        serializer_class=ProductListSerializer,
    )
    def favorites(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Add or Remove Product from Favorites",
        operation_description="""
            Add or Remove Product from Favorites
        """,
        tags=[
            "Product",
        ],
    )
    @action(
        detail=True,
        methods=["GET"],
        url_path="favorite",
    )
    def favorite(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            Favorite.objects.favorite_for_user(instance, request.user).delete()
        except Favorite.DoesNotExist:
            Favorite.add_favorite(instance, request.user)
        serializer = ProductSerializer(instance=instance, context={"request": request})
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Featured products",
        operation_description="""
            List user's featured products
        """,
        tags=[
            "Product",
        ],
    )
    @action(
        detail=False,
        methods=["GET"],
        url_path="featured",
    )
    def featured(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(is_featured=True)
        page = self.paginate_queryset(instance)
        serializer = ProductListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    http_method_names = ["get"]
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.active()
    filterset_class = CategoryFilter

    @method_decorator(
        name="retrieve",
        decorator=swagger_auto_schema(
            operation_summary="Retrieve Category",
            tags=[
                "Category",
            ],
        ),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(
        name="list",
        decorator=swagger_auto_schema(
            operation_summary="List Categories",
            tags=[
                "Category",
            ],
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class InventoryView(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = InventorySerializer
    permission_classes = [
        permissions.AllowAny,
    ]
    queryset = Inventory.objects.all()
    filterset_class = InventoryFilter

    @method_decorator(
        name="list",
        decorator=swagger_auto_schema(
            operation_summary="List Inventories",
            tags=[
                "Inventory",
            ],
        ),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(
        name="retrieve",
        decorator=swagger_auto_schema(
            operation_summary="Retrieve Inventory",
            tags=[
                "Inventory",
            ],
        ),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TransactionsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PaymentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Payment.objects.all()

    def get_queryset(self):
        return Payment.objects.filter(
            user=self.request.user, status=Payment.PaymentStatus.SUCCESS.value
        ).order_by("payment_post_at")

    @swagger_auto_schema(
        operation_summary="List Users's Captured Transactions",
        operation_description="""
            List Users's Captured Transactions
        """,
        tags=[
            "payment",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PaymentMethodViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PaymentMethodSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = PaymentMethod.objects.all()

    def get_queryset(self):
        return PaymentMethod.objects.active()

    @swagger_auto_schema(
        operation_summary="List Payment Methods",
        operation_description="""
            List Payment methods
        """,
        tags=[
            "Payment Method",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ShippingMethodViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ShippingMethodSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = ShippingMethod.objects.all()

    def get_queryset(self):
        return ShippingMethod.objects.active()

    @swagger_auto_schema(
        operation_summary="List Shipping Methods",
        operation_description="""
            List Shipping methods
        """,
        tags=[
            "Store",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TaxViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TaxSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Tax.objects.all()

    @swagger_auto_schema(
        operation_summary="List Taxes",
        operation_description="""
            List Taxes
        """,
        tags=[
            "Tax",
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
