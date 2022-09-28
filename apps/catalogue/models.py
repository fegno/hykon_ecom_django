from django.db import models

# Create your models here.


class ProductAttributes(models.Model):
    products_id = models.IntegerField()
    attribute_id = models.IntegerField()
    attribute_value_id = models.IntegerField(blank=True, null=True)
    attribute_value = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attributes'


class ProductCateoryAttributeGroups(models.Model):
    category_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cateory_attribute_groups'


class ProductCateoryAttributeValues(models.Model):
    attribute_id = models.IntegerField()
    value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cateory_attribute_values'


class ProductCateoryAttributes(models.Model):
    category_id = models.IntegerField()
    attribute_name = models.CharField(max_length=191)
    attribute_type = models.CharField(max_length=20)
    group_id = models.IntegerField(blank=True, null=True)
    show_as_variant = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cateory_attributes'


class ProductImagesTb(models.Model):
    id = models.IntegerField(primary_key=True)
    product_code = models.CharField(max_length=250, db_collation='utf8mb3_general_ci', blank=True, null=True)
    is_main = models.IntegerField()
    big_image_url = models.CharField(max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)
    thumb_image_url = models.CharField(max_length=500, db_collation='utf8mb3_general_ci', blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_images_tb'


class ProductInventoryByVendor(models.Model):
    vendor_id = models.IntegerField()
    variant_id = models.IntegerField()
    barcode = models.CharField(max_length=250, blank=True, null=True)
    retail_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    landing_price = models.FloatField(blank=True, null=True)
    available_quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_inventory_by_vendor'


class ProductPriceHistory(models.Model):
    inventory_id = models.IntegerField()
    retail_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    new_retail_price = models.FloatField(blank=True, null=True)
    new_sale_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_price_history'


class ProductReviews(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    products_id = models.IntegerField()
    title = models.CharField(max_length=250)
    review = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    is_verified = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_reviews'


class ProductStockHistory(models.Model):
    inventory_id = models.IntegerField()
    last_stock = models.IntegerField(blank=True, null=True)
    added_stock = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_stock_history'


class ProductVariantImages(models.Model):
    variant_id = models.IntegerField()
    image_id = models.IntegerField()
    title = models.CharField(max_length=250, blank=True, null=True)
    alt = models.CharField(max_length=250, blank=True, null=True)
    is_common = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variant_images'


class ProductVariants(models.Model):
    search = models.CharField(max_length=250, blank=True, null=True)
    products_id = models.IntegerField()
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    code = models.CharField(max_length=250, blank=True, null=True)
    level1_attribute_value_id = models.IntegerField(blank=True, null=True)
    level2_attribute_value_id = models.IntegerField(blank=True, null=True)
    level3_attribute_value_id = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    sku = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    offer_status = models.IntegerField()
    combo_offer_status = models.IntegerField()
    is_new = models.IntegerField()
    is_topseller = models.IntegerField()
    is_active = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variants'


class ProductViews(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    products_id = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_views'


class Products(models.Model):
    product_code = models.CharField(max_length=250, blank=True, null=True)
    category_id = models.IntegerField()
    product_name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    use_psp = models.IntegerField()
    tagline = models.CharField(max_length=250, blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    top_description = models.TextField(blank=True, null=True)
    bottom_description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    hsn_code = models.IntegerField(blank=True, null=True)
    cgst = models.IntegerField(blank=True, null=True)
    sgst = models.IntegerField(blank=True, null=True)
    igst = models.IntegerField(blank=True, null=True)
    is_featured_in_home_page = models.IntegerField()
    is_featured_in_category = models.IntegerField()
    is_new = models.IntegerField()
    is_top_seller = models.IntegerField()
    is_today_deal = models.IntegerField()
    is_active = models.IntegerField()
    is_completed = models.IntegerField()
    default_image_id = models.IntegerField(blank=True, null=True)
    page_heading = models.CharField(max_length=250)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    is_warranty_product = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Waranty(models.Model):
    installation_address_id = models.IntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    mail = models.CharField(max_length=250)
    billing_address_id = models.IntegerField()
    type = models.CharField(max_length=250, blank=True, null=True)
    pro_type = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=250, blank=True, null=True)
    pro_model = models.CharField(max_length=250, blank=True, null=True)
    serial_number = models.CharField(max_length=250)
    dealer = models.CharField(max_length=250, blank=True, null=True)
    inst_date = models.DateField()
    contact_person = models.CharField(max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'waranty'


class Vendors(models.Model):
    vendor_name = models.CharField(max_length=250)
    page_heading = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    contact_name = models.CharField(max_length=250, blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendors'


class GroupProducts(models.Model):
    groups_id = models.IntegerField()
    products_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_products'


class Groups(models.Model):
    group_name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_by = models.IntegerField()
    updated_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Categories(models.Model):
    category_code = models.CharField(max_length=250, blank=True, null=True)
    parent_category_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    priority = models.IntegerField()
    type = models.CharField(max_length=100, blank=True, null=True)
    policies = models.TextField(blank=True, null=True)
    top_description = models.TextField(blank=True, null=True)
    bottom_description = models.TextField(blank=True, null=True)
    page_title = models.TextField(blank=True, null=True)
    browser_title = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    banner_image = models.IntegerField(blank=True, null=True)
    thumbnail_image = models.IntegerField(blank=True, null=True)
    brochure_pdf = models.IntegerField(blank=True, null=True)
    is_popular = models.IntegerField()
    is_domestic = models.IntegerField()
    is_corporate = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

class Brands(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_code = models.CharField(max_length=250, blank=True, null=True)
    brand_name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    website = models.CharField(max_length=250, blank=True, null=True)
    media_id = models.IntegerField(blank=True, null=True)
    page_heading = models.CharField(max_length=250, blank=True, null=True)
    browser_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    meta_keywords = models.CharField(max_length=520, blank=True, null=True)
    status = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'