import os
import re
import veryfi


class Read:
    multi = re.M
    dic = {}
    files = []
    client_id = "vrfiRtZobtTrwnPJay7EG8LXy8y1OnwIiovJZup"
    client_secret = "nuFKukMS8leUx1FAY44ddf4NnIn8l9lulA2HlNullmPFgFGb9pzgWSpl5cVYFfPN9NSm02LSfIVBLZSTEDrBJuCdLxgFW4pZkDzDEAVX9hYR5sbUg5M7D1jNSv37rNpH"
    username = "xbastianbitsx"
    api_key = "91ca4d457eafdfea8cf42fad779d2625"

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.client = veryfi.Client(self.client_id, self.client_secret, self.username, self.api_key)

    def get_file_names(self):
        file_names = []
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                file_names.append(filename)
        self.files = file_names
        return file_names

    def get_ocr_text(self, dic):
        if 'ocr_text' in dic:
            return dic['ocr_text']
        else:
            return None

    def get_vendor_name(self, dic):
        orc_text = self.get_ocr_text(dic)
        # regex = r"(?:THE\t)([\w ]*)(?:\t|\n)"
        regex = r"^([A-Z]{3,})(?:\t{1,}).+"
        try:
            result = re.findall(regex, orc_text, self.multi)
            vendor_name = ' '.join(map(str, result[:4]))
        except IndexError:
            vendor_name = None
        return vendor_name

    def get_bill_to_name(self, dic):
        orc_text = self.get_ocr_text(dic)
        regex = r"(?<=(?:ATTN|Atta):)([\w .]+)"
        try:
            bill_to_name = re.findall(regex, orc_text)[0]
        except IndexError:
            bill_to_name = None
        return bill_to_name

    def get_bill_to_address(self, dic):

        orc_text = self.get_ocr_text(dic)
        regex = r"(.+(?:Street|Avenue).+\s.+\s|.+\s)(.+\, \w{2} \d{5})"
        try:
            result = re.findall(regex, orc_text, self.multi)
            formated_list = list(result[0])
            line1 = formated_list[0].split('\t\t')[0].split('\n')[0].replace('P	', '')
            bill_to_address = f"{line1} {formated_list[1]}"
        except IndexError:
            bill_to_address = None
        return bill_to_address

    def get_ship_to_name(self, dic):

        orc_text = self.get_ocr_text(dic)
        regex = r"(?<=(?:\t(?:ATTN|Atta)): )([\w .]+)$"
        try:
            ship_to_name = re.findall(regex, orc_text, self.multi)[0]
        except IndexError:
            ship_to_name = None
        return ship_to_name

    def get_ship_to_address(self, dic):

        orc_text = self.get_ocr_text(dic)
        regex = r"(?:\t(\d.+)\s.+P\s)(.+\w{2}\s\d{5})$"
        try:
            response = re.findall(regex, orc_text, self.multi)
            formated_response = list(response[0])
            if len(formated_response) > 0:
                ship_to_address = ' '.join(map(str, formated_response[:2]))
            else:
                ship_to_address = None
        except IndexError:
            ship_to_address = None
        return ship_to_address

    def get_line_items_quantity(self, dic):
        orc_text = self.get_ocr_text(dic)
        regex = r"(?:PRICE$)(?:\n|.+\n)+\s^([\d,]+)(?:\t)"

        try:
            line_items_quantity = re.findall(regex, orc_text, self.multi)[0]
        except IndexError:
            line_items_quantity = None
        return line_items_quantity

    def get_quantity_and_price(self, dic):
        orc_text = self.get_ocr_text(dic)
        regex = r"(?:PRICE$)(?:\n|.+\n)+\s^([\d,]+)(?:\t.+)\$([\d.]+) (?:each|ea)"
        result = re.search(regex, orc_text, self.multi)
        return list(result.groups())

    def get_item_description(self, dic):
        orc_text = self.get_ocr_text(dic)
        regex = r"\t+(.+)\t+\$.+(?:each|ea)\n((.+\s)+)(?:.$\n|^(?:\n|\t))"
        result = re.search(regex, orc_text, self.multi)
        groups = result.groups()
        res = ' '.join(map(str, groups[:2]))
        return res

    def create_line_items(self, dic):

        q_and_p = self.get_quantity_and_price(dic)
        description = f"Description : {self.get_item_description(dic)}"
        line_items = [f'quantity: {q_and_p[0]}', description, f'price: {q_and_p[1]}']
        return line_items

    def create_json_return(self, dic):

        return {
            'vendor_name': self.get_vendor_name(dic),
            'bill_to_name': self.get_bill_to_name(dic),
            'bill_to_address': self.get_bill_to_address(dic),
            'ship_to_name': self.get_ship_to_name(dic),
            'ship_to_address': self.get_ship_to_address(dic),
            'line_items': self.create_line_items(dic)
        }

    # def get_json_from_file(self):
    #
    #     self.dic = self.client.process_document(self.file)
    #     return self.dic



if __name__ == "__main__":
    invo = Read('../files/')

    # dic = input("Ingresa tu dic: ")
    print(invo.get_file_names())
