import json
import re

# PLEASE change the path to import the class
from Git.src.Read import Read

"""
This files contains the functions to perform unit tests with pytest
"""

invoice = {'account_number': None,
           'bill_to': {'address': '212 Highlawn Avenue\nBrooklyn, NY 11223', 'name': 'EDEN JEWELRY CO., INC.',
                       'parsed_address': None, 'vat_number': None}, 'cashback': None, 'category': 'Job Supplies',
           'created_date': '2023-04-19 18:33:14', 'currency_code': 'USD', 'date': '1991-01-09 00:00:00',
           'delivery_date': None, 'discount': None, 'document_reference_number': None,
           'document_title': 'SPECIAL NOTICE', 'document_type': 'purchase_order', 'due_date': '2023-05-19',
           'duplicate_of': None, 'external_id': None, 'id': 131730677, 'img_file_name': '131730677.jpg',
           'img_thumbnail_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/f010eff2-5d3c-488e-a6d6-31714b59c673/thumbnail.jpg?Expires=1681930094&Signature=VWJnpEU7a~4TuMOmGl1-z1G-4ZBw-5wMSuYcOd9Ij7n5LOw9PLL5G4QsmSr-TbgxxzUrESL4YRkn4NBs57lUqWnNzeGmway5qIGGv6jdqWXf5wd98330BvKKULJvPx0X1NV-cxEDYPpy7tRo81FHjacWbvoK1XXVMpqNmBgM7nj1oPsk~m0penLsBO2EhYoJXaEpe50iVCCyuFh1-UhBq74uRq5io8iGYA6sFlB89MqGNRtO5Zx815SyquxxWij4vWpJ52ejh~C9EXeHhG94e9KGdx8vgnyKHvTM2Acnubodo04~3KyhInns-2mTH3olObWwyKYdWvcBjVCYpHUaDA__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
           'img_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/f010eff2-5d3c-488e-a6d6-31714b59c673/2689496b-e78f-40be-9c0e-321409c1b6bc.jpg?Expires=1681930094&Signature=QwkHC-Y~eRlPjj3sbwMap~tNMZq66KHXnNkaBBY1rQxCjbyXSrZvj-yMQehxP07O-vOnGT35WM2iqr4T1FABVnd7LSLuw9v1HBJwVrg2eX3Da7DXYOXV7p0ANjEFhMjH-2XINIiBi6q-Tw6pjQ3PUxLEhIPvU9vR3scrf9SsFrkOuluwlwMdYlV2ZheLEFWo0SCv6Y5MJsJDKDNcFRDYQAnyVmopIcDxYnoKLm07pzMZQiajCOX0xSGm8kMo3kNvxwKU-Pc4~cSzJoER8RBnjY2zVP7FipWDMWPaWZJ71AR9Kadi9~-SMCG3ur66l7FBjx7kn7ftTwXBcOzNgA9XIg__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
           'insurance': None, 'invoice_number': None, 'is_duplicate': False, 'is_money_in': False, 'line_items': [
        {'date': None, 'description': 'Keyrings to be used in connection with the', 'discount': None,
         'discount_rate': None, 'id': 548393918, 'order': 0, 'price': None, 'quantity': 1.0, 'reference': None,
         'section': None, 'sku': None, 'tags': [], 'tax': None, 'tax_rate': None,
         'text': 'Keyrings to be used in connection with the', 'total': None, 'type': 'product',
         'unit_of_measure': None, 'upc': None},
        {'date': None, 'description': 'PALL MALL Quality Collection Self-Liquidating\nPromotion.', 'discount': None,
         'discount_rate': None, 'id': 548393919, 'order': 1, 'price': None, 'quantity': 1.0, 'reference': None,
         'section': None, 'sku': None, 'tags': [], 'tax': None, 'tax_rate': None,
         'text': 'PALL MALL Quality Collection Self-Liquidating\nPromotion', 'total': None, 'type': 'product',
         'unit_of_measure': None, 'upc': None}, {'date': None,
                                                 'description': 'Keyrings, as per sample submitted\nand approved; Gold Finish, engraved\nand color filled in red PALL MALL.\nKeyrings are to be packaged in a\nCardboard Gift Box.',
                                                 'discount': None, 'discount_rate': None, 'id': 548393920, 'order': 2,
                                                 'price': None, 'quantity': 1.0, 'reference': None, 'section': None,
                                                 'sku': '6,500', 'tags': [], 'tax': None, 'tax_rate': None,
                                                 'text': '6,500\tKeyrings, as per sample submitted\t\t$1.45 each\nand approved; Gold Finish, engraved\nand color filled in red PALL MALL.\nKeyrings are to be packaged in a\nCardboard Gift Box',
                                                 'total': 1.45, 'type': 'product', 'unit_of_measure': None,
                                                 'upc': None}], 'meta': {'owner': 'xbastianbitsx'}, 'notes': None,
           'ocr_text': 'THE\tSIX STAMFORD FORUM\t\t\t\tSPECIAL NOTICE\nF.C. BOX 10380\nAMERICAN\tSTAMFORD CONNECTICUT (6904-2007\t\tTHIS ORDER IS SUBJECT TO ACCEPTANCE EXPRESSLY\n\tLIMITED TO THE PROVISIONS ON THE FACE AND\nTOBACCO\t\t\t\t\tREVERSE SIDE AND TO THOSE APPENDED HERETO\nCOMPANY\t\t\t\t\tOUR ORDER NUMBER CODE NUMBER AND\n\tACCOUNTING CHARGE NUMBER MUST APPEAR ON ALL\n\tPACKAGES, CORRESPONDENCE AND INVOICES\nBILLING INSTRUCTIONS MAL YOUR INVOICES IN DUPLICATE TO CONSIGNEE\nUNLESS INSTRUCTED OTHERWISE BELOW,\nMAIL INVOICES TO OUR ADMINISTRATIVE CENTER,\nGENERAL ACCOUNTING OFFICE:\t\t\t\tPURCHASE ORDER NO. M12005\nP.O. BOX 1100\nCHESTER, VIRGINIA 23831-8100\t\t\t\tDATE\tJanuary 9, 1991\nAS SHOWN BELOW\t\t\t\t\tREQ. NO. Auth. #M-2; Budget # GF1\nSTO:\t\t\t\t\tS\nEDEN JEWELRY CO., INC.\t\tH THE FULFILLMENT HOUSE\n212 Highlawn Avenue\t\t\t7 Midland Avenue\nBrooklyn, NY 11223\t\tP\tHicksville, NY\t11801\nATTN: Mr. Dennis Flyer.\t\tATTN: Mr. Bob Pollack\n\nSHIPMENT TO ARRIME NOT LASER THAN\t\t\tVIA\nMarch 15, 1991\t\t\t\tBest Way Lowest Cost Method\nFOR\t\t\t\t\t\tTERMS\nYour Plant\t\t\t\tNet 30 Days\nQUANTITY\tCODE NO.\t\t\tDESCRIPTION\t\t\tPRICE\n\nKeyrings to be used in connection with the\nPALL MALL Quality Collection Self-Liquidating\nPromotion.\n\n6,500\tKeyrings, as per sample submitted\t\t$1.45 each\nand approved; Gold Finish, engraved\nand color filled in red PALL MALL.\nKeyrings are to be packaged in a\nCardboard Gift Box.\nThis Purchase Order is subject to and\nacceptance hereof expressly limited to the\nterms and conditions on the face and reverse\nside hereof and on the Specification Sheets.\nattached hereto and expressly made a part\nhereof.\n\nACCOUNTING CHARGE NO.\n\tMarketing Adv. Expense\nEXEMPTION CERTIFICATE\tIN YOUR FILES\nSTATE SALES TAX NOT TO BE CHARGED-SEE OUR\tDIRECT PAYMENT PERMIT\tO ATTACHED\n\t4. Vances Lules\nPlease contact V. Puleo\non any questions regarding this Purchase Order.\t\tBy\nQUALITY OF PRODUCT IS ESSENTIAL TO CONTINUING SUCCESS\nAT 173-M 15-AR)',
           'order_date': None,
           'payment': {'card_number': None, 'display_name': None, 'terms': 'Net 30 Days', 'type': None},
           'pdf_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/f010eff2-5d3c-488e-a6d6-31714b59c673/c5352692-5aaf-424e-8af6-f439b417bfc2.pdf?Expires=1681930094&Signature=T8hmD3zmMErwITUMBQDmw~o0BymR28u7tuhvUC32WysqZ3Wfb9TD6yEDNeoekp3wnUiOWqc8DFD-3BZ8tvKG8I9Sk-wHFkTz1-WHgQjBXZapB2VuaxJcFe~acYC4aeGIfGDneySP8Ahv3ZgATTKJYpl4fek2qy1TI82-whmUBlYRPjogPXfG~MxWeez3M1lvuif78-NFnIkgG16KQCc19lTeZ2OY-jF8FGu4SyxyE1IIfbCi-A~XqXars7tgZVXVUsTmDMu-jq~orWRwkAQM9fJ1xtQKlJFYNEFFpshR3G92Z7i9WjdAMZaI94MG9PQurNEWc5aiXT0XtriBMhcz9g__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
           'purchase_order_number': 'M12005', 'reference_number': 'VBBDH-30677', 'rounding': None,
           'service_end_date': None, 'service_start_date': None, 'ship_date': None,
           'ship_to': {'address': '7 Midland Avenue', 'name': 'THE FULFILLMENT HOUSE', 'parsed_address': None},
           'shipping': None, 'store_number': None, 'subtotal': None, 'tags': [], 'tax': None, 'tax_lines': [],
           'tip': None, 'total': 1.45, 'total_weight': None, 'tracking_number': None,
           'updated_date': '2023-04-19 18:33:14',
           'vendor': {'abn_number': None, 'account_number': None, 'address': None, 'bank_name': None,
                      'bank_number': None, 'bank_swift': None, 'category': None, 'email': None, 'fax_number': None,
                      'iban': None, 'lat': None, 'lng': None,
                      'logo': 'https://cdn.veryfi.com/logos/tmp/6d7bc54f-868a-4842-b412-45a27df0e331.png',
                      'name': 'Six Stamford Forum', 'phone_number': None, 'raw_address': None,
                      'raw_name': 'SIX STAMFORD FORUM', 'reg_number': None, 'type': None, 'vat_number': None,
                      'web': None}}
