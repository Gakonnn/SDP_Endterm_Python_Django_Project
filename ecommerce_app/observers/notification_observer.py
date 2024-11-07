class OrderObserver:
    def update(self, order):
        if order.status == 'shipped':
            self.notify_user(order)

    def notify_user(self, order):
        print(f"Notification sent to {order.user_email}: Your order #{order.id} has been shipped.")
