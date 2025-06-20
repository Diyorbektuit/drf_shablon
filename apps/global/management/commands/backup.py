import subprocess
import os
import gzip
import requests

from django.core.management.base import BaseCommand
from core.security import backend_security

token = backend_security.TELEGRAM_BOT_TOKEN
chat_id = backend_security.TELEGRAM_CHAT_ID


class Command(BaseCommand):
    help = 'Take a database dump and send it to a Telegram bot'

    def handle(self, *args, **kwargs):
        self.get_backup_file()
        file_path = 'take_backup.sql'

        if not os.path.isfile(file_path):
            self.stdout.write(self.style.ERROR(f'File "{file_path}" does not exist.'))
            return

        self.send_file(file_path)

    def send_file(self, sql_file_path):
        gzip_file_path = f"{sql_file_path}.gz"

        try:
            # SQL faylni gzip formatiga siqish
            with open(sql_file_path, 'rb') as f_in:
                with gzip.open(gzip_file_path, 'wb') as f_out:
                    f_out.writelines(f_in)

            if not os.path.exists(gzip_file_path):
                self.stdout.write(self.style.ERROR(f'Failed to create gzip file: {gzip_file_path}'))
                return

            # Faylni Telegram API orqali yuborish
            with open(gzip_file_path, 'rb') as file:
                url = f"https://api.telegram.org/bot{token}/sendDocument"
                files = {'document': file}
                data = {'chat_id': chat_id, 'caption': "#project_name take_backup.py SQL file"}
                response = requests.post(url, data=data, files=files)

            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS(f'Successfully sent file: {gzip_file_path}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to send file: {response.json()}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to send file: {e}'))

        finally:
            # Vaqtinchalik faylni o'chirish
            if os.path.exists(gzip_file_path):
                os.remove(gzip_file_path)
                self.stdout.write(self.style.SUCCESS(f'Deleted gzip file: {gzip_file_path}'))

    def get_backup_file(self):
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')

        output_file = 'take_backup.sql'

        dump_command = [
            '/usr/bin/docker', 'exec', 'project_name_postgres_container', 'pg_dump',
            '-U', db_user,
            db_name
        ]

        os.environ['PGPASSWORD'] = db_password

        try:
            with open(output_file, 'w') as f:
                subprocess.run(dump_command, stdout=f, check=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully dumped the database to {output_file}'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Error during dump: {e}'))
        finally:
            del os.environ['PGPASSWORD']
