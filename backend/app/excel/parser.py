import pandas as pd
from fastapi import UploadFile
from typing import List, Dict
from decimal import Decimal

async def parse_excel_products(file: UploadFile) -> List[Dict]:
    """
    Parse Excel file and extract product data
    Expected columns: name, sku, description, category, quantity, unit_price, supplier, reorder_level
    """
    contents = await file.read()
    
    # Read Excel file
    df = pd.read_excel(contents)
    
    # Normalize column names (remove spaces, lowercase)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Expected columns mapping
    column_mapping = {
        'name': 'name',
        'sku': 'sku',
        'description': 'description',
        'category': 'category',
        'quantity': 'quantity',
        'unit_price': 'unit_price',
        'price': 'unit_price',
        'supplier': 'supplier',
        'reorder_level': 'reorder_level',
        'reorder': 'reorder_level'
    }
    
    # Rename columns based on mapping
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns and new_col != old_col:
            df.rename(columns={old_col: new_col}, inplace=True)
    
    # Convert DataFrame to list of dictionaries
    products = []
    for _, row in df.iterrows():
        product = {
            'name': str(row.get('name', '')),
            'sku': str(row.get('sku', '')),
            'description': str(row.get('description', '')) if pd.notna(row.get('description')) else None,
            'category': str(row.get('category', '')) if pd.notna(row.get('category')) else None,
            'quantity': int(row.get('quantity', 0)) if pd.notna(row.get('quantity')) else 0,
            'unit_price': Decimal(str(row.get('unit_price', 0))) if pd.notna(row.get('unit_price')) else Decimal('0'),
            'supplier': str(row.get('supplier', '')) if pd.notna(row.get('supplier')) else None,
            'reorder_level': int(row.get('reorder_level', 10)) if pd.notna(row.get('reorder_level')) else 10,
        }
        products.append(product)
    
    return products
