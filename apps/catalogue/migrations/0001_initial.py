# Generated by Django 4.1.1 on 2022-09-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand_code', models.CharField(blank=True, max_length=250, null=True)),
                ('brand_name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('media_id', models.IntegerField(blank=True, null=True)),
                ('page_heading', models.CharField(blank=True, max_length=250, null=True)),
                ('browser_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=520, null=True)),
                ('status', models.IntegerField()),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'brands',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(blank=True, max_length=250, null=True)),
                ('parent_category_id', models.IntegerField(blank=True, null=True)),
                ('category_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('priority', models.IntegerField()),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('policies', models.TextField(blank=True, null=True)),
                ('top_description', models.TextField(blank=True, null=True)),
                ('bottom_description', models.TextField(blank=True, null=True)),
                ('page_title', models.TextField(blank=True, null=True)),
                ('browser_title', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('tagline', models.TextField(blank=True, null=True)),
                ('banner_image', models.IntegerField(blank=True, null=True)),
                ('thumbnail_image', models.IntegerField(blank=True, null=True)),
                ('brochure_pdf', models.IntegerField(blank=True, null=True)),
                ('is_popular', models.IntegerField()),
                ('is_domestic', models.IntegerField()),
                ('is_corporate', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups_id', models.IntegerField()),
                ('products_id', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'group_products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_id', models.IntegerField()),
                ('attribute_id', models.IntegerField()),
                ('attribute_value_id', models.IntegerField(blank=True, null=True)),
                ('attribute_value', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_attributes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCateoryAttributeGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(blank=True, null=True)),
                ('group_name', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_cateory_attribute_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCateoryAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('attribute_name', models.CharField(max_length=191)),
                ('attribute_type', models.CharField(max_length=20)),
                ('group_id', models.IntegerField(blank=True, null=True)),
                ('show_as_variant', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_cateory_attributes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCateoryAttributeValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_id', models.IntegerField()),
                ('value', models.CharField(blank=True, max_length=191, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_cateory_attribute_values',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImagesTb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_code', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=250, null=True)),
                ('is_main', models.IntegerField()),
                ('big_image_url', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=500, null=True)),
                ('thumb_image_url', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=500, null=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'product_images_tb',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductInventoryByVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.IntegerField()),
                ('variant_id', models.IntegerField()),
                ('barcode', models.CharField(blank=True, max_length=250, null=True)),
                ('retail_price', models.FloatField(blank=True, null=True)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('landing_price', models.FloatField(blank=True, null=True)),
                ('available_quantity', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_inventory_by_vendor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.IntegerField()),
                ('retail_price', models.FloatField(blank=True, null=True)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('new_retail_price', models.FloatField(blank=True, null=True)),
                ('new_sale_price', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_price_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('products_id', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('is_verified', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(blank=True, max_length=250, null=True)),
                ('category_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('use_psp', models.IntegerField()),
                ('tagline', models.CharField(blank=True, max_length=250, null=True)),
                ('brand_id', models.IntegerField(blank=True, null=True)),
                ('vendor_id', models.IntegerField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('top_description', models.TextField(blank=True, null=True)),
                ('bottom_description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('mrp', models.FloatField(blank=True, null=True)),
                ('sale_price', models.FloatField(blank=True, null=True)),
                ('hsn_code', models.IntegerField(blank=True, null=True)),
                ('cgst', models.IntegerField(blank=True, null=True)),
                ('sgst', models.IntegerField(blank=True, null=True)),
                ('igst', models.IntegerField(blank=True, null=True)),
                ('is_featured_in_home_page', models.IntegerField()),
                ('is_featured_in_category', models.IntegerField()),
                ('is_new', models.IntegerField()),
                ('is_top_seller', models.IntegerField()),
                ('is_today_deal', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('is_completed', models.IntegerField()),
                ('default_image_id', models.IntegerField(blank=True, null=True)),
                ('page_heading', models.CharField(max_length=250)),
                ('browser_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('is_warranty_product', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductStockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.IntegerField()),
                ('last_stock', models.IntegerField(blank=True, null=True)),
                ('added_stock', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_stock_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariantImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_id', models.IntegerField()),
                ('image_id', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('alt', models.CharField(blank=True, max_length=250, null=True)),
                ('is_common', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_variant_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductVariants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(blank=True, max_length=250, null=True)),
                ('products_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('code', models.CharField(blank=True, max_length=250, null=True)),
                ('level1_attribute_value_id', models.IntegerField(blank=True, null=True)),
                ('level2_attribute_value_id', models.IntegerField(blank=True, null=True)),
                ('level3_attribute_value_id', models.IntegerField(blank=True, null=True)),
                ('is_default', models.IntegerField()),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('image_id', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('reviews', models.IntegerField(blank=True, null=True)),
                ('offer_status', models.IntegerField()),
                ('combo_offer_status', models.IntegerField()),
                ('is_new', models.IntegerField()),
                ('is_topseller', models.IntegerField()),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_variants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('products_id', models.IntegerField()),
                ('count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'product_views',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=250)),
                ('page_heading', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('contact_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_code', models.IntegerField(blank=True, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('browser_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vendors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_address_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=250)),
                ('billing_address_id', models.IntegerField()),
                ('type', models.CharField(blank=True, max_length=250, null=True)),
                ('pro_type', models.CharField(blank=True, max_length=250, null=True)),
                ('model', models.CharField(blank=True, max_length=250, null=True)),
                ('pro_model', models.CharField(blank=True, max_length=250, null=True)),
                ('serial_number', models.CharField(max_length=250)),
                ('dealer', models.CharField(blank=True, max_length=250, null=True)),
                ('inst_date', models.DateField()),
                ('contact_person', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'waranty',
                'managed': False,
            },
        ),
    ]
