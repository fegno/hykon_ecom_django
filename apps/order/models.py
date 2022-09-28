from django.db import models

# Create your models here.


class Wishlist(models.Model):
    user_id = models.BigIntegerField()
    variant_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist'


class OfferCategories(models.Model):
    categories_id = models.IntegerField()
    offers_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_categories'


class OfferComboFreeProducts(models.Model):
    products_id = models.IntegerField(blank=True, null=True)
    offers_id = models.IntegerField()
    type = models.CharField(max_length=20)
    fixed_price = models.FloatField(blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_percentage = models.IntegerField(blank=True, null=True)
    max_discount_amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_combo_free_products'


class OfferComboProducts(models.Model):
    products_id = models.IntegerField()
    offers_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_combo_products'


class OfferGroups(models.Model):
    groups_id = models.IntegerField()
    offers_id = models.IntegerField()
    how_many_to_buy = models.IntegerField()
    how_many_to_get_free = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_groups'


class OfferPriceProducts(models.Model):
    products_id = models.IntegerField()
    offers_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_price_products'


class Offers(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.IntegerField()
    slug = models.CharField(max_length=250, blank=True, null=True)
    offer_name = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    validity_start_date = models.DateField()
    validity_end_date = models.DateField()
    applicable_for_full_order = models.IntegerField()
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    min_purchase_amount = models.FloatField(blank=True, null=True)
    max_discount_amount = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField()
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=520, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offers'


class OrderDetails(models.Model):
    orders_id = models.IntegerField()
    products_id = models.IntegerField()
    cart_offer_id = models.IntegerField(blank=True, null=True)
    offer_parent = models.IntegerField(blank=True, null=True)
    product_offer_id = models.IntegerField(blank=True, null=True)
    mrp = models.FloatField()
    quantity = models.IntegerField()
    sale_price = models.FloatField()
    price = models.FloatField()
    discount = models.FloatField()
    expected_delivery_date = models.DateField(blank=True, null=True)
    customer_instructions = models.TextField(blank=True, null=True)
    waranty_id = models.IntegerField(blank=True, null=True)
    warranty_parent = models.IntegerField(blank=True, null=True)
    is_returned = models.IntegerField()
    returned_reason = models.TextField(blank=True, null=True)
    is_cancelled = models.IntegerField()
    cancelled_reason = models.TextField(blank=True, null=True)
    refund_request_id = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderStatusLabelsMaster(models.Model):
    name = models.CharField(max_length=250)
    display_order = models.IntegerField()
    color_code = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status_labels_master'


class OrderTracking(models.Model):
    order_details_id = models.IntegerField()
    order_status_labels_master_id = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_tracking'


class Orders(models.Model):
    status = models.CharField(max_length=17)
    users_id = models.IntegerField()
    transaction_id = models.CharField(max_length=150)
    coupon_id = models.IntegerField(blank=True, null=True)
    coupon_discount = models.FloatField(blank=True, null=True)
    order_reference_number = models.CharField(max_length=150)
    total_mrp = models.FloatField()
    total_discount = models.FloatField()
    total_sale_price = models.FloatField()
    total_final_price = models.FloatField()
    payment_method = models.CharField(max_length=250)
    payment_status = models.IntegerField()
    payment_receive_status = models.IntegerField()
    delivery_address_id = models.IntegerField()
    delivery_instructions = models.TextField(blank=True, null=True)
    response_data = models.TextField(blank=True, null=True)
    is_cancelled = models.IntegerField()
    cancelled_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
