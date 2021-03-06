# Generated by Django 4.0.4 on 2022-05-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xcoord', models.FloatField()),
                ('ycoord', models.FloatField()),
                ('label', models.IntegerField()),
            ],
            options={
                'db_table': 'favorite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FavoriteGroup',
            fields=[
                ('group_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'favorite_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genes',
            fields=[
                ('index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('unnamed_0', models.BigIntegerField(blank=True, db_column='Unnamed: 0', null=True)),
                ('x', models.BigIntegerField(blank=True, db_column='X', null=True)),
                ('original_request', models.TextField(blank=True, db_column='Original_request', null=True)),
                ('function', models.TextField(blank=True, db_column='Function', null=True)),
                ('entry', models.TextField(blank=True, db_column='Entry', null=True)),
                ('entry_name', models.TextField(blank=True, db_column='Entry_name', null=True)),
                ('protein_names', models.TextField(blank=True, db_column='Protein_names', null=True)),
                ('gene_names', models.TextField(blank=True, db_column='Gene_names', null=True)),
                ('organism', models.TextField(blank=True, db_column='Organism', null=True)),
                ('length', models.BigIntegerField(blank=True, db_column='Length', null=True)),
                ('go', models.TextField(blank=True, db_column='GO', null=True)),
                ('disease', models.TextField(blank=True, db_column='Disease', null=True)),
                ('expr', models.TextField(blank=True, db_column='Expr', null=True)),
            ],
            options={
                'db_table': 'genes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user_table',
                'managed': False,
            },
        ),
    ]
