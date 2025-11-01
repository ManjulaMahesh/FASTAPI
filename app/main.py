from fastapi import FastAPI
from  app.routers import product_router

app = FastAPI(title="Product API")

# Include routes
app.include_router(product_router.router)
