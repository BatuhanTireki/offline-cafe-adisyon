"""
Sipariş yönetimi API endpoint'leri
"""
from flask import Blueprint, jsonify, request
from models import OrderModel

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/table/<int:table_id>', methods=['GET'])
def get_table_orders(table_id):
    """Masanın siparişlerini getir"""
    try:
        orders = OrderModel.get_table_orders(table_id)
        return jsonify({'success': True, 'data': orders})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orders_bp.route('/add', methods=['POST'])
def add_order():
    """Masaya ürün ekle"""
    try:
        data = request.get_json()
        table_id = data.get('table_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        
        if not table_id or not product_id:
            return jsonify({'success': False, 'error': 'Masa ve ürün ID gerekli'}), 400
        
        result = OrderModel.add_product_to_table(table_id, product_id, quantity)
        return jsonify({'success': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orders_bp.route('/<int:order_id>/quantity', methods=['PUT'])
def update_quantity(order_id):
    """Sipariş adedini güncelle"""
    try:
        data = request.get_json()
        quantity = data.get('quantity')
        
        if quantity is None or quantity < 1:
            return jsonify({'success': False, 'error': 'Geçerli adet giriniz'}), 400
        
        result = OrderModel.update_order_quantity(order_id, quantity)
        return jsonify({'success': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@orders_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Siparişi sil"""
    try:
        result = OrderModel.remove_order(order_id)
        return jsonify({'success': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
