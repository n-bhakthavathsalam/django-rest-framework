from rest_framework import authentication, generics, mixins, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from ..api.permissions import IsStaffEditorPermission
# from api.authentication import TokenAuthentication
from api.mixins import (StaffEditorPermissionMixin, UserQuerySetMixin)

# ===================================================================
class ProductListCreateAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, authentication.SessionAuthentication] #authentication.TokenAuthentication,                        
    # permission_classes =[permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]
    # permission_classes =[permissions.DjangoModelPermissions]
    # permission_classes =[IsStaffEditorPermission]



    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)



    # def query_set(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()



# ==================================================================
class ProductCreateAPIView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        # or None
        if content is None:
            content = title
        serializer.save(content=content)
       
product_create_view = ProductCreateAPIView.as_view()




# =======================================================
class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup field  = 'pk'
    # permission_classes =[permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


product_detail_view = ProductDetailAPIView.as_view()


# =============================================================
class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field  = 'pk'
    # permission_classes =[permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()



# =======================================================
class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field  = 'pk'
    # permission_classes =[permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly]


    def perform_destroy(self, instance):
        # insatnce
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()


# ==============================================================
# class ProductListAPIView(generics.ListAPIView):

#     ''' Not going to use this method'''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup field  = 'pk'


# =====================================================================
class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()



# ===================================================================
# Using Function Based Views For Create Retrieve or List
@api_view(['GET', 'POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk) 
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None: 
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid': 'not good data'}, status=400)
    