own_invoice = {'account_number': '18764031582771',
               'bill_to': {'address': 'CR 30 40 SUR 25', 'name': None, 'parsed_address': None,
                           'vat_number': '222222222-7'}, 'cashback': None, 'category': 'Meals & Entertainment',
               'created_date': '2023-04-20 03:10:56', 'currency_code': 'COP', 'date': '2023-04-12 12:26:52',
               'delivery_date': None, 'discount': None, 'document_reference_number': None, 'document_title': None,
               'document_type': 'receipt', 'due_date': None, 'duplicate_of': 131763669, 'external_id': None,
               'id': 131796294, 'img_file_name': '131796294.jpg',
               'img_thumbnail_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/ddaea1fd-9c5d-411c-b6e6-e8d47a48f241/thumbnail.jpg?Expires=1681961156&Signature=JJseqpHdvNFBU4dbDMJ06bK6AuvaSNoDKaUB1rMyivLMsNicQZrulLBcVBgPMfg8xHmGGJetdyflftEjoIM3~B~K~87UO2aR~KjwhpD7FekE86wpgUw2aXw9~BqaY75wc5lEjANtODDoDXcJNSQ1FRWdA5USBPMhtd4TXhuDK25gEy29YM1ppyjtpLdcS5b4oeYFCSW0a5IKWvhZ30cMKoxgdgCZeaVdghbOQpdzu4PHbOddRWFQ3nxQ6oMtFVqUUC7fpzqpOhr6N7eaneEc5P7FlXFL2cSzJBTtmex3iaYTsmNjB~jQryIWxlzG5b7gMO7S-XbkaMxrN9RP1ovZuQ__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
               'img_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/ddaea1fd-9c5d-411c-b6e6-e8d47a48f241/88735cee-bd70-4fb3-9d7d-6486492935f9.jpg?Expires=1681961156&Signature=X1jh9cEKCR19vAE0fvqRlmIsbmpnOOW6MwsqS5GcQ4yrFYQZSBzYFVIKGkUUnPA67Sp2KXT3C2xAgPYz-cx~rpo0S42I0uB4yLw6AIW51wcDU4yXIWrUumyJ6yo~EuDksXt6BrisepbjguOkbxsJZ882rcl6z44mO3m3Le1m0vM~2QmfaHEWIu8EXsGdyp7j9kFe-tvNsvZxLb2LBZVzysVF~UDSDpxjoK0~g2pXRa3s66lNXcX8p5hofTQt4y97H9toToAkIVKkL03jCrwFOKtTsVuzxWfbP8rZotGl~-ci5wi3TMl0LN9n-N-gRyKgSAy8N3nYMQ~tNvU48Bcy2A__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
               'insurance': None, 'invoice_number': '229296', 'is_duplicate': True, 'is_money_in': False,
               'line_items': [
                   {'date': None, 'description': 'CHATA', 'discount': None, 'discount_rate': None, 'id': 548765592,
                    'order': 0, 'price': None, 'quantity': 1.0, 'reference': None, 'section': None, 'sku': '100',
                    'tags': [], 'tax': None, 'tax_rate': None, 'text': '100 CHATA\t\t\t*1', 'total': None,
                    'type': 'food', 'unit_of_measure': None, 'upc': None},
                   {'date': None, 'description': None, 'discount': None, 'discount_rate': None, 'id': 548765593,
                    'order': 1, 'price': 43000.0, 'quantity': 0.94, 'reference': None, 'section': None, 'sku': None,
                    'tags': [], 'tax': None, 'tax_rate': None, 'text': '0.9443,000 $\t40,420', 'total': 40420.0,
                    'type': None, 'unit_of_measure': None, 'upc': None},
                   {'date': None, 'description': 'TABLA MOLIDA', 'discount': None, 'discount_rate': None,
                    'id': 548765594, 'order': 2, 'price': None, 'quantity': 1.0, 'reference': None, 'section': None,
                    'sku': '134', 'tags': [], 'tax': None, 'tax_rate': None, 'text': '134\tTABLA MOLIDA\t\t*1',
                    'total': None, 'type': 'food', 'unit_of_measure': None, 'upc': None}],
               'meta': {'owner': 'xbastianbitsx'}, 'notes': None,
               'ocr_text': 'CARNES LAS INCOMPARABLES N 13 S.A.S\nNIT: 901359360-7\nRESPONSABLE DE IVA\nDIRECCION:\nCR 30 40 SUR 25\nINCOMPARABLE\nTel: 2762162\nAUTORIZACION NUMERACION DE FACTURACION\n18764031582771\nMod: P.O.S\nFec: 25/07/2022\nVIGENCIA 12 MESES\nAUTORIZACIÓN DEL POS 200001 al POS 300000\nNumero Factura : POS 229296\nFecha Factura: 12/04/2023 12:26:52\n======ORIGINAL=\nDetalles de factura\n100 CHATA\t\t\t*1\n0.94\tX $\t43,000 $\t40,420\n134\tTABLA MOLIDA\t\t*1\n0.5\tx $\t34,000 $\t17,000\nDiscriminacion de Impuestos\nID % BASE\tIVA\n#1 0\t57,420\n*1 EXCE, *2 EXCLU, *3 19%,\n*4 10%, *5 20%, *6 5%,\nvalor Bruto\t: $ 57,420\nDESCUENTO\t:$ 0\nImpuestos\t: $ 0\nImpo Consumo\t:S O\nValor Total\t:$ 57,420\nTotal Recibido: $ 57,420\nTotal Cambio :$ 0\nFORMAS DE PAGO\nDatafono\t57,420\n\nTotal Articulos: 0\nKilos: 1.44\nNit\t: 222222222-7\nVENTAS POS\nDireccion: DG 33 34 D SUR 05\nTelefono: 2762162\nVendedor: JHON\ncajero: caja\nEquipo: SRV-INC13\nConserve su tirilla para reclamos',
               'order_date': None,
               'payment': {'card_number': None, 'display_name': 'Cash', 'terms': None, 'type': 'cash'},
               'pdf_url': 'https://scdn.veryfi.com/receipts/0fc8dc70b069948d/ddaea1fd-9c5d-411c-b6e6-e8d47a48f241/f81b5369-1c3c-4186-a378-9526c419f168.pdf?Expires=1681961156&Signature=ROhA1OBO2xuQxOTUbaCrAl7SvJwfAavzna~SHCsjJTvd7wgcUUhey3BzAzpVDasvJr-wLZSjYDwUFXQ5NmHKn1qGBnC4FsZOxI~xtviZArYYBeWWcVEAVR8h1gaWJ6Pva7ROZL4U40qhkAdeJ8Uc~Ge5O9uXEt5kTbPResJXf6U1NKH0jInF0nRmkaLxnqkKPoDr82sEMtGlOBcXl3D70mFJvdNwKbnzV60SOfKpwFP-LpcQXURZCJOqckKm5O-7f1V18qA3NHnEHc7kDF~fZeDAJZC~v3~iMMCY~Ciini5M14mrGZJUuuAOXYX3ahgBu1pXVFAAE4rmyUL341-Nug__&Key-Pair-Id=APKAJCILBXEJFZF4DCHQ',
               'purchase_order_number': None, 'reference_number': 'VBBDH-96294', 'rounding': None,
               'service_end_date': None, 'service_start_date': None, 'ship_date': None,
               'ship_to': {'address': 'DG 33 34 D SUR 05', 'name': None, 'parsed_address': None}, 'shipping': None,
               'store_number': '2762162', 'subtotal': 57420.0, 'tags': [], 'tax': None, 'tax_lines': [], 'tip': None,
               'total': 57420.0, 'total_weight': '1.44', 'tracking_number': None, 'updated_date': '2023-04-20 03:10:57',
               'vendor': {'abn_number': None, 'account_number': None, 'address': 'INCOMPARABLE\nTel', 'bank_name': None,
                          'bank_number': None, 'bank_swift': None, 'category': 'Food', 'email': None,
                          'fax_number': None, 'iban': None, 'lat': None, 'lng': None,
                          'logo': 'https://cdn.veryfi.com/logos/tmp/3f74edee-eacf-422b-a905-b7d499714f9a.png',
                          'name': 'Carnes Las Incomparables N 13 S.a.s', 'phone_number': '2762162', 'raw_address': None,
                          'raw_name': 'CARNES LAS INCOMPARABLES N 13 S.A.S', 'reg_number': None, 'type': 'Food',
                          'vat_number': '901359360-7', 'web': None}}

