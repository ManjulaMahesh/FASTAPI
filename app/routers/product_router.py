from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.models.product_model import Product
from app.crud import product_crud

router = APIRouter(prefix="/products", tags=["Products"])
templates = Jinja2Templates(directory="app/templates")

# HTML frontend route
@router.get("/")
def show_products(request: Request):
    products = product_crud.get_all_products()
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

# API endpoint – Get all
@router.get("/api")
def get_products():
    return product_crud.get_all_products()

# API endpoint – Get one
@router.get("/api/{product_id}")
def get_product(product_id: int):
    product = product_crud.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# API endpoint – Add
@router.post("/api")
def create_product(product: Product):
    product_crud.add_product(product)
    return {"message": "Product added successfully"}

# API endpoint – Update
@router.put("/api/{product_id}")
def modify_product(product_id: int, product: Product):
    product_crud.update_product(product_id, product)
    return {"message": "Product updated successfully"}

# API endpoint – Delete
@router.delete("/api/{product_id}")
def remove_product(product_id: int):
    product_crud.delete_product(product_id)
    return {"message": "Product deleted successfully"}

# HTML Form actions
@router.post("/add")
def add_product_form(name: str = Form(...), price: float = Form(...), warranty: str = Form(...)):
    product_crud.add_product(Product(name=name, price=price, warranty=warranty))
    return RedirectResponse("/products/", status_code=303)

@router.post("/update/{product_id}")
def update_product_form(product_id: int, name: str = Form(...), price: float = Form(...), warranty: str = Form(...)):
    product_crud.update_product(product_id, Product(name=name, price=price, warranty=warranty))
    return RedirectResponse("/products/", status_code=303)

@router.get("/delete/{product_id}")
def delete_product_form(product_id: int):
    product_crud.delete_product(product_id)
    return RedirectResponse("/products/", status_code=303)
