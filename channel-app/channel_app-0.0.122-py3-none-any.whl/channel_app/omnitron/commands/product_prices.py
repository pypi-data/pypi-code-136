from typing import List

from omnisdk.omnitron.endpoints import ChannelIntegrationActionEndpoint, \
    ChannelProductPriceEndpoint, ChannelBatchRequestEndpoint, \
    ChannelExtraProductPriceEndpoint
from omnisdk.omnitron.models import ProductPrice

from channel_app.core.commands import OmnitronCommandInterface
from channel_app.core.data import BatchRequestResponseDto
from channel_app.omnitron.commands.batch_requests import ProcessBatchRequests
from channel_app.omnitron.constants import (ContentType, BatchRequestStatus,
                                            IntegrationActionStatus,
                                            FailedReasonType)


class GetUpdatedProductPrices(OmnitronCommandInterface):
    endpoint = ChannelProductPriceEndpoint
    path = "updates"
    BATCH_SIZE = 100
    content_type = ContentType.product_price.value

    def get_data(self) -> List[ProductPrice]:
        prices = self.get_product_prices()
        prices = self.get_integration_actions(prices)
        return prices

    def get_product_prices(self) -> List[ProductPrice]:
        prices = self.endpoint(
            path=self.path,
            channel_id=self.integration.channel_id
        ).list(
            params={
                "limit": self.BATCH_SIZE
            }
        )
        prices = prices[:self.BATCH_SIZE]
        objects_data = self.create_batch_objects(data=prices,
                                                 content_type=self.content_type)
        self.update_batch_request(objects_data=objects_data)
        return prices

    def get_integration_actions(self, prices: List[ProductPrice]):
        if not prices:
            return []
        endpoint = ChannelIntegrationActionEndpoint(
            channel_id=self.integration.channel_id)
        price_integration_actions = endpoint.list(
            params={
                "local_batch_id": self.integration.batch_request.local_batch_id,
                "status": IntegrationActionStatus.processing,
                "channel_id": self.integration.channel_id
            })
        for price_batch in endpoint.iterator:
            price_integration_actions.extend(price_batch)
        price_ia_dict = {ia.object_id: ia for ia in price_integration_actions}
        for price in prices:
            price_ia = price_ia_dict[price.pk]
            price.remote_id = price_ia.remote_id
        return prices


class GetInsertedProductPrices(GetUpdatedProductPrices):
    path = "inserts"

    def get_integration_actions(self, prices: List[ProductPrice]):
        if not prices:
            return []
        endpoint = ChannelIntegrationActionEndpoint(
            channel_id=self.integration.channel_id)
        product_ids = [str(price.product) for price in prices]
        product_ias = endpoint.list(
            params={"object_id__in": ",".join(product_ids),
                    "content_type_name": ContentType.product.value,
                    "status": IntegrationActionStatus.success,
                    "channel_id": self.integration.channel_id
                    })
        for product_batch in endpoint.iterator:
            product_ias.extend(product_batch)
        product_integrations_by_id = {ia.object_id: ia for ia in product_ias}

        for price in prices:
            if price.product in product_integrations_by_id:
                product_ia = product_integrations_by_id[price.product]
                price.remote_id = product_ia.remote_id
            else:
                price.failed_reason_type = FailedReasonType.channel_app.value
                self.failed_object_list.append(
                    (price, ContentType.product_price.value,
                     "Product has not been sent"))
        return prices


class GetInsertedProductPricesFromExtraPriceList(OmnitronCommandInterface):
    endpoint = ChannelExtraProductPriceEndpoint
    path = "inserts"
    BATCH_SIZE = 100
    content_type = ContentType.product_price.value

    def get_data(self) -> List[ProductPrice]:
        self.price_list_id = self.objects
        prices = self.get_product_prices()
        prices = self.get_integration_actions(prices)
        return prices

    def get_product_prices(self) -> List[ProductPrice]:
        endpoint = self.endpoint(path=self.path,
                                 channel_id=self.integration.channel_id)
        prices = endpoint.list(
            params={"price_list": self.price_list_id}
        )
        for price_batch in endpoint.iterator:
            prices.extend(price_batch)
            if len(prices) >= self.BATCH_SIZE:
                break
        prices = prices[:self.BATCH_SIZE]
        objects_data = self.create_batch_objects(data=prices,
                                                 content_type=self.content_type)
        self.update_batch_request(objects_data=objects_data)
        return prices

    def get_integration_actions(self, prices: List[ProductPrice]):
        if not prices:
            return []
        endpoint = ChannelIntegrationActionEndpoint(
            channel_id=self.integration.channel_id)
        price_integration_actions = endpoint.list(
            params={
                "local_batch_id": self.integration.batch_request.local_batch_id,
                "status": IntegrationActionStatus.processing
            })
        for price_batch in endpoint.iterator:
            price_integration_actions.extend(price_batch)
        price_ia_dict = {ia.object_id: ia for ia in price_integration_actions}
        for price in prices:
            price_ia = price_ia_dict[price.pk]
            price.remote_id = price_ia.remote_id
        return prices


class GetUpdatedProductPricesFromExtraPriceList(
    GetInsertedProductPricesFromExtraPriceList):
    path = "updates"


class ProcessPriceBatchRequests(OmnitronCommandInterface, ProcessBatchRequests):
    endpoint = ChannelBatchRequestEndpoint
    content_type = ContentType.product_price.value
    CHUNK_SIZE = 50
    BATCH_SIZE = 100

    def get_data(self):
        return self.objects

    def validated_data(self, data: List[BatchRequestResponseDto]):
        for item in data:
            assert isinstance(item, BatchRequestResponseDto)
        return data

    def send(self, validated_data):
        result = self.process_item(validated_data)
        return result

    @property
    def update_state(self, *args, **kwargs) -> BatchRequestStatus:
        return BatchRequestStatus.done

    def check_run(self, is_ok, formatted_data):
        if not is_ok and self.is_batch_request:
            self.integration.batch_request.objects = None
            self.batch_service(self.integration.channel_id).to_fail(
                self.integration.batch_request)
        return False

    def get_channel_items_by_reference_object_ids(self, channel_response,
                                                  model_items_by_content,
                                                  integration_actions):
        product_ids = [str(item) for item in
                       model_items_by_content["productprice"]]

        model_items_by_content_product = self.get_products(product_ids)

        channel_items_by_product_id = {}
        for product_id, product in model_items_by_content_product.items():
            for channel_item in channel_response:
                # TODO: comment
                sku = self.get_barcode(obj=product)
                if channel_item.sku != sku:
                    continue
                remote_item = channel_item
                channel_items_by_product_id[product_id] = remote_item
                break
        return channel_items_by_product_id
