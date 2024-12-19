import gdown


class GoogleDriveDownloader:
    def __init__(self, urls):
        self.urls = urls

    def extract_file_id(self, url):
        return url.split('/d/')[1].split('/')[0]

    def download_file(self, file_id, output_path):
        download_url = f'https://drive.google.com/uc?id={file_id}'

        # Download the file
        gdown.download(download_url, output_path, quiet=False)
        print(f'File downloaded successfully and saved as {output_path}')

    def download_files(self):
        for index, url in enumerate(self.urls):
            file_id = self.extract_file_id(url)
            output_path = f'downloaded_file_{index + 1}'  # Save with a unique name for each file
            self.download_file(file_id, output_path)


urls = [
    'https://drive.google.com/file/d/1TBX7hLraMiiLucknM1mhblNVomO9-Y0r/view?usp=sharing',
    'https://drive.google.com/file/d/1JmEsU0GYUD5iVdefMOZpeWa_iYnmK_7w/view?usp=sharing',
    'https://drive.google.com/file/d/1g8tzzW5BNPzHXlamuMQOvdwlHRa-29Vp/view?usp=sharing',
    'https://drive.google.com/file/d/1lq7ksWeD3FzaIwowRbe_BvCmSmOG12-f/view?usp=sharing'
]

if __name__ == '__main__':
    downloader = GoogleDriveDownloader(urls)

    downloader.download_files()
