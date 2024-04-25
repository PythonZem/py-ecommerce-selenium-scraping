import csv
import dataclasses
from dataclasses import dataclass
from urllib.parse import urljoin


BASE_URL = "https://webscraper.io/"

ENDPOINTS_URL = {
    "home": ""
}

HOME_URL = urljoin(BASE_URL, "test-sites/e-commerce/more/")
COMPUTERS_URL = urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/")
LAPTOPS_URL = urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/laptops")
TABLETS_URL = urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/tablets")
PHONES_URL = urljoin(BASE_URL, "/test-sites/e-commerce/more/phones")
TOUCH_URL = urljoin(BASE_URL, "/test-sites/e-commerce/more/phones/touch")


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


PRODUCT_FIELDS = [filed.name for filed in dataclasses.fields(Product)]


def get_all_products() -> None:
    pass


def write_products_to_csv(products: [Product]) -> None:
    with open("products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(PRODUCT_FIELDS)
        writer.writerows([dataclasses.astuple(product) for product in products])


if __name__ == "__main__":
    get_all_products()
