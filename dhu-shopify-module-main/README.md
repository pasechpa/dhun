# shopify-odoo-template-module
Este es un modulo que funciona en Odoo 14, que se conecta a Shopify por medio del shopify-odoo-template-webservice. Es necesario contar con un usuario y contraseña que pueda crear ordenes y editar productos

Para que funcione es necesario eliminar el codigo en el modelo sales, solo dejar la funcion send_data_to_webserver() y crear un **Automated Actions** en Odoocon las siguientes configuraciones:
- Modelo: stock.move
- Trigger Condition: On Update
- Action To Do: Execute Python Code
- Código: ``` record.with_context(updated_stock_move_qty=True, stock_move_id=record).send_data_to_webserver() ```
