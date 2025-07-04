from django.contrib import admin
from .models import CoffeeTypes, Order, Users, EmployeesData, Payments

# Inline Model for Orders (optional)
class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

# Admin for Orders
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'coffee', 'quantity', 'order_date', 'status')

    def user_name(self, obj):
        return obj.user.name

    user_name.short_description = "Customer"

# Inline Model for Payments (optional)
class PaymentsInline(admin.TabularInline):
    model = Payments
    extra = 1

# Admin for Payments
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('Order_user_name', 'ammount', 'payment_status', 'payment_date')
    
    def Order_user_name(self, obj):
        return obj.Order.user.User.name

    Order_user_name.short_description = "Customer"

# Register Models
admin.site.register(CoffeeTypes)
admin.site.register(EmployeesData)
admin.site.register(Users)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payments, PaymentsAdmin)
