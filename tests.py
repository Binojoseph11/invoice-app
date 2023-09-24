from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
import json

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            "date": "2023-09-24",
            "customer_name": "Test Customer"
        }
        self.invoice_detail_data = {
            "invoice": None,  # Initialize as None
            "description": "Test Item",
            "quantity": 2,
            "unit_price": "10.0",
            "price": "20.0"
        }

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invoice_detail(self):
        # Create an Invoice
        invoice = Invoice.objects.create(**self.invoice_data)

        # Set the invoice ID in the invoice_detail_data
        self.invoice_detail_data["invoice"] = invoice.id

        # Serialize the data to JSON format
        data = json.dumps(self.invoice_detail_data)
        response = self.client.post('/api/invoice-details/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_list(self):
        response = self.client.get('/api/invoices/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_detail(self):
        # Create an Invoice
        invoice = Invoice.objects.create(**self.invoice_data)

        # Create an InvoiceDetail associated with the Invoice
        self.invoice_detail_data["invoice"] = invoice.id

        # Serialize the data to JSON format
        data = json.dumps(self.invoice_detail_data)
        response = self.client.post('/api/invoice-details/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the created InvoiceDetail
        response = self.client.get(f'/api/invoice-details/{response.data["id"]}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_detail_list(self):
        response = self.client.get('/api/invoice-details/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice_detail_detail(self):
        # Create an Invoice
        invoice = Invoice.objects.create(**self.invoice_data)

        # Create an InvoiceDetail associated with the Invoice
        self.invoice_detail_data["invoice"] = invoice.id

        # Serialize the data to JSON format
        data = json.dumps(self.invoice_detail_data)
        response = self.client.post('/api/invoice-details/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the created InvoiceDetail
        response = self.client.get(f'/api/invoice-details/{response.data["id"]}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
