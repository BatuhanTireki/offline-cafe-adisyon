"""
Menü yönetimi API endpoint'leri
"""
from flask import Blueprint, jsonify, request
from models import MenuModel

menu_bp = Blueprint('menu', __name__)

@menu_bp.route('/categories', methods=['GET'])
def get_categories():
    """Tüm kategorileri getir"""
    try:
        categories = MenuModel.get_all_categories()
        return jsonify({'success': True, 'data': categories})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@menu_bp.route('/categories', methods=['POST'])
def add_category():
    """Yeni kategori ekle"""
    try:
        data = request.get_json()
        name = data.get('name')
        
        if not name:
            return jsonify({'success': False, 'error': 'Kategori adı gerekli'}), 400
        
        category_id = MenuModel.add_category(name)
        if category_id:
            return jsonify({'success': True, 'id': category_id})
        return jsonify({'success': False, 'error': 'Kategori eklenemedi'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@menu_bp.route('/products', methods=['GET'])
def get_products():
    """Tüm ürünleri getir"""
    try:
        products = MenuModel.get_all_products()
        return jsonify({'success': True, 'data': products})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@menu_bp.route('/products', methods=['POST'])
def add_product():
    """Yeni ürün ekle"""
    try:
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        category_id = data.get('category_id')
        
        if not name or price is None or not category_id:
            return jsonify({'success': False, 'error': 'Tüm alanlar gerekli'}), 400
        
        product_id = MenuModel.add_product(name, float(price), category_id)
        return jsonify({'success': True, 'id': product_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@menu_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Ürün güncelle"""
    try:
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        category_id = data.get('category_id')
        
        if not name or price is None or not category_id:
            return jsonify({'success': False, 'error': 'Tüm alanlar gerekli'}), 400
        
        MenuModel.update_product(product_id, name, float(price), category_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@menu_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Ürünü sil"""
    try:
        MenuModel.delete_product(product_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
