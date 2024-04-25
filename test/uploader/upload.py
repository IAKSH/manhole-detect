import argparse
import base64
import requests


def encode_image(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def post_image(image_path, url):
    image_base64 = encode_image(image_path)
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    data = {'sensor_id': 1, 'image': image_base64}
    response = requests.post(url, json=data, headers=headers)
    return response.text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='packup')
    parser.add_argument('--image', type=str, required=True, help='path to image')
    parser.add_argument('--server', type=str, required=False, default='http://192.168.110.110/api/sensor/upload',
                        help='upload server ip')
    args = parser.parse_args()

    print(post_image(args.image, args.server))