# Make the instance on the class to test
read_instance = Read('../files', '', '', '', '')


def test_vendor_name():
    """
    This function validates that the vendor_name of the invoice is equal to the one
    generated by the get_vendor_name function that takes the ocr_text as a reference
    to create the vendor_name
    """
    vendor_name = 'THE AMERICAN TOBACCO COMPANY'
    get_vendor_name = read_instance.get_vendor_name(invoice)
    own_invoice_vendor_name = read_instance.get_vendor_name(own_invoice)
    assert vendor_name == get_vendor_name
    assert vendor_name != own_invoice_vendor_name


def test_bill_to_name():
    """
    This function validates that the bill_to_name generated by the get_bill_to_name
     function complies with the correct format
    """
    regex = r"^[A-Z][a-z]+.+[a-z|\.]"
    get_bill_to_name = read_instance.get_bill_to_name(invoice)
    own_invoice_bill_to_name = read_instance.get_bill_to_name(own_invoice)
    assert get_bill_to_name is not None
    assert re.match(regex, get_bill_to_name) is not None
    assert own_invoice_bill_to_name is None


def test_bill_to_address():
    """
    This function validates that the bill_to_address generated by the get_bill_to_address
    function complies with the correct format
    """
    regex = r".+[A-Z]{2}\s\d{5}$"
    get_bill_to_address = read_instance.get_bill_to_address(invoice)
    own_invoice_bill_to_address = read_instance.get_bill_to_address(own_invoice)
    assert get_bill_to_address is not None
    assert re.match(regex, get_bill_to_address) is not None
    assert own_invoice_bill_to_address is None


