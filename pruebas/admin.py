from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from import_export import fields, resources
# from .models import Producto,Marca,Genero,Genre


# class GenreResources(resources.ModelResource):
#     class Meta:
#         model = Genre

# class GenreAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ('name','parent',)

# class GeneroAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre',)
#     search_fields = ('nombre',)
#     list_editable = ('nombre',)

# class ProductosResource(resources.ModelResource):
#     class Meta:
#         model = Producto

# class MarcaResource(resources.ModelResource):

#     class Meta:
#         model = Marca

# class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ('id','cod','nombre', 'marca', 'precio','stock','precioMayor',)
#     list_filter  = ( 'marca', 'stock',)
#     search_fields = ('cod','nombre', 'marca', 'precio')
#     list_editable = ('cod','nombre', 'marca', 'precio','stock','precioMayor',)
#     readonly_fields = ('created', 'updated')
#     resources_class = ProductosResource


# class MarcaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ('id','categoria')
#     search_fields = ('categoria',)
#     resources_class = MarcaResource




# admin.site.register(Producto, ProductoAdmin)
# admin.site.register(Marca, MarcaAdmin)
# admin.site.register(Genero, GeneroAdmin)
# admin.site.register(Genre,GenreAdmin)
