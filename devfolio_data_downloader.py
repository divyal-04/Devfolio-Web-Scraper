import pandas as pd
import json

#this is the main script class 

class DevfolioDataDownloader:
    def __init__(self, filename):
        self.filename = filename

    def load_data_from_json(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def extract_user_data(self, data):
        user_data = []
        for participant in data['result']:
            user_info = participant['user']
            user_extra = user_info.get('user_extra', {})
            user_data.append({
                'username': user_info['username'],
                'email': user_info['email'],
                'first_name': user_info['first_name'],
                'last_name': user_info['last_name'],
                'gender': user_info['gender'],
                'phone_number': user_info['phone_number'],
            })
        return user_data

    def create_dataframe(self, user_data):
        df = pd.DataFrame(user_data)
        return df

    def display_data(self):
        data = self.load_data_from_json()
        user_data = self.extract_user_data(data)
        df = self.create_dataframe(user_data)
        print(df)

    def save_to_csv(self, csv_filename):
        data = self.load_data_from_json()
        user_data = self.extract_user_data(data)
        df = self.create_dataframe(user_data)
        df.to_csv(csv_filename, index=False)