def test_ship_to_name():
    """
    This function validates that the ship_to_name generated by the get_ship_to_name function
    complies with the correct format
    """
    regex = r"^[A-Z][a-z]+.+[a-z|\.]"
    get_ship_to_name = read_instance.get_bill_to_name(invoice)
    own_invoice_ship_to_name = read_instance.get_bill_to_name(own_invoice)
    assert get_ship_to_name is not None
    assert re.match(regex, get_ship_to_name) is not None
    assert own_invoice_ship_to_name is None


def test_ship_to_address():
    """
    This function validates that the ship_to_address generated by the get_ship_to_address
    function complies with the correct format
    """
    regex = r".+[A-Z]{2}\s\d{5}$"
    get_ship_to_address = read_instance.get_bill_to_address(invoice)
    own_invoice_ship_to_address = read_instance.get_bill_to_address(own_invoice)
    assert get_ship_to_address is not None
    assert re.match(regex, get_ship_to_address) is not None
    assert own_invoice_ship_to_address is None


def test_get_quantity_and_price():
    """
    This function validates that the amount and the value are a valid pair with the values
    to be validated from one of the invoices
    """
    correct = ('6,500', '1.45')
    get_get_quantity_and_price = read_instance.get_quantity_and_price(invoice)
    assert correct == get_get_quantity_and_price
    assert correct[0] == '6,500'
    assert correct[1] == '1.45'


def test_get_description():
    """
    This function validates that the text of the description of one of the invoices is correct
    for the one generated
    """
    correct = 'Keyrings to be used in connection with thePALL MALL Quality Collection Self-LiquidatingPromotion. ' \
              'Keyrings, as per sample submitted and approved; Gold Finish, engravedand color filled in red PALL ' \
              'MALL.Keyrings are to be packaged in aCardboard Gift Box.This Purchase Order is subject to ' \
              'andacceptance hereof expressly limited to theterms and conditions on the face and reverseside hereof ' \
              'and on the Specification Sheets.attached hereto and expressly made a parthereof.'
    get_description = read_instance.get_item_description(invoice)
    assert correct == get_description


def test_create_json_return():
    """
    This function validates that the final value returned has a valid json structure
    """
    json_value = read_instance.create_json_return(invoice)

    try:
        json.loads(json_value)
        assert True
    except ValueError:
        assert False, "The variable is not a valid JSON"
