from django.http import HttpResponse


class StripeWH_Handler:
    """
    Stripe webhooks handler
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic webhook events
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded event from Stripe
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle payment intent payment failed event from Stripe
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)