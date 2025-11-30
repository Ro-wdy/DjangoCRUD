from django.shortcuts import render, redirect, get_object_or_404
from Admin.models import Product

# Display all products on admin dashboard
def admin(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'admin.html', context)


# Add a new product
def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Product.objects.create(
            name=name,
            price=price,
            description=description
        )

        return redirect('admin')

    # GET request → show the form
    return render(request, 'add_item.html')


# Delete a product
def delete_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('admin')

# Update a product
def update_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            brand = request.POST.get('brand')
            category = request.POST.get('category')
            quantity = request.POST.get('quantity')

            # Update existing product
            product.name = name
            product.price = price
            product.description = description
            product.brand = brand
            product.category = category
            product.quantity = quantity
            product.save()

            return redirect('admin')

        except Exception as e:
            print("Update Error:", e)

    context = {'product': product}
    return render(request, 'update_item.html', context)