from django.shortcuts import render,redirect,HttpResponse   
from django.views import View
from shop.models import category,Product
from shop.forms import CategoryForm,ProductForm

# Create your views here.

class Categoryview(View):
    def get(self,request):
        cat = category.objects.all()
        return render(request,'category.html',{'cat':cat})

class subcategoryview(View):
    def get(self, request,i):
        cat = category.objects.get(id=i)
        return render(request, 'subcategory.html', {'cat':cat})

class ProdDetailView(View):
    def get(self, request, i):
        pro = Product.objects.get(id=i)
        return render(request, 'productdetail.html', {'pro':pro})

class NewCategory(View):
        def get(self,request,*args,**kwargs):
            form_instance = CategoryForm()
            return render(request,'admin/formdisp.html',{'form':form_instance})
        def post(self,request,*args,**kwargs):
            form_instance=CategoryForm(request.POST,request.FILES)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('shop:Newcat')

class Newproduct(View):
        def get(self,request,*args,**kwargs):
            form_instance = ProductForm()
            return render(request,'admin/formdisp.html',{'form':form_instance})
        def post(self,request,*args,**kwargs):
            form_instance=ProductForm(request.POST,request.FILES)
            if form_instance.is_valid():
                form_instance.save()
                return redirect('shop:newprod')

class UpdateProduct(View):
    def get(self,request,i):
        b=Product.objects.get(id=i)
        form_instance=ProductForm(instance=b)
        return render(request,'admin/formdisp.html',{'form':form_instance})

    def post(self,request,i):
        b = Product.objects.get(id=i)
        form_instance=ProductForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
                form_instance.save()
                return redirect('loginfo:superadmin')
        else:
            return HttpResponse("Product Update Failed")

class UpdateCategory(View):
    def get(self,request,i):
        b=category.objects.get(id=i)
        form_instance=CategoryForm(instance=b)
        return render(request,'admin/formdisp.html',{'form':form_instance})

    def post(self,request,i):
        b = Product.objects.get(id=i)
        form_instance=ProductForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
                form_instance.save()
                return redirect('loginfo:superadmin')
        else:
             return HttpResponse("Category Update Failed")



class DeleteProduct(View):
    def get(self,request,i):
        b=Product.objects.get(id=i)
        b.delete()
        return redirect('loginfo:superadmin')
class DeleteCategory(View):
    def get(self,request,i):
        b=category.objects.get(id=i)
        b.delete()
        return redirect('loginfo:superadmin')
    

class Proddetail(View):
     def get(self, request, i):
        pro = Product.objects.get(id=i)
        return render(request, 'admin/detail.html', {'prod':pro})
     
class Categodetail(View):
     def get(self, request, i):
        cat = category.objects.get(id=i)
        return render(request, 'admin/detail.html', {'cat':cat})
